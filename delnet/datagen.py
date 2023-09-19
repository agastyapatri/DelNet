import numpy as np 
import os 
import matplotlib.pyplot as plt 
files = os.listdir("data/")
file = files[0]
with open(os.path.join("data", file), "r") as f:
    lines = f.readlines()


#   PARSING A DATAFILE
excludes = ["\n", "", " ", "[", "]"]
for line in lines:
    chars = line.split("output")
    points = chars[0].split(" ")
    triangulation = chars[1].split(" ")
    points = [float(point) for point in points if point not in excludes]
    triangulation = [float(num)-1 for num in triangulation if num not in excludes]

    i = 0
    arranging_points = []
    while (i<len(points)):
        arranging_points.append([points[i], points[i+1]])
        i += 2
    vertices = np.array(arranging_points, dtype=np.float32)

    j = 0
    arranging_triangles = []
    while j < len(triangulation):
        arranging_triangles.append([triangulation[j], triangulation[j+1], triangulation[j+2]])
        j += 3
        
    break 
