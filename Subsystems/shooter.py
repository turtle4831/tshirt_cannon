import rev
import wpilib

import config
import utils


class PneumaticStates(enum.Enum):
    On=1,
    Off=2

class Shooter(Wrappers.TurtleSubsystem.TurtleSubsystem()):
    
    def __init__(self):
        self.motor = rev.CANSparkMax(config.testicular_torsion_can, rev.CANSparkMax.MotorType.kBrushless)
        self.motorEnc = self.motor.getEncoder()
        self.chamber_setpoints = (
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100,
            100
        )
        self.chamber_pointer = 0
        self.load_state = PneumaticStates.Off
        self.fire_state = PneumaticStates.Off
        
        self.load_solenoid = wpilib.Solenoid(config.load_solenoid_port,wpilib.PneumaticsModuleType.CTREPCM)
        self.fire_solenoid = wpilib.Solenoid(config.fire_solenoid_port,wpilib.PneumaticsModuleType.CTREPCM)
    def goToNextPosition(self):
        if self.chamber_pointer < 10:
            self.chamber_pointer += 1
            self.motor.set(config.chamber_pid.calculate(self.motorEnc.getPosition(),self.chamber_setpoints[self.chamber_pointer]))
        else:
            self.chamber_pointer = 0
        
    def goToPreviousPosition(self):
        if self.chamber_pointer > 0:
            self.chamber_pointer -= 1
            self.motor.set(config.chamber_pid.calculate(self.motorEnc.getPosition(),self.chamber_setpoints[self.chamber_pointer]))
        else:
            self.chamber_pointer = 10
            
    def ToggleLoadSolenoid(self, fire:bool):
        self.load_solenoid.set(fire)
        
    
    def ToggleShotSolenoid(self, fire:bool):
        self.fire_solenoid.set(fire)
    
    def powerDaMoto(self):
        self.motor.set(
            config.chamber_pid.calculate(self.motorEnc.getPosition(), self.chamber_setpoints[self.chamber_pointer]))
    
    def motoAtSetpoint(self):
        return utils.within_tolerance(self.motorEnc.getPosition(), self.chamber_setpoints[self.chamber_pointer],0.5)
    
    def scaryShutdown(self):
        self.ToggleLoadSolenoid(False)
        self.ToggleShotSolenoid(False)
    
    def init(self):
        pass
    def periodic(self):
        pass
    
    