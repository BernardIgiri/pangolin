import threading, socketserver, json, faceRecognizer

class faceRecognitionServer:
	def __init__(self, port, bufferSize, numberOfConnections, faceRootDirectory):
		runner = self
		self.faceRecognizer = faceRecognizer.faceRecognizer(faceRootDirectory)
		class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
			def handle(self):
				isOpen = True
				while isOpen:
					data = self.request.recv(bufferSize)
					if data:
						text = data.decode('utf-8').strip()
						try:
							request = json.loads(text)
							if request['action'] == 'close':
								isOpen = False
								print("Client {0[0]}:{0[1]} disconnected.".format(self.client_address))
								self.request.sendall("Goodbye.\n".encode('utf-8'))
							elif request['action'] == 'shutdown':
								isOpen = False
								print("Client {0[0]}:{0[1]} requesting shutdown.".format(self.client_address))
								self.request.sendall('Shutting down...\n'.encode('utf-8'))
								runner.exit()
							elif request['action'] == 'compare':
								isOpen = False
								print(request)
								if runner.faceRecognizer.isMatch(request['faceA'], request['faceB']):
									self.request.sendall('true\n'.encode('utf-8'))
								else:
									self.request.sendall('false\n'.encode('utf-8'))
							elif request['action'] == 'test':
								self.request.sendall("Test okay.\n".encode('utf-8'))
						except BaseException as e:
							print("Uknown error {}".format(str(e)))
							continue
		class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
			pass
		host = '0.0.0.0'
		self.server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
	def run(self):
		serverThread = threading.Thread(target=self.server.serve_forever)
		serverThread.daemon = True
		serverThread.start()
		print("Face recognition server started on {0[0]}:{0[1]}".format(self.server.server_address))
		serverThread.join()
	def exit(self):
		print("Server shutting down...")
		self.server.shutdown()
		self.server.server_close()
