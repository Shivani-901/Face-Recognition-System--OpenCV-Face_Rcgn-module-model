**Description:**
This face recognition project uses the Face Recognition library in Python to recognize faces in real-time using a webcam. It loads pre-trained face encodings from images of known individuals, compares them with the face encodings of detected faces in the webcam feed, and assigns a name to the recognized faces based on the closest match.

**Steps to Execute the Project:**

Install Required Libraries:
Make sure you have Python installed on your system along with the necessary ****libraries like OpenCV and Face Recognition**. **You can install these libraries using pip:**pip install opencv-python face-recognition**


**Prepare Training Data:**
Organize your training data by creating directories for each person you want to recognize. Each directory should contain multiple images of the respective person's face.

**Update the Code:**
Modify the Python script to point to the directories containing images of known individuals. Update the angelina_dir and tomcruise_dir variables with the actual paths to the directories.

**Run the Script:**
Execute the Python script by running it in your preferred Python environment. Make sure you have a webcam connected to your system.

Copy code
**python your_script_name.py**
Face Recognition:
Once the script is running, it will capture the webcam feed and attempt to recognize faces in real-time. The recognized faces will be labeled with the corresponding names assigned to them.

**Quit the Program:**
Press 'q' on your keyboard to exit the program and close the webcam feed.

Note:
Ensure that the images used for training have good quality and clear visibility of the faces.
Experiment with different face recognition parameters and thresholds to improve accuracy if needed.
You may need to adjust the paths and directories according to your system configuration and file structure.
Feel free to customize the script further to suit your specific requirements or integrate it into larger projects.
