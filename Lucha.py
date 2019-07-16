import rodi
import time
import random
robot = rodi.RoDI()


try:
    while True:
        robot.sense()
        sensor = robot.sense()
        if sensor [0] < 100 and sensor [1] < 100:
            w = random.randrange(255)
            a = random.randrange(255)
            y = random.randrange(255)
            if robot.see() < 10 :
                robot.move(100,100) 
                robot.pixel(50,0,0)
            elif robot.see() <= 4:
                robot.pixel(50,50,0)
                robot.move(-70,-70)
                time.sleep(0.2)
                robot.move(100,100)
            else:
                robot.pixel(w,a,y)
                time.sleep(0.0000001)
                robot.move(-50,50)
        else:
            if sensor[0] > 100 and sensor [1] > 100:
                robot.move_backward()
                time.sleep(1)
            elif sensor[0] > 100 and sensor [1] < 100:
                robot.move_right()
                time.sleep(1)
                robot.move_stop()
            elif sensor[0] < 100 and sensor [1] > 100:
                robot.move_left()
                time.sleep(1)
                robot.move_stop()

except KeyboardInterrupt:
    print("Secuencia terminada")
    robot.move_stop()
    robot.pixel(0,0,0)