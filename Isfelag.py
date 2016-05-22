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
	trace.Put("No Pallet for pack in context")
else:
	trace.Put("Pack has Pallet in context")

	if context.CurrentPack.Record.Weight < context.CurrentPallet.Record.Weight:
		if context.CurrentPallet.Record.Weight > 0:
			trace.Put("Pallet has more than 0 kg. so update required, weight on pallet with new pack Kg. {0}",context.CurrentPallet.Record.Weight)
			brettif = context.CurrentPack.Record.Weight - context.CurrentPallet.Record.Weight
			##New pack must be more weight than the pallet if we are adding to the pallet.
			##brettif = context.CurrentPallet.Record.Weight - context.CurrentPack.Record.Weight
			trace.Put("Start weight of pallet Kg. {0}",brettif)
			pakkie = (context.CurrentPack.Record.Weight) - (brettif)
			trace.Put("Weight of the pack we are going to add Kg. {0}",pakkie)
			##Breytum þyngd pakka í það sem verið er að bæta við; set the weight record to what we are adding to the pallet.
			context.CurrentPack.Record.Weight = pakkie
		
			trace.Put("Pack weight added to the pallet")
			context.CurrentPallet.Record.Weight = brettif + pakkie
			context.CurrentPallet.Record.CurAmount = brettif + pakkie
		
		else:
			trace.Put("The pallet is 0 or less weight")
			##Svo við bætum einfaldlega þynd pakka við bretið, so we add the pack weight to the pallet.
	else:
		trace.Put("Total pack weight can not be less than pallet, we are adding to the pallet.")
		#Vantar eitthvað hér til þess að stopa keyrsluna á unitOp Margeir
		#raise Exception("Getur ekki verið minna en bretti")
		
