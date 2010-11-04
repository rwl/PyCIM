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

from CIM14v13.IEC61968.Common.Agreement import Agreement

class RightOfWay(Agreement):
    """A right-of-way (ROW) is for land where it is lawful to use for a public road, an electric power line, etc. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """

    def __init__(self, propertyData='', LandProperties=None, *args, **kw_args):
        """Initializes a new 'RightOfWay' instance.

        @param propertyData: Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        @param LandProperties: All land properties this right of way applies to.
        """
        #: Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.
        self.propertyData = propertyData

        self._LandProperties = []
        self.LandProperties = [] if LandProperties is None else LandProperties

        super(RightOfWay, self).__init__(*args, **kw_args)

    def getLandProperties(self):
        """All land properties this right of way applies to.
        """
        return self._LandProperties

    def setLandProperties(self, value):
        for p in self._LandProperties:
            filtered = [q for q in p.RightOfWays if q != self]
            self._LandProperties._RightOfWays = filtered
        for r in value:
            if self not in r._RightOfWays:
                r._RightOfWays.append(self)
        self._LandProperties = value

    LandProperties = property(getLandProperties, setLandProperties)

    def addLandProperties(self, *LandProperties):
        for obj in LandProperties:
            if self not in obj._RightOfWays:
                obj._RightOfWays.append(self)
            self._LandProperties.append(obj)

    def removeLandProperties(self, *LandProperties):
        for obj in LandProperties:
            if self in obj._RightOfWays:
                obj._RightOfWays.remove(self)
            self._LandProperties.remove(obj)

