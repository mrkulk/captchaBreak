import zmq
import sys
from Renderer import *


LOAD_IMAGE = 1
LOAD_XRP = 2
RENDER_IMAGE = 3
GET_LIKELIHOOD = 4

port = 5555
context = zmq.Context()
print "Connedting to Server ..."

socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

r = Renderer()

def dispatch(message):
	op,args = parse(message)
	if op == LOAD_IMAGE:
		r.loadImage(args['filename'])
		return 1
	else if op == LOAD_XRP:
		return 1
	else if op == RENDER_IMAGE:
		r.renderImage(args['params'])
		return 1
	else if op == GET_LIKELIHOOD:
		return getLogLikelihood()
	else 
		print "[ERROR] Cannot recognize OPCODE"
		return -1


while True:
	message = socket.recv()
	print "Recieved reply", request, "[", message, "]"
	dispatch(message)
	print "Sending request", request, "..."
	socket.send("Hello")

