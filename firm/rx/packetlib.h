class MotorPacket {
  public:
    typedef struct PacketStruct {
      char head;
      uint32_t seq_nr;
      byte what_motors;
      byte pwm_levels[8];
      byte control_word1;
      byte control_word2;
    } PacketStruct;
    union PacketData{
      PacketStruct info;
      byte toStream[sizeof(PacketStruct)];
    }PacketData;

    union PacketData packetData;

    MotorPacket() {
      packetData.info.head = 'm';
      packetData.info.seq_nr = 0;
      packetData.info.what_motors = 0x00;
      packetData.info.pwm_levels[8] = {};
      packetData.info.control_word1 = 0x00; //all off
      packetData.info.control_word2 = 0x00;
    }
    
};
