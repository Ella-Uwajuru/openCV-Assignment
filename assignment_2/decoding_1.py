import cv2
import numpy as np

# Read the image
image = cv2.imread("img1.jpg")

if image is None:
    print("Error: Could not read image. Make sure img1.jpg exists.")
    exit(1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create barcode detector
barcode_detector = cv2.barcode_BarcodeDetector()

# Detect and decode
retval, decoded_info, decoded_type, points = barcode_detector.detectAndDecode(gray)

if retval:
    print(f"Decoded Data: {decoded_info}")
    print(f"Barcode Type: {decoded_type}")
else:
    print("No barcode detected")

cv2.imshow("Barcode", image)
cv2.waitKey(0)
cv2.destroyAllWindows()