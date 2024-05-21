import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/IBI/IBI1_2023-24/Practical7")
#the code for importing works
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")
#show the forth colimn from every 10th row
dalys_data.iloc[0:101:10,3]
#use a boolean to show DALYs for Afghanistan

my_columns=[True,True,False,True]
dalys_data.iloc[0:3,my_columns]
dalys_data.loc[2:4,"Year"]
#compute the mean DALYs in China
china_data=dalys_data.iloc[1140:1170,:]
np.mean(china_data.iloc[:,3])
#a plot showing the DALYs overs time in China
plt.plot(china_data.Year,china_data.DALYs,"r+")
plt.show()
plt.close()

#Are there places in the World where the DALYs in 2019 is less than 18,000? If so, where are they?
Select=dalys_data[dalys_data.Year==2019]
low_daly_places = Select[Select['DALYs'] < 18000]
print(low_daly_places['Entity'])






