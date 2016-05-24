#SSU Iceland MREY
#afgreidsla.py heitir þetta hjá þeim.....

import Marel.Mp5.Process.UnitOperations
from Marel.Mp5.Process import *
import System
from System import *
from System.Runtime import *

if trace.TraceInfo :
	trace.Put("Executing script")

# Working with weight
if trace.TraceInfo :
	trace.Put("uw = {0} and pc = {1}", context.Data.UnitWeight, context.Data.PackCreateCount)		
if context.Data.UnitPieces == 0 :
	context.Data.UnitPieces = 1