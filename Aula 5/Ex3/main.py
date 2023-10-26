#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#!/usr/bin/env python3

import cv2
import numpy
import argparse
from functools import partial

val = 0
window_name = 'window - Ex3a'
image_gray = None


def onTrackbar(val):

    _,thresh = cv2.threshold(image_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, thresh)


def main():

    
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers')
    parser.add_argument('-if', '--image_filename', type=str, required=False, help='', default='../home/vitor/Documentos/PSR23-24/my_PSR_23-24/Aula 5/Ex1/atlascar.png')
    #parser.add_argument('Altascar2', type=str, help='', default='../home/vitor/Documentos/PSR23-24/my_PSR_23-24/Aula 5/Ex1/atlascar2.png')

    args =  vars(parser.parse_args())

    image_filename = args['image_filename']
    image1 = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    global image_gray

    image_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow(window_name)

    cv2.imshow('Original', image1)  # Display the image

    cv2.createTrackbar('Threshold', window_name, 0, 255, onTrackbar)

    cv2.setTrackbarPos('threshold', window_name, val)

    onTrackbar(100)

    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()