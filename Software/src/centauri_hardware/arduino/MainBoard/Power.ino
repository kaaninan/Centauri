long unsigned stp_wait = 0; // Stop Tusuna Basma Suresi

long unsigned sinir_kapat = 7000; // Basma Suresi Kapamak Icin
long unsigned sinir_topla = 16000; // Basma Suresi Kolları Toplayarak Kapanması Icin


void power_switch() {

  // Voltajları oku
  read_voltage();

  // Stop Button
  shutdown_func();

  // Pil seviyesini kontrol et
  int volt = bat_voltage * 10;
  if (volt > low_voltage) {
    digitalWrite(power_pin, HIGH);
  } else {
    // Pil seviyesi düşük - Uyarı ver
    battery_low_warning();
    delay(3000);
    digitalWrite(power_pin, LOW);
    delay(1000);
  }

}



void stop_func() {
  // Setupda stop tusuna basılıysa sistemi açma
  int stp = analogRead(stop_button_pin);
  if (stp > 100) {
    digitalWrite(power_pin, 0);
    delay(10000);
  }
}



void shutdown_func(){
  // Tusa Basma Suresine Göre Sistemi Kapatır veya Robotu Toplu Hale Getirir
  int stp = analogRead(stop_button_pin);
  if (stp > 100) {

    // Döngüyü Başlat

    int single_play_kapat = 0;
    int single_play_topla = 0;

    while (1) {
      stp = analogRead(stop_button_pin);

//      Serial.println(stp_wait);

      if (stp_wait > sinir_topla && single_play_topla == 0) {
        digitalWrite(buzzer_pin, 1);
        delay(250);
        digitalWrite(buzzer_pin, 0);
        single_play_topla = 1;

      } else if (stp_wait > sinir_kapat && single_play_kapat == 0) {
        digitalWrite(buzzer_pin, 1);
        delay(50);
        digitalWrite(buzzer_pin, 0);
        single_play_kapat = 1;
      }


      if (stp == 0) {

        if (stp_wait < sinir_kapat) {
          // Islem Yapma
          break;
          
        } else if (stp_wait > sinir_topla) {
          // Toplanma Komutu (Kollar icin)
          servo_topla();
          delay(8000);
          poweroff();
          
        } else {
          // Sistemi Kapat
          delay(1000);
          digitalWrite(power_pin, LOW);
          delay(10000);
        }

        stp_wait = 0;


      } else {
        stp_wait++;
      }
    }
  }
}




void battery_low_warning() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(buzzer_pin, 1);
    delay(100);
    digitalWrite(buzzer_pin, 0);
    delay(100);
  }
  digitalWrite(buzzer_pin, 1);
  delay(300);
  digitalWrite(buzzer_pin, 0);
  delay(100);
}



void read_voltage() {

  // Analog değerleri oku
  int v1 = analogRead(voltage_pin);

  // Voltaja çevir
  float v1f = v1 * (5.0 / 1023.0);
//  Serial.print(v1f);

  // Orantı yap
  bat_voltage = (v1f * 11.46)/2.41;
//  Serial.print(" - ");
//  Serial.println(bat_voltage);
//  battery_level = ((5 * bat_voltage) - 52);

}


void poweroff() {
  delay(1000);
  digitalWrite(buzzer_pin, HIGH);
  delay(150);
  digitalWrite(buzzer_pin, LOW);
  digitalWrite(power_pin, LOW);
  delay(10000);
}

void(* resetFunc) (void) = 0;
