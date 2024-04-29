from hub import light_matrix
from hub import port
import motor
import runloop
import motor_pair
import color_sensor
import color

async def main():
    # write your code here

    motor_pair.pair(motor_pair.PAIR_1, port.E, port.D)
    #pairs the two motors together
    await motor_pair.move_for_time(motor_pair.PAIR_1, 3000, 0)
    # await- doesn't stop the loop until the function is complete
    # move_for_time(pair: int, duration: int, steering: int, *, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000)
    if color_sensor.color(port.F) is color.GREEN:
        print("Green detected")
        motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, -1000, 2000)
    
    await light_matrix.write("Hi!")

runloop.run(main())
