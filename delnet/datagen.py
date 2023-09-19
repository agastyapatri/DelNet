import numpy as np 
import os 
import matplotlib.pyplot as plt 


PATH = "data/delaunay_5_sorted.txt"

with open(PATH, "r") as f:
    lines = f.readlines()

vertices = np.array([float(i) for i in lines[0].split(" ")[:10]])


