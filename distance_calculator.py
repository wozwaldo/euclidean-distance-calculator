import math

# Define the list of points as tuples
points = [(0, 0), (3, 4), (5, 12), (9, 40)] 

# Euclidean Distance function
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Calculate distances between every pair of points
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Find the minimum distance
min_distance = min(distances)

# Print results
print("The distances between points are:", distances)
print("The minimum distance is:", min_distance)