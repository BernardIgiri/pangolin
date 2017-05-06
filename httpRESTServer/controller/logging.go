package controller

import "log"

// LogError logs an error
func LogError(logger *log.Logger, err error, endpoint string) {
	logger.Printf("Error: %s at endpoint: %s", err, endpoint)
}

// LogWarning logs a warning
func LogWarning(logger *log.Logger, warning string, endpoint string) {
	logger.Printf("Warning: %s at endpoint: %s", warning, endpoint)
}
