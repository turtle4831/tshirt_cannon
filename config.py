import wpimath.controller

left_a_can = 1
right_a_can = 2
left_b_can = 3
right_b_can = 4
turret_can = 5
pivot_can = 6
pneumatic_can = 7
testicular_torsion_can = 8


load_solenoid_port = 1
fire_solenoid_port = 2

turret_max_pos = 1000
turret_min_pos = -1000

shooter_pivot_max_pos = 1000
shooter_pivot_min_pos = -1000


turret_pid = wpimath.controller.PIDController(0.00001,0,0)
pivot_pid = wpimath.controller.PIDController(0.00001,0,0)
chamber_pid = wpimath.controller.PIDController(0.00001,0,0)
turret_joystick_gain = 500
shooter_pivot_joystick_gain = 500
