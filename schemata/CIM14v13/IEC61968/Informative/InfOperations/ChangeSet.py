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

class ChangeSet(IdentifiedObject):
    """The updates required in a transaction for an existing data set are grouped into a single ChangeSet. In data sets (e.g., NetworkDataSet), each major step in the ChangeSet is described through a separate ChangeItem associated with the data set. Within each data set, each inidividual object change is described with a seperate ChangeItem associated with the object.
    """

    def __init__(self, LandBases=None, NetworkDataSets=None, ChangeItems=None, status=None, Documents=None, *args, **kw_args):
        """Initializes a new 'ChangeSet' instance.

        @param LandBases:
        @param NetworkDataSets:
        @param ChangeItems:
        @param status:
        @param Documents:
        """
        self.LandBases = [] if LandBases is None else LandBases

        self._NetworkDataSets = []
        self.NetworkDataSets = [] if NetworkDataSets is None else NetworkDataSets

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self.status = status

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        super(ChangeSet, self).__init__(*args, **kw_args)

    def add_LandBases(self, *LandBases):
        for obj in LandBases:
            self.LandBases.append(obj)

    def remove_LandBases(self, *LandBases):
        for obj in LandBases:
            self.LandBases.remove(obj)

    def getNetworkDataSets(self):
        
        return self._NetworkDataSets

    def setNetworkDataSets(self, value):
        for p in self._NetworkDataSets:
            filtered = [q for q in p.ChangeSets if q != self]
            self._NetworkDataSets._ChangeSets = filtered
        for r in value:
            if self not in r._ChangeSets:
                r._ChangeSets.append(self)
        self._NetworkDataSets = value

    NetworkDataSets = property(getNetworkDataSets, setNetworkDataSets)

    def addNetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            if self not in obj._ChangeSets:
                obj._ChangeSets.append(self)
            self._NetworkDataSets.append(obj)

    def removeNetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            if self in obj._ChangeSets:
                obj._ChangeSets.remove(self)
            self._NetworkDataSets.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._ChangeSet = None
        for y in value:
            y._ChangeSet = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._ChangeSet = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._ChangeSet = None
            self._ChangeItems.remove(obj)

    status = None

    def getDocuments(self):
        
        return self._Documents

    def setDocuments(self, value):
        for p in self._Documents:
            filtered = [q for q in p.ChangeSets if q != self]
            self._Documents._ChangeSets = filtered
        for r in value:
            if self not in r._ChangeSets:
                r._ChangeSets.append(self)
        self._Documents = value

    Documents = property(getDocuments, setDocuments)

    def addDocuments(self, *Documents):
        for obj in Documents:
            if self not in obj._ChangeSets:
                obj._ChangeSets.append(self)
            self._Documents.append(obj)

    def removeDocuments(self, *Documents):
        for obj in Documents:
            if self in obj._ChangeSets:
                obj._ChangeSets.remove(self)
            self._Documents.remove(obj)

