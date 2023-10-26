#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#!/usr/bin/env python3

import argparse
from functools import partial

import cv2
import numpy as np
from colorama import Fore, Style

def mouseCallBack (event, x, y, flags, *userdata, image, drawing_data):
    
    #print('x=' + str(x) + ', y=' + str(y))
    if event == cv2.EVENT_LBUTTONDOWN:
        print('pencil is down')
        drawing_data['pencil_down'] = True
        

    elif event == cv2.EVENT_LBUTTONUP:
        print('pencil is up')
        drawing_data['pencil_down'] = False
    
    if drawing_data['pencil_down'] == True:
        #cv2.circle(image, (x, y), 2, (255, 255, 255), -1)
        cv2.line(image, (drawing_data['previous_x'], drawing_data['previous_y']), (x, y), drawing_data['pencil_color'], 2) 

    drawing_data['previous_x'] = x
    drawing_data['previous_y'] = y


def main():

    #---------------------------------------------
    #       Initialization 
    #---------------------------------------------
    
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-if', '--Altascar', type=str, help='', default='../home/vitor/Documentos/PSR23-24/my_PSR_23-24/Aula 6/Ex1/atlascar.png')
    #parser.add_argument('Altascar2', type=str, help='', default='../home/vitor/Documentos/PSR23-24/my_PSR_23-24/Aula 5/Ex1/atlascar2.png')

    args =  vars(parser.parse_args())
    print(args)

    image_filename = 'atlascar.png'
    #image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image = np.ones((400, 600, 3),dtype=np.uint8) * 255
    

    drawing_data = {'pencil_down' : False, 'previous_x' : 0, 'previous_y' : 0, 'pencil_color' : (255, 255, 255)}

    window_name = 'Video'
    h, w, nc = image.shape
    capture = cv2.VideoCapture(0)
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback(window_name, partial(mouseCallBack, image=image, drawing_data=drawing_data))

        
    
    #---------------------------------------------
    #       Execution
    #---------------------------------------------
    
    # Draw circle in image

    center_coordinates = (320, 180)
    radius = 20
    color = (255, 0 , 0)
    tickness = (40)
    cv2.circle(image, center_coordinates, radius, color, tickness)

    

    # Write PSR in image

    image = cv2.putText(image, 'PSR', (50, 60), cv2.FONT_HERSHEY_SIMPLEX, 2,  
                (0,0,255), 2, cv2.LINE_AA, False) 
    

    #---------------------------------------------
    #       visaulisation
    #---------------------------------------------

    while True:

        _, image = capture.read()
        cv2.imshow(window_name, image)  # Display the image

        key = cv2.waitKey(1)
        if key == ord('r'):
            drawing_data['pencil_color'] = (0, 0, 255)
            print('Change pencil color to red')
        if key == ord('g'):
            drawing_data['pencil_color'] = (0, 255, 0)
            print('Change pencil color to green')  
        if key == ord('b'):
            drawing_data['pencil_color'] = (255, 0, 0)
            print('Change pencil color to blue')
        if key == ord('q'):
            print("Programa a encerrar")
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()