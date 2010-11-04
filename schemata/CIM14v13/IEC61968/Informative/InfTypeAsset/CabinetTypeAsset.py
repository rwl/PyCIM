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

from CIM14v13.IEC61968.Informative.InfTypeAsset.StructureTypeAsset import StructureTypeAsset

class CabinetTypeAsset(StructureTypeAsset):
    """Documentation for a generic cabinet that may be used for various purposes such as work planning.
    """

    def __init__(self, CabinetModels=None, **kw_args):
        """Initializes a new 'CabinetTypeAsset' instance.

        @param CabinetModels:
        """
        self._CabinetModels = []
        self.CabinetModels = [] if CabinetModels is None else CabinetModels

        super(CabinetTypeAsset, self).__init__(**kw_args)

    def getCabinetModels(self):
        
        return self._CabinetModels

    def setCabinetModels(self, value):
        for x in self._CabinetModels:
            x._CabinetTypeAsset = None
        for y in value:
            y._CabinetTypeAsset = self
        self._CabinetModels = value

    CabinetModels = property(getCabinetModels, setCabinetModels)

    def addCabinetModels(self, *CabinetModels):
        for obj in CabinetModels:
            obj._CabinetTypeAsset = self
            self._CabinetModels.append(obj)

    def removeCabinetModels(self, *CabinetModels):
        for obj in CabinetModels:
            obj._CabinetTypeAsset = None
            self._CabinetModels.remove(obj)

