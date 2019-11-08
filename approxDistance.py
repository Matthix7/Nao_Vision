# -*- coding: utf-8 -*-

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

radius = np.array([4.03,4.30,4.94,7.5,9.55,13.9,22.12,27.2,53])
dist = np.array([3.078,2.793,1.975,1.568,1.227,0.927,0.626,0.555,0.333])

def getDistance(radius, Sf, offset, px):
    buoySize = 0.09
    distBuoy = offset + buoySize/np.tan(2*Sf*radius+px)    #Possibly too much parameters, risk of overfitting
    return distBuoy

parameters, sigma = curve_fit(getDistance, radius, dist, [0.003, 0, 0])
factor = parameters[0]
offset = parameters[1]
px = parameters[2]

print "\nApproximated parameters :\n", "Sf: ", factor, "\nOffset: ", offset, "\npixel offset: ", px
print "\nwith variance :\n",  sigma

#Sf = 0.003
testRadius = np.linspace(4, 55, 100)
plt.plot(radius, dist, 'ob', label = "Measured distances")
plt.plot(testRadius, getDistance(testRadius, factor, offset, px), 'xr', label = "Calculated distances")

plt.legend()
plt.xlabel("Measured radius in pixels")
plt.ylabel("Distance in m")
plt.grid()
plt.show()


err = np.sum((getDistance(radius, factor, offset, px)-dist)**2)
print "With R²: ", err



#Sf = 0.01
#radius = linspace(3,20,20) 
#plt.plot(radius, 0.09/tan(2*Sf*radius), 'xr', label = "Calculated distances")
#plt.show()  




