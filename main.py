import client
import lisp_parser # From here: http://norvig.com/lispy.html
from venture_infrastructure import *
from itertools import *

class stochastic_test(venture_infrastructure):

  def LoadProgram(self):
    MyRIPL = self.RIPL
    
    MyRIPL.clear() # To delete previous sessions data.

    (last_directive, _) = MyRIPL.predict(lisp_parser.parse("(>= (normal 0.0 1.0) 0.0)"))

    # add directives needed
    directives=list()
    directives.append(last_directive)

    self.directives = directives

  def __init__(self):
    import os.path
    self.name = os.path.basename(__file__)
    self.description = "TBA."
    self.posterior = {}
    self.posterior[True] = 0.5
    self.posterior[False]= 0.5
   
