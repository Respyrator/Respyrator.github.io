#include <Arduino.h>

String msg = "Hello World";

void serialEvent(){
    msg = "";
    while(Serial.available()){
        msg += (char)Serial.read();
    }
}

void setup() {
    // put your setup code here, to run once:
    Serial.begin(115200);
}

void loop() {
    // put your main code here, to run repeatedly:
    Serial.println(msg);
    delay(200);
}