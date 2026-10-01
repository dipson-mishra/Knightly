import chess
import random


def play_random(fen):
    """Selects a random legal move for the computer."""
    board = chess.Board(fen)
    move = random.choice(list(board.legal_moves))
    return str(move)


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
    play_game(play_random)