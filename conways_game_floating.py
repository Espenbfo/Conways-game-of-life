import cv2
import numpy as np
import scipy.signal
SIZE_X = 150
SIZE_Y = 150
SCALE = 8

area = 3
USE_COLOR = True
CLIP = False
CLIP_LIMIT = 0.5

CONFIG_1 = [0,5,2.495, 3.25]
CONFIG_2 = [1.5,5,2.87, 4.]
CONFIG_3 = [1.2,4,2.5, 4.]
CONFIG_4 = [0.7, 6, 3.4, 5.] #Square
CONFIG_5 = [8, 8, 0, 8] #Square
life_bottom,life_top,dead_bottom,dead_top = CONFIG_1

def apply_logic(board):
    convolve = scipy.signal.convolve2d(board, np.ones((area,area)), "same")
    random = np.random.random((SIZE_Y, SIZE_X))*0.5
    new_board = np.where(((board > 0.5) & ((convolve > life_bottom) & (convolve < life_top))) |
                         (board < 0.5) & ((convolve > dead_bottom) & (convolve < dead_top)),
                         random+0.5,0.)
    return new_board#new_board


def run():
    #board = np.random.random((SIZE_Y, SIZE_X)) * 0.7
    board = np.zeros((SIZE_Y, SIZE_X))
    board[50:100,50:100] = 0.6
    board[0:50,80:90] = 0.6
    while True:
        board = apply_logic(board)
        show_board = board.copy()

        if CLIP:
            show_board = np.where(board > CLIP_LIMIT, 1., 0.)
        if USE_COLOR:
            show_board = np.stack((show_board ** 3, show_board ** 2 * 0.5, show_board ** 2),
                                  axis=2)


        #print(show_board)
        if SCALE > 1:
            if USE_COLOR:
                show_board =np.kron(show_board, np.ones((SCALE, SCALE,1), dtype=board.dtype))
            else:
                show_board = np.kron(show_board, np.ones((SCALE, SCALE),
                                                        dtype=board.dtype))
            cv2.imshow("game of life", show_board)
        else:
            cv2.imshow("game of life", show_board)
        cv2.waitKey(1)

if __name__ == "__main__":
    run()