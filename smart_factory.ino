
int tempval = 0;  // variable to store temperature value read at analog pin 2
int waterval = 100; // variable to store analog water level value
float temp = 0;   //leftover from previous Test sketch

//Setup of setpoint, UCL, and LCL
int setpoint = 510;
//int setpoint = analogRead(5);
int UCL = setpoint + 10;
int LCL = setpoint - 10;

void setup() {

  pinMode(8, OUTPUT); //digital pin 8 controls Fan Motor
  pinMode(11, OUTPUT); //digital pin 7 controls LED Heater
  pinMode(13, OUTPUT); //digital pin 6 controls Mini-Pump
  Serial.begin(9600); //set up to print out text to monitor
}

void loop() {
   digitalWrite(13, HIGH);
  delay(8000);
  digitalWrite(13, LOW);
  //  Serial.print("Setpoint = ");
  //  Serial.print(setpoint);
  Serial.print("UCL = "); Serial.print(UCL);
  Serial.print("  LCL = "); Serial.println(LCL);
  tempval = analogRead(2);  // read thermister analog input pin 5
  Serial.print("Current Temp = ");
  Serial.println(tempval);    // print thermister value to serial monitor

  //IF-THEN-ELSE for Temperature
  if (tempval < LCL)
  {
    Serial.println("***tempval < LCL -- Turn ON LED");
    LEDON();
  }
  else if (tempval > UCL)
  {
    Serial.println("***tempval > UCL -- Turn OFF LED, Turn ON Fan");
    LEDOFF();
  }
  else {}
  
 delay(7000);
}

void LEDON() {
  //  Serial.println("In LCL Function");
  digitalWrite(11, HIGH); //LED ON
}

void LEDOFF() {
  //  Serial.println("In UCL Function");
  digitalWrite(11, LOW);  //LED OFF
  digitalWrite(8, HIGH); //Fan ON
  delay(5000);
  digitalWrite(8, LOW);  //Fan OFF
}

void PUMPON() {
  Serial.println("In PUMP Function");
  digitalWrite(13, HIGH);  //Mini-pump ON
  delay(5000);  //time to operate mini-pump
  digitalWrite(13, LOW);   //Turn OFF mini-pump
}

//digitalWrite(8, HIGH); //Fan ON
//delay(2000);
//digitalWrite(8, LOW);  //Fan OFF
//delay(2000);

//digitalWrite(7, HIGH); //LED ON
//delay(2000);
//digitalWrite(7, LOW);  //LED OFF
//delay(2000);
