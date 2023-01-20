from simtellopy import Tello

drone = Tello(name='solution')
drone.connect()

drone.takeoff()

drone.rotate_counter_clockwise(90)
drone.move_down(50)
drone.take_photo()

drone.move_forward(200)
drone.rotate_counter_clockwise(90)
drone.take_photo()

drone.rotate_counter_clockwise(45)
drone.move_forward(100)
drone.take_photo()

drone.land()

drone.simulate()
