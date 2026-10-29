"""Material evaluation with minimax and alpha-beta pruning."""

import argparse

import chess


PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20_000,
}
MATE_SCORE = 99_999


def evaluate_material(board):
    """Return a material score from White's perspective."""
    if board.is_checkmate():
        return -MATE_SCORE if board.turn == chess.WHITE else MATE_SCORE
    if board.is_game_over(claim_draw=True):
        return 0

    score = 0
    for piece in board.piece_map().values():
        value = PIECE_VALUES[piece.piece_type]
        score += value if piece.color == chess.WHITE else -value
    return score


def minimax(board, depth, is_maximizing):
    """Search the game tree and return (score, best_move)."""
    if depth == 0 or board.is_game_over(claim_draw=True):
        return evaluate_material(board), None

    best_move = None
    if is_maximizing:
        best_score = float("-inf")
        for move in board.legal_moves:
            board.push(move)
            score, _ = minimax(board, depth - 1, False)
            board.pop()
            if score > best_score:
                best_score, best_move = score, move
        return best_score, best_move

    best_score = float("inf")
    for move in board.legal_moves:
        board.push(move)
        score, _ = minimax(board, depth - 1, True)
        board.pop()
        if score < best_score:
            best_score, best_move = score, move
    return best_score, best_move


def minimax_alphabeta(board, depth, alpha, beta, is_maximizing):
    """Minimax search with alpha-beta pruning."""
    if depth == 0 or board.is_game_over(claim_draw=True):
        return evaluate_material(board), None

    best_move = None
    if is_maximizing:
        best_score = float("-inf")
        for move in board.legal_moves:
            board.push(move)
            score, _ = minimax_alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            if score > best_score:
                best_score, best_move = score, move
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score, best_move

    best_score = float("inf")
    for move in board.legal_moves:
        board.push(move)
        score, _ = minimax_alphabeta(board, depth - 1, alpha, beta, True)
        board.pop()
        if score < best_score:
            best_score, best_move = score, move
        beta = min(beta, best_score)
        if alpha >= beta:
            break
    return best_score, best_move


def play_chess_bot(depth=3):
    """Play as White against the AI, which plays Black."""
    board = chess.Board()
    while not board.is_game_over(claim_draw=True):
        print("\n" + "=" * 30)
        print(board)
        print("=" * 30)

        if board.turn == chess.WHITE:
            move_input = input("Your move (SAN or UCI, or 'quit'): ").strip()
            if move_input.lower() in {"quit", "exit"}:
                print("Game exited.")
                return
            try:
                try:
                    move = board.parse_san(move_input)
                except ValueError:
                    move = chess.Move.from_uci(move_input)
                    if move not in board.legal_moves:
                        raise ValueError("Illegal move")
                board.push(move)
            except ValueError as error:
                print(f"Invalid move: {error}")
        else:
            print("AI is thinking...")
            _, move = minimax_alphabeta(
                board, depth, float("-inf"), float("inf"), is_maximizing=False
            )
            if move is None:
                break
            board.push(move)
            print(f"AI played: {move.uci()}")

    print("\n" + "=" * 30)
    print(board)
    print("GAME OVER")
    print(f"Result: {board.result(claim_draw=True)}")
    outcome = board.outcome(claim_draw=True)
    print(f"Reason: {outcome.termination.name if outcome else 'Unknown'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--depth", type=int, default=3, help="search depth (default: 3)")
    args = parser.parse_args()
    if args.depth < 1:
        parser.error("--depth must be at least 1")
    play_chess_bot(depth=args.depth)
