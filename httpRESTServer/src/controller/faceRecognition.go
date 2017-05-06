package controller

import (
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

var myLog log.Logger
var myRouter mux.Router

// New creates new faceRecognition route controller
func New(router *mux.Router, logger *log.Logger) error {
	router.HandleFunc("/compare", compareFaceEndpoint).Methods("GET")
	return nil
}

func compareFaceEndpoint(w http.ResponseWriter, req *http.Request) {
	//w.Header().Set("Content-Type", "application/json")
	w.Write([]byte("Hello Go"))
}
