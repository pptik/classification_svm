import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

X = [[6],[8],[10],[14],[18]]
y = [[7],[9],[13],[17.5],[18]]

# plt.figure()
# plt.title('Pizza Price plotted against diamater')
# plt.xlabel('Diameter in inches')
# plt.ylabel('Price in dollar')
# plt.plot(X,y, color='red')
# plt.axis([0,25,0,25])
# plt.grid(True)
# plt.show

model = LinearRegression()

model.fit(X,y)
print(model)
result = model.predict([12],[0])
print(result)