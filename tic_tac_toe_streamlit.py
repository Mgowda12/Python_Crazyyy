import numpy as np
import streamlit as st

def create_board():
    return np.zeros((3, 3), dtype=int)

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def row_win(board, player):
    for x in range(3):
        if all(board[x, :] == player):
            return [(x, i) for i in range(3)]
    return []

def col_win(board, player):
    for x in range(3):
        if all(board[:, x] == player):
            return [(i, x) for i in range(3)]
    return []

def diag_win(board, player):
    win_coords = []
    if all(board[i, i] == player for i in range(3)):
        win_coords = [(i, i) for i in range(3)]
    elif all(board[i, 2 - i] == player for i in range(3)):
        win_coords = [(i, 2 - i) for i in range(3)]
    return win_coords

def evaluate(board):
    for player in [1, 2]:
        win_coords = row_win(board, player) or col_win(board, player) or diag_win(board, player)
        if win_coords:
            return player, win_coords
    if np.all(board != 0):
        return -1, []
    return 0, []

def display_board(board, win_coords=[]):
    color_map = {0: "#FFFFFF", 1: "#FF6347", 2: "#4682B4"}
    symbols = {0: "", 1: "X", 2: "O"}
    board_html = ""
    cell_number = 1  # Start numbering the cells from 1 to 9

    for i in range(3):
        row_html = ""
        for j in range(3):
            color = color_map[board[i][j]]
            if (i, j) in win_coords:
                color = "#FFFF00"  # Highlight winning cells with yellow
            row_html += (
                f'<td style="width: 100px; height: 100px; background-color: {color}; '
                f'text-align: center; font-size: 30px; border: 1px solid black;" '
                f'onclick="select_cell({cell_number})">{symbols[board[i][j]]}</td>'
            )
            cell_number += 1
        board_html += f"<tr>{row_html}</tr>"
    return f'<table style="border: 2px solid black; border-collapse: collapse; margin: 20px auto;">{board_html}</table>'

def play_game():
    st.title("Tic-Tac-Toe Game")

    if "board" not in st.session_state:
        st.session_state.board = create_board()
        st.session_state.turn = 1
        st.session_state.winner = 0
        st.session_state.game_over = False
        st.session_state.win_coords = []

    winner, win_coords = evaluate(st.session_state.board)
    if winner != 0:
        st.session_state.game_over = True
        st.session_state.win_coords = win_coords
        if winner == -1:
            st.subheader("It's a Tie!")
        else:
            st.subheader(f"Player {winner} Wins!")
        st.markdown(display_board(st.session_state.board, win_coords), unsafe_allow_html=True)
        return

    st.markdown(display_board(st.session_state.board), unsafe_allow_html=True)

    if not st.session_state.game_over:
        st.subheader(f"Player {st.session_state.turn}'s Turn")
        moves = possibilities(st.session_state.board)

        # Create individual buttons for each cell (1 to 9)
        cell_number = 1  # Start from cell 1
        for i in range(3):
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.session_state.board[i, 0] == 0:
                    if st.button(f"{cell_number}", key=f"cell_{i}_0"):
                        st.session_state.board[i, 0] = st.session_state.turn
                        st.session_state.turn = 2 if st.session_state.turn == 1 else 1
                        st.rerun()
                cell_number += 1
            with col2:
                if st.session_state.board[i, 1] == 0:
                    if st.button(f"{cell_number}", key=f"cell_{i}_1"):
                        st.session_state.board[i, 1] = st.session_state.turn
                        st.session_state.turn = 2 if st.session_state.turn == 1 else 1
                        st.rerun()
                cell_number += 1
            with col3:
                if st.session_state.board[i, 2] == 0:
                    if st.button(f"{cell_number}", key=f"cell_{i}_2"):
                        st.session_state.board[i, 2] = st.session_state.turn
                        st.session_state.turn = 2 if st.session_state.turn == 1 else 1
                        st.rerun()
                cell_number += 1

if __name__ == "__main__":
    play_game()
