author = "Vladyslav M"
url = "https://github.com/vlmarch"

import clr
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("System")
import System
from System import Array
from System.Collections.Generic import List

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import *
# from Autodesk.Revit.UI import Selection

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# clr.AddReference('DSCoreNodes')
# from DSCore import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
# app = uiapp.Application
uidoc = uiapp.ActiveUIDocument

# view = doc.ActiveView

# Selected elements
# elems_ids = uidoc.Selection.GetElementIds()
# elems = []

# for id in elems_ids:
#	try: elems.append(doc.GetElement(id))
#	except: elems.append(None)

dataEnteringNode = IN

if isinstance(IN[0],list): elems = UnwrapElement(IN[0])
else: elems = [UnwrapElement(IN[0])]

# TransactionManager.Instance.EnsureInTransaction(doc)
# TransactionManager.Instance.TransactionTaskDone()

# new_transaction = Transaction(doc)
# new_transaction.Start("New Transaction")
# new_transaction.Commit()

OUT = elems
