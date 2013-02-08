#include "zmq.hpp"
#include <string>
#include <iostream>
#include <unistd.h>

int main () {
    //  Prepare our context and socket
    zmq::context_t context (1);
    zmq::socket_t socket (context, ZMQ_REP);
    socket.bind ("tcp://*:5555");


    zmq::context_t context2 (1);
    zmq::socket_t socket2 (context2, ZMQ_REP);
    socket2.bind ("tcp://*:5551");

    while (true) {
        zmq::message_t request;
        zmq::message_t request2;

        //  Wait for next request from client
        socket.recv (&request);
        socket2.recv (&request2);
        std::cout << "Received 2 servers" << std::endl;

        //  Do some 'work'
        sleep (1);

        //  Send reply back to client
        zmq::message_t reply (5);
        memcpy ((void *) reply.data (), "World", 5);
        socket.send (reply);

        zmq::message_t reply2 (5);
        memcpy ((void *) reply2.data (), "WHATT", 5);
        socket2.send (reply2);
    }
    return 0;
}