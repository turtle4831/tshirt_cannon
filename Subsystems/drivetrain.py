import commands2
import commands2.command
import phoenix5
from phoenix5 import TalonSRXControlMode

import Wrappers.TurtleSubsystem
import config


class SrxMotorGroup:
    def __init__(self, leftMotors: list[phoenix5.TalonSRX], rightMotors: list[phoenix5.TalonSRX]):
        self.leftMotors = leftMotors
        self.rightMotors = rightMotors
        pass
    
    def setSpeeds(self, leftSpeed, rightSpeed):
        for motor in self.leftMotors:
            motor.set(TalonSRXControlMode.PercentOutput, -leftSpeed)
        for motor in self.rightMotors:
            motor.set(TalonSRXControlMode.PercentOutput, rightSpeed)
    
    def checkForErrors(self):
        errors = []
        for motor in self.leftMotors:
            errors.append(motor.get)
        for motor in self.rightMotors:
            errors.append(motor.get)
        
        return errors


class Drivetrain(Wrappers.TurtleSubsystem.TurtleSubsystem):
    def __init__(self):
        self.leftA = phoenix5.TalonSRX(config.left_a_can)
        self.leftB = phoenix5.TalonSRX(config.left_b_can)
        self.rightA = phoenix5.TalonSRX(config.right_a_can)
        self.rightB = phoenix5.TalonSRX(config.right_b_can)
        
        self.motor_group = SrxMotorGroup(
            [self.leftA, self.leftB],
            [self.rightA, self.rightB]
        )
        super().__init__()
    
    def drive(self, y, z):
        leftSpeed = y - z
        rightSpeed = y + z
        self.motor_group.setSpeeds(leftSpeed, rightSpeed)
        
    def driveCommand(self,y,z):
        return commands2.InstantCommand(
            self.drive(y,z)
        )
    
    def init(self):
        pass
    
    def periodic(self) -> None:
        pass
