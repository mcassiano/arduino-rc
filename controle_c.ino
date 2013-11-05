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

      if (results.value == 16720605)
        Serial.println("previous");

      if (results.value == 16712445)
        Serial.println("next");

      if (results.value == 16761405)
        Serial.println("play");

      if (results.value == 16754775)
        Serial.println("vup");  

      if (results.value == 16769055)
        Serial.println("vdown");
                
       delay(500);
      
        irrecv.resume(); // Receive the next value
      }
    }
