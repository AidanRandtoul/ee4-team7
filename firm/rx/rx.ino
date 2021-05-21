#include <SPI.h>
#include "printf.h"
#include "RF24.h"
#include "packetlib.h"


#define MTR_PWM_RIGHT 5
#define MTR_PWM_LEFT 6
#define LEFT_FWD 7
#define LEFT_BWD 8
#define RIGHT_FWD 9
#define RIGHT_BWD 10


RF24 radio(A2,A3);
bool role = false;
#define SIZE 32
byte buffer[SIZE + 1];


MotorPacket myPacket;

void setup() {
  //set pins 
  pinMode(MTR_PWM_RIGHT, OUTPUT);
  pinMode(MTR_PWM_LEFT, OUTPUT);
  pinMode(LEFT_FWD, OUTPUT);
  pinMode(LEFT_BWD, OUTPUT);
  pinMode(RIGHT_FWD, OUTPUT);
  pinMode(RIGHT_BWD, OUTPUT);
  
  buffer[SIZE] = 0;
  Serial.begin(115200);
  while(!Serial){}
  Serial.println("booting up");
  if(!radio.begin()){
    Serial.println("radio hardware not responding!");
    while (1) {} //radio problem, loop forever
  }
  char input = Serial.parseInt();
  radio.setPALevel(RF24_PA_LOW);
  radio.setPayloadSize(SIZE);
  radio.openWritingPipe(0x65646f4e32);
  radio.openReadingPipe(1, 0x65646f4e31); 
  radio.startListening();
  printf_begin();
  radio.printPrettyDetails();
}

void updateInstructionBuffer(){
  if(radio.available()){
    radio.read(&buffer, SIZE);
    Serial.write("Packet:");
    //copy relevant buffer bytes to packetStruct
    for(int i = 0; i < sizeof(MotorPacket::PacketStruct); i++){
      myPacket.packetData.toStream[i] = buffer[i];
      Serial.print(myPacket.packetData.toStream[i], HEX);  
    }
    Serial.println();
  }

}

void motorUpdateLeft(bool first, bool second){
    analogWrite(MTR_PWM_LEFT, myPacket.packetData.info.pwm_levels[1]);
    digitalWrite(LEFT_FWD, first);
    digitalWrite(LEFT_BWD, second);
    Serial.println("LEFT");
    Serial.println(myPacket.packetData.info.pwm_levels[1]);
    Serial.println(first);
    Serial.println(second);

}
void motorUpdateRight(bool first, bool second){
  analogWrite(MTR_PWM_RIGHT, myPacket.packetData.info.pwm_levels[0]);  
  digitalWrite(RIGHT_FWD, first);
  digitalWrite(RIGHT_BWD, second);
  Serial.println("RIGHT");
  Serial.println(myPacket.packetData.info.pwm_levels[0]);
  Serial.println(first);
  Serial.println(second);
  
}

void actOnBuffer(){
  byte control_word1 = myPacket.packetData.info.control_word1;
  //Serial.println(control_word1, BIN);
  byte mask = 0x80;
  bool first = control_word1 & 0x80;
  bool second = control_word1 & 0x40;
  motorUpdateLeft(first, second);
  first = control_word1 & 0x20;
  second = control_word1 & 0x10;
  motorUpdateRight(first, second);
}

void loop() {
  updateInstructionBuffer();
  actOnBuffer();

}
