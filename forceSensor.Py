from hub import light_matrix
from hub import port
import motor
import runloop
import motor_pair
import force_sensor

async def main():
    # write your code here

    motor_pair.pair(motor_pair.PAIR_1, port.E, port.D)
    
    #pairs the two motors together
    await motor_pair.move_for_time(motor_pair.PAIR_1, 3000, 0)
    # await- doesn't stop the loop until the function is complete
    # move_for_time(pair: int, duration: int, steering: int, *, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000)
    if force_sensor.pressed(port.F):
        light_matrix.write("Object Detected")
        motor_pair.move_tank_for_time(motor_pair.PAIR_1, -1000, -1000, 1000)
    


runloop.run(main())
