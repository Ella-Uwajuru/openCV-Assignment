import cv2  

image = cv2.imread('C:/Users/Pacis/Desktop/year 3/robotics/OpenCV-Masterclass-main/Basic_Operations/assignment-001-given.jpg')
cv2.rectangle(image, (263, 185), (991, 924), (0, 255, 0), 8)
cv2.addWeighted(cv2.rectangle(image.copy(), (815, 70), (1250, 182), (0, 0, 0), -1), 0.5, image, 1 - 0.5, 0, dst=image)
cv2.putText(image, 'RAH972U', (820, 160), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 7)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.imwrite('C:/Users/Pacis/Desktop/year 3/robotics/OpenCV-Masterclass-main/Basic_Operations/assignment_done.jpg', image)
cv2.destroyAllWindows()