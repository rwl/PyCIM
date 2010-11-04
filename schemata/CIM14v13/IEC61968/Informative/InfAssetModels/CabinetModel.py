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

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel

class CabinetModel(AssetModel):
    """Documentation for a type of Cabinet of a particular product model made by a manufacturer.
    """

    def __init__(self, Cabinets=None, CabinetTypeAsset=None, **kw_args):
        """Initializes a new 'CabinetModel' instance.

        @param Cabinets:
        @param CabinetTypeAsset:
        """
        self._Cabinets = []
        self.Cabinets = [] if Cabinets is None else Cabinets

        self._CabinetTypeAsset = None
        self.CabinetTypeAsset = CabinetTypeAsset

        super(CabinetModel, self).__init__(**kw_args)

    def getCabinets(self):
        
        return self._Cabinets

    def setCabinets(self, value):
        for x in self._Cabinets:
            x._CabinetModel = None
        for y in value:
            y._CabinetModel = self
        self._Cabinets = value

    Cabinets = property(getCabinets, setCabinets)

    def addCabinets(self, *Cabinets):
        for obj in Cabinets:
            obj._CabinetModel = self
            self._Cabinets.append(obj)

    def removeCabinets(self, *Cabinets):
        for obj in Cabinets:
            obj._CabinetModel = None
            self._Cabinets.remove(obj)

    def getCabinetTypeAsset(self):
        
        return self._CabinetTypeAsset

    def setCabinetTypeAsset(self, value):
        if self._CabinetTypeAsset is not None:
            filtered = [x for x in self.CabinetTypeAsset.CabinetModels if x != self]
            self._CabinetTypeAsset._CabinetModels = filtered

        self._CabinetTypeAsset = value
        if self._CabinetTypeAsset is not None:
            self._CabinetTypeAsset._CabinetModels.append(self)

    CabinetTypeAsset = property(getCabinetTypeAsset, setCabinetTypeAsset)

