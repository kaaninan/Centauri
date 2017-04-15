void sharp_read() {
  int i = analogRead(sharp_on_pin);
  front_distance = (6762 / (i - 9)) - 4;

  int a = analogRead(sharp_arka_pin);
  back_distance = (6762 / (a - 9)) - 4;
}

