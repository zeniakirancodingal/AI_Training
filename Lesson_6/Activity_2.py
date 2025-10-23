import cv2

image = cv2.imread('./bird.jpeg')

if image is None:
    print("Error: Could not read image!")

# convert image into grayscale image
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize the image to a specific size 
resized = cv2.resize(gray_img, (500, 500))  # width = 500, height = 500

# Display the resized image
cv2.imshow('Resized Image', resized)

cv2.waitKey(0)  # Wait for a key press

cv2.destroyAllWindows()  # Close the window

 

# Print image properties

print(f"Image Dimensions: {image.shape}")  # Height, Width, Channels