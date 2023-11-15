# Ultrasonic-Badge
Custom PCB device for detecting distances and beeping when something is too close

Repository contains KiCad PCB files for your own fabrication, as well as the 'main.py' file containing the firmware script that runs continuously on the Raspberry Pi Pico

## Materials

To build your own Ultrasonic Badge you will need (per 1 unit)

- Custom PCB from the included KiCad files
- 1x 12x9mm Buzzer
- 1x LED
- 1x RCWL-1601 Ultrasonic Sensor (You do not want the HC-SR04 since it requires 5v, which is greater than the Pico's 3.3v output)
- 1x Raspberry Pi Pico

Optional
- 1x Battery pack with positive and negative leads, with a toggle switch if you wish.
- 1x Case, see 'case_body_rev.stl'
