#include "RF24.h"
#include <SPI.h>
#include "packetlib.h"
const byte ledPin = 13;
uint32_t count = 0;


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
  radio.setPayloadSize(sizeof(MotorPacket::PacketStruct));
  radio.openWritingPipe(address[0]);
  radio.openReadingPipe(0, address[!1]);
  radio.stopListening(); //change when ack packets implemented
  pinMode(ledPin, OUTPUT);
}

void checkForInfo() {

  //todo poll serial stream from GUI.
  //for now just set preset values
  myPacket.packetData.info.seq_nr = count;
  myPacket.packetData.info.what_motors = 0xCC;
  for (byte i = 0; i < 8; i++) {
    myPacket.packetData.info.pwm_levels[i] = i * 32;
  }
  myPacket.packetData.info.control_word  = 0xAA; //all on
  count++;
  delay(750);
}

void sendPacket() {
  radio.flush_tx();
  digitalWrite(ledPin, HIGH);
  int i = 0;
  //while(i < sizeof(MotorPacket::PacketStruct)){
    if(!radio.writeFast(&myPacket.packetData.toStream, sizeof(MotorPacket::PacketStruct))){
      Serial.println("Packet: " + String(count) + " failed!");
      radio.reUseTX();
    }else{
      radio.txStandBy();
    }
  //  else{
  //    i++;
  //  }
  //}
  
  Serial.write("Packet:");
  for(int i = 0; i < sizeof(MotorPacket::PacketStruct); i++){
    Serial.print(myPacket.packetData.toStream[i], HEX);
  }
  //Serial.write((byte*)&myPacket.toStream.stream, sizeof(MotorPacket::PacketInfo));
  Serial.println();
  digitalWrite(ledPin, LOW);
  
}

void loop() {
  checkForInfo();
  sendPacket();

}
