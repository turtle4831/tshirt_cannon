import wpilib

from robotcontainer import RobotContainer


class Robot(wpilib.TimedRobot):
    def __init__(self):
        self.robot_container = RobotContainer()
        super().__init__()
    
    def robotInit(self):
        pass
    
    def robotPeriodic(self):
        pass
    
    def teleopInit(self):
        pass
    
    def teleopPeriodic(self):
        pass
