import Wrappers.TurtleSubsystem
import rev

import config


class Turret(Wrappers.TurtleSubsystem.TurtleSubsystem):
    def __init__(self):
        self.motor = rev.CANSparkMax(config.turret_can,rev.CANSparkMax.MotorType.kBrushless)
        self.motor_enc = self.motor.getEncoder()
        super().__init__()
        
    def joystickControl(self,power):
        self.motor.set(config.turret_pid.calculate(self.motor_enc.getPosition(), power * config.turret_joystick_gain))
        
    def init(self):
        pass
    def periodic(self) -> None:
        pass