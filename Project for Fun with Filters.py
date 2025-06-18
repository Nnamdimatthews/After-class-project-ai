import cv2
import numpy as np

def display_image(title, image):
    """Utility function to display an image"""
    cv2.imshow(title, image)
    cv2.waitKey(0)  # Wait indefinitely until any key is pressed
    cv2.destroyAllWindows()

def apply_filter(image, filter_type, intensity=0):
    """Apply specified filter type to the image"""
    filtered_image = None

    if filter_type == 'gray':
        filtered_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'binary':
        _, filtered_image = cv2.threshold(image, intensity, 255, cv2.THRESH_BINARY)
    elif filter_type == 'binary_inv':
        _, filtered_image = cv2.threshold(image, intensity, 255, cv2.THRESH_BINARY_INV)
    elif filter_type == 'trunc':
        _, filtered_image = cv2.threshold(image, intensity, 255, cv2.THRESH_TRUNC)
    elif filter_type == 'tozero':
        _, filtered_image = cv2.threshold(image, intensity, 255, cv2.THRESH_TOZERO)
    elif filter_type == 'tozero_inv':
        _, filtered_image = cv2.threshold(image, intensity, 255, cv2.THRESH_TOZERO_INV)

    return filtered_image

def main():
    """Main function to apply filters to the image"""
    filename = input("Enter the filename of the image (without extension): ")
    filter_type = input("Enter the filter type (gray, binary, binary_inv, trunc, tozero, tozero_inv): ")
    intensity = int(input("Enter the intensity value (0-255) if applicable: "))

    image = cv2.imread(f"{filter}.jpg")