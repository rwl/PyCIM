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

from CIM14v13.IEC61968.Informative.InfAssets.Structure import Structure

class Tower(Structure):
    """Large structure used to carry transmission lines, subtransmission lines, and/or other equipment/lines (e.g., communication). Dimensions of the Tower are specified in associated DimensionsInfo class.
    """

    def __init__(self, constructionKind='suspension', TowerAssetModel=None, *args, **kw_args):
        """Initializes a new 'Tower' instance.

        @param constructionKind: Construction structure on the tower. Values are: "suspension", "tension"
        @param TowerAssetModel:
        """
        #: Construction structure on the tower. Values are: "suspension", "tension"
        self.constructionKind = constructionKind

        self._TowerAssetModel = None
        self.TowerAssetModel = TowerAssetModel

        super(Tower, self).__init__(*args, **kw_args)

    def getTowerAssetModel(self):
        
        return self._TowerAssetModel

    def setTowerAssetModel(self, value):
        if self._TowerAssetModel is not None:
            filtered = [x for x in self.TowerAssetModel.Towers if x != self]
            self._TowerAssetModel._Towers = filtered

        self._TowerAssetModel = value
        if self._TowerAssetModel is not None:
            self._TowerAssetModel._Towers.append(self)

    TowerAssetModel = property(getTowerAssetModel, setTowerAssetModel)

