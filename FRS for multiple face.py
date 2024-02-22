import os
import cv2
import face_recognition

# Define the paths to the directories containing images for each person
angelina_dir = '/path/to/angelina_images/'
tomcruise_dir = '/path/to/tomcruise_images/'

# Load images and extract face encodings
known_face_encodings = []
known_face_names = []

# Load images for Angelina
for img_path in os.listdir(Angelina_dir):
    img = face_recognition.load_image_file(os.path.join(angelina_dir, img_path))
    face_encoding = face_recognition.face_encodings(img)[0]  # Assume only one face per image
    known_face_encodings.append(face_encoding)
    known_face_names.append('Angelina')

# Load images for Tom Cruise
for img_path in os.listdir(Tom_dir):
    img = face_recognition.load_image_file(os.path.join(tomcruise_dir, img_path))
    face_encoding = face_recognition.face_encodings(img)[0]  # Assume only one face per image
    known_face_encodings.append(face_encoding)
    known_face_names.append('Tom Cruise')


# Initialize webcam
cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame from BGR to RGB (face_recognition uses RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    
    # Iterate through each detected face
    for (top, right, bottom, left) in face_locations:
        # Extract face encoding from the region of interest (ROI)
        face_encoding = face_recognition.face_encodings(rgb_frame, [(top, right, bottom, left)])[0]

        # Compare face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # Check if any known face encoding matches the current face encoding
        if True in matches:
            match_index = matches.index(True)
            name = known_face_names[match_index]

        # Draw rectangle around the face and display name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Exit loop on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
