import cv2

# Initialize LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml')  # Load trained model

# Load Haar Cascade for face detection
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)  # Initialize haar cascade for object detection

# Define font for displaying name and accuracy on the video frame
font = cv2.FONT_HERSHEY_SIMPLEX  # Font type

# List of names (Ensure the index corresponds to the face ID)
names = ['', 'harini']  # Leave the first index empty as the ID counter starts from 1

# Initialize video capture (0 for the default camera)
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to avoid warnings

# Set video frame width and height
cam.set(3, 640)  # Set video frame width
cam.set(4, 480)  # Set video frame height

# Define minimum window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

# Start video capture loop
while True:
    ret, img = cam.read()  # Read the frames from the video
    if not ret:
        break

    # Convert the image to grayscale (necessary for face detection)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    # For each detected face, predict the ID and accuracy
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around the face

        # Predict the face
        id, accuracy = recognizer.predict(gray[y:y+h, x:x+w])

        # Check if accuracy is less than 100 (0 means a perfect match)
        if accuracy < 100:
            name = names[id] if id < len(names) else "Unknown"
            accuracy_text = " {0}%".format(round(100 - accuracy))
        else:
            name = "Unknown"
            accuracy_text = " {0}%".format(round(100 - accuracy))

        # Display the name and accuracy on the video frame
        cv2.putText(img, str(name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(accuracy_text), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    # Display the video frame with detection
    cv2.imshow('camera', img)

    # Break the loop if 'ESC' key is pressed
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()
