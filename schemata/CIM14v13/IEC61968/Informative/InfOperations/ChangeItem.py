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

class ChangeItem(IdentifiedObject):
    """Description for a single change within an ordered list of changes.
    """

    def __init__(self, kind='add', sequenceNumber=0, PowerSystemResource=None, Location=None, Organisation=None, status=None, Asset=None, Document=None, GmlObservation=None, ErpPerson=None, Measurement=None, GmlSelector=None, ChangeSet=None, NetworkDataSet=None, **kw_args):
        """Initializes a new 'ChangeItem' instance.

        @param kind: Kind of change for the associated object. Values are: "add", "modify", "delete"
        @param sequenceNumber: Relative order of this ChangeItem in an ordered sequence of changes. 
        @param PowerSystemResource:
        @param Location:
        @param Organisation:
        @param status:
        @param Asset:
        @param Document:
        @param GmlObservation:
        @param ErpPerson:
        @param Measurement:
        @param GmlSelector:
        @param ChangeSet:
        @param NetworkDataSet:
        """
        #: Kind of change for the associated object.Values are: "add", "modify", "delete"
        self.kind = kind

        #: Relative order of this ChangeItem in an ordered sequence of changes.
        self.sequenceNumber = sequenceNumber

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._Location = None
        self.Location = Location

        self._Organisation = None
        self.Organisation = Organisation

        self.status = status

        self._Asset = None
        self.Asset = Asset

        self._Document = None
        self.Document = Document

        self._GmlObservation = None
        self.GmlObservation = GmlObservation

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._Measurement = None
        self.Measurement = Measurement

        self._GmlSelector = None
        self.GmlSelector = GmlSelector

        self._ChangeSet = None
        self.ChangeSet = ChangeSet

        self._NetworkDataSet = None
        self.NetworkDataSet = NetworkDataSet

        super(ChangeItem, self).__init__(**kw_args)

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.ChangeItems if x != self]
            self._PowerSystemResource._ChangeItems = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._ChangeItems.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getLocation(self):
        
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.ChangeItems if x != self]
            self._Location._ChangeItems = filtered

        self._Location = value
        if self._Location is not None:
            self._Location._ChangeItems.append(self)

    Location = property(getLocation, setLocation)

    def getOrganisation(self):
        
        return self._Organisation

    def setOrganisation(self, value):
        if self._Organisation is not None:
            filtered = [x for x in self.Organisation.ChangeItems if x != self]
            self._Organisation._ChangeItems = filtered

        self._Organisation = value
        if self._Organisation is not None:
            self._Organisation._ChangeItems.append(self)

    Organisation = property(getOrganisation, setOrganisation)

    status = None

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.ChangeItems if x != self]
            self._Asset._ChangeItems = filtered

        self._Asset = value
        if self._Asset is not None:
            self._Asset._ChangeItems.append(self)

    Asset = property(getAsset, setAsset)

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.ChangeItems if x != self]
            self._Document._ChangeItems = filtered

        self._Document = value
        if self._Document is not None:
            self._Document._ChangeItems.append(self)

    Document = property(getDocument, setDocument)

    def getGmlObservation(self):
        
        return self._GmlObservation

    def setGmlObservation(self, value):
        if self._GmlObservation is not None:
            filtered = [x for x in self.GmlObservation.ChangeItems if x != self]
            self._GmlObservation._ChangeItems = filtered

        self._GmlObservation = value
        if self._GmlObservation is not None:
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
            self._ErpPerson._ChangeItems.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

    def getMeasurement(self):
        
        return self._Measurement

    def setMeasurement(self, value):
        if self._Measurement is not None:
            filtered = [x for x in self.Measurement.ChangeItems if x != self]
            self._Measurement._ChangeItems = filtered

        self._Measurement = value
        if self._Measurement is not None:
            self._Measurement._ChangeItems.append(self)

    Measurement = property(getMeasurement, setMeasurement)

    def getGmlSelector(self):
        
        return self._GmlSelector

    def setGmlSelector(self, value):
        if self._GmlSelector is not None:
            filtered = [x for x in self.GmlSelector.ChangeItems if x != self]
            self._GmlSelector._ChangeItems = filtered

        self._GmlSelector = value
        if self._GmlSelector is not None:
            self._GmlSelector._ChangeItems.append(self)

    GmlSelector = property(getGmlSelector, setGmlSelector)

    def getChangeSet(self):
        
        return self._ChangeSet

    def setChangeSet(self, value):
        if self._ChangeSet is not None:
            filtered = [x for x in self.ChangeSet.ChangeItems if x != self]
            self._ChangeSet._ChangeItems = filtered

        self._ChangeSet = value
        if self._ChangeSet is not None:
            self._ChangeSet._ChangeItems.append(self)

    ChangeSet = property(getChangeSet, setChangeSet)

    def getNetworkDataSet(self):
        
        return self._NetworkDataSet

    def setNetworkDataSet(self, value):
        if self._NetworkDataSet is not None:
            filtered = [x for x in self.NetworkDataSet.ChangeItems if x != self]
            self._NetworkDataSet._ChangeItems = filtered

        self._NetworkDataSet = value
        if self._NetworkDataSet is not None:
            self._NetworkDataSet._ChangeItems.append(self)

    NetworkDataSet = property(getNetworkDataSet, setNetworkDataSet)

