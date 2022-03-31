#include<Servo.h>
//import library

Servo serX;
Servo serY;

String serialData;
setup()
void  {

  serX.attach(8);
  serY.attach(9);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  //lol
}

void serialEvent() {//this function happens every time we get information
  
  serialData = Serial.readString();
  //this line reads the information and stores it to the name "serial data"
  
  x_value = parseDataX(serialData);
  //take the information you got and strip it to get only the x value
  
  y_value = parseDataY(serialData);
  
  //take the information you got and strip it to get only the y value
  
  serX.write(x_value);
  //write the x value to the x servo
  serY.write(y_value);
  //write the y value to the y servo
}

int parseDataX(String data){ 
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);
  return data.toInt();
}

int parseDataY(String data){//
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
