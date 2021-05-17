#include "RF24.h"
#include <SPI.h>
#include "packetlib.h"
const byte ledPin = 13;
uint32_t count = 0;
#define SIZE 32

int radioNumber = 0;
MotorPacket myPacket;

uint8_t address[][6] = {"1Node", "2Node"};
RF24 radio(7, 8);

void setup() {
  Serial.begin(9600);
  while (!Serial) {}
  if (!radio.begin()) {
    Serial.println(F("radio hardware not responding!"));
    while (1) {} //radio problem, loop forever
  }
  radio.setPALevel(RF24_PA_LOW);
  radio.setPayloadSize(SIZE);
  radio.openWritingPipe(address[0]);
  radio.openReadingPipe(1, address[1]);
  radio.startListening(); //change when ack packets implemented
  pinMode(ledPin, OUTPUT);
}

void checkForInfo() {

  //todo poll serial stream from GUI.
  //for now just set preset values
  myPacket.packetData.info.seq_nr = count;
  myPacket.packetData.info.what_motors = 0xCC;
  for (byte i = 0; i < 8; i++) {
    myPacket.packetData.info.pwm_levels[i] = count % 255;
  }
  myPacket.packetData.info.control_word1  = 0xAA; //all on
  myPacket.packetData.info.control_word2  = 0xAA;
  count++;
  delay(750);
}

void sendPacket() {
  radio.stopListening();
  radio.flush_tx();
  digitalWrite(ledPin, HIGH);
  int i = 0;
  int failures = 0;
 
  while(i < SIZE){
    if(!radio.writeFast(&myPacket.packetData.toStream, SIZE)){
      //Serial.println("Packet: " + String(count) + " failed!");
      radio.reUseTX();
      failures++;
    }else{
      Serial.println("byte transmit success");
      i++;
    }
    if(failures >= 100){
      Serial.println("Too many failures, abort payload");
      break;
    }
  }
  
  radio.startListening();  
  Serial.write("Packet:");
  for(int i = 0; i < sizeof(MotorPacket::PacketStruct); i++){
    Serial.print(myPacket.packetData.toStream[i], HEX);
  }
  Serial.println();
  digitalWrite(ledPin, LOW);
  
}

void loop() {
  checkForInfo();
  sendPacket();

}
