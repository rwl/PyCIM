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

from CIM14.Element import Element

class TelephoneNumber(Element):
    """Telephone number.
    """

    def __init__(self, countryCode='', cityCode='', areaCode='', localNumber='', extension='', **kw_args):
        """Initializes a new 'TelephoneNumber' instance.

        @param countryCode: Country code. 
        @param cityCode: (if applicable) City code. 
        @param areaCode: Area or region code. 
        @param localNumber: Main (local) part of this telephone number. 
        @param extension: (if applicable) Extension for this telephone number. 
        """
        #: Country code.
        self.countryCode = countryCode

        #: (if applicable) City code.
        self.cityCode = cityCode

        #: Area or region code.
        self.areaCode = areaCode

        #: Main (local) part of this telephone number.
        self.localNumber = localNumber

        #: (if applicable) Extension for this telephone number.
        self.extension = extension

        super(TelephoneNumber, self).__init__(**kw_args)

