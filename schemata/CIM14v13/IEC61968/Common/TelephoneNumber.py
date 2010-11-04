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

class TelephoneNumber(IdentifiedObject):
    """Telephone number.
    """

    def __init__(self, cityCode='', countryCode='', extension='', areaCode='', localNumber='', Organisation=None, Location=None, *args, **kw_args):
        """Initializes a new 'TelephoneNumber' instance.

        @param cityCode: (if applicable) City code. 
        @param countryCode: Country code. 
        @param extension: (if applicable) Extension for this telephone number. 
        @param areaCode: Area or region code. 
        @param localNumber: Main (local) part of this telephone number. 
        @param Organisation: Organisation owning this telephone number.
        @param Location: Location owning this telephone number.
        """
        #: (if applicable) City code.
        self.cityCode = cityCode

        #: Country code.
        self.countryCode = countryCode

        #: (if applicable) Extension for this telephone number.
        self.extension = extension

        #: Area or region code.
        self.areaCode = areaCode

        #: Main (local) part of this telephone number.
        self.localNumber = localNumber

        self._Organisation = None
        self.Organisation = Organisation

        self._Location = None
        self.Location = Location

        super(TelephoneNumber, self).__init__(*args, **kw_args)

    def getOrganisation(self):
        """Organisation owning this telephone number.
        """
        return self._Organisation

    def setOrganisation(self, value):
        if self._Organisation is not None:
            filtered = [x for x in self.Organisation.TelephoneNumbers if x != self]
            self._Organisation._TelephoneNumbers = filtered

        self._Organisation = value
        if self._Organisation is not None:
            self._Organisation._TelephoneNumbers.append(self)

    Organisation = property(getOrganisation, setOrganisation)

    def getLocation(self):
        """Location owning this telephone number.
        """
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.TelephoneNumbers if x != self]
            self._Location._TelephoneNumbers = filtered

        self._Location = value
        if self._Location is not None:
            self._Location._TelephoneNumbers.append(self)

    Location = property(getLocation, setLocation)

