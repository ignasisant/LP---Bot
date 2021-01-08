import os
from os import listdir, remove, getcwd
from os.path import isfile, join, abspath
import pickle
import re


class GestorSkylines:

    def __init__(self):
        self.path = ''

    def skylinesFets(self):
        return {re.sub(r'.sky', '', file) for file in listdir(os.getcwd()) if isfile( file)}

    def loadSkyline(self, path):
        file = open(path, 'rb')
        dades = pickle.load(file)
        file.close()
        return dades

    def saveSkyline(self, skyline):
        try:
            os.mkdir(self.path[:self.path.find('/')])
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        fh = open(self.path, "wb")
        pickle.dump(skyline, fh)
        fh.close()

        # outfile = open(id + '.sky', 'wb')
        # pickle.dump(skyline, outfile)
        # outfile.close()
    


    
    