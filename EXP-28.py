import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\house.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:

    # Sobel along X-axis
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

    # Sobel along Y-axis
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Gradient Magnitude
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize to 0-255
    gradient_magnitude = cv2.normalize(
        gradient_magnitude,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    gradient_magnitude = np.uint8(gradient_magnitude)

    # Save output
    cv2.imwrite(r"C:\Users\tejv3\OneDrive\Desktop\sobel_output.jpg",
                gradient_magnitude)

    print("Output saved as sobel_output.jpg")

else:
    print("Error: Could not load the image.")
