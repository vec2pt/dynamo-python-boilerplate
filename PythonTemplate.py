# https://dynamopythonprimer.gitbook.io/dynamo-python-primer/
# https://primer.dynamobim.org/10_Custom-Nodes/10-4_Python.html
# https://github.com/DynamoDS/Dynamo/issues/7604
# https://dynamopythonprimer.gitbook.io/dynamo-python-primer/getting-started/boilerplate-setup-code
# https://sites.google.com/view/dto/python/anatomy-of-python-dynamo
# https://sites.google.com/view/dto/python/dynamo-dll-whats-inside


__author__ = 'Vladyslav Marchenko'
__version__ = "0.1.0"
__license__ = ""


import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Imports the standard IronPython libraries
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

# Import Dynamo's nodes for Revit
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

# Import Revit elements
from Revit.Elements import *

# Import DocumentManager / TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import DesignScript
clr.AddReference('DSCoreNodes')
from DSCore import *

# Adding reference to Revit's API DLLs
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
# from Autodesk.Revit.DB.Structure import *

# Adding reference to Revit's API DLLs
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

# The System namespace at the root of .NET
clr.AddReference('System')
import System
from System import Array
# from System.Collections.Generic import *
from System.Collections.Generic import List

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = DocumentManager.Instance.CurrentUIApplication.Application
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument


# Start Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# End Transaction
TransactionManager.Instance.TransactionTaskDone()



# app = __revit__.Application
# Ui = __revit__.ActiveUIDocument
# doc = __revit__.ActiveUIDocument.Document
# view = doc.ActiveView
#
#
# from Autodesk.Revit.UI import Selection
#
# Selected = Ui.Selection.GetElementIds()


input = UnwrapElement(IN[0])

OUT = 0
