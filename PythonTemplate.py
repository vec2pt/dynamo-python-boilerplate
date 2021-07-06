author = "Vladyslav M"
url = "https://github.com/vlmarch"

import clr
import sys
# sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("System")
# import System
from System import Array
# from System.Collections.Generic import List

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
clr.ImportExtensions(Revit.Elements) # ToDSType()
clr.ImportExtensions(Revit.GeometryConversion) # ToProtoType(), ToRevitType()

doc = DocumentManager.Instance.CurrentDBDocument
# uiapp = DocumentManager.Instance.CurrentUIApplication
# app = uiapp.Application
# uidoc = uiapp.ActiveUIDocument

elems = UnwrapElement(IN[0])

OUT = elems
