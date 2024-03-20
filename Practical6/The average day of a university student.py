Ac={"Sleeping":8,"Classes":6,"Studying":3.5,"TV":2,"Music":1}
Ac["Other"]=24-Ac["Sleeping"]-Ac["Classes"]-Ac["Studying"]-Ac["TV"]-Ac["Music"]
import matplotlib.pyplot as plt
ac=["Sleeping","Classes","Studying","TV","Music"]
Time=[Ac["Sleeping"],Ac["Classes"],Ac["Studying"],Ac["TV"],Ac["Music"]]
plt.figure()
plt.pie(Time,labels=ac)
plt.show()
plt.clf()


