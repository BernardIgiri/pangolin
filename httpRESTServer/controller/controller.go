package controller

import (
	"encoding/json"
	"net/http"
)

// ErrorJSON response for web service call errors
type ErrorJSON struct {
	Success   bool   `json:"success"`
	ErrorName string `json:"error"`
}

// SuccessJSON response for web service calls
type SuccessJSON struct {
	Success  bool        `json:"success"`
	Response interface{} `json:"response"`
}

// NewErrorJSON creates ErrorJSON stuct with proper defaults
func NewErrorJSON(errorName string) ErrorJSON {
	return ErrorJSON{
		false,
		errorName}
}

// NewSuccessJSON creates SuccessJSON stuct with proper defaults
func NewSuccessJSON(response interface{}) SuccessJSON {
	return SuccessJSON{
		true,
		response}
}

// WriteJSONSuccess returns success json message to http client
func WriteJSONSuccess(w http.ResponseWriter, response interface{}) error {
	return WriteJSON(w, NewSuccessJSON(response))
}

// WriteJSONError returns error json message to http client
func WriteJSONError(w http.ResponseWriter, errorName string) error {
	return WriteJSON(w, NewErrorJSON(errorName))
}

// WriteJSON returns json message to http client
func WriteJSON(w http.ResponseWriter, value interface{}) error {
	w.Header().Set("Content-Type", "application/json")
	return json.NewEncoder(w).Encode(value)
}
