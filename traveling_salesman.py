#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:19:41 2024

@author: mariakatibi
"""

from sys import maxsize 
from itertools import permutations
import time
import matplotlib.pyplot as plt
V = 4

def travellingSalesmanProblem(graph, s): 

	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 
 
	min_path = maxsize 
	next_permutation=permutations(vertex)
	for i in next_permutation:

		current_pathweight = 0

		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		min_path = min(min_path, current_pathweight) 
		
	return min_path 

def measure_time(num_integers):
    graph = [[0] * num_integers for _ in range(num_integers)]
    for i in range(num_integers):
        for j in range(num_integers):
            if i != j:
                graph[i][j] = 10  
    s = 0
    start_time = time.time() 
    travellingSalesmanProblem(graph, s) 
    end_time = time.time() 

    return end_time - start_time

if __name__ == "__main__": 
    num_integers_list = [4, 5, 6, 7, 8]
    time_spent_list = []

    for num_integers in num_integers_list:
        time_spent = measure_time(num_integers)
        time_spent_list.append(time_spent)

    plt.plot(num_integers_list, time_spent_list, marker='o', color='b')
    plt.title('Time Spent by Algorithm vs. Number of Integers')
    plt.xlabel('Number of Integers')
    plt.ylabel('Time Spent (s)')
    plt.grid(True)
    plt.show()

