# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:36:23 2024

@author: Katib
"""
from pulp import LpMaximize, LpProblem, LpVariable

def solve_lp():
    # Create the LP problem
    prob = LpProblem("Maximize_Z", LpMaximize)

    # Define the variables
    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)
    x3 = LpVariable("x3", lowBound=0)

    # Define the objective function: Maximize z = x1 + 4*x2 + 2*x3
    prob += x1 + 4*x2 + 2*x3

    # Define the constraints:
    prob += 5*x1 + 2*x2 + 2*x3 <= 145
    prob += 4*x1 + 8*x2 - 8*x3 <= 260
    prob += x1 + x2 + 4*x3 <= 190

    # Solve the problem
    prob.solve()

    # Output the results
    if prob.status == 1:  # Optimal
        print('Objective value =', prob.objective.value())
        print('x1 =', x1.value())
        print('x2 =', x2.value())
        print('x3 =', x3.value())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == "__main__":
    solve_lp()
