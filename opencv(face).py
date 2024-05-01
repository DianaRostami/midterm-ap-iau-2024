import cv2

# Load cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Check if the cascade is loaded successfully
if face_cascade.empty():
    print("Error: Cascade Classifier not loaded!")
    exit(0)
