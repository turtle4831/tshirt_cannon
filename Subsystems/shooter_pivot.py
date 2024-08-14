import Wrappers.TurtleSubsystem
import config
import rev

class ShooterPivot(Wrappers.TurtleSubsystem.TurtleSubsystem):
    def __init__(self):
        self.motor = rev.CANSparkMax(config.pivot_can, rev.CANSparkMax.MotorType.kBrushless)
        self.motor_enc = self.motor.getEncoder()
        super().__init__()
    
    def joystickControl(self, power):
        self.motor.set(config.pivot_pid.calculate(self.motor_enc.getPosition(), power * config.shooter_pivot_joystick_gain))
        
    
    def setPower(self,power):
        if self.motor_enc.getPosition() == config.shooter_pivot_min_pos or config.shooter_pivot_max_pos:
            power = 0
        
        self.motor.set(power)
    def getAtLimit(self):
        return self.motor_enc.getPosition() == config.shooter_pivot_min_pos or config.shooter_pivot_max_pos
        
    def init(self):
        super().init()
        
    def periodic(self):
        pass