#include <AltSoftSerial.h>
#include <DynamixelSerial.h>

// Variables
float bat_voltage = 0;

int low_voltage = 108; // Shutdown Voltage

// Digital IO
const int motor1_dir1_pin = 2;
const int motor1_dir2_pin = 4;
const int motor1_pwm_pin = 3;
const int motor2_dir1_pin = 5;
const int motor2_dir2_pin = 7;
const int motor2_pwm_pin = 6;
const int buzzer_pin = 11;
const int dynamixel_pin = 10;
const int power_pin = 12;

// Analog
const int sharp_on_pin = A0;
const int sharp_arka_pin = A1;
const int stop_button_pin = A2;
const int voltage_pin = A3;

// Local
int front_distance = 0;
int back_distance = 0;
String command = "";

AltSoftSerial piSerial;


void setup() {

  stop_func();

  set_pinmode();
  power_switch();

  piSerial.begin(19200);

  Dynamixel.begin(1000000, 2);
//      Serial.begin(19200);
//      debugSerial();


  // Acilma Sesi
  digitalWrite(buzzer_pin, HIGH);
  delay(50);
  digitalWrite(buzzer_pin, LOW);

  // Turn On Servo Leds
  delay(1000);
  Dynamixel.ledStatus(7, ON);

}


void loop() {

  power_switch();
  sharp_read();

  //  debugSerial();


  while (piSerial.available()) {

    power_switch();
    sharp_read();

    char gelen = piSerial.read();
    if (gelen == '&') {
      parseCommand(command);
      command = "";
    } else {
      command += gelen;
    }
  }

}


