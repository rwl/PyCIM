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

class Organisation(IdentifiedObject):
    """Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.
    """

    def __init__(self, BusinessRoles=None, TelephoneNumbers=None, streetAddress=None, MarketRoles=None, postalAddress=None, ElectronicAddresses=None, *args, **kw_args):
        """Initializes a new 'Organisation' instance.

        @param BusinessRoles:
        @param TelephoneNumbers: All telephone numbers of this organisation.
        @param streetAddress: Street address.
        @param MarketRoles:
        @param postalAddress: Postal address, potentially different than 'streetAddress' (e.g., another city).
        @param ElectronicAddresses: All electronic addresses of this organisation.
        """
        self._BusinessRoles = []
        self.BusinessRoles = [] if BusinessRoles is None else BusinessRoles

        self._TelephoneNumbers = []
        self.TelephoneNumbers = [] if TelephoneNumbers is None else TelephoneNumbers

        self.streetAddress = streetAddress

        self._MarketRoles = []
        self.MarketRoles = [] if MarketRoles is None else MarketRoles

        self.postalAddress = postalAddress

        self._ElectronicAddresses = []
        self.ElectronicAddresses = [] if ElectronicAddresses is None else ElectronicAddresses

        super(Organisation, self).__init__(*args, **kw_args)

    def getBusinessRoles(self):
        
        return self._BusinessRoles

    def setBusinessRoles(self, value):
        for p in self._BusinessRoles:
            filtered = [q for q in p.Organisations if q != self]
            self._BusinessRoles._Organisations = filtered
        for r in value:
            if self not in r._Organisations:
                r._Organisations.append(self)
        self._BusinessRoles = value

    BusinessRoles = property(getBusinessRoles, setBusinessRoles)

    def addBusinessRoles(self, *BusinessRoles):
        for obj in BusinessRoles:
            if self not in obj._Organisations:
                obj._Organisations.append(self)
            self._BusinessRoles.append(obj)

    def removeBusinessRoles(self, *BusinessRoles):
        for obj in BusinessRoles:
            if self in obj._Organisations:
                obj._Organisations.remove(self)
            self._BusinessRoles.remove(obj)

    def getTelephoneNumbers(self):
        """All telephone numbers of this organisation.
        """
        return self._TelephoneNumbers

    def setTelephoneNumbers(self, value):
        for x in self._TelephoneNumbers:
            x._Organisation = None
        for y in value:
            y._Organisation = self
        self._TelephoneNumbers = value

    TelephoneNumbers = property(getTelephoneNumbers, setTelephoneNumbers)

    def addTelephoneNumbers(self, *TelephoneNumbers):
        for obj in TelephoneNumbers:
            obj._Organisation = self
            self._TelephoneNumbers.append(obj)

    def removeTelephoneNumbers(self, *TelephoneNumbers):
        for obj in TelephoneNumbers:
            obj._Organisation = None
            self._TelephoneNumbers.remove(obj)

    # Street address.
    streetAddress = None

    def getMarketRoles(self):
        
        return self._MarketRoles

    def setMarketRoles(self, value):
        for p in self._MarketRoles:
            filtered = [q for q in p.Organisations if q != self]
            self._MarketRoles._Organisations = filtered
        for r in value:
            if self not in r._Organisations:
                r._Organisations.append(self)
        self._MarketRoles = value

    MarketRoles = property(getMarketRoles, setMarketRoles)

    def addMarketRoles(self, *MarketRoles):
        for obj in MarketRoles:
            if self not in obj._Organisations:
                obj._Organisations.append(self)
            self._MarketRoles.append(obj)

    def removeMarketRoles(self, *MarketRoles):
        for obj in MarketRoles:
            if self in obj._Organisations:
                obj._Organisations.remove(self)
            self._MarketRoles.remove(obj)

    # Postal address, potentially different than 'streetAddress' (e.g., another city).
    postalAddress = None

    def getElectronicAddresses(self):
        """All electronic addresses of this organisation.
        """
        return self._ElectronicAddresses

    def setElectronicAddresses(self, value):
        for x in self._ElectronicAddresses:
            x._Organisation = None
        for y in value:
            y._Organisation = self
        self._ElectronicAddresses = value

    ElectronicAddresses = property(getElectronicAddresses, setElectronicAddresses)

    def addElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            obj._Organisation = self
            self._ElectronicAddresses.append(obj)

    def removeElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            obj._Organisation = None
            self._ElectronicAddresses.remove(obj)

