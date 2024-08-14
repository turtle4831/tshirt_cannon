import commands2
import wpilib
from commands2 import button

from Commands.fire_command import FireCommand,FinishFireCommand
from Wrappers.TurtleSubsystem import TurtleSubsystem
from Subsystems.drivetrain import Drivetrain
from Subsystems.shooter import Shooter
from Subsystems.shooter_pivot import ShooterPivot
from Subsystems.turret import Turret


class RobotContainer:
    def __init__(self):
        self.driver1 = wpilib.PS5Controller(1)
        
        self.subsystems = [TurtleSubsystem()]
        
        self.shooter = Shooter()
        self.drivetrain = Drivetrain()
        self.shooter_pivot = ShooterPivot()
        self.turret = Turret()
        
        self.subsystems.append(self.drivetrain)
        self.subsystems.append(self.shooter)
        self.subsystems.append(self.shooter_pivot)
        self.subsystems.append(self.turret)
        
        for i in self.subsystems:
            i.init()
            
        
        self.configureBindings()
        
    def configureBindings(self):
        
        commands2.RunCommand(self.drivetrain.driveCommand(
            self.driver1.getLeftY(),
            self.driver1.getRightX(),
        ),self.drivetrain)
        
        button.Trigger(
            self.driver1.getL2ButtonPressed()
        ).onTrue(
            FireCommand(self.shooter).andThen(
                commands2.WaitCommand(2)
            ).andThen(
                FinishFireCommand(self.shooter)
            )
        )
        
        button.Trigger(
            self.driver1.getSquareButtonPressed()
        ).onTrue(
            commands2.InstantCommand(
                self.shooter.scaryShutdown(),self.shooter
            )
        )
    def scaryShutdown(self):
        """
        used at the start of disabled init to make sure that none of the pneumatics accidentally fires
        :return:
        """
        self.shooter.scaryShutdown()
        
    
        
       