#include "RF24.h"
#include <SPI.h>
#include "packetlib.h"
const byte ledPin = 13;

int radioNumber = 1;
uint8_t address[][6] = {"Node1", "Node2"};
RF24 radio(7,8);
MotorPacket myPacket;

void setup() {
  Serial.begin(9600);
  Serial.println("booting up");
  while(!Serial){}
  if(!radio.begin()){
    Serial.println("radio hardware not responding!");
    while (1) {} //radio problem, loop forever
  }
  radio.setPALevel(RF24_PA_LOW);
  radio.setPayloadSize(sizeof(MotorPacket::PacketStruct));
  radio.openWritingPipe(address[radioNumber]);
  radio.openReadingPipe(radioNumber, address[!radioNumber]); 
  radio.startListening();
}

void loop() {
  if(radio.available()){
    radio.read(&myPacket.packetData.toStream, sizeof(MotorPacket::PacketStruct));
    Serial.write("Packet:");
    for(int i = 0; i < sizeof(MotorPacket::PacketStruct); i++){
      Serial.print(myPacket.packetData.toStream[i], HEX);  
    }
    Serial.println();
  }
  //Serial.println("Loop");

}
