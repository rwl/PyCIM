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

from CIM14v13.IEC61968.Informative.InfCommon.Role import Role

class LocLocRole(Role):
    """The relationship between one Location and another Location. One 'roleType' is 'Directions,' for which an additional attribute serves for providing a textual description for navigating from one location to another location.
    """

    def __init__(self, directionInfo='', ToLocation=None, FromLocation=None, *args, **kw_args):
        """Initializes a new 'LocLocRole' instance.

        @param directionInfo: Detailed directional information. 
        @param ToLocation:
        @param FromLocation:
        """
        #: Detailed directional information.
        self.directionInfo = directionInfo

        self._ToLocation = None
        self.ToLocation = ToLocation

        self._FromLocation = None
        self.FromLocation = FromLocation

        super(LocLocRole, self).__init__(*args, **kw_args)

    def getToLocation(self):
        
        return self._ToLocation

    def setToLocation(self, value):
        if self._ToLocation is not None:
            filtered = [x for x in self.ToLocation.FromLocationRoles if x != self]
            self._ToLocation._FromLocationRoles = filtered

        self._ToLocation = value
        if self._ToLocation is not None:
            self._ToLocation._FromLocationRoles.append(self)

    ToLocation = property(getToLocation, setToLocation)

    def getFromLocation(self):
        
        return self._FromLocation

    def setFromLocation(self, value):
        if self._FromLocation is not None:
            filtered = [x for x in self.FromLocation.ToLocationRoles if x != self]
            self._FromLocation._ToLocationRoles = filtered

        self._FromLocation = value
        if self._FromLocation is not None:
            self._FromLocation._ToLocationRoles.append(self)

    FromLocation = property(getFromLocation, setFromLocation)

