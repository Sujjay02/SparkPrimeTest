from hub import light_matrix
from hub import port
import color_sensor
import motor
import motor_pair
import color
import runloop

async def main():
    # write your code here
    #motor.run(port.A, -1000)

    if color_sensor.color(port.E) is color.YELLOW:
        motor.run(port.A, -5000)

    
runloop.run(main())
