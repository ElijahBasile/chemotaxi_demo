
from PySteppables import *
import CompuCell
import sys
from random import randint

class diffusion_controlSteppable(SteppableBasePy):

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)

        
    def start(self):
        fgf = self.getConcentrationField('FGF')
        
        for x in range(100):
            for y in range(100):
                fgf[x,y,0] = x
                
        #size of cell will be 3x3x1
        first_cell = self.newCell(self.A)
        self.cellField[10:12, 50:52, 0] = first_cell
                

        for cell in self.cellList:
            cell.targetVolume = 30.0
            cell.lambdaVolume = 10.0
            
            
        
        #assign field value
#         fgf[50,50,0] = 2000.0
        
        
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        for cell in self.cellList:
            print "cell.id=",cell.id
    def finish(self):
        # Finish Function gets called after the last MCS
        pass
        