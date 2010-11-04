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

class TowerTypeAsset(StructureTypeAsset):
    """Documentation for a generic tower that may be used for various purposes such as work planning. A transmission tower carrying two 3-phase circuits will have 2 instances of Connection, each of which will have 3 MountingPoint instances, one for each phase all with coordinates relative to a common origin on the tower. (It may also have a 3rd Connection with a single MountingPoint for the Neutral line).
    """

    def __init__(self, TowerAssetModels=None, **kw_args):
        """Initializes a new 'TowerTypeAsset' instance.

        @param TowerAssetModels:
        """
        self._TowerAssetModels = []
        self.TowerAssetModels = [] if TowerAssetModels is None else TowerAssetModels

        super(TowerTypeAsset, self).__init__(**kw_args)

    def getTowerAssetModels(self):
        
        return self._TowerAssetModels

    def setTowerAssetModels(self, value):
        for x in self._TowerAssetModels:
            x._TowerTypeAsset = None
        for y in value:
            y._TowerTypeAsset = self
        self._TowerAssetModels = value

    TowerAssetModels = property(getTowerAssetModels, setTowerAssetModels)

    def addTowerAssetModels(self, *TowerAssetModels):
        for obj in TowerAssetModels:
            obj._TowerTypeAsset = self
            self._TowerAssetModels.append(obj)

    def removeTowerAssetModels(self, *TowerAssetModels):
        for obj in TowerAssetModels:
            obj._TowerTypeAsset = None
            self._TowerAssetModels.remove(obj)

