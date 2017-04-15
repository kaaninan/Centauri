// DC MOTOR
void yon(int sag, int sol) {
  if (sag == 1) {
    digitalWrite(motor1_dir1_pin, LOW);
    digitalWrite(motor1_dir2_pin, HIGH);
  } else if (sag == 0) {
    digitalWrite(motor1_dir1_pin, HIGH);
    digitalWrite(motor1_dir2_pin, LOW);
  }
  if (sol == 1) {
    digitalWrite(motor2_dir1_pin, LOW);
    digitalWrite(motor2_dir2_pin, HIGH);
  } else if (sol == 0) {
    digitalWrite(motor2_dir1_pin, HIGH);
    digitalWrite(motor2_dir2_pin, LOW);
  }
}

void hiz_sag(int hiz) {
  analogWrite(motor1_pwm_pin, hiz);
}

void hiz_sol(int hiz) {
  analogWrite(motor2_pwm_pin, hiz);
}


// SERVO MOTOR


void torqueOff(){
  Dynamixel.torqueStatus(1, 0);
  Dynamixel.torqueStatus(2, 0);
  Dynamixel.torqueStatus(3, 0);
  Dynamixel.torqueStatus(4, 0);
  Dynamixel.torqueStatus(5, 0);
  Dynamixel.torqueStatus(6, 0);
  Dynamixel.torqueStatus(7, 0);
}

// Cache incoming data from piSerial
int servo_temp_id = 0;
int servo_temp_speed = 0;
int servo_temp_pos = 0;

void servo_move(int id, int pos, int speed) {
  Dynamixel.moveSpeed(id, pos, speed);
  servo_temp_id = 0;
  servo_temp_speed = 0;
  servo_temp_pos = 0;
}

void servo_topla() {
  // Kolları ve kafayı toplayarak kapatır
  int speed = 50;
  Dynamixel.moveSpeed(1, 420, speed);
  Dynamixel.moveSpeed(2, 630, speed);
  Dynamixel.moveSpeed(3, 880, speed + 100);
  Dynamixel.moveSpeed(4, 600, speed);
  Dynamixel.moveSpeed(5, 370, speed);
  Dynamixel.moveSpeed(6, 140, speed + 100);
  Dynamixel.moveSpeed(7, 512, speed);
  Dynamixel.moveSpeed(8, 520, speed);
}

