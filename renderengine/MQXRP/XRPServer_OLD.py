import zmq
import sys
from Renderer import *
import pdb

LOAD_XRP = 1
LOAD_IMAGE = 2
RENDER_IMAGE = 3
GET_LIKELIHOOD = 4

port = 4444
context = zmq.Context()
print "Starting Server ..."

socket = context.socket(zmq.REP)
socket.bind("tcp://*:" + str(port))

r = Renderer()

def dispatch(message):
	message = message.split(":")
	op = int(message[0])
	print "\n", "OP:", op,"|" ,message
	if op == LOAD_IMAGE:
		r.loadImage('demo') #TODO fixme
		return 1
	elif op == LOAD_XRP:
		return 1
	elif op == RENDER_IMAGE:
		things = []
		things.append({'left':int(message[1]), 'top':int(message[2]), 'id':chr(int(message[3])+65), 'size':int(message[4]), 'blur_sigsq':0})
		r.get_rendered_image(things)
		return 1
	elif op == GET_LIKELIHOOD:
		return r.getLogLikelihood()
	else:
		print "[ERROR] Cannot recognize OPCODE"
		return -1


while True:
	#print "Waiting for clients ..."
	message = socket.recv()
	#print "Recieved reply", "[", message, "]"
	ret = str(dispatch(message))
	#print "Sending request"	, "...", ret
	socket.send(ret)

