package controller

import (
	"log"
	"net/http"

	"github.com/bernardigiri/PangolinRESTServer/peerService"
	"github.com/gorilla/mux"
)

type faceRecognitionRoutes struct {
	log *log.Logger
	frs *peerService.FaceRecognitionService
}

// ConnectFaceRecognitionRoutes creates controller for face recognition
func ConnectFaceRecognitionRoutes(router *mux.Router, logger *log.Logger,
	faceServerHost string, faceServerPort int, faceRootDir string) {
	frr := faceRecognitionRoutes{
		logger,
		peerService.NewFaceRecognitionService(faceServerHost,
			faceServerPort,
			faceRootDir)}
	router.HandleFunc("/compare/{faceA}/{faceB}", frr.compareFacesEndpoint()).Methods("GET")
}

func (frr *faceRecognitionRoutes) compareFacesEndpoint() func(
	w http.ResponseWriter, req *http.Request) {
	return func(w http.ResponseWriter, req *http.Request) {
		params := mux.Vars(req)
		isMatch, err := frr.frs.CompareFaces(params["faceA"], params["faceB"])
		if err == nil {
			WriteJSONSuccess(w, isMatch)
		} else {
			WriteJSONError(w, ErrorBadParams)
			LogError(frr.log, err, "compareFaces")
		}
	}
}
