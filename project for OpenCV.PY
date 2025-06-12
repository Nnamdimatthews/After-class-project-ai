import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('sonic_colors_4_/neurips.jpg')

# Convert to RGB for displaying with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = image.shape

# Add 5-directional arrow for width visualization
arrow_start_left = (20, height - 50)  # Left starting point
arrow_end_right = (width - 20, height - 50)  # Right end point

# Draw arrows in both directions
cv2.arrowedLine(image_rgb, arrow_start_left, arrow_end_right, (255, 0, 0), 1, tipLength=0.05) # Left-right arrow
cv2.arrowedLine(image_rgb, arrow_end_right, arrow_start_left, (255, 0, 0), 1, tipLength=0.05) # Right-left arrow

# Annotate the width value
width_text_position = (width // 2 - 100, height - 35)

# Save the annotated image
cv2.imwrite('output_image/annotated_width.jpg', image_rgb)

# Display the annotated image
plt.imshow(cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB))
plt.title('Image Width Visualization with Arrow')
plt.axis('off')
plt.show()