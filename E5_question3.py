# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:40:13 2024

@author: Katib
"""

from pulp import LpMinimize, LpProblem, LpVariable

def solve_dual_lp():
    # Create the LP problem
    prob = LpProblem("Minimize_W", LpMinimize)

    # Define the variables
    y1 = LpVariable("y1", lowBound=0)
    y2 = LpVariable("y2", lowBound=0)
    y3 = LpVariable("y3", lowBound=0)

    # Define the objective function: Minimize 145*y1 + 260*y2 + 190*y3
    prob += 145 * y1 + 260 * y2 + 190 * y3

    # Define the constraints:
    prob += 5 * y1 + 4 * y2 + y3 >= 1
    prob += 2 * y1 + 8 * y2 - 8 * y3 >= 4
    prob += 2 * y1 - 8 * y2 + 4 * y3 >= 2

    # Solve the problem
    prob.solve()

    # Output the results
    if prob.status == 1:  # Optimal
        print('Objective value =', prob.objective.value())
        print('y1 =', y1.value())
        print('y2 =', y2.value())
        print('y3 =', y3.value())
    else:
        print('The problem does not have an optimal solution.')


if __name__ == "__main__":
    solve_dual_lp()
