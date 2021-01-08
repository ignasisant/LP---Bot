import sys
import os.path
sys.path.insert(1, os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"/cl")
from GestorSkylines import GestorSkylines
import random

class Skyline:

    def __init__(self):
        self.skylines = []
        self.data = GestorSkylines()
        self.variables = {}
        self.last_letter = None

    def getPrintSkyline(self):
        if self.last_letter:
            return self.getSkyline(self.last_letter)
        else:
            return self.skylines or None

    def getSkylinesID(self):
        return self.variables.keys() or None
    
    def getSkyline(self, id):
        return self.variables.get(id) or None

    def addBuilding(self,r):
        self.skylines.append(r)
    
    def printSkylines(self):
        print('Skylines')
        print(self.skylines)
        print('vars')
        print(self.variables)
    
    def generateRandom(self,n,h,w,xmin,xmax):
        random_skyline = []
        while(n>0):
            altura = random.randint(0,h)
            amplada = random.randint(0,w)
            xinici = random.randint(xmin,xmax-amplada)
            xfi = xinici + amplada
            random_skyline.append([xinici,altura,xfi])
            n -= 1
        return random_skyline

    def assignaVar(self,var, skyline):
        self.variables[var]=skyline

    def setVar(self, var):
        if not self.last_letter:
            self.last_letter=var
     
    def setNewMessage(self):
        self.last_letter=None
        self.skylines=[]
    
    def getArea(self, skyline):
        sum_area = 0

        for i in range(0, len(skyline)):
            x_min = skyline[i][0]
            height = skyline[i][1]
            x_max = skyline[i][2]

            sum_area += (x_max-x_min)*height       
        return sum_area




    