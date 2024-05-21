#Create the dictionary containing the average time of students
Ac={"Sleeping":8,"Classes":6,"Studying":3.5,"TV":2,"Music":1}
Ac["Other"]=24-Ac["Sleeping"]-Ac["Classes"]-Ac["Studying"]-Ac["TV"]-Ac["Music"]
import matplotlib.pyplot as plt
#Set the labels of the graph
ac=["Sleeping","Classes","Studying","TV","Music","others"]
Time=[Ac["Sleeping"],Ac["Classes"],Ac["Studying"],Ac["TV"],Ac["Music"],Ac["others"]]
plt.figure()
plt.pie(Time,labels=ac)
plt.show()
plt.clf()

activity = input("which activity do you want to query?" +"")
if activity in Ac:
    print(f"The average number of hours spent on {activity}: {Ac[activity]} hours")
else:
    print(f"Activity '{activity}' is not included in the data.")

