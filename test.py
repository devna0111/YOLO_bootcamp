from sklearn.linear_model import LinearRegression

model = LinearRegression()
x = [[2,4,6,8]]
y = [[81,93,91,97]]

model.fit(x,y)
print(model.predict(x))
