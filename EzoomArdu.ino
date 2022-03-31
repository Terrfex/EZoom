#include<Servo.h>

Servo serX;
Servo serY;

String serialData;

void setup() {

  serX.attach(8);
  serY.attach(9);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  //lol
}

void serialEvent() {
  serialData = Serial.readString();
  Serial.print(serialData);
  serX.write(parseDataX(serialData));
  serY.write(parseDataY(serialData));
}

int parseDataX(String data){
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  
  return data.toInt();
}

int parseDataY(String data){
  data.remove(0,data.indexOf("Y") + 1);
  return data.toInt();
}





/*
  01000101 
  01111001 
  01100001 
  01101100 
  00100000 
  01000010 
  01100101 
  01101110 
  01100010 
  01100101 
  01101110 
  01101001 
  01110011 
  01101000 
  01110100 
  01111001 
  00100000 
  01100001 
  01101110 
  01100100 
  00100000 
  01010010 
  01101001 
  01101110 
  01100001 
  01110100 
  00100000 
  01100010 
  01101110 
  01100101 
  01101001 
  00100000 
  01111010 
  01101111 
  01101110 
  01101111 
  01110100
 */
