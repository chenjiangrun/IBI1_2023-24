uk_cities=[0.56,0.62,0.04,9.7]
china_cities=[0.58,8.4,29.9,22.2]
import matplotlib.pyplot as plt
ukcities=["Edinburgh","Glasgow","Stirling","London"]
chinacities=["Haning","Hangzhou","Shanghai","Beijing"]
#draw UK cityies figure
plt.figure()
plt.bar(ukcities,uk_cities)
plt.ylabel("Population")
plt.xlabel("UK Cities")
plt.title("UK Cities size")
plt.show()
plt.clf()
#draw China cities figure
plt.figure()
plt.bar(chinacities,china_cities)
plt.ylabel("Population")
plt.xlabel("China Cities")
plt.title("China Cities size")
plt.show()
plt.clf()