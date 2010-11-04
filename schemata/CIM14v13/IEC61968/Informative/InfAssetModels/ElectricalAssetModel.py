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

class ElectricalAssetModel(AssetModel):
    """Documentation for a type of ElectricalAsset of a particular product model made by a manufacturer.
    """

    def __init__(self, ElectricalInfos=None, **kw_args):
        """Initializes a new 'ElectricalAssetModel' instance.

        @param ElectricalInfos:
        """
        self._ElectricalInfos = []
        self.ElectricalInfos = [] if ElectricalInfos is None else ElectricalInfos

        super(ElectricalAssetModel, self).__init__(**kw_args)

    def getElectricalInfos(self):
        
        return self._ElectricalInfos

    def setElectricalInfos(self, value):
        for p in self._ElectricalInfos:
            filtered = [q for q in p.ElectricalAssetModels if q != self]
            self._ElectricalInfos._ElectricalAssetModels = filtered
        for r in value:
            if self not in r._ElectricalAssetModels:
                r._ElectricalAssetModels.append(self)
        self._ElectricalInfos = value

    ElectricalInfos = property(getElectricalInfos, setElectricalInfos)

    def addElectricalInfos(self, *ElectricalInfos):
        for obj in ElectricalInfos:
            if self not in obj._ElectricalAssetModels:
                obj._ElectricalAssetModels.append(self)
            self._ElectricalInfos.append(obj)

    def removeElectricalInfos(self, *ElectricalInfos):
        for obj in ElectricalInfos:
            if self in obj._ElectricalAssetModels:
                obj._ElectricalAssetModels.remove(self)
            self._ElectricalInfos.remove(obj)

