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

class ChangeItem(IdentifiedObject):
    """Description for a single change within an ordered list of changes.Description for a single change within an ordered list of changes.
    """

    def __init__(self, sequenceNumber=0, kind="add", GmlSelector=None, Organisation=None, Document=None, Asset=None, status=None, GmlObservation=None, ErpPerson=None, PowerSystemResource=None, ChangeSet=None, Location=None, NetworkDataSet=None, *args, **kw_args):
        """Initialises a new 'ChangeItem' instance.

        @param sequenceNumber: Relative order of this ChangeItem in an ordered sequence of changes. 
        @param kind: Kind of change for the associated object. Values are: "add", "modify", "delete"
        @param GmlSelector:
        @param Organisation:
        @param Document:
        @param Asset:
        @param status:
        @param GmlObservation:
        @param ErpPerson:
        @param PowerSystemResource:
        @param ChangeSet:
        @param Location:
        @param NetworkDataSet:
        """
        #: Relative order of this ChangeItem in an ordered sequence of changes.
        self.sequenceNumber = sequenceNumber

        #: Kind of change for the associated object. Values are: "add", "modify", "delete"
        self.kind = kind

        self._GmlSelector = None
        self.GmlSelector = GmlSelector

        self._Organisation = None
        self.Organisation = Organisation

        self._Document = None
        self.Document = Document

        self._Asset = None
        self.Asset = Asset

        self.status = status

        self._GmlObservation = None
        self.GmlObservation = GmlObservation

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._ChangeSet = None
        self.ChangeSet = ChangeSet

        self._Location = None
        self.Location = Location

        self._NetworkDataSet = None
        self.NetworkDataSet = NetworkDataSet

        super(ChangeItem, self).__init__(*args, **kw_args)

    _attrs = ["sequenceNumber", "kind"]
    _attr_types = {"sequenceNumber": int, "kind": str}
    _defaults = {"sequenceNumber": 0, "kind": "add"}
    _enums = {"kind": "ChangeItemKind"}
    _refs = ["GmlSelector", "Organisation", "Document", "Asset", "status", "GmlObservation", "ErpPerson", "PowerSystemResource", "ChangeSet", "Location", "NetworkDataSet"]
    _many_refs = []

    def getGmlSelector(self):
        
        return self._GmlSelector

    def setGmlSelector(self, value):
        if self._GmlSelector is not None:
            filtered = [x for x in self.GmlSelector.ChangeItems if x != self]
            self._GmlSelector._ChangeItems = filtered

        self._GmlSelector = value
        if self._GmlSelector is not None:
            if self not in self._GmlSelector._ChangeItems:
                self._GmlSelector._ChangeItems.append(self)

    GmlSelector = property(getGmlSelector, setGmlSelector)

    def getOrganisation(self):
        
        return self._Organisation

    def setOrganisation(self, value):
        if self._Organisation is not None:
            filtered = [x for x in self.Organisation.ChangeItems if x != self]
            self._Organisation._ChangeItems = filtered

        self._Organisation = value
        if self._Organisation is not None:
            if self not in self._Organisation._ChangeItems:
                self._Organisation._ChangeItems.append(self)

    Organisation = property(getOrganisation, setOrganisation)

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.ChangeItems if x != self]
            self._Document._ChangeItems = filtered

        self._Document = value
        if self._Document is not None:
            if self not in self._Document._ChangeItems:
                self._Document._ChangeItems.append(self)

    Document = property(getDocument, setDocument)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.ChangeItems if x != self]
            self._Asset._ChangeItems = filtered

        self._Asset = value
        if self._Asset is not None:
            if self not in self._Asset._ChangeItems:
                self._Asset._ChangeItems.append(self)

    Asset = property(getAsset, setAsset)

    status = None

    def getGmlObservation(self):
        
        return self._GmlObservation

    def setGmlObservation(self, value):
        if self._GmlObservation is not None:
            filtered = [x for x in self.GmlObservation.ChangeItems if x != self]
            self._GmlObservation._ChangeItems = filtered

        self._GmlObservation = value
        if self._GmlObservation is not None:
            if self not in self._GmlObservation._ChangeItems:
                self._GmlObservation._ChangeItems.append(self)

    GmlObservation = property(getGmlObservation, setGmlObservation)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.ChangeItems if x != self]
            self._ErpPerson._ChangeItems = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            if self not in self._ErpPerson._ChangeItems:
                self._ErpPerson._ChangeItems.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.ChangeItems if x != self]
            self._PowerSystemResource._ChangeItems = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            if self not in self._PowerSystemResource._ChangeItems:
                self._PowerSystemResource._ChangeItems.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getChangeSet(self):
        
        return self._ChangeSet

    def setChangeSet(self, value):
        if self._ChangeSet is not None:
            filtered = [x for x in self.ChangeSet.ChangeItems if x != self]
            self._ChangeSet._ChangeItems = filtered

        self._ChangeSet = value
        if self._ChangeSet is not None:
            if self not in self._ChangeSet._ChangeItems:
                self._ChangeSet._ChangeItems.append(self)

    ChangeSet = property(getChangeSet, setChangeSet)

    def getLocation(self):
        
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.ChangeItems if x != self]
            self._Location._ChangeItems = filtered

        self._Location = value
        if self._Location is not None:
            if self not in self._Location._ChangeItems:
                self._Location._ChangeItems.append(self)

    Location = property(getLocation, setLocation)

    def getNetworkDataSet(self):
        
        return self._NetworkDataSet

    def setNetworkDataSet(self, value):
        if self._NetworkDataSet is not None:
            filtered = [x for x in self.NetworkDataSet.ChangeItems if x != self]
            self._NetworkDataSet._ChangeItems = filtered

        self._NetworkDataSet = value
        if self._NetworkDataSet is not None:
            if self not in self._NetworkDataSet._ChangeItems:
                self._NetworkDataSet._ChangeItems.append(self)

    NetworkDataSet = property(getNetworkDataSet, setNetworkDataSet)

