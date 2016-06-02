import Marel.Mp5.Process.UnitOperations
from Marel.Mp5.Process import *
import System
from System import *
from Marel.Mp5.Base.Diagnostics import MpsTraceSwitch
from Marel.Mp5.Process.UnitOperations import UnitException
from Marel.Mp5.Process.Services.UnitOperations import OperationContext
from System import Random


trace.Put("Running script for calculating pallet weight")


if context.CurrentPack.Record.Pallet == None:
	trace.Put("No Pallet for pack")
else:
	trace.Put("Pakki er á bretti.")
	#trace.Put("Pakki stærð {0} og Bretti stærð {1}",context.CurrentPack.Record.Weight,context.CurrentPallet.Record.Weight)

	if context.CurrentPallet.Record.Weight > 0:
		trace.Put("Pallet has more than 1 pack so update required Bretti Kg. {0}",context.CurrentPallet.Record.Weight)
		brettif = context.CurrentPallet.Record.Weight - context.CurrentPack.Record.Weight
		if context.CurrentPack.Record.Weight > 0.2 and context.CurrentPack.Record.Weight < brettif:
			raise Marel.Mp5.Process.UnitOperations.UnitException(Marel.Mp5.Process.UnitOperations.Result.CustomException, "Getur ekki verið minna en brettið")

		trace.Put("Fyrir þennan pakka var brettið Kg. {0}",brettif)
		pakkie = (context.CurrentPack.Record.Weight) - (brettif)
		context.CurrentPack.Record.Weight = pakkie
		context.CurrentPallet.Record.Weight = brettif + pakkie
		context.CurrentPallet.Record.CurAmount = brettif + pakkie
	else:
		trace.Put("Nýtt bretti!!!!")