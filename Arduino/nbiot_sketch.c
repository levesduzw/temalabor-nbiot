#include "Sodaq_nbIOT.h"
#include <Sodaq_wdt.h>

#ifdef ARDUINO_SODAQ_EXPLORER
#define MODEM_ON_OFF_PIN 7
#define MODEM_STREAM Serial
#else
#error "You need to declare the modem on/off pin and stream for your particular board!"
#endif

#define DEBUG_STREAM SerialUSB
#define DEBUG_STREAM_BAUD 115200

// Uses Sodaq_NBIOT Arduino library
// https://github.com/SodaqMoja/Sodaq_nbIOT

const char* apn = "oceanconnect.t-mobile.nl";
const char* cdp = "172.16.14.22";
const char* forceOperator = "20416"; // optional - depends on SIM / network

Sodaq_nbIOT nbiot;

void setup()
{
    DEBUG_STREAM.begin(DEBUG_STREAM_BAUD);
    MODEM_STREAM.begin(nbiot.getDefaultBaudrate());

    nbiot.init(MODEM_STREAM, MODEM_ON_OFF_PIN);
    nbiot.setDiag(DEBUG_STREAM);

    if (nbiot.connect(apn, cdp, forceOperator)) {
        DEBUG_STREAM.println("Connected succesfully!");
    }
    else {
        DEBUG_STREAM.println("Failed to connect!");
        return;
    }

    const char* message = "Hello World!";

    if (!nbiot.sendMessage(message)) {
        DEBUG_STREAM.println("Could not queue message!");
    }
    else {
        DEBUG_STREAM.println("Message queued for transmission!");
    }
}

void loop()
{
}