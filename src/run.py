#!/usr/bin/env python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), 'src'))
import faceRecognitionServer

from optparse import OptionParser

defaultRoot = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

parser = OptionParser(version="%prog 0.1")
parser.add_option(
	"-p",
	"--port",
	dest="port",
	help="Server port",
	default=4000)
parser.add_option(
	"-b",
	"--buffer",
	dest="buffer",
	help="Buffer Size",
	default=4096)
parser.add_option(
	"-c",
	"--connections",
	dest="connections",
	help="Max number of connections",
	default=10)
parser.add_option(
	"-d",
	"--data-root",
	dest="rootDir",
	help="Root directory of files",
	default=defaultRoot)

(options, args) = parser.parse_args()

core = faceRecognitionServer.faceRecognitionServer(
	int(options.port),
	int(options.buffer),
	int(options.connections),
	options.rootDir)
core.run()
