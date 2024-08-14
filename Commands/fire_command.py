import commands2
import wpilib
import Subsystems.shooter


class FireCommand(commands2.Command):
    def __init__(self, shooter:Subsystems.shooter.Shooter()):
        self.shooter = shooter
        super().__init__()
        
    def initialize(self):
        pass
    def execute(self):
        self.shooter.ToggleLoadSolenoid(False)
        self.shooter.ToggleShotSolenoid(True)
    def isFinished(self):
        return True
    
        
class FinishFireCommand(commands2.Command):
    def __init__(self, shooter:Subsystems.shooter.Shooter):
        self.shooter = shooter
        super().__init__()
    def initialize(self):
        self.shooter.ToggleShotSolenoid(False)
        self.shooter.ToggleLoadSolenoid(True)
        self.shooter.goToNextPosition()
    def execute(self):
        self.shooter.powerDaMoto()
    def isFinished(self):
        self.shooter.motoAtSetpoint()
    
    