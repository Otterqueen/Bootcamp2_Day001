import numpy as np
import math

class TinyStatistician():

    def mean(self, array):
        tot = 0 
        cmpt = 0
        for val in array:
            cmpt = cmpt + 1
            tot = tot + val
        moy = tot / cmpt
        return (float(moy))

    def median(self, array):
        array = np.sort(array)
        middle = len(array)/2
        if type(middle) == int :
            median = (array[middle] + array[middle+1]) / 2
        else:
            median = array[int(middle)]
        return float(median)
    
    def quartiles(self, array, percentile):
        array = np.sort(array)
        l = len(array)
        if percentile == 50: 
            return self.median(array)
        index = (percentile * l)/100
        if type(index) == int :
            quart = array[index]
        else:
            quart = array[int(index)]
        return float(quart)
    
    def var(self, array):
        tot = 0
        moy = self.mean(array)
        l = len(array)
        for x in array:
            tot = tot + pow(x - moy, 2)
        var = tot / l 
        return float(var)

    def std(self, array):
        var = self.var(array)
        ecart = math.sqrt(var)
        return float(ecart)