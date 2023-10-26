#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#!/usr/bin/env python3

import argparse
import cv2

def main():
    
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--Altascar', type=str, help='', default='../home/vitor/Documentos/PSR23-24/my_PSR_23-24/Aula 5/Ex1/atlascar.png')
    #parser.add_argument('Altascar2', type=str, help='', default='../home/vitor/Documentos/PSR23-24/my_PSR_23-24/Aula 5/Ex1/atlascar2.png')

    args =  vars(parser.parse_args())
    print(args)

    image1_filename = 'atlascar.png'
    image2_filename = 'atlascar2.png'
    image1 = cv2.imread(image1_filename, cv2.IMREAD_COLOR) # Load an image
    image2 = cv2.imread(image2_filename, cv2.IMREAD_COLOR)
    

    image_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) 

    retval, image_thresholded = cv2.threshold(image_gray, 234, 255, cv2.THRESH_BINARY)

    print("Pressione qualquer tecla para encerrar o programa...")

    while True:
        cv2.imshow('Atlascar', image1)  # Display the image
        cv2.waitKey(3000) # wait for a key press before proceeding
        cv2.imshow('Atlascar', image2)  # Display the image
        cv2.imshow('Atlascar', image_gray)  # Display the image
        cv2.imshow('Atlascar', image_thresholded)  # Display the image
        cv2.waitKey(3000) # wait for a key press before proceeding

        key = cv2.waitKey(1)
        if key != -1:
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()