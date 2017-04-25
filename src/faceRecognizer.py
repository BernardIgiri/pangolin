import face_recognition
import os

class faceRecognizer:
	def __init__(self, rootDir):
		self.rootDir = rootDir
	def isMatch(self, knownFacePath, unknownFacePath):
		knownPicture = face_recognition.load_image_file(self.rootDir + knownFacePath)
		unknownPicture = face_recognition.load_image_file(self.rootDir + unknownFacePath)
		knownEncoding = face_recognition.face_encodings(knownPicture)[0]
		unknownEncoding = face_recognition.face_encodings(unknownPicture)[0]
		results = face_recognition.compare_faces([knownEncoding], unknownEncoding)
		return results[0]
