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

class CULaborCode(IdentifiedObject):
    """Labor code associated with various compatible unit labor items.
    """

    def __init__(self, code='', CULaborItems=None, status=None, *args, **kw_args):
        """Initializes a new 'CULaborCode' instance.

        @param code: Labor code. 
        @param CULaborItems:
        @param status:
        """
        #: Labor code. 
        self.code = code

        self._CULaborItems = []
        self.CULaborItems = [] if CULaborItems is None else CULaborItems

        self.status = status

        super(CULaborCode, self).__init__(*args, **kw_args)

    def getCULaborItems(self):
        
        return self._CULaborItems

    def setCULaborItems(self, value):
        for x in self._CULaborItems:
            x._CULaborCode = None
        for y in value:
            y._CULaborCode = self
        self._CULaborItems = value

    CULaborItems = property(getCULaborItems, setCULaborItems)

    def addCULaborItems(self, *CULaborItems):
        for obj in CULaborItems:
            obj._CULaborCode = self
            self._CULaborItems.append(obj)

    def removeCULaborItems(self, *CULaborItems):
        for obj in CULaborItems:
            obj._CULaborCode = None
            self._CULaborItems.remove(obj)

    status = None

