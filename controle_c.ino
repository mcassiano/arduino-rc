/*
   * IRremote: IRrecvDemo - demonstrates receiving IR codes with IRrecv
 * An IR detector/demodulator must be connected to the input RECV_PIN.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 */
#include <IRremote.h>

int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);

decode_results results;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) {
      
    if (results.value == 0xFF0008F7)
      Serial.println("previous");

    if (results.value == 0xFF0058A7)
      Serial.println("next");

    if (results.value == 0xFF009867)
      Serial.println("play");

    if (results.value == 0xFF00E817)
      Serial.println("vup");  

    if (results.value == 0xFF00D827) 
      Serial.println("vdown");
      
     if (results.value == 0xFF0018E7)
      Serial.println("fullscreen");
      
     if (results.value == 0xFF00D02F)
      Serial.println("subtitle");

    irrecv.resume(); // Receive the next value
  }
}

