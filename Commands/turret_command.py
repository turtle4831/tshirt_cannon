import wpilib
from commands2 import Command, Subsystem

import Subsystems.shooter_pivot
import Subsystems.turret


class TurretCommand(Command):
    def __init__(self, shooter_pivot:Subsystems.shooter_pivot.ShooterPivot, turret:Subsystems.Turret, driver:wpilib.PS5Controller):
        self.shooter_pivot = shooter_pivot
        self.turret = turret
        self.driver = driver
        
        super().__init__()
    def initialize(self):
        pass
    def execute(self):
        self.turret.joystickControl(self.driver.getRightX())
        self.shooter_pivot.joystickControl(self.driver.getRightY())
    
    def isFinished(self):
        return False