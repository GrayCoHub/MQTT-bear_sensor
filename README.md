An Arduino type project using the ESP8622 NodeMCU12 / PIR sensor.  Remote, waterproof component with independent power supply, is monitoring the garbage can for movement.  Using the mosquitto MQTT protocol, a mqtt broker has been created.  This client has been subscribed on the PC using the mosquitto subscribe utility.  

This project was testing the MQTT extension using VS Code.  A simple python script file accesses the MQTT service and subscribes to the topic which results in a near continuous loop of sensor data.  There is a message, "Bear at the garbage can" when the client connects to the broker.  Then there is the repeating message every 5 seconds, quiet.  If movement is detected ... and there are periodic false signals due to wind movments etc.., then there is a message: "Motion Alert!".

This vsCode project w/in venv using python v 3.7.4. 
