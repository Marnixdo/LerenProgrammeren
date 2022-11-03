from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for x in range(1, 3):
    robotArm.moveRight()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
for x in range(1, 4):
    robotArm.moveRight()
robotArm.drop()
for x in range(1, 4):
    robotArm.moveLeft()
robotArm.grab()
for x in range(1, 5):
    robotArm.moveRight()
robotArm.drop()
for x in range(1, 5):
    robotArm.moveLeft()
robotArm.grab()
for x in range(1, 6):
    robotArm.moveRight()
robotArm.drop()
for x in range(1, 6):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for x in range(1, 4):
    robotArm.moveRight()
robotArm.grab()
for x in range(1, 4):
    robotArm.moveLeft()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveRight()
robotArm.grab()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.drop()
for x in range(1, 5):
    robotArm.moveRight()
robotArm.grab()
for x in range(1, 5):
    robotArm.moveLeft()
robotArm.drop()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()