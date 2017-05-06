package peerService

import (
	"bufio"
	"fmt"
	"net"
	"path"
	"strconv"
)

// FaceRecognitionService processes face recognition requests
type FaceRecognitionService struct {
	server  string
	rootDir string
}

// NewFaceRecognitionService creates new FaceRecognitionService
func NewFaceRecognitionService(host string,
	port int,
	rootDir string) *FaceRecognitionService {
	return &FaceRecognitionService{
		host + ":" + strconv.Itoa(port),
		rootDir}
}

// CompareFaces compares two faces and returns true if they match
func (frs *FaceRecognitionService) CompareFaces(pathA, pathB string) (bool, error) {
	var connection net.Conn
	var err error
	var result string
	connection, err = net.Dial("tcp", frs.server)
	defer connection.Close()
	if err != nil {
		return false, err
	}
	fmt.Fprintf(connection, `{"action":"compare","faceA":"%s","faceB":"%s"}`,
		path.Join(frs.rootDir, pathA),
		path.Join(frs.rootDir, pathB))
	result, err = bufio.NewReader(connection).ReadString('\n')
	return result == "true\n", err
}
