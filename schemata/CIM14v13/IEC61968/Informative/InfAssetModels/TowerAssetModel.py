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

class TowerAssetModel(AssetModel):
    """A type of tower supplied by a given manufacturer or constructed from a common design.
    """

    def __init__(self, TowerTypeAsset=None, Towers=None, *args, **kw_args):
        """Initializes a new 'TowerAssetModel' instance.

        @param TowerTypeAsset:
        @param Towers:
        """
        self._TowerTypeAsset = None
        self.TowerTypeAsset = TowerTypeAsset

        self._Towers = []
        self.Towers = [] if Towers is None else Towers

        super(TowerAssetModel, self).__init__(*args, **kw_args)

    def getTowerTypeAsset(self):
        
        return self._TowerTypeAsset

    def setTowerTypeAsset(self, value):
        if self._TowerTypeAsset is not None:
            filtered = [x for x in self.TowerTypeAsset.TowerAssetModels if x != self]
            self._TowerTypeAsset._TowerAssetModels = filtered

        self._TowerTypeAsset = value
        if self._TowerTypeAsset is not None:
            self._TowerTypeAsset._TowerAssetModels.append(self)

    TowerTypeAsset = property(getTowerTypeAsset, setTowerTypeAsset)

    def getTowers(self):
        
        return self._Towers

    def setTowers(self, value):
        for x in self._Towers:
            x._TowerAssetModel = None
        for y in value:
            y._TowerAssetModel = self
        self._Towers = value

    Towers = property(getTowers, setTowers)

    def addTowers(self, *Towers):
        for obj in Towers:
            obj._TowerAssetModel = self
            self._Towers.append(obj)

    def removeTowers(self, *Towers):
        for obj in Towers:
            obj._TowerAssetModel = None
            self._Towers.remove(obj)

