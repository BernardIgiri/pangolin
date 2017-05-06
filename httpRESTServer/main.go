package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/bernardigiri/PangolinRESTServer/controller"
	"github.com/gorilla/mux"
)

const logfile = "server.log"
const port = "8080"
const host = ""
const frsHost = "localhost"
const frsPort = 4000
const frsDir = "unknown"

func main() {
	router := mux.NewRouter()
	errorlogFileHandler, err := os.OpenFile(logfile,
		os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		fmt.Printf("error opening file: %v", err)
		os.Exit(1)
	}
	myLog := log.New(errorlogFileHandler,
		"RestServer", log.LUTC|log.LstdFlags|log.Llongfile)
	controller.ConnectFaceRecognitionRoutes(router, myLog, frsHost, frsPort, frsDir)
	log.Fatal(http.ListenAndServe(host+":"+port, router))
}
