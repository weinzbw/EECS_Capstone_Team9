# EECS_Capstone_Team9

## Team Members
[Benjamin Weinzirl](https://github.com/weinzbw)\
[Del Endecott](https://github.com/d3lwyrn)\
[Samuel Harrison](https://github.com/s768h447)\
[Naran Bat](https://github.com/AnnaAanaa)\
[Oluwatimilehin Falusi](https://github.com/timfal123)


## Project Desription
The Marco Polo Robo (MPR) is a small robot that can play Marco Polo with a person, hiding and seeking capabilities.

[image](https://cdn.discordapp.com/attachments/1002612287942701119/1361116751189774501/20250412_103758.jpg?ex=67fd9641&is=67fc44c1&hm=060d0b9f593ae4a54656646daccff62080b385733e900ed5b5a7b7b34347b413&)

## Parts
3D Printed Base\
PYNQ-Z1 Base Board\
HC-SR501 Infrared PIR motion sensor\
Ultrasonic Distance Sensor\
KeeYees L298N Motor Drives and Wheels

## How to Make this Myself
Assuming you have a PYNQ-Z1 board and the same parts, you will need to connect the pins to the same setup as in our repo
or edit the code to point to the correct pin connections for the devices.

Once everything is connected, running the bootup.ipynb in the Jupyter Notebook environemnt for the PYNQ-Z1 baord will initialize the MPR's Bootup.

## How to Use
After booting up, the MPR will ask if the user wants to "hide" or "seek".
Choosing "Hide" will start a countdown for the MPR before it starts moving and saying "Marco".
The user must then respond to the "Marco" for the MPR to determine the user's position from the sound.

When the MPR is sufficiently close to the User, it will determine that the game is over, and ask to play another.

If "Seek" is chosen, the MPR will ask what difficulty to hide at, "Easy", "Medium", or "Hard", then the MPR will go around the environemnt to find a suitable hiding spot.
The MPR will alert the user when it has found a hiding spot, thus beginning the searching. The MPR will respond to any "Marco" with a response of "Polo".

When the User is sufficiently close to the MPR, the MPR will determine that the game is over, and ask to play another.
