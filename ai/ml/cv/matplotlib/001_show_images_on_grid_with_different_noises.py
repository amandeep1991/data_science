import matplotlib

import cv2
import numpy as np

from directory_utils import change_directory_to_data
from ml.utils.visual_utils import show_grid_via_matplotlib

absolute_input_image_path = change_directory_to_data() + "/001_TheGorgeousDishaPatani.jpg"
gorgeous_disha = cv2.imread(absolute_input_image_path, cv2.IMREAD_COLOR)
gorgeous_disha = matplotlib.image.imread(absolute_input_image_path, cv2.IMREAD_COLOR)

# cv2.imshow("No Noise", gorgeous_disha)

image = gorgeous_disha.copy()
# Add noises to the image
noise_minor = image + 3 * np.std(image) * np.random.random(image.shape)
noise_alot = 2 * image.max() * np.random.random(image.shape)
noise_major = image + noise_alot

show_grid_via_matplotlib(2, 2, {
    'no_noise'   : image,
    'noise_minor': noise_minor,
    'noise_major': noise_major,
    'noise_alot' : noise_alot}, matplotlib.colors.to_rgb).show()

# cv2.imshow("Salt Noise", gorgeous_disha_1)
cv2.waitKey(0)
cv2.destroyAllWindows()