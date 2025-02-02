import cv2
import numpy as np

# Read the image
image = cv2.imread("img2.jpg")

if image is None:
    print("Error: Could not read image. Make sure img2.jpg is in the same folder as this script.")
    exit(1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create QR code detector (can also detect Data Matrix)
detector = cv2.QRCodeDetector()

# Detect and decode
try:
    data, bbox, _ = detector.detectAndDecode(gray)
    
    if bbox is not None:
        # Convert points to integers
        bbox = bbox.astype(int)
        
        # Draw green boundary
        for i in range(len(bbox)):
            cv2.line(image, 
                     tuple(bbox[i][0]), 
                     tuple(bbox[(i+1) % len(bbox)][0]), 
                     (0, 255, 0), 
                     2)
        
        if data:
            print(f"Decoded Data: {data}")
            # Add text above code
            cv2.putText(image, data, 
                        (bbox[0][0][0], bbox[0][0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        else:
            print("Code detected but couldn't decode data")
    else:
        print("No code detected in image")

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Save the result
cv2.imwrite("decoded_datamatrix.png", image)
print("Annotated image saved as decoded_datamatrix.png")

# Show the result
cv2.imshow("Decoded Data Matrix", image)
print("Press any key to close the window")
cv2.waitKey(0)
cv2.destroyAllWindows() 