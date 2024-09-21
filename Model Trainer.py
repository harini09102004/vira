import cv2
import numpy as np
from PIL import Image
import os
# Path for samples already taken
path = 'samples'

# Local Binary Patterns Histograms recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the Haar Cascade classifier for face detection
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Function to fetch the images and labels
def Images_And_Labels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    
    # Iterate through image paths
    for imagePath in imagePaths:
        # Convert it to grayscale
        gray_img = Image.open(imagePath).convert('L')  # Using PIL to open image and convert to grayscale
        img_arr = np.array(gray_img, 'uint8')  # Creating an array
        
        # Extract the ID from the image filename (assuming filenames follow the pattern: User.ID.Number.jpg)
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        
        # Detect faces in the image array
        faces = detector.detectMultiScale(img_arr)
        
        # For each detected face, append the face region and the corresponding ID
        for (x, y, w, h) in faces:
            faceSamples.append(img_arr[y:y+h, x:x+w])
            ids.append(id)
    
    return faceSamples, ids

# Main part of the code to train the recognizer
print("Training faces. This will take a few seconds. Please wait...")

# Get the faces and their corresponding IDs
faces, ids = Images_And_Labels(path)

# Train the recognizer with the faces and IDs
recognizer.train(faces, np.array(ids))

# Save the trained model as 'trainer.yml'
recognizer.write('trainer/trainer.yml')

print("Model trained. Now we can recognize your face.")