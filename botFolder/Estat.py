import sys
import os.path
from antlr4 import *

import pathlib
sys.path.append(
    os.path.join(pathlib.Path(__file__).parent.absolute(), '../cl')
)

from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from SkylineVisitor import SkylineVisitor
from GestorSkylines import GestorSkylines
from Skyline import Skyline
from Grafics import Grafics

class Estat:

    def __init__(self):
        self.data = GestorSkylines()
        self.skyline = Skyline()
        self.grafic = Grafics()
        

    # enllaç amb la gramatica
    def inputSkyline(self, input):
        input_stream = InputStream(input)
        lexer = SkylineLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()
        #print(tree.toStringTree(recog=parser))  #fins aqui funciona
        visitor = SkylineVisitor(self.skyline)
        visitor.visit(tree)
        
        skyline_var = self.skyline.getPrintSkyline()
        
        if skyline_var:
            img_buffer = self.grafic.pintaGrafic(skyline_var)
            area, h = self.grafic.getArea(skyline_var)

            return img_buffer, f'area: {area} \nalçada: {h}'
        else:
            return None, 'Error: Skyline format error.'

    # guardar skyline a arixu .sky
    def save(self, id, nom):
        if id:
            self.data.path = nom+'/'+id+'.sky'
            all = self.skyline.variables
            self.data.saveSkyline(all)
            return 'S\'ha guardat correctament'

        else: return  'Error al guardar'
    
    # obrir arxiu
    def load(self, id, nom):
        if id:
            self.data.path = nom+'/'+id+'.sky'
            dades = self.data.loadSkyline(id)
            self.skyline.variables = dades
            return 'S\'ha obert correctament'
        else: return  'Error al obrir'

    # llistar skylines guardats a variables
    def llista(self):
        text = ''
        for key in self.skyline.variables:
            sky = self.skyline.getSkyline(key)
            area = self.skyline.getArea(sky)
            text += 'Skyline: ' + key +'\n'
            text += 'Area: '+str(area)+'\n'
        if text == '':
            text = 'No hi ha Skylines a llistar'
        return text
    
    # borrar tots els skylines guardats a variables
    def clean(self):
        self.skyline.variables = {}
        text = "S\'han esborrat tots els skylines"
        return text


            
