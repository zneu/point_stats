# Point Statistics
Takes coordinates of multiple points from user and calculates the total Euclidean distance between subsequent pairs of points (i.e., line segments). The use story is as follows:
* The user specifies the number of points she wants to input (e.g., 3).
* Sequentially, for each point, the user enters its coordinates, for example, (x1, y1), (x2, y2), (x3, y3) or x1, y1, x2, y2, x3, y3.
* The code calculates the distance from point Pk to the consecutive point Pk+1 (e.g., from point P1 to point P2, from P2 to P3; see figure 1).
* The total distance (Total_d) is derived by summing up the lengths of the individual line segments (e.g., Total_d = dP1P2 + dP2P3).
* The total distance is displayed to the user in a descriptive manner.
* Code works for any number of points (e.g., 0, 1, 10, 100+).
