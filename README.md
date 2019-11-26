# Laser Security System
Project for Electrical Engineering course (Semester 1)

## Info
* Flask app that recieves notifications
* Nodemcu code has the code that has to be flashed on the nodemcu.

## Complete Project Report
https://github.com/IceWreck/ElectricalProject/raw/master/static/report.pdf

## Circuit Overview
We have used a small computer/ IOT platform, called a nodeMCU to link various parts
of our circuit.
The nodeMCU allows us to interface with electrical components through the use of
pins.
* The analogue pins have an analogue to digital convertor built into them. They
sense voltage between 0 and 3V and map it into 1024 parts which can be
accessed by the nodeMCU.
* The digital pins are switches which have ON and OFF states and can be
controlled by the computer.
* VV pins allow us to directly access the full voltage provided by the USB ie 5
Volts.
4
Electrical Project – Laser Security System
* 3V pins - 3 Volts.
* Ground pins.
The entire circuit is divided into two parts, which are in turn connected to the
nodemcu.
The LDR is connected an analouge pin on one side and to a (pull down) resistor which
then goes to the ground on the other side.
We have an NPN transistor on the other side.
* Base is connected to a digital pin with a resistor to prevent back current in
between.
* Emitter is connected to the ground.
* Collector is connected to the buzzer and led, which are connected to an always
on 5V pin on the other side.
Finally, the laser module is connected to an always on 3V pin.

## Working
When the system is switched on, the laser pointing at the LDR sends a signal of >700
to the computer.
However, when the laser is blocked by external factors, the LDR can only sense light
from other sources like tubelights, which send a signal of 300 max.
In this case, we have programmed our computer to do two things.
* Send a notification to our web app present at http://electricalproject.abifog.com/
* Turn on the digital pin which sends a tiny current to the transistor's base. This
causes the led and buzzer to go off.
Thus, the user can be alerted if someone tries to bypass our laser security system.
