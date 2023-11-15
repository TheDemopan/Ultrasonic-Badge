import machine
import utime
from machine import Pin, PWM

# Define the pins
trig_pin = machine.Pin(3, machine.Pin.OUT)
echo_pin = machine.Pin(2, machine.Pin.IN)
buzzer = PWM(Pin(4))
led = Pin(5, Pin.OUT)

def get_distance():
    # Trigger pulse
    trig_pin.low()
    utime.sleep_us(2)
    trig_pin.high()
    utime.sleep_us(5)
    trig_pin.low()

    # Measure the pulse duration on the Echo pin
    pulse_duration = machine.time_pulse_us(echo_pin, 1, 60000)

    # Calculate distance in centimeters
    distance_cm = pulse_duration / 58.0

    return distance_cm

# Main loop
while True:
    distance = get_distance()
    print("Distance: {:.2f} cm".format(distance)) # Print to console
    utime.sleep_ms(100)
    
    if distance < 10:
        buzzer.freq(500) 
        buzzer.duty_u16(1000)
        led.toggle()
        utime.sleep_ms(50)  # Sound the buzzer and LED for 1 second
        buzzer.duty_u16(0)  
        led.toggle()		# Stop the buzzer and LED
        

