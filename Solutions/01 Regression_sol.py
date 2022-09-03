class LinearRegression:
    def __init__(self):
        self.m = 0
        self.b = 0

    def fit(self, x, y):
        xMean = sum(x)/len(x)
        yMean = sum(y)/len(y)
        sig_xy = 0
        sig_x2 = 0
        for i, j in zip(x, y):
            sig_xy += i*j
            sig_x2 += i**2
        sig_x = sum(x)
        self.m = (sig_xy - sig_x * yMean)/(sig_x2 - sig_x * xMean)
        self.b = yMean - self.m * xMean

    def predict(self, X):
        return self.m * X + self.b

    def slope(self):
        return self.m

    def intercept(self):
        return self.b

x = [1, 2, 3, 4, 5]
y = [5, 7, 9, 11, 14]
p = LinearRegression()
p.fit(x, y)
print("Slope:", p.slope())
print("B:", round(p.intercept(), 3))
print("Prediction:", p.predict(6))
