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
	if context.CurrentPallet.Record.Weight > 1:
		trace.Put("Pallet has more than 1 pack so update required")
		context.CurrentPack.Record.Weight = (context.CurrentPack.Record.Weight) - (context.CurrentPallet.Weight)
		trace.Put("Pallet weight set to pack count times fixed weight")
	else:
		trace.Put("Ekki 1 pakki á bretti!!!!")