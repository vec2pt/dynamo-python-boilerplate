author = "vec2pt"
url = "https://github.com/vec2pt"

import clr
import sys
# sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# clr.AddReference('DSCoreNodes')
# from DSCore import *

clr.AddReference("System")
# import System
from System import Array
# from System.Collections.Generic import List
# from System.Collections.Generic import *

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *
# from Autodesk.Revit.UI import Selection

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements) # ToDSType()
clr.ImportExtensions(Revit.GeometryConversion) # ToPoint(), ToVector(), ToProtoType(), ToXyz(), ToTransform(), ToRevitType()
# from Revit.GeometryConversion import *

# Dynamo
doc = DocumentManager.Instance.CurrentDBDocument
# uiapp = DocumentManager.Instance.CurrentUIApplication
# app = uiapp.Application
# uidoc = uiapp.ActiveUIDocument

# RevitPythonShell / pyRevit
# doc = __revit__.ActiveUIDocument.Document
# uidoc = __revit__.ActiveUIDocument


#############################################################################

# Instance Elements Collector
walls_inst = FilteredElementCollector(doc).OfClass(Wall).WhereElementIsNotElementType().ToElements() # ToElementIds(), FirstElement(), FirstElementId()
# .OfClass(clr.GetClrType(Wall))
windows_inst = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()

# Type Elements Collector
windows_types = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsElementType().ToElements()

# Multicategory Collector
categories_list = [BuiltInCategory.OST_Doors, BuiltInCategory.OST_Windows]
categories = List[BuiltInCategory](categories_list)
elem_filter = ElementMulticategoryFilter(categories)
elems_inst = FilteredElementCollector(doc).WherePasses(elem_filter).WhereElementIsNotElementType().ToElements()

# Filter
collector = FilteredElementCollector(doc)
category_filter = ElementCategoryFilter(BuiltInCategory.OST_Doors)
doors_inst = collector.WherePasses(category_filter).WhereElementIsNotElementType().ToElements()

# Get parameter value
elem.LookupParameter("Keynote").AsString()
elem.GetParameters("Keynote")[0].AsString()
view.get_Parameter(BuiltInParameter.VIEW_TYPE).AsString()

# Set parameter value
elem.LookupParameter("Keynote").Set("xxx")

# Selected elements
uidoc.Selection.GetElementIds()
selection = [doc.GetElement(id) for id in uidoc.Selection.GetElementIds()]

# Parameters
elem.Parameters
elem.GetOrderedParameters()
elem.ParametersMap # elem.ParametersMap.Contains("Keynote")

# Active view
view = doc.ActiveView

# Get by ID
elem = doc.GetElement(id)

# Revit Command
command_id = RevitCommandId.LookupPostableCommandId(PostableCommand.Render)
uiapp.PostCommand(command_id)

# Transaction - option 1
TransactionManager.Instance.EnsureInTransaction(doc)
TransactionManager.Instance.TransactionTaskDone()

# Transaction - option 2
new_transaction = Transaction(doc)
new_transaction.Start("Transaction name")
new_transaction.Commit()

# Transaction / SubTransaction - option 3
TransactionManager.Instance.EnsureInTransaction(doc)
sub_transaction = SubTransaction()
sub_transaction.Start()
try:
  sub_transaction.Commit()
except:
  sub_transaction.RollBack()
TransactionManager.Instance.TransactionTaskDone()

# Transaction Group
tg = TransactionGroup(doc, "Transaction Group")
tg.Start()
t1 = Transaction(doc)
t1.Start("Transaction 1")
t1.Commit()
t2 = Transaction(doc)
t2.Start("Transaction 2")
t2.Commit()
tg.Assimilate()

#############################################################################



elems = UnwrapElement(IN[0])

OUT = elems
