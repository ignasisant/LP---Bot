import sys
import os.path
sys.path.insert(1, os.path.abspath(os.path.join(os.getcwd(), os.pardir))+"/botFolder")
from Skyline import Skyline
from antlr4 import *
from functools import reduce
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

    # desplaçament
    def desplaca(mat, d):
        for i in range (0, len(mat)):
            mat[i][0] += d
            mat[i][2] += d
        return mat
    
    # ens permet obtenir el xmin minim de tot el skyline, el xmax maxim de tot el skyline
    # i l'altura de l'edifici més alt del skyline
    def getMaxHMin(mat):
        _max,h,_min = reduce(
            lambda x, y: ( max(x[0],x[2],y[0],y[2]),max(x[1],y[1]), min(x[0],x[2],y[0],y[2]) ), 
            mat
        )
        return _max,h,_min

    # operacio mirall :  ens gira el skyline
    def gira(mat):
        _max,_,_min = getMaxHMin(mat)

        point_transform = lambda p: _max-(p-_min)

        return list(map(
            lambda x: [point_transform(x[2]), x[1], point_transform(x[0])], 
            mat
        ))
    
    # operació replicació 
    def repeteix(mat, d):
        result = mat.copy()
        _max,_, _min = getMaxHMin(mat)

        for square in mat:
            for i in range(1,d):
                move = (_max-_min)*i # desplaçament que haurem de fer
                result.append([square[0]+move, square[1], square[2]+move])
        return result

    # suma 1 a la posició si hi ha un edifici que ocupa la posició    
    def omple_mat(mat_skyline, mat, _mint):
        for i in range(len(mat)):
            min = mat[i][0] - _mint
            h = mat[i][1] 
            max = mat[i][2] - _mint
            for j in range(min, max):
                for t in range(0, h): #altura 0 no es compta
                    mat_skyline[j][t] += 1
        return mat_skyline
    
    # per a la unió ha de tenir en compte les posicions que tenen valor
    # més gran que 0
    def extreu_resultat_unio(mat_skyline, _mint):
        res = []
        bmin , bh , bmax= False, False, False
        min, h, max = 0,0,0
        for x in range(len(mat_skyline)):
            for y in range(len(mat_skyline[0])):
                if not(bmin):
                    if y == 0 and  mat_skyline[x][y]>0 : #comença edifici
                        bmin = True
                        min = x + _mint

                if not(bh) and bmin:
                    if y == len(mat_skyline[0])-1:  #altiura maxima no cal mirar mes
                        bh = True
                        h = y+1 #altura 0 no es compta

                    elif mat_skyline[x][y+1]==0:
                        bh = True
                        h = y+1 #altura 0 no es compta
                        
                if not(bmax) and bh and y==h-1:
                    if x == len(mat_skyline)-1: #ultim edifici, no cal mirar mes
                        bmax = True
                        max = x + _mint 
                       
                    elif mat_skyline[x+1][y] == 0:
                        #comenca un nou edifici més baix
                        bmax = True
                        max = x + _mint 

                    elif y < len(mat_skyline[0])-1:#no es l'edifici més alt
                        if mat_skyline[x+1][y]>0 and  mat_skyline[x+1][y+1]>0:
                            #comença un nou edifici mes alt
                            bmax = True
                            max = x + _mint 
                    
                # s'ha copletat un edifici , el guardem i tornem a buscar un altre
                if bmin and bh and bmax: 
                    res.append([min, h, max+1])
                    bmin , bh , bmax= False, False, False
        return res

    # operació unió
    def unio(mat1, mat2):
        matTotal = mat1
        for i in range(0, len(mat2)):
            matTotal.append(mat2[i])
        _maxt, ht, _mint = getMaxHMin(mat1 + mat2)    
        mat_skyline = [[0 for x in range(ht)] for y in range(_maxt-_mint)] 
        mat_skyline = omple_mat(mat_skyline, mat1, _mint)
        mat_skyline = omple_mat(mat_skyline, mat2, _mint)
        return extreu_resultat_unio(mat_skyline, _mint)

class SkylineVisitor(ParseTreeVisitor):

    def __init__(self, s):
        self.skyline = s

       
    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        # r = self.visitChildren(ctx)
        l = [n for n in ctx.getChildren()]
        self.skyline.setNewMessage()
        r = self.visit(l[0])
        try:
            for i in range(0, len(r)):
                self.skyline.addBuilding(r[i])
        except:
            print('Resgurardat')


    # Visit a parse tree produced by SkylineParser#skyline.
    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        l = [n for n in ctx.getChildren()] 
        if len(l) == 0:
            return []
        elif len(l) == 1:
            v = l[0].getText()
            sky = self.skyline.getSkyline(v)
            print(sky)
            return sky

        elif len(l) == 2 and l[0] == ctx.MINUS():
            aux = self.visit(l[1])
            return gira(aux)

        elif len(l) == 3: #mida 3
            if l[0] == ctx.PARO() and l[2]==ctx.PARC():
                return self.visit(l[1])             

            elif l[1] == ctx.MINUS(): #mirall
                aux = self.visit(l[0])
                return desplaca(aux, -int(l[2].getText()))

            elif l[0] == ctx.VAR(): #operacions amb variables
                v = l[0].getText()
                if l[1] == ctx.IGUAL():
                    self.skyline.setVar(v)#assignacio variable
                    self.skyline.assignaVar(l[0].getText(), self.visit(l[2]))
                    return []

                elif l[1] == ctx.MUL(): #replicacio
                    result = self.skyline.getSkyline(v)
                    return repeteix(result, int(l[2].getText()))

                elif l[1] == ctx.MES(): #unio 
                    sky = self.skyline.getSkyline(v)
                    result = self.visit(l[2])
                    return unio(sky, result)
            
            elif l[1] == ctx.MUL(): #replicacio sense variable
                if l[2] == ctx.NUM(0):
                    result = self.visit(l[0])
                    return repeteix(result, int(l[2].getText()))

                else:  #INTERSECCIO
                    aux = self.visit(l[0])
                    aux2 = self.visit(l[2])
                    for i in range(0, len(aux2)):
                        aux.append(aux2[i])
                    return aux
            
            elif l[1] == ctx.MES():
                if l[2] == ctx.NUM(0):
                    result = self.visit(l[0])
                    return desplaca(result, int(l[2].getText()))

                else: #UNIO
                    aux = self.visit(l[0])
                    aux2 = self.visit(l[2])
                    return unio(aux, aux2) 


        elif len(l) == 4:
            aux = self.visit(l[1])
            aux2 = self.visit(l[2])
            for i in range(0, len(aux2)):
                aux.append(aux2[i])
            return aux

        elif len(l) == 7: # un skyline simple
            xmin = int(l[1].getText())
            h = int(l[3].getText())
            xmax = int(l[5].getText())
            if xmax<xmin or h<0: return None
            return [[xmin,h,xmax]]  

        elif len(l) == 9: #per produir el conjunt d'skylines
            xmin = int(l[2].getText())
            h = int(l[4].getText())
            xmax = int(l[6].getText())
            if xmax<xmin or h<0: return None
            aux=[[xmin,h,xmax]]
            result = self.visit(l[8])
            for i in range(0, len(result)):
                aux.append(result[i])
            return aux

        elif len(l) == 11: #skyline random
            n = int(l[1].getText())
            h = int(l[3].getText())
            w = int(l[5].getText())
            xmin = int(l[7].getText())
            xmax = int(l[9].getText())
            if xmax<xmin or h<0 or w<0 or n<0: return None
            return unio(self.skyline.generateRandom(n,h,w,xmin,xmax), [])        

del SkylineParser