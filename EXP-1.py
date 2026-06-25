import cv2

# Read image
img = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\image-1.jpg")

# Resize image
img = cv2.resize(img, (600, 400))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show original image
cv2.imshow("Original Image", img)

# Show grayscale image
cv2.imshow("Gray Scale Image", gray)

# Wait until key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
