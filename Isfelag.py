import Marel.Mp5.Process.UnitOperations
from Marel.Mp5.Process import *
import System
from System import *
from Marel.Mp5.Base.Diagnostics import MpsTraceSwitch
from Marel.Mp5.Process.UnitOperations import UnitException
from Marel.Mp5.Process.Services.UnitOperations import OperationContext
from System import Random


trace.Put("Running script for calculating pallet weight")
#Það sem vantar er að geta bail þegar brettið er þyngra en það sem verið er að vigta.

if context.CurrentPack.Record.Pallet == None:
	trace.Put("No Pallet for pack")
else:
	trace.Put("Pack has Pallet")
	if context.CurrentPallet.Record.Weight > 0:
		trace.Put("Brettið er með þyngd á sér {0}",context.CurrentPallet.Weight)
		context.CurrentPack.Record.Weight = (context.CurrentPack.Record.Weight) - (context.CurrentPallet.Weight)
		trace.Put("Ný þyngd á pakka er {0}", context.CurrentPack.Weight)
	else:
		trace.Put("Ekki 1 pakki á bretti!!!!")