from math import sqrt
class BinaryKNN:
    def __init__(self, k):
        self.k = k
        self.neighbors = []
    
    def fit(self, data):
        for row in data:
            self.neighbors.append(row)

    def Euclidean_distance(self, x, y):
        return round(sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2), 2)

    def predict(self, data):
        distances = {}; k_nearest = []
        zeros = 0; ones = 0
        for neighbor in self.neighbors:
            d = self.Euclidean_distance(data, neighbor[0])
            k_nearest.append(d)
            distances[d] = neighbor[1]
        k_nearest = sorted(k_nearest)[:self.k]
        for i in k_nearest:
            if distances[i] == 0:
                zeros += 1
            else:
                ones += 1
        return 0 if zeros > ones else 1

    def nearest_neighbors(self):
        return self.k

# [x, y, Class]
xy = [[[7, 7], 0], [[7, 4], 0], [[3, 4], 1], [[1, 4], 1]]
k = 3
# instance = [3, 7]
instance = [6, 5]

obj = BinaryKNN(k)
obj.fit(xy)
print(instance, "is Class", obj.predict(instance))