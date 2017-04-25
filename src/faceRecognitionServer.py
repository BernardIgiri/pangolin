import socket, select, json, faceRecognizer

class faceRecognitionServer:
	def __init__(self, port, bufferSize, numberOfConnections, faceRootDirectory):
		self.connectionList = []
		self.bufferSize = bufferSize
		self.port = port
		self.numberOfConnections = numberOfConnections
		self.running = False
		self.faceRecognizer = faceRecognizer.faceRecognizer(faceRootDirectory)
	def run(self):
		self.running = True
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.serverSocket.bind(("0.0.0.0", self.port))
		self.serverSocket.listen(self.numberOfConnections)
		self.connectionList.append(self.serverSocket)
		print("Face recognition server started on port " + str(self.port))
		while self.running:
			readSockets,writeSockets,errorSockets = select.select(self.connectionList,[],[])
			for clientSocket in readSockets:
				if clientSocket == self.serverSocket:
					client, address = self.serverSocket.accept()
					self.connectionList.append(client)
					print("Client (%s, %s) connected" % address)
				else:
					try:
						data = clientSocket.recv(self.bufferSize)
						if data:
							text = data.decode('utf-8').strip()
							try:
								request = json.loads(text)
								if request['action'] == 'close':
									self.closeClient(clientSocket, address)
								elif request['action'] == 'exit':
									self.closeClient(clientSocket, address)
									self.exit()
								elif request['action'] == 'compare':
									if self.faceRecognizer.isMatch(request['known'], request['unknown']):
										clientSocket.send('true\n'.encode('utf-8'))
									else:
										clientSocket.send('false\n'.encode('utf-8'))
								elif request['action'] == 'test':
									clientSocket.send('Test okay.\n'.encode('utf-8'))
							except BaseException as e:
								print("Uknown error")
								print(e)
								continue
					except BaseException as e:
						print("Uknown error")
						print(e)
						self.closeClient(clientSocket, address)
						continue
		self.serverSocket.close()
	def exit(self):
		print('Exiting...')
		self.running = False
		self.serverSocket.shutdown(socket.SHUT_RDWR)
		self.serverSocket.close()
	def close(self):
		print('Closing...')
		self.serverSocket.close()
	def closeClient(self, clientSocket, address):
		if clientSocket in self.connectionList:
			print("Client (%s, %s) is now offline" % address)
			clientSocket.close()
			self.connectionList.remove(clientSocket)
