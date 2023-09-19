import numpy as np 
import os 
import torch.nn as nn 
from torch.utils.data import Dataset, DataLoader
import pickle 

def generate_data(
        path_to_file:str, 
        save:bool, 
        name:str
    ):
    """
    Function to generate data for a particular discretization

    [args]:

    path_to_file:str - path to the .txt file containing the point, triangulation data 
    save:bool - whether to save the data as pickle
    name:str - name of the file to be saved.
    """
    point_arrays = []
    triangle_arrays = []
    with open(path_to_file, "r") as f:
        lines = f.readlines()
    excludes = ["\n", "", " ", "[", "]"]
    for line in lines:
        chars = line.split("output")
        points = chars[0].split(" ")
        triangulation = chars[1].split(" ")
        points = [float(point) for point in points if point not in excludes]
        triangulation = [float(num)-1 for num in triangulation if num not in excludes]
        
        #   extracting the points
        i = 0
        arranging_points = []
        while (i<len(points)):
            arranging_points.append([points[i], points[i+1]])
            i += 2
        vertices = np.array(arranging_points, dtype=np.float32)
        
        #   extracting the triangles
        j = 0
        arranging_triangles = []
        while j < len(triangulation):
            arranging_triangles.append([triangulation[j], triangulation[j+1], triangulation[j+2]])
            j += 3
        triangles = np.array(arranging_triangles, dtype=np.float32)
        
        point_arrays.append(vertices)
        triangle_arrays.append(triangles)
    
    if save:
        name_point = name + "_points"
        with open(os.path.join("data/", name_point), "wb") as pkl:
            pickle.dump(point_arrays, pkl)
        name_tri = name + "_triangles"
        with open(os.path.join("data/", name_tri), "wb") as pkl:
            pickle.dump(point_arrays, pkl)

    return point_arrays, triangle_arrays


class DelData(Dataset):
    """
    Defining the dataset of the delaunay triangulations
    """
    def __init__(self, path_to_points:str, path_to_tri:str) -> None:
        super().__init__()
        self.pointdata = pickle.load(path_to_points)
        self.tridata = pickle.load(path_to_tri)
        
    def __getitem__(self, idx) -> tuple:
        return (self.pointdata[idx], self.tridata[idx])

    def __len__(self, ) -> int:
        return len(self.pointdata)


