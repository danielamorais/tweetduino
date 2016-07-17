#include <SPI.h>
#include <UIPEthernet.h>

byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
char server[] = "107.191.118.73";
IPAddress ip(192, 168, 1, 177);
EthernetClient client;

void setup() {
  Serial.begin(9600);
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    Ethernet.begin(mac, ip);
  }
}

void loop() {
 
  if (client.connect(server, 8080)) {
    Serial.println("connected");
    // Make a HTTP request:
    client.println("GET /sendTweet/Hello%20world%20by%20Arduino HTTP/1.1");
    client.println("Host: 107.191.118.73:8080");
    client.println("Connection: close");
    client.println();
client.stop();
  } else {
    Serial.println("connection failed");
  }
  
  delay(5000);
}
