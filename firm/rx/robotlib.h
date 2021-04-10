#include "packetlib.h"
class Robot{
  public:
    const int MTR_PWM_RIGHT = 9;
    const int MTR_PWM_LEFT = 10;
    const int LEFT_FWD = 11;
    const int LEFT_BWD = 12;
    const int RIGHT_FWD = 13;
    const int RIGHT_BWD = 14;
    int current_seq_nr = 0;
    
    Robot(){
      current_seq_nr = 0;
    }
    void UpdateStateFromPacket(MotorPacket packet){
      //do some stuff
    }
}
