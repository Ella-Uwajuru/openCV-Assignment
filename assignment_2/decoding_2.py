import ctypes
import cv2
from pylibdmtx.pylibdmtx import decode

try:
    ctypes.windll.LoadLibrary(r"C:\Users\Pacis\AppData\Local\Programs\Python\Python312\Lib\site-packages\pylibdmtx\libdmtx-64.dll")
except OSError as e:
    print(f"Error loading libdmtx-64.dll: {e}")
    exit(1)

# Load the image
image_path = "img2.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"Error: Could not load image {image_path}. Check if the file exists.")
    exit(1)

# Decode the Data Matrix
decoded_objects = decode(image, timeout=500)

if not decoded_objects:
    print("No Data Matrix code found in the image.")
else:
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
        print("Decoded Data:", data)

# Save and display the image
output_file = "decoded_datamatrix_code.png"
cv2.imwrite(output_file, image)
print(f"Annotated image saved as {output_file}")

cv2.imshow("Decoded Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
