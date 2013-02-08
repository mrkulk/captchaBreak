import zmq
import sys

port = 5551
context = zmq.Context()
print "Connedting to Server ..."

socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

for request in range(1,10):
	print "Sending request", request, "..."
	socket.send("BOOM")
	#Getting reply
	message = socket.recv()
	print "Recieved reply", request, "[", message, "]"


