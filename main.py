import numpy as np
import cv2 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path')      # option that takes a value
args = parser.parse_args()

# Read color image
path = './sceneL.png'
path_horz = './scene_hor.png'
path_vert = './scene_vert.png'
img = cv2.imread(path)

# Convert the RGB image to a grayscaled image
# 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue
img_g = img[:,:,0] * 0.299 + img[:,:,1] * 0.114 + img[:,:,2] * 0.587
#cv2.imwrite(path_write, img_g)

# Kernel for horizontal sobel filtering
kernel1 = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
# Kernel for horizontal sobel filtering
kernel2 = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])

# Applying the filter2D() function
img_horz = cv2.filter2D(src=img_g, ddepth=-1, kernel=kernel1)
cv2.imwrite(path_horz, img_horz)

img_vert = cv2.filter2D(src=img_g, ddepth=-1, kernel=kernel2)
cv2.imwrite(path_vert, img_vert)
