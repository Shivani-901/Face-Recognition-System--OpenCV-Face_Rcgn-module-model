
import os
import cv2
import face_recognition

# Define the path to the directory containing images for the new person
new_person_dir = '/path/to/new_person_images/'

# Load images and extract face encodings for the new person
new_person_face_encodings = []
new_person_face_names = []

# Load images for the new person
for img_path in os.listdir(new_person_dir):
    img = face_recognition.load_image_file(os.path.join(new_person_dir, img_path))
    face_encoding = face_recognition.face_encodings(img)[0]  # Assume only one face per image
    new_person_face_encodings.append(face_encoding)
    new_person_face_names.append('NewPerson')  # Add the label for the new person

# Add the new person's face encodings to the known face encodings
known_face_encodings += new_person_face_encodings
known_face_names += new_person_face_names
