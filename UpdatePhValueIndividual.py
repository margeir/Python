import Marel.Mp5.Process.UnitOperations
from Marel.Mp5.Process import *
from Marel.Mp5.Base.Diagnostics import *

import System
from System import *
from System.Runtime import *

if (trace.TraceInfo) :
	trace.Put("Executing script")  

ItemRecord = context.CurrentItemRecord
#MatRecord = Marel.Mp5.Process.Data.MaterialTransactionRecordType.Instance.SelectForUpdate(System.String.Format("item={0} and xactpath=65", context.CurrentItemRecord.Id), None)

mats = Marel.Mp5.Process.Data.IndividualRecords.Select(System.String.Format("id={0}", context.Data.UnitIndividual), None); 
for record in mats: 
	if (trace.TraceInfo) :
		trace.Put("The current ItemRecord is {0}, MatXact is {1}", ItemRecord,record)

	record.PhValue = context.Data.UnitPhValue
	record.UpdateChangedByKey(); 

if (trace.TraceInfo) :
	trace.Put("Finished")

