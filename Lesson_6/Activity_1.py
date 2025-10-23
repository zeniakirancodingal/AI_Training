import cv2

image = cv2.imread('./bird.jpeg')

if image is None:
    print("Error: Could not read image!")
# Resize the window to a specific size without resizing the image

resized = cv2.resize(image, (500, 500))  # width = 500, height = 500

# Display the resized image
cv2.imshow('Resized Image', resized)

cv2.waitKey(0)  # Wait for a key press

cv2.destroyAllWindows()  # Close the window

 

# Print image properties

print(f"Image Dimensions: {image.shape}")  # Height, Width, Channels