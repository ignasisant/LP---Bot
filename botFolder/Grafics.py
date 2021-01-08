import io
import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import MaxNLocator
from GestorSkylines import GestorSkylines

class Grafics:

    def initGrafic(self):
        self.grafic = plt.figure()
        self.ax = self.grafic.add_subplot(111,aspect='equal')
        self.ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        self.gestorSkylines = GestorSkylines()
      
    # guarda el grafic al buffer
    def __get_grafic_buffer(self):
        buffer = io.BytesIO()
        self.grafic.savefig(buffer, format='png')
        buffer.seek(0)

        return buffer
    
    # genera el grafic
    def pintaGrafic(self, skyline):
        self.initGrafic()

        for i in range(0 , len(skyline)):
            x_min = skyline[i][0]
            height = skyline[i][1]
            x_max = skyline[i][2]

            building = patches.Rectangle(
                xy=(x_min,0),
                width=x_max-x_min, 
                height=height,
                facecolor="red")
            
            self.ax.add_patch(building)
            plt.axis("scaled")

        return self.__get_grafic_buffer()

    # calcul area
    def getArea(self, skyline):
        sum_area = 0
        h_max = 0

        for i in range(0, len(skyline)):
            x_min = skyline[i][0]
            height = skyline[i][1]
            x_max = skyline[i][2]

            sum_area += abs(x_max-x_min)*height
            h_max = max(h_max, height) 
        
        return sum_area, h_max
