from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
for x in range(1, 8):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(1, 3):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()