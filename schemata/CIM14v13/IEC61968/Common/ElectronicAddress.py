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

class ElectronicAddress(IdentifiedObject):
    """Electronic address information.
    """

    def __init__(self, web='', email='', password='', lan='', userID='', radio='', ErpTelephoneNumbers=None, Locations=None, Cashier=None, ErpPerson=None, Asset=None, status=None, Document=None, Organisation=None, *args, **kw_args):
        """Initializes a new 'ElectronicAddress' instance.

        @param web: World Wide Web address. 
        @param email: Email address. 
        @param password: Password needed to log in. 
        @param lan: Address on local area network. 
        @param userID: User ID needed to log in, which can be for an individual person, an organisation, a location, etc. 
        @param radio: Radio address. 
        @param ErpTelephoneNumbers:
        @param Locations: All locations having this electronic address.
        @param Cashier:
        @param ErpPerson:
        @param Asset: Asset owning this electronic address.
        @param status: Status of this electronic address.
        @param Document:
        @param Organisation: Organisation owning this electronic address.
        """
        #: World Wide Web address.
        self.web = web

        #: Email address.
        self.email = email

        #: Password needed to log in.
        self.password = password

        #: Address on local area network.
        self.lan = lan

        #: User ID needed to log in, which can be for an individual person, an organisation, a location, etc.
        self.userID = userID

        #: Radio address.
        self.radio = radio

        self._ErpTelephoneNumbers = []
        self.ErpTelephoneNumbers = [] if ErpTelephoneNumbers is None else ErpTelephoneNumbers

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._Cashier = None
        self.Cashier = Cashier

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._Asset = None
        self.Asset = Asset

        self.status = status

        self._Document = None
        self.Document = Document

        self._Organisation = None
        self.Organisation = Organisation

        super(ElectronicAddress, self).__init__(*args, **kw_args)

    def getErpTelephoneNumbers(self):
        
        return self._ErpTelephoneNumbers

    def setErpTelephoneNumbers(self, value):
        for x in self._ErpTelephoneNumbers:
            x._ElectronicAddress = None
        for y in value:
            y._ElectronicAddress = self
        self._ErpTelephoneNumbers = value

    ErpTelephoneNumbers = property(getErpTelephoneNumbers, setErpTelephoneNumbers)

    def addErpTelephoneNumbers(self, *ErpTelephoneNumbers):
        for obj in ErpTelephoneNumbers:
            obj._ElectronicAddress = self
            self._ErpTelephoneNumbers.append(obj)

    def removeErpTelephoneNumbers(self, *ErpTelephoneNumbers):
        for obj in ErpTelephoneNumbers:
            obj._ElectronicAddress = None
            self._ErpTelephoneNumbers.remove(obj)

    def getLocations(self):
        """All locations having this electronic address.
        """
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.ElectronicAddresses if q != self]
            self._Locations._ElectronicAddresses = filtered
        for r in value:
            if self not in r._ElectronicAddresses:
                r._ElectronicAddresses.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._ElectronicAddresses:
                obj._ElectronicAddresses.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._ElectronicAddresses:
                obj._ElectronicAddresses.remove(self)
            self._Locations.remove(obj)

    def getCashier(self):
        
        return self._Cashier

    def setCashier(self, value):
        if self._Cashier is not None:
            filtered = [x for x in self.Cashier.ElectronicAddresses if x != self]
            self._Cashier._ElectronicAddresses = filtered

        self._Cashier = value
        if self._Cashier is not None:
            self._Cashier._ElectronicAddresses.append(self)

    Cashier = property(getCashier, setCashier)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.ElectronicAddresses if x != self]
            self._ErpPerson._ElectronicAddresses = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            self._ErpPerson._ElectronicAddresses.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

    def getAsset(self):
        """Asset owning this electronic address.
        """
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.ElectronicAddresses if x != self]
            self._Asset._ElectronicAddresses = filtered

        self._Asset = value
        if self._Asset is not None:
            self._Asset._ElectronicAddresses.append(self)

    Asset = property(getAsset, setAsset)

    # Status of this electronic address.
    status = None

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            self._Document._ElectronicAddress = None

        self._Document = value
        if self._Document is not None:
            self._Document._ElectronicAddress = self

    Document = property(getDocument, setDocument)

    def getOrganisation(self):
        """Organisation owning this electronic address.
        """
        return self._Organisation

    def setOrganisation(self, value):
        if self._Organisation is not None:
            filtered = [x for x in self.Organisation.ElectronicAddresses if x != self]
            self._Organisation._ElectronicAddresses = filtered

        self._Organisation = value
        if self._Organisation is not None:
            self._Organisation._ElectronicAddresses.append(self)

    Organisation = property(getOrganisation, setOrganisation)

