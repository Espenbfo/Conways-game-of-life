""" An implementation of Conway's game of life
 using numpy and scipy"""

import cv2
import numpy as np
import scipy.signal

SIZE_X = int(1000/2)
SIZE_Y = int(1000/2)
SCALE = 2

area = 3
FPS = 24
video_length = 40*FPS
def apply_logic(board):
    convolve = scipy.signal.convolve2d(board, np.ones((area,area)), "same")
    new_board = np.where(((board == 1) & ((convolve == 3) | (convolve == 4))) |
                         (board == 0) & (convolve == 3), 1.,0.)
    return new_board#new_board


def run(display=True, save_as=None):
    board = np.round(np.random.random((SIZE_Y, SIZE_X)) * 0.9)

    if save_as is not None:
        saving = True
        video = cv2.VideoWriter(save_as, cv2.VideoWriter_fourcc(*'mp4v'), FPS, (int(SIZE_X*SCALE), int(SIZE_Y*SCALE)))

    else:
        saving = False

    for frame in range(video_length):
        if (frame+1)%100 == 0:
            print("frame",frame+1,"of",video_length)

        board = apply_logic(board)

        if SCALE > 1:
            show_board =np.kron(board, np.ones((SCALE, SCALE), dtype=board.dtype))
            if saving:
                video.write(np.stack([show_board*255,show_board*255,show_board*255], axis=2).astype("uint8"))
            if display:
                cv2.imshow("game of life", show_board)
        else:
            if saving:
                print(board.shape)
                video.write(np.stack([board*255,board*255,board*255], axis=2).astype("uint8"))#)
            if display:
                cv2.imshow("game of life", board)

        if display:
            cv2.waitKey(1)

    if saving:
        video.release()
if __name__ == "__main__":
    run(display=True, save_as="conway.mp4")