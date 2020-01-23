import skfuzzy as fuzz
from skfuzzy import control as ctrl

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# New Antecedent/Consequent objects hold universe variables and membership
# functions
distance = ctrl.Antecedent(np.arange(0,11,1),'distance')
total_cost = ctrl.Antecedent(np.arange(0,11,1),'total_cost')
priority = ctrl.Consequent(np.arange(0,26,1),'priority')

distance['low'] = fuzz.trimf(distance.universe,[0,0,5])
distance['moderate'] = fuzz.trimf(distance.universe,[0,5,10])
distance['high'] = fuzz.trimf(distance.universe,[5,10,10])

total_cost['low'] = fuzz.trimf(total_cost.universe,[0,0,5])
total_cost['moderate'] = fuzz.trimf(total_cost.universe,[0,5,10])
total_cost['high'] = fuzz.trimf(total_cost.universe,[5,10,10])

priority['low'] = fuzz.trimf(priority.universe,[0,0,13])
priority['moderate'] = fuzz.trimf(priority.universe,[0,13,26])
priority['high'] = fuzz.trimf(priority.universe,[13,26,26])

distance.view()
total_cost.view()

priority.view()
rule1 = ctrl.Rule(distance['high'] & total_cost['low'],priority['low'])
rule2 = ctrl.Rule(distance['moderate'] & total_cost['low'],priority['low'])
rule3 = ctrl.Rule(distance['low'] & total_cost['low'],priority['moderate'])

rule4 = ctrl.Rule(distance['high'] & total_cost['moderate'],priority['moderate'])
rule5 = ctrl.Rule(distance['moderate'] & total_cost['moderate'],priority['moderate'])
rule6 = ctrl.Rule(distance['low'] & total_cost['moderate'],priority['high'])

rule7 = ctrl.Rule(distance['high'] & total_cost['high'],priority['high'])
rule8 = ctrl.Rule(distance['moderate'] & total_cost['high'],priority['high'])
rule9 = ctrl.Rule(distance['low'] & total_cost['high'],priority['moderate'])

rule1.view()


# Control System Creation and Simulation
priority_ctrl = ctrl.ControlSystem(rules=[rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9])
priority_sys = ctrl.ControlSystemSimulation(priority_ctrl)

priority_sys






# We can now simulate our control system by simply specifying the inputs and calling the compute method. Suppose
# we rated the quality 6.5 out of 10 and the service 9.8 of 10.
priority_sys.input['distance'] = 6.5
priority_sys.input['total_cost'] = 9.8

# compute the tip
priority_sys.compute()

distance.view(sim=priority_sys)

total_cost.view(sim=priority_sys)
priority_sys.output['priority']


priority.view(sim=priority_sys)


















