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

class NetworkDataSet(IdentifiedObject):
    """Categorized as a type of document, model of a portion of the electrical network that includes a list of the equipment, along with relevant connectivity, electrical characteristics, geographical location, and various parameters associated with the equipment.
    """

    def __init__(self, category='', Documents=None, CircuitSections=None, ChangeSets=None, PowerSystemResources=None, LandBases=None, ChangeItems=None, status=None, *args, **kw_args):
        """Initializes a new 'NetworkDataSet' instance.

        @param category: Category of network data set. 
        @param Documents:
        @param CircuitSections: A NetworkDataSet may contain sections of circuits (vs. whole circuits).
        @param ChangeSets:
        @param PowerSystemResources:
        @param LandBases:
        @param ChangeItems:
        @param status:
        """
        #: Category of network data set. 
        self.category = category

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        self._CircuitSections = []
        self.CircuitSections = [] if CircuitSections is None else CircuitSections

        self._ChangeSets = []
        self.ChangeSets = [] if ChangeSets is None else ChangeSets

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        self.LandBases = [] if LandBases is None else LandBases

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self.status = status

        super(NetworkDataSet, self).__init__(*args, **kw_args)

    def getDocuments(self):
        
        return self._Documents

    def setDocuments(self, value):
        for p in self._Documents:
            filtered = [q for q in p.NetworkDataSets if q != self]
            self._Documents._NetworkDataSets = filtered
        for r in value:
            if self not in r._NetworkDataSets:
                r._NetworkDataSets.append(self)
        self._Documents = value

    Documents = property(getDocuments, setDocuments)

    def addDocuments(self, *Documents):
        for obj in Documents:
            if self not in obj._NetworkDataSets:
                obj._NetworkDataSets.append(self)
            self._Documents.append(obj)

    def removeDocuments(self, *Documents):
        for obj in Documents:
            if self in obj._NetworkDataSets:
                obj._NetworkDataSets.remove(self)
            self._Documents.remove(obj)

    def getCircuitSections(self):
        """A NetworkDataSet may contain sections of circuits (vs. whole circuits).
        """
        return self._CircuitSections

    def setCircuitSections(self, value):
        for p in self._CircuitSections:
            filtered = [q for q in p.NetworkDataSets if q != self]
            self._CircuitSections._NetworkDataSets = filtered
        for r in value:
            if self not in r._NetworkDataSets:
                r._NetworkDataSets.append(self)
        self._CircuitSections = value

    CircuitSections = property(getCircuitSections, setCircuitSections)

    def addCircuitSections(self, *CircuitSections):
        for obj in CircuitSections:
            if self not in obj._NetworkDataSets:
                obj._NetworkDataSets.append(self)
            self._CircuitSections.append(obj)

    def removeCircuitSections(self, *CircuitSections):
        for obj in CircuitSections:
            if self in obj._NetworkDataSets:
                obj._NetworkDataSets.remove(self)
            self._CircuitSections.remove(obj)

    def getChangeSets(self):
        
        return self._ChangeSets

    def setChangeSets(self, value):
        for p in self._ChangeSets:
            filtered = [q for q in p.NetworkDataSets if q != self]
            self._ChangeSets._NetworkDataSets = filtered
        for r in value:
            if self not in r._NetworkDataSets:
                r._NetworkDataSets.append(self)
        self._ChangeSets = value

    ChangeSets = property(getChangeSets, setChangeSets)

    def addChangeSets(self, *ChangeSets):
        for obj in ChangeSets:
            if self not in obj._NetworkDataSets:
                obj._NetworkDataSets.append(self)
            self._ChangeSets.append(obj)

    def removeChangeSets(self, *ChangeSets):
        for obj in ChangeSets:
            if self in obj._NetworkDataSets:
                obj._NetworkDataSets.remove(self)
            self._ChangeSets.remove(obj)

    def getPowerSystemResources(self):
        
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for p in self._PowerSystemResources:
            filtered = [q for q in p.NetworkDataSets if q != self]
            self._PowerSystemResources._NetworkDataSets = filtered
        for r in value:
            if self not in r._NetworkDataSets:
                r._NetworkDataSets.append(self)
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self not in obj._NetworkDataSets:
                obj._NetworkDataSets.append(self)
            self._PowerSystemResources.append(obj)

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self in obj._NetworkDataSets:
                obj._NetworkDataSets.remove(self)
            self._PowerSystemResources.remove(obj)

    def add_LandBases(self, *LandBases):
        for obj in LandBases:
            self.LandBases.append(obj)

    def remove_LandBases(self, *LandBases):
        for obj in LandBases:
            self.LandBases.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._NetworkDataSet = None
        for y in value:
            y._NetworkDataSet = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._NetworkDataSet = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._NetworkDataSet = None
            self._ChangeItems.remove(obj)

    status = None

