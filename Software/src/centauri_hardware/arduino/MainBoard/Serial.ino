
// ### Serial ###

void parseCommand(String com) {

  String part1;
  String part2;

  part1 = com.substring(0, com.indexOf(" "));
  part2 = com.substring(com.indexOf(" ") + 1);



  // Outgoing

  // Distance
  if (part1.equalsIgnoreCase("1")) {
    piSerial.print("1!");
    piSerial.print(front_distance);
    piSerial.print("-");
    piSerial.println(back_distance);
  }
  // Voltage
  else if (part1.equalsIgnoreCase("2")) {
    int volt = bat_voltage * 10;
    piSerial.print("2!");
    piSerial.println(volt);
  }


  // Incoming

  // DC DIR
  else if (part1.equalsIgnoreCase("3")) {
    int incoming = part2.toInt();
    if(incoming == 1){
      yon(1,1);
    }else if(incoming == 2){
      yon(1,0);
    }else if(incoming == 3){
      yon(0,1);
    }else if(incoming == 4){
      yon(0,0);
    }
  }
  
  // DC PWM Left
  else if (part1.equalsIgnoreCase("4")) {
    int incoming = part2.toInt();
    hiz_sol(incoming);
  }
  
  // DC PWM Right
  else if (part1.equalsIgnoreCase("5")) {
    int incoming = part2.toInt();
    hiz_sag(incoming);
  }


  // SERVO BULK

  // ID
  else if (part1.equalsIgnoreCase("6")) {
    int incoming = part2.toInt();
    servo_temp_id = incoming;
  }
  // POS
  else if (part1.equalsIgnoreCase("7")) {
    int incoming = part2.toInt();
    servo_temp_pos = incoming;
  }
  // SPEED
  else if (part1.equalsIgnoreCase("8")) {
    int incoming = part2.toInt();
    servo_temp_speed = incoming;
    servo_move(servo_temp_id, servo_temp_pos, servo_temp_speed);
  }

  // SHUTDOWN
  else if (part1.equalsIgnoreCase("9")) {
    poweroff();
  }

  // RESET
  else if (part1.equalsIgnoreCase("99")) {
    resetFunc();
  }

}
