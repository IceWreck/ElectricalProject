#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>


/* Set these to your desired credentials. */
const char *ssid = "Yourmom";  //ENTER YOUR WIFI SETTINGS
const char *password = "123456789";

const int buzzer_pin = 5;
unsigned long previousMillis = 0;
const long interval = 50;
bool tripped = false;
int ledState = LOW;

//Web/Server address to read/write from

//=======================================================================
//                    Power on setup
//=======================================================================

void setup() {
  delay(1000);
  Serial.begin(115200);
  WiFi.mode(WIFI_OFF);        //Prevents reconnection issue (taking too long to connect)
  delay(1000);
  WiFi.mode(WIFI_STA);        //This line hides the viewing of ESP as wifi hotspot

  WiFi.begin(ssid, password);     //Connect to your WiFi router
  Serial.println("");

  Serial.print("Connecting");
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    randomSeed(analogRead(A0));

  }

  pinMode(buzzer_pin, OUTPUT);


  //If connection successful show IP address in serial monitor
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  //IP address assigned to your ESP
}

//=======================================================================
//                    Main Program Loop
//=======================================================================
void loop() {

  int adcvalue = analogRead(A0); //Read Analog value of LDR
  Serial.print(adcvalue);
  Serial.println();
  delay(50);



  if ((adcvalue < 500) && (!(tripped))) {
    while (analogRead(A0) < 500) {
      digitalWrite(buzzer_pin, HIGH);
      delay(50);
      digitalWrite(buzzer_pin, LOW);
      delay(50);
    }

    HTTPClient http;    //Declare object of class HTTPClient


    String Link;
    //GET Data

    Link = "http://other.abifog.com/POSTtest/?Yourmomsfat=True" + String(random(500));

    http.begin(Link);     //Specify request destination

    int httpCode = http.GET();            //Send the request
    String payload = http.getString();    //Get the respsonse payload

    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload

    http.end();  //Close connection

    tripped = true;
  }

  if ((adcvalue > 500) && tripped) {
    tripped = false;

  }



}
//=======================================================================
