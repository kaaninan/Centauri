void debug() {
  // Pi'Ye Yolla
  piSerial.print("Battery Voltage: ");
  piSerial.println(bat_voltage);
  piSerial.print("Front Dis: ");
  piSerial.println(front_distance);
  piSerial.print("Back Dis: ");
  piSerial.println(back_distance);
  piSerial.println("---------------");
}

void debugSerial() {
  // Serial'e Yolla
  Serial.print("Battery Voltage: ");
  Serial.println(bat_voltage);
  Serial.print("Front Dis: ");
  Serial.println(front_distance);
  Serial.print("Back Dis: ");
  Serial.println(back_distance);
  Serial.println("---------------");
}
