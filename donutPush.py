from hub import motion_sensor, port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

    # Move straight at default velocity for 1 second
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, 1000, 1000)

    await runloop.sleep_ms(2000)

    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 1000, -1000, 645)
    #1000, 50, 400, 600, 550, 600, 700, 650, 645


    motor_pair.move(motor_pair.PAIR_1,0, velocity=1000)

    # cant use await on move function. Too basic

runloop.run(main())
