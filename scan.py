import cv2

image = cv2.imread('1.jpg')
decoder = cv2.QRCodeDetector()
data, coordinates, _ = decoder.detectAndDecode(image)

print("Data: ", data)
print("Coordinates: ", coordinates)

cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()