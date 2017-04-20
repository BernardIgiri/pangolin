#!/usr/bin/env python
import face_recognition
import os

root_dir = os.path.dirname(os.path.abspath(__file__))

known_picture = face_recognition.load_image_file(root_dir + "/resources/faces/known/barack-obama.jpg");
unknown_picture = face_recognition.load_image_file(root_dir + "/resources/faces/unknown/President_Barack_Obama.jpg");

known_encoding = face_recognition.face_encodings(known_picture)[0];
unknown_encoding = face_recognition.face_encodings(unknown_picture)[0];

results = face_recognition.compare_faces([known_encoding], unknown_encoding);

print("Is the face known? {}".format(results[0]))
