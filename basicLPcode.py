# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:55:51 2024

@author: Katib
"""
from pulp import LpMaximize, LpProblem, LpVariable

def solve_lp():

    # Create the LP problem

    prob = LpProblem("Maximize_Z", LpMaximize)



    # Define the variables

    x1 = LpVariable("x1", lowBound=0)

    x2 = LpVariable("x2", lowBound=0)  



    # Define the objective function: Maximize 3x1 + x2

    prob += 3 * x1 + x2



    # Define the constraints:

    prob += x2 <= 5

    prob += x1 + x2 <= 10

    prob += -x1 + x2 >= -2



    # Solve the problem

    prob.solve()



    # Output the results

    if prob.status == 1:  # Optimal

        print('Objective value =', prob.objective.value())

        print('x1 =', x1.value())

        print('x2 =', x2.value())

    else:

        print('The problem does not have an optimal solution.')



if __name__ == "__main__":

    solve_lp()