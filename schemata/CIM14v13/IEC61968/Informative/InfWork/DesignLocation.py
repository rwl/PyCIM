# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class DesignLocation(IdentifiedObject):
    """A logical part of the design (e.g., pole and all equipment on a pole). This includes points and spans.
    """

    def __init__(self, spanLength=0.0, MaterialItems=None, DesignLocationCUs=None, Designs=None, status=None, MiscCostItems=None, ConditionFactors=None, Diagrams=None, ErpBomItemDatas=None, WorkLocations=None, *args, **kw_args):
        """Initializes a new 'DesignLocation' instance.

        @param spanLength: The legth of the span from the previous pole to this pole. 
        @param MaterialItems:
        @param DesignLocationCUs:
        @param Designs:
        @param status:
        @param MiscCostItems:
        @param ConditionFactors:
        @param Diagrams:
        @param ErpBomItemDatas:
        @param WorkLocations:
        """
        #: The legth of the span from the previous pole to this pole. 
        self.spanLength = spanLength

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        self._Designs = []
        self.Designs = [] if Designs is None else Designs

        self.status = status

        self._MiscCostItems = []
        self.MiscCostItems = [] if MiscCostItems is None else MiscCostItems

        self._ConditionFactors = []
        self.ConditionFactors = [] if ConditionFactors is None else ConditionFactors

        self._Diagrams = []
        self.Diagrams = [] if Diagrams is None else Diagrams

        self._ErpBomItemDatas = []
        self.ErpBomItemDatas = [] if ErpBomItemDatas is None else ErpBomItemDatas

        self._WorkLocations = []
        self.WorkLocations = [] if WorkLocations is None else WorkLocations

        super(DesignLocation, self).__init__(*args, **kw_args)

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for x in self._MaterialItems:
            x._DesignLocation = None
        for y in value:
            y._DesignLocation = self
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj._DesignLocation = self
            self._MaterialItems.append(obj)

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj._DesignLocation = None
            self._MaterialItems.remove(obj)

    def getDesignLocationCUs(self):
        
        return self._DesignLocationCUs

    def setDesignLocationCUs(self, value):
        for x in self._DesignLocationCUs:
            x._DesignLocation = None
        for y in value:
            y._DesignLocation = self
        self._DesignLocationCUs = value

    DesignLocationCUs = property(getDesignLocationCUs, setDesignLocationCUs)

    def addDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            obj._DesignLocation = self
            self._DesignLocationCUs.append(obj)

    def removeDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            obj._DesignLocation = None
            self._DesignLocationCUs.remove(obj)

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

    status = None

    def getMiscCostItems(self):
        
        return self._MiscCostItems

    def setMiscCostItems(self, value):
        for x in self._MiscCostItems:
            x._DesignLocation = None
        for y in value:
            y._DesignLocation = self
        self._MiscCostItems = value

    MiscCostItems = property(getMiscCostItems, setMiscCostItems)

    def addMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj._DesignLocation = self
            self._MiscCostItems.append(obj)

    def removeMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj._DesignLocation = None
            self._MiscCostItems.remove(obj)

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

    def getErpBomItemDatas(self):
        
        return self._ErpBomItemDatas

    def setErpBomItemDatas(self, value):
        for x in self._ErpBomItemDatas:
            x._DesignLocation = None
        for y in value:
            y._DesignLocation = self
        self._ErpBomItemDatas = value

    ErpBomItemDatas = property(getErpBomItemDatas, setErpBomItemDatas)

    def addErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj._DesignLocation = self
            self._ErpBomItemDatas.append(obj)

    def removeErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj._DesignLocation = None
            self._ErpBomItemDatas.remove(obj)

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

