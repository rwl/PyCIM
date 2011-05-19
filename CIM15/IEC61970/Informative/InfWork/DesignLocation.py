# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class DesignLocation(IdentifiedObject):
    """A logical part of the design (e.g., pole and all equipment on a pole). This includes points and spans.A logical part of the design (e.g., pole and all equipment on a pole). This includes points and spans.
    """

    def __init__(self, spanLength=0.0, status=None, MaterialItems=None, Designs=None, DesignLocationCUs=None, WorkLocations=None, Diagrams=None, MiscCostItems=None, ErpBomItemDatas=None, ConditionFactors=None, *args, **kw_args):
        """Initialises a new 'DesignLocation' instance.

        @param spanLength: The legth of the span from the previous pole to this pole. 
        @param status:
        @param MaterialItems:
        @param Designs:
        @param DesignLocationCUs:
        @param WorkLocations:
        @param Diagrams:
        @param MiscCostItems:
        @param ErpBomItemDatas:
        @param ConditionFactors:
        """
        #: The legth of the span from the previous pole to this pole.
        self.spanLength = spanLength

        self.status = status

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        self._Designs = []
        self.Designs = [] if Designs is None else Designs

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        self._WorkLocations = []
        self.WorkLocations = [] if WorkLocations is None else WorkLocations

        self._Diagrams = []
        self.Diagrams = [] if Diagrams is None else Diagrams

        self._MiscCostItems = []
        self.MiscCostItems = [] if MiscCostItems is None else MiscCostItems

        self._ErpBomItemDatas = []
        self.ErpBomItemDatas = [] if ErpBomItemDatas is None else ErpBomItemDatas

        self._ConditionFactors = []
        self.ConditionFactors = [] if ConditionFactors is None else ConditionFactors

        super(DesignLocation, self).__init__(*args, **kw_args)

    _attrs = ["spanLength"]
    _attr_types = {"spanLength": float}
    _defaults = {"spanLength": 0.0}
    _enums = {}
    _refs = ["status", "MaterialItems", "Designs", "DesignLocationCUs", "WorkLocations", "Diagrams", "MiscCostItems", "ErpBomItemDatas", "ConditionFactors"]
    _many_refs = ["MaterialItems", "Designs", "DesignLocationCUs", "WorkLocations", "Diagrams", "MiscCostItems", "ErpBomItemDatas", "ConditionFactors"]

    status = None

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for x in self._MaterialItems:
            x.DesignLocation = None
        for y in value:
            y._DesignLocation = self
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj.DesignLocation = self

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj.DesignLocation = None

    def getDesigns(self):
        
        return self._Designs

    def setDesigns(self, value):
        for p in self._Designs:
            filtered = [q for q in p.DesignLocations if q != self]
            self._Designs._DesignLocations = filtered
        for r in value:
            if self not in r._DesignLocations:
                r._DesignLocations.append(self)
        self._Designs = value

    Designs = property(getDesigns, setDesigns)

    def addDesigns(self, *Designs):
        for obj in Designs:
            if self not in obj._DesignLocations:
                obj._DesignLocations.append(self)
            self._Designs.append(obj)

    def removeDesigns(self, *Designs):
        for obj in Designs:
            if self in obj._DesignLocations:
                obj._DesignLocations.remove(self)
            self._Designs.remove(obj)

    def getDesignLocationCUs(self):
        
        return self._DesignLocationCUs

    def setDesignLocationCUs(self, value):
        for x in self._DesignLocationCUs:
            x.DesignLocation = None
        for y in value:
            y._DesignLocation = self
        self._DesignLocationCUs = value

    DesignLocationCUs = property(getDesignLocationCUs, setDesignLocationCUs)

    def addDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            obj.DesignLocation = self

    def removeDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            obj.DesignLocation = None

    def getWorkLocations(self):
        
        return self._WorkLocations

    def setWorkLocations(self, value):
        for p in self._WorkLocations:
            filtered = [q for q in p.DesignLocations if q != self]
            self._WorkLocations._DesignLocations = filtered
        for r in value:
            if self not in r._DesignLocations:
                r._DesignLocations.append(self)
        self._WorkLocations = value

    WorkLocations = property(getWorkLocations, setWorkLocations)

    def addWorkLocations(self, *WorkLocations):
        for obj in WorkLocations:
            if self not in obj._DesignLocations:
                obj._DesignLocations.append(self)
            self._WorkLocations.append(obj)

    def removeWorkLocations(self, *WorkLocations):
        for obj in WorkLocations:
            if self in obj._DesignLocations:
                obj._DesignLocations.remove(self)
            self._WorkLocations.remove(obj)

    def getDiagrams(self):
        
        return self._Diagrams

    def setDiagrams(self, value):
        for p in self._Diagrams:
            filtered = [q for q in p.DesignLocations if q != self]
            self._Diagrams._DesignLocations = filtered
        for r in value:
            if self not in r._DesignLocations:
                r._DesignLocations.append(self)
        self._Diagrams = value

    Diagrams = property(getDiagrams, setDiagrams)

    def addDiagrams(self, *Diagrams):
        for obj in Diagrams:
            if self not in obj._DesignLocations:
                obj._DesignLocations.append(self)
            self._Diagrams.append(obj)

    def removeDiagrams(self, *Diagrams):
        for obj in Diagrams:
            if self in obj._DesignLocations:
                obj._DesignLocations.remove(self)
            self._Diagrams.remove(obj)

    def getMiscCostItems(self):
        
        return self._MiscCostItems

    def setMiscCostItems(self, value):
        for x in self._MiscCostItems:
            x.DesignLocation = None
        for y in value:
            y._DesignLocation = self
        self._MiscCostItems = value

    MiscCostItems = property(getMiscCostItems, setMiscCostItems)

    def addMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj.DesignLocation = self

    def removeMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj.DesignLocation = None

    def getErpBomItemDatas(self):
        
        return self._ErpBomItemDatas

    def setErpBomItemDatas(self, value):
        for x in self._ErpBomItemDatas:
            x.DesignLocation = None
        for y in value:
            y._DesignLocation = self
        self._ErpBomItemDatas = value

    ErpBomItemDatas = property(getErpBomItemDatas, setErpBomItemDatas)

    def addErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj.DesignLocation = self

    def removeErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj.DesignLocation = None

    def getConditionFactors(self):
        
        return self._ConditionFactors

    def setConditionFactors(self, value):
        for p in self._ConditionFactors:
            filtered = [q for q in p.DesignLocations if q != self]
            self._ConditionFactors._DesignLocations = filtered
        for r in value:
            if self not in r._DesignLocations:
                r._DesignLocations.append(self)
        self._ConditionFactors = value

    ConditionFactors = property(getConditionFactors, setConditionFactors)

    def addConditionFactors(self, *ConditionFactors):
        for obj in ConditionFactors:
            if self not in obj._DesignLocations:
                obj._DesignLocations.append(self)
            self._ConditionFactors.append(obj)

    def removeConditionFactors(self, *ConditionFactors):
        for obj in ConditionFactors:
            if self in obj._DesignLocations:
                obj._DesignLocations.remove(self)
            self._ConditionFactors.remove(obj)

