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

from CIM14v13.IEC61968.Informative.InfAssetModels.ElectricalAssetModel import ElectricalAssetModel

class CurrentTransformerAssetModel(ElectricalAssetModel):
    """A particular model supplied by a manufacturer of a Current Transformer (CT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.
    """

    def __init__(self, CurrentTransformerTypeAsset=None, CurrentTransformerInfo=None, CurrentTransformerAssets=None, **kw_args):
        """Initializes a new 'CurrentTransformerAssetModel' instance.

        @param CurrentTransformerTypeAsset:
        @param CurrentTransformerInfo:
        @param CurrentTransformerAssets:
        """
        self._CurrentTransformerTypeAsset = None
        self.CurrentTransformerTypeAsset = CurrentTransformerTypeAsset

        self._CurrentTransformerInfo = None
        self.CurrentTransformerInfo = CurrentTransformerInfo

        self._CurrentTransformerAssets = []
        self.CurrentTransformerAssets = [] if CurrentTransformerAssets is None else CurrentTransformerAssets

        super(CurrentTransformerAssetModel, self).__init__(**kw_args)

    def getCurrentTransformerTypeAsset(self):
        
        return self._CurrentTransformerTypeAsset

    def setCurrentTransformerTypeAsset(self, value):
        if self._CurrentTransformerTypeAsset is not None:
            filtered = [x for x in self.CurrentTransformerTypeAsset.CurrentTransformerAssetModels if x != self]
            self._CurrentTransformerTypeAsset._CurrentTransformerAssetModels = filtered

        self._CurrentTransformerTypeAsset = value
        if self._CurrentTransformerTypeAsset is not None:
            self._CurrentTransformerTypeAsset._CurrentTransformerAssetModels.append(self)

    CurrentTransformerTypeAsset = property(getCurrentTransformerTypeAsset, setCurrentTransformerTypeAsset)

    def getCurrentTransformerInfo(self):
        
        return self._CurrentTransformerInfo

    def setCurrentTransformerInfo(self, value):
        if self._CurrentTransformerInfo is not None:
            filtered = [x for x in self.CurrentTransformerInfo.CurrentTransformerAssertModels if x != self]
            self._CurrentTransformerInfo._CurrentTransformerAssertModels = filtered

        self._CurrentTransformerInfo = value
        if self._CurrentTransformerInfo is not None:
            self._CurrentTransformerInfo._CurrentTransformerAssertModels.append(self)

    CurrentTransformerInfo = property(getCurrentTransformerInfo, setCurrentTransformerInfo)

    def getCurrentTransformerAssets(self):
        
        return self._CurrentTransformerAssets

    def setCurrentTransformerAssets(self, value):
        for x in self._CurrentTransformerAssets:
            x._CurrentTransformerAssetModel = None
        for y in value:
            y._CurrentTransformerAssetModel = self
        self._CurrentTransformerAssets = value

    CurrentTransformerAssets = property(getCurrentTransformerAssets, setCurrentTransformerAssets)

    def addCurrentTransformerAssets(self, *CurrentTransformerAssets):
        for obj in CurrentTransformerAssets:
            obj._CurrentTransformerAssetModel = self
            self._CurrentTransformerAssets.append(obj)

    def removeCurrentTransformerAssets(self, *CurrentTransformerAssets):
        for obj in CurrentTransformerAssets:
            obj._CurrentTransformerAssetModel = None
            self._CurrentTransformerAssets.remove(obj)

