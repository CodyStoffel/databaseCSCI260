import matplotlib.pyplot as plt
from db import *

cursor = connectDB()

cursor.execute("select avg(price), area from housing group by area;")
data=cursor.fetchall()
prices = [x[0] for x in data]
area = [x[1] for x in data]
#print(prices)

plt.scatter(area, prices)
plt.ylabel('avg price')
plt.xlabel('area')
plt.show()

disconnectDB()