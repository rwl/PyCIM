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

class NetworkDataSet(IdentifiedObject):
    """Categorized as a type of document, model of a portion of the electrical network that includes a list of the equipment, along with relevant connectivity, electrical characteristics, geographical location, and various parameters associated with the equipment.Categorized as a type of document, model of a portion of the electrical network that includes a list of the equipment, along with relevant connectivity, electrical characteristics, geographical location, and various parameters associated with the equipment.
    """

    def __init__(self, category='', status=None, Documents=None, ChangeItems=None, ChangeSets=None, PowerSystemResources=None, *args, **kw_args):
        """Initialises a new 'NetworkDataSet' instance.

        @param category: Category of network data set. 
        @param status:
        @param Documents:
        @param ChangeItems:
        @param ChangeSets:
        @param PowerSystemResources:
        """
        #: Category of network data set.
        self.category = category

        self.status = status

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._ChangeSets = []
        self.ChangeSets = [] if ChangeSets is None else ChangeSets

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        super(NetworkDataSet, self).__init__(*args, **kw_args)

    _attrs = ["category"]
    _attr_types = {"category": str}
    _defaults = {"category": ''}
    _enums = {}
    _refs = ["status", "Documents", "ChangeItems", "ChangeSets", "PowerSystemResources"]
    _many_refs = ["Documents", "ChangeItems", "ChangeSets", "PowerSystemResources"]

    status = None

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

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x.NetworkDataSet = None
        for y in value:
            y._NetworkDataSet = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.NetworkDataSet = self

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.NetworkDataSet = None

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

