import face_recognition

known_face = face_recognition.load_image_file("resources/faces/barack-obama.jpg");
unknown_face = face_recognition.load_image_file("resources/faces/President_Barack_Obama.jpg");

known_faces = [known_face];

results = face_recognition.compare_face(known_faces, unknown_face);

print("Is the face known? {}".format(results[0]))
