package controller

import (
	"log"

	"github.com/gorilla/mux"
)

// Controller interface for route controllers
type Controller interface {
	New(router *mux.Router, log *log.Logger) error
}
