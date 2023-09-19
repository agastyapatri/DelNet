#   **DelNet**
_Producing Delaunay triangulations using Neural Nets_

##  **Introduction**
Given a set of points $S$, a Delaunay Triangulation $DT(S)$ is such that:

1.  The minimum of the angles in each triangle is maximized. 
2.  For any 3 points $\{p_1, p_2, p_3\} \in S$, no other point $\{p_k\} \in S$ falls inside the circumcircle of the triangle formed by the 3 points

This project is aimed at modeling the generation of a delaunay triangulation of an arbitrary set of points.  Classical methods are numerous, some of which have a $O(n \log (n))$ complexity. 

It is yet to be seen how the spatial information will be encoded. 

### **Notes**

*   Datafiles can be parsed, this needs to be done for every single datafile, which contains thousands of figures.


