async def main():
    # write your code here

    if distance_sensor.distance(port.D) != -1:
        motor.run(port.F, -500)

    
runloop.run(main())
