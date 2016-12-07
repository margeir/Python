import Marel.Mp5.Process.UnitOperations
from Marel.Mp5.Process import *
import System
from System import *
from Marel.Mp5.Base.Diagnostics import MpsTraceSwitch
from Marel.Mp5.Process.UnitOperations import UnitException
from Marel.Mp5.Process.Services.UnitOperations import OperationContext
from System import Random
#Búinn að gera þær breytingar hér sem þarf 
 
trace.Put("Running script for calculating pallet weight")
sktara = context.Data.UnitDeviceTare
context.Data.UnitDeviceTare = 0

if context.CurrentPack.Record.Pallet == None:
	trace.Put("No Pallet for pack")
else:
	trace.Put("Pakki er á bretti.")
	#trace.Put("Pakki stærð {0} og Bretti stærð {1}",context.CurrentPack.Record.Weight,context.CurrentPallet.Record.Weight)
 
	if context.CurrentPallet.Record.Weight > 0:
		trace.Put("Pallet has more than 1 pack so update required Bretti Kg. {0}",context.CurrentPallet.Record.Weight)
		brettif = context.CurrentPallet.Record.Weight - context.CurrentPack.Record.Weight
		brettig = context.CurrentPallet.Record.Gross
		pakkie = (context.CurrentPack.Record.Weight) - (brettif)
		if brettif <= sktara:
			context.CurrentPallet.Record.Tare = sktara
			#pakkie = pakkie - sktara
			#context.CurrentPallet.Record.Gross = pakkie + sktara
		if context.CurrentPack.Record.Weight > 0.2 and context.CurrentPack.Record.Weight <= brettif:
			raise Marel.Mp5.Process.UnitOperations.UnitException(Marel.Mp5.Process.UnitOperations.Result.CustomException, "Getur ekki verið minna en brettið.")
		#if context.CurrentPack.Record.Weight < sktara:
		#	raise Marel.Mp5.Process.UnitOperations.UnitException(Marel.Mp5.Process.UnitOperations.Result.CustomException, "Getur ekki verið minna en tara.")
 		trace.Put("Fyrir þennan pakka var brettið Kg. {0}",brettif)
		context.CurrentPack.Record.Weight = pakkie
		context.CurrentPack.Record.CurNominal = pakkie
		context.CurrentPack.Record.Nominal = pakkie
		context.CurrentPack.Record.CurWeight = pakkie
		context.CurrentPack.Record.Target = pakkie

		context.CurrentPallet.Record.Weight = brettif + pakkie
		context.CurrentPallet.Record.CurAmount = brettif + pakkie
		context.CurrentPallet.Record.Gross = brettif + pakkie + sktara
		mats = Marel.Mp5.Process.Data.MaterialTransactionRecords.Select(System.String.Format("pack={0}", context.CurrentPack.Record.Id), None)
		for matxact in mats:
			matxact.Weight = pakkie
			matxact.Nominal = pakkie
			matxact.UpdateChangedByKey();
			trace.PutIfTraceInfo(String.Format("Material Transaction {1} for pack {0} is now updated",context.CurrentPack.Record.Id, pakkie))
		context.CurrentPack.Record.UpdateChangedByKey();		
	else:
		trace.Put("Nýtt bretti!!!!")


