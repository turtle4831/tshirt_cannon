import Wrappers.TurtleSubsystem
import rev

import config


class Turret(Wrappers.TurtleSubsystem.TurtleSubsystem):
    def __init__(self):
        self.motor = rev.CANSparkMax(config.turret_can,rev.CANSparkMax.MotorType.kBrushless)
        self.motor_enc = self.motor.getEncoder()
        super().__init__()
    
    def setPower(self, power):
        if self.motor_enc.getPosition() == config.turret_min_pos or config.turret_max_pos:
            power = 0
        
        self.motor.set(power)
    
    def getAtLimit(self):
        return self.motor_enc.getPosition() == config.shooter_pivot_min_pos or config.shooter_pivot_max_pos
    
    
    def joystickControl(self,power):
        self.motor.set(config.turret_pid.calculate(self.motor_enc.getPosition(), power * config.turret_joystick_gain))
        
    def init(self):
        pass
    def periodic(self) -> None:
        pass