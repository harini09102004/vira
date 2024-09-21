import cv2


# Create a video capture object to capture video through the webcam
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # Change the camera index as necessary

# Set video frame width and height
cam.set(3, 640)  # Set video frame width
cam.set(4, 480)  # Set video frame height

# Load the Haar Cascade classifier for face detection
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Haar Cascade classifier is an effective object detection method
face_id = input("Enter a Numeric user ID here: ")

# Use a unique integer ID for every new face (e.g., 0,1,2,3, etc.)
print("Taking samples, look at the camera.......")

# Initialize the sampling face count
count = 0

while True:
    # Read the frames using the video capture object
    ret, img = cam.read()

    if not ret:
        print("Failed to capture image.")
        break

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around the detected faces and save samples
    for (x, y, w, h) in faces:
        count += 1
        # Draw rectangle on the face
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Save the captured image in the dataset folder
        cv2.imwrite("samples/face." +str(face_id) + "." +str(count)+".jpg", gray[y:y+h, x:x+w])

        # Display the image with a rectangle around the face
        cv2.imshow('image', img)

    # Break the loop when 'q' is pressed or enough samples are taken
    if cv2.waitKey(100) & 0xFF == ord('q') or count >= 30:
        break

# Release the video capture object and close all windows
print("samples are taken thank you for your co-operation.....")
cam.release()
cv2.destroyAllWindows()
