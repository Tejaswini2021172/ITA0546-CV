import cv2

img = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\house.jpg")
logo = cv2.imread(r"C:\Users\tejv3\OneDrive\Desktop\coffee.jpg")

logo = cv2.resize(logo, (100, 100))

h_logo, w_logo, _ = logo.shape
h_img, w_img, _ = img.shape

center_y = h_img // 2
center_x = w_img // 2

top_y = center_y - h_logo // 2
left_x = center_x - w_logo // 2

bottom_y = top_y + h_logo
right_x = left_x + w_logo

roi = img[top_y:bottom_y, left_x:right_x]

result = cv2.addWeighted(roi, 1, logo, 0.5, 0)

img[top_y:bottom_y, left_x:right_x] = result

cv2.imwrite(r"C:\Users\tejv3\OneDrive\Desktop\watermarked.jpg", img)

print("Watermarked image saved successfully!")
