import matplotlib
import cv2
import numpy as np

from directory_utils import add_resources_to_path
from ml.utils.visual_utils import show_grid_via_matplotlib

absolute_input_image_path = add_resources_to_path() + "/001_TheGorgeousDishaPatani.jpg"
gorgeous_disha = cv2.imread(absolute_input_image_path, cv2.IMREAD_COLOR)


image = gorgeous_disha.copy()
# I just resized the image to a quarter of its original size
image = cv2.resize(image, (0, 0), None, .25, .25)
grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# Make the grey scale image have three channels
grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
numpy_vertical = np.vstack((image, grey_3_channel))
numpy_horizontal = np.hstack((image, grey_3_channel))
numpy_vertical_concat = np.concatenate((image, grey_3_channel), axis=0)
numpy_horizontal_concat = np.concatenate((image, grey_3_channel), axis=1)

# cv2.imshow('Main', image)
cv2.imshow('Numpy Vertical', numpy_vertical)
# cv2.imshow('Numpy Horizontal', numpy_horizontal)
# cv2.imshow('Numpy Vertical Concat', numpy_vertical_concat)
# cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

cv2.waitKey()