/**
 * oscP5parsing by andreas schlegel
 * example shows how to parse incoming osc messages "by hand".
 * it is recommended to take a look at oscP5plug for an
 * alternative and more convenient way to parse messages.
 * oscP5 website at http://www.sojamo.de/oscP5
 */

import oscP5.*;
import netP5.*;

PFont f;

OscP5 oscP5;
NetAddress myRemoteLocation;

void setup() {
  
  size(640, 300);
  
  // Create the font
  printArray(PFont.list());
  f = createFont("Avenir-Black", 30);
  textFont(f);
  
  oscP5 = new OscP5(this,7400);
  myRemoteLocation = new NetAddress("192.168.0.100",8000);
}




void keyPressed() {

  if (key == 65) { // A
    
    println("ok");
  
    OscMessage idea_1 = new OscMessage("/mind/idea_1");
    idea_1.add(1);
    oscP5.send(idea_1, myRemoteLocation);
    
  }else if (key == 66) { // B
    
    OscMessage idea_2 = new OscMessage("/mind/idea_2");
    idea_2.add(1);
    oscP5.send(idea_2, myRemoteLocation);
    
  }

}


void oscEvent(OscMessage theOscMessage) {
  
  // EMOTIV Mind Your OSC (to) ROS OSC
  
  // Gelen Mesaji Parse Et
  String name = theOscMessage.addrPattern();
  float value = theOscMessage.get(0).floatValue();
  
  OscMessage blink = new OscMessage("/mind/blink");
  OscMessage look_left = new OscMessage("/mind/look_left");
  OscMessage look_right = new OscMessage("/mind/look_right");
  OscMessage wink_left = new OscMessage("/mind/wink_left");
  OscMessage wink_right = new OscMessage("/mind/wink_right");
  
  
  if(name.equals("/EXP/BLINK")){
    blink.add(value);
    oscP5.send(blink, myRemoteLocation);
  }else if(name.equals("/EXP/WINK_LEFT")){
    wink_left.add(value);
    oscP5.send(wink_left, myRemoteLocation);
  }else if(name.equals("/EXP/WINK_RIGHT")){
    wink_right.add(value);
    oscP5.send(wink_right, myRemoteLocation);
  }else if(name.equals("/EXP/LEFT_LID")){
    look_left.add(value);
    oscP5.send(look_left, myRemoteLocation);
  }else if(name.equals("/EXP/RIGHT_LID")){
    look_right.add(value);
    oscP5.send(look_right, myRemoteLocation);
  }
  
}


void draw() {
  background(240);
  textAlign(CENTER);
  drawType(width * 0.5);
}

void drawType(float x) {
  line(x, 0, x, 65);
  line(x, 220, x, height);
  fill(0);
  text("RoboMental Mind Server", x, 150);
  fill(51);
}