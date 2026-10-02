import chess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Input

# Initialize the board
board = chess.Board()

def one_hot_encode_piece(piece):
    pieces = list('rnbqkpRNBQKP.')
    arr = np.zeros(len(pieces))
    piece_to_index = {p: i for i, p in enumerate(pieces)}
    index = piece_to_index[piece]
    arr[index] = 1
    return arr

def encode_board(board):
    board_str = str(board)
    board_str = board_str.replace(' ', '')
    board_list = []
    for row in board_str.split('\n'):
        row_list = []
        for piece in row:
            row_list.append(one_hot_encode_piece(piece))
        board_list.append(row_list)
    return np.array(board_list)

# Test encoding on the starting board
print("Starting board shape:", encode_board(chess.Board()).shape)

# Load data
train_df = pd.read_csv('data/raw/train.csv', index_col='id')

# We'll only use the first 10000 examples so things run fast,
# but you'll get better performance if you remove this line
train_df = train_df[:10000]

# We'll also grab the last 1000 examples as a validation set
val_df = train_df[-1000:]
print(train_df.head())

def encode_fen_string(fen_str):
    board = chess.Board(fen=fen_str)
    return encode_board(board)

X_train = np.stack(train_df['board'].apply(encode_fen_string))
y_train = train_df['black_score']

X_val = np.stack(val_df['board'].apply(encode_fen_string))
y_val = val_df['black_score']

# Build the Keras Sequential model
model = Sequential([
    Input(shape=(8, 8, 13)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1),
])

model.compile(
    optimizer='rmsprop',
    loss='mean_squared_error'
)

# Train the model
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    validation_data=(X_val, y_val)
)

# Plot training history
plt.style.use('ggplot')
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.legend()
plt.title('Loss During Training')
plt.show()

def play_nn(fen, show_move_evaluations=False, player='b'):
    board = chess.Board(fen=fen)

    moves = []
    for move in board.legal_moves:
        candidate_board = board.copy()
        candidate_board.push(move)
        input_vector = encode_board(candidate_board).astype(np.float32)


        score = model.predict(np.expand_dims(input_vector, axis=0), verbose=0)[0][0]
        moves.append((score, move))
        if show_move_evaluations:
            print(f'{move}: {score}')

    best_move = sorted(moves, reverse=player=='b')[0][1]

    return str(best_move)

#%%
def play_game(function):
    """Manages the chess game loop between a human player and the computer."""
    board = chess.Board()

    while board.outcome() is None:
        print("\n" + "=" * 25)
        print(board)  # Prints a text-based ASCII representation of the board
        print("=" * 25)

        # White is the human player
        if board.turn == chess.WHITE:
            user_move = input("Enter your move (e.g., e2e4 or 'quit'): ").strip()
            if user_move.lower() == "quit":
                print("Game Over! You lose.")
                break

            while user_move not in [str(move) for move in board.legal_moves]:
                print("Invalid move or not legal. Please try again.")
                user_move = input("Enter your move: ").strip()

            board.push(chess.Move.from_uci(user_move))

        # Black is the computer player
        elif board.turn == chess.BLACK:
            move = function(board.fen())
            print(f"Computer plays: {move}")
            board.push(chess.Move.from_uci(move))

    # Handle end game state
    if board.outcome() is not None:
        print("\n" + "=" * 25)
        print(board)
        print("=" * 25)
        print("Game Over!")
        print(f"Result: {board.outcome().result()}")
if __name__ == "__main__":
    play_game(play_nn)