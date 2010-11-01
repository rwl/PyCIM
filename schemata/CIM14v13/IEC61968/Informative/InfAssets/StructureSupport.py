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

from CIM14v13.IEC61968.Assets.Asset import Asset

class StructureSupport(Asset):
    """Support for Structures.
    """

    def __init__(self, length=0.0, direction=0.0, size='', rodLength=0.0, rodCount=0, SecuredStructure=None, *args, **kw_args):
        """Initializes a new 'StructureSupport' instance.

        @param length: Length of anchor lead or guy. 
        @param direction: Direction of supporting anchor or guy. 
        @param size: Size of anchor or guy. 
        @param rodLength: Length of rod used for an anchor. 
        @param rodCount: Number of rods used for an anchor. 
        @param SecuredStructure:
        """
        #: Length of anchor lead or guy. 
        self.length = length

        #: Direction of supporting anchor or guy. 
        self.direction = direction

        #: Size of anchor or guy. 
        self.size = size

        #: Length of rod used for an anchor. 
        self.rodLength = rodLength

        #: Number of rods used for an anchor. 
        self.rodCount = rodCount

        self._SecuredStructure = None
        self.SecuredStructure = SecuredStructure

        super(StructureSupport, self).__init__(*args, **kw_args)

    def getSecuredStructure(self):
        
        return self._SecuredStructure

    def setSecuredStructure(self, value):
        if self._SecuredStructure is not None:
            filtered = [x for x in self.SecuredStructure.StructureSupports if x != self]
            self._SecuredStructure._StructureSupports = filtered

        self._SecuredStructure = value
        if self._SecuredStructure is not None:
            self._SecuredStructure._StructureSupports.append(self)

    SecuredStructure = property(getSecuredStructure, setSecuredStructure)

