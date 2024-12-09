import matplotlib.pyplot as plt
from db import *

# select label,sqrt((x-cx)*(x-cx)+(y-cy)*(y-cy)+(z-cz)*(z-cz)) 

def add3DScatterData(axs,newLabel,newColor,xs,ys,zs,newS):
    axs.scatter(xs,ys,zs,label=newLabel,color=newColor,s=newS)

def add3DScatter(axs,newlabel,newcolor,newS):
    cursor.execute("select x,y,z from points where label='%s'; "%(newlabel))
    data=cursor.fetchall()
    xs = [x[0] for x in data]
    ys = [x[1] for x in data]
    zs = [x[2] for x in data]

    axs.scatter(xs,ys,zs,label=newlabel,color=newcolor,s=newS)

cursor = connectDB()
fig, axs = plt.subplots(subplot_kw={"projection": "3d"})
axs.set_xlabel('X')
axs.set_ylabel('Y')
axs.set_zlabel('Z')

add3DScatter(axs,'Red','r',5)
add3DScatter(axs,'Green','g',5)
add3DScatter(axs,'Blue','b',5)

cx,cy,cz=input("Please enter the xyz of the point you want to check: ").split()
add3DScatterData(axs,'Test','k',[int(cx)],[int(cy)],[int(cz)],200)

plt.show()

disconnectDB()