import cv2
import numpy as np
import scipy.signal
SIZE_X = 2000
SIZE_Y = 2000
SCALE = 1

def check_y(i):
    return 0 <= i < SIZE_Y

def check_x(j):
    return 0 <= j < SIZE_X

directions = np.array([(1,0),
                       (-1,0),
                       (0,1),
                       (0,-1),
                       (1,-1),
                       (-1,1),
                       (1,1),
                       (-1,-1)])

area = 3
def apply_logic(board):
    convolve = scipy.signal.convolve2d(board, np.ones((area,area)), "same")
    new_board = np.where(((board == 1) & ((convolve == 3) | (convolve == 4))) |
                         (board == 0) & (convolve == 3), 1.,0.)
    return new_board#new_board


def run():
    board = np.round(np.random.random((SIZE_Y, SIZE_X)) * 0.55)
    while True:
        board = apply_logic(board)
        if SCALE > 1:
            show_board =np.kron(board, np.ones((SCALE, SCALE), dtype=board.dtype))
            cv2.imshow("game of life", show_board)
        else:
            cv2.imshow("game of life", board)
        cv2.waitKey(1)

if __name__ == "__main__":
    run()