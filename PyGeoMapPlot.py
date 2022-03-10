# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 14:12:11 2022

@author: cgdwo
"""



import matplotlib

import shapefile as shp
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from rasterio.plot import show



# set the family font 
font1={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':35}
font_legend={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':30}

MaskShp_path = "./Vector_mask/MASK.shp"
#reading the shape file by using reader function of the shape lib
sf = shp.Reader(MaskShp_path)
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]

filepath_1 = "../../Results/GOVar_SM_2010071600.asc"
filepath_2 = "../../Results/GOVar_SM_2010071700.asc"
filepath_3 = "../../Results/GOVar_SM_2010071800.asc"
filepath_4 = "../../Results/GOVar_SM_2010071900.asc"

with rasterio.open(filepath_1) as SoilMoisture_1:
    print('Opening:', filepath_1)
  
    SoilMoistureValue_1 = SoilMoisture_1.read(1)
    SoilMoistureValue_1[SoilMoistureValue_1 == -9999] = np.nan


with rasterio.open(filepath_2) as SoilMoisture_2:
    print('Opening:', filepath_2)
  
    SoilMoistureValue_2 = SoilMoisture_2.read(1)
    SoilMoistureValue_2[SoilMoistureValue_2 == -9999] = np.nan

with rasterio.open(filepath_3) as SoilMoisture_3:
   print('Opening:', filepath_3)
 
   SoilMoistureValue_3 = SoilMoisture_3.read(1)
   SoilMoistureValue_3[SoilMoistureValue_3 == -9999] = np.nan   
   
with rasterio.open(filepath_4) as SoilMoisture_4:
    print('Opening:', filepath_2)
  
    SoilMoistureValue_4 = SoilMoisture_4.read(1)
    SoilMoistureValue_4[SoilMoistureValue_4 == -9999] = np.nan

LeftBound = SoilMoisture_1.bounds[0]
RightBound = SoilMoisture_1.bounds[2]
BottomBound = SoilMoisture_1.bounds[1]
TopBound = SoilMoisture_1.bounds[3]



fig, axes = plt.subplots(2,2, figsize=(22,12), sharex=True, sharey=True)
plt.subplots_adjust(left=0.0,bottom=0.0,top=0.95,right=0.9,hspace=0.1,wspace=0)
plt.sca(axes[0,0])
# sr.plot(facecolor='w', edgecolor='k')
plt.plot(x, y, 'k')
plt.imshow(SoilMoistureValue_1, extent=[LeftBound,RightBound,BottomBound,TopBound], cmap='YlGnBu', vmin=0, vmax=100)
#plt.colorbar(shrink=0.5)
plt.title('(a) 07-16 00:00', font1)
plt.axis('off')




plt.sca(axes[0,1])
#plt.imshow(SoilMoistureValue_2, cmap='YlGnBu', vmin=0, vmax=100)
plt.imshow(SoilMoistureValue_2, extent=[LeftBound,RightBound,BottomBound,TopBound], cmap='YlGnBu', vmin=0, vmax=100)
plt.plot(x, y, 'k')
#plt.colorbar(shrink=0.5)
plt.title('(b) 07-17 00:00', font1)
plt.axis('off')

plt.sca(axes[1,0])
#plt.imshow(SoilMoistureValue_3, cmap='YlGnBu', vmin=0, vmax=100)
plt.imshow(SoilMoistureValue_3, extent=[LeftBound,RightBound,BottomBound,TopBound], cmap='YlGnBu', vmin=0, vmax=100)
plt.plot(x, y, 'k')
#plt.colorbar(shrink=0.5)
plt.title('(c) 07-18 00:00', font1)
plt.axis('off')

plt.sca(axes[1,1])          
im = plt.imshow(SoilMoistureValue_4, extent=[LeftBound,RightBound,BottomBound,TopBound], cmap='YlGnBu', vmin=0, vmax=100)
plt.plot(x, y, 'k')
#plt.colorbar(shrink=0.5)
plt.title('(d) 07-19 00:00', font1)
plt.axis('off')

cbar_ax = fig.add_axes([0.9, 0.2, 0.03, 0.6])
cbar_ax.tick_params(labelsize=30)
cb = fig.colorbar(im, cax=cbar_ax)
cb.set_label('Soil moisture (%)', fontdict = font1)
# a = axes.colorbar(SoilMoistureValue_4, cmap='YlGnBu')

plt.show()
print("plot success!")

























