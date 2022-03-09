String serialData;

void setup() {

  serX.attach(11);
  serY.attach(10);
  Serial.begin(9600);//default broad rate of serial communication on Arduino
  Serial.setTimeout(10);//10 ms delay(default is 1 sec) 
}

void loop() {
  //lol
}

void serialEvent() {
  serialData = Serial.readString();
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

