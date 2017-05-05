import face_recognition
import os

class faceRecognizer:
	def __init__(self, rootDir):
		self.rootDir = rootDir
	def isMatch(self, faceAPath, faceBPath):
		print(os.path.join(self.rootDir, faceBPath.lstrip("/")))
		faceAImage = face_recognition.load_image_file(os.path.join(self.rootDir, faceAPath.lstrip("/")))
		faceBImage = face_recognition.load_image_file(os.path.join(self.rootDir, faceBPath.lstrip("/")))
		faceAEncoding = face_recognition.face_encodings(faceAImage)[0]
		faceBEncoding = face_recognition.face_encodings(faceBImage)[0]
		results = face_recognition.compare_faces([faceAEncoding], faceBEncoding)
		return results[0]
