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

class ErpSiteLevelData(IdentifiedObject):
    """For a utility, general information that describes physical locations of organizations or the location codes and their meanings. This enables ERP applications to ensure that the physical location identifiers are synchronized between the business applications.
    """

    def __init__(self, status=None, LandProperty=None, *args, **kw_args):
        """Initializes a new 'ErpSiteLevelData' instance.

        @param status:
        @param LandProperty:
        """
        self.status = status

        self._LandProperty = None
        self.LandProperty = LandProperty

        super(ErpSiteLevelData, self).__init__(*args, **kw_args)

    status = None

    def getLandProperty(self):
        
        return self._LandProperty

    def setLandProperty(self, value):
        if self._LandProperty is not None:
            filtered = [x for x in self.LandProperty.ErpSiteLevelDatas if x != self]
            self._LandProperty._ErpSiteLevelDatas = filtered

        self._LandProperty = value
        if self._LandProperty is not None:
            self._LandProperty._ErpSiteLevelDatas.append(self)

    LandProperty = property(getLandProperty, setLandProperty)

