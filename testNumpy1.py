import numpy as np
import matplotlib.pyplot as plt

# Create the numpy array img_hsv
img_hsv = np.zeros((250, 500, 3), np.uint8)

# Visualize the numpy array as an image
plt.imshow(img_hsv)
plt.axis('off')  # Turn off axis
plt.show()