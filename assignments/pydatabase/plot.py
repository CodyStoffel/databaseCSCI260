import matplotlib.pyplot as plt
from db import *

def makeplotYN(cursor,axs,field,value,xpos,ypos):
    cursor.execute("select price from housing where %s='%s'; "%(field,value))
    data=cursor.fetchall()
    prices = [x[0] for x in data]
    #fieldValues = [x[1] for x in data]

    axs[xpos,ypos].hist(prices,bins=10,range=(1750000,13300000))
    axs[xpos,ypos].set_ylabel("%s=%s"%(field,value))
    axs[xpos,ypos].set_xlabel("price")

def makeplot(cursor,axs,field,xpos,ypos):
    cursor.execute("select avg(price), %s from housing group by %s;"%(field,field))
    data=cursor.fetchall()
    prices = [x[0] for x in data]
    fieldValues = [x[1] for x in data]

    axs[xpos,ypos].scatter(fieldValues, prices)
    axs[xpos,ypos].set_ylabel("avg price")
    axs[xpos,ypos].set_xlabel(field)


cursor = connectDB()

fig, axs = plt.subplots(nrows=5,ncols=4)

makeplot(cursor,axs,"area",0,0)
makeplot(cursor,axs,"stories",0,1)
makeplot(cursor,axs,"bathrooms",0,2)
makeplot(cursor,axs,"bedrooms",0,3)


makeplotYN(cursor,axs,"prefarea","yes",1,0)
makeplotYN(cursor,axs,"prefarea","no",1,1)
makeplotYN(cursor,axs,"mainroad","yes",1,2)
makeplotYN(cursor,axs,"mainroad","no",1,3)

makeplotYN(cursor,axs,"basement","yes",2,0)
makeplotYN(cursor,axs,"basement","no",2,1)
makeplotYN(cursor,axs,"guestroom","yes",2,2)
makeplotYN(cursor,axs,"guestroom","no",2,3)

makeplotYN(cursor,axs,"hotwaterheating","yes",3,0)
makeplotYN(cursor,axs,"hotwaterheating","no",3,1)
makeplotYN(cursor,axs,"airconditioning","yes",3,2)
makeplotYN(cursor,axs,"airconditioning","no",3,3)

makeplotYN(cursor,axs,"furnishingstatus","unfurnished",4,0)
makeplotYN(cursor,axs,"furnishingstatus","semi-furnished",4,1)
makeplotYN(cursor,axs,"furnishingstatus","furnished",4,2)
makeplot(cursor,axs,"parking",4,3)


plt.show()

disconnectDB()