import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image"""
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def apply_edge_detection(image, method='sobel', ksize=3, threshold1=100, threshold2=200):
    """Applies the selected edge detection method"""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if method == 'sobel':
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=ksize)
        edge_image = cv2.magnitude(sobelx, sobely)
    elif method == 'laplacian':
        edge_image = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=ksize)
    elif method == 'canny':
        edge_image = cv2.Canny(gray_image, threshold1, threshold2)
    elif method == 'gaussian':
        blurred_image = cv2.GaussianBlur(gray_image, (ksize, ksize), 0)
        edge_image = cv2.Canny(blurred_image, threshold1, threshold2)
    else:
        raise ValueError("Invalid edge detection method")

    return edge_image

def main():
    """Interactive utility for edge detection and filtering"""
    image = cv2.imread('sample.jpg')
    if image is None:
        print("Error: Image not found!")
        return

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Laplacian Edge Detection")
    print("3. Canny Edge Detection")
    print("4. Gaussian Filtering")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            ksize = int(input("Enter kernel size for Sobel (odd number): "))
            edge_image = apply_edge_detection(image, method='sobel', ksize=ksize)
            display_image("Sobel Edge Detection", edge_image)
        elif choice == '2':
            ksize = int(input("Enter kernel size for Laplacian (odd number): "))
            edge_image = apply_edge_detection(image, method='laplacian', ksize=ksize)
            display_image("Laplacian Edge Detection", edge_image)
        elif choice == '3':
            threshold1 = int(input("Enter first threshold for Canny: "))
            threshold2 = int(input("Enter second threshold for Canny: "))
            edge_image = apply_edge_detection(image, method='canny', threshold1=threshold1, threshold2=threshold2)
            display_image("Canny Edge Detection", edge_image)
        elif choice == '4':
            ksize = int(input("Enter kernel size for Gaussian smoothing (odd number): "))
            threshold1 = int(input("Enter first threshold for Canny: "))
            threshold2 = int(input("Enter second threshold for Canny: "))
            edge_image = apply_edge_detection(image, method='gaussian', ksize=ksize, threshold1=threshold1, threshold2=threshold2)
            display_image("Gaussian Smoothed Image", edge_image)
        elif choice == '5':
                        break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()