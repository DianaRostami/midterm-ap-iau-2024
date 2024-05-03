import cv2

# Load cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Check if the cascade is loaded successfully
if face_cascade.empty():
    print("Error: Cascade Classifier not loaded!")
    exit(0)
# Load image (write the path of image you want to check)
our_image_color = cv2.imread("c:\\Users\\lenovo\\Pictures\\people.jpg")

# Convert image to grayscale
our_image_gray = cv2.cvtColor(our_image_color, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(our_image_gray, scaleFactor=1.05, minNeighbors=5)

# Draw a rectangle around each face
for x, y, w, h in faces:
    cv2.rectangle(our_image_color, (x, y), (x+w, y+h), (0, 255, 0), 3)

# Show image
cv2.imshow("Face Detection", our_image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
