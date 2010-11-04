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

class LocationGrant(Agreement):
    """A grant provides a right, as defined by type, for a parcel of land. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """

    def __init__(self, propertyData='', LandProperty=None, *args, **kw_args):
        """Initializes a new 'LocationGrant' instance.

        @param propertyData: Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        @param LandProperty: Land property this location grant applies to.
        """
        #: Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.
        self.propertyData = propertyData

        self._LandProperty = None
        self.LandProperty = LandProperty

        super(LocationGrant, self).__init__(*args, **kw_args)

    def getLandProperty(self):
        """Land property this location grant applies to.
        """
        return self._LandProperty

    def setLandProperty(self, value):
        if self._LandProperty is not None:
            filtered = [x for x in self.LandProperty.LocationGrants if x != self]
            self._LandProperty._LocationGrants = filtered

        self._LandProperty = value
        if self._LandProperty is not None:
            self._LandProperty._LocationGrants.append(self)

    LandProperty = property(getLandProperty, setLandProperty)

