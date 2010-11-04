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

from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset

class CurrentTransformerAsset(ElectricalAsset):
    """Physical asset performing Current Transformer (CT) function.
    """

    def __init__(self, typeCT='', CurrentTransformerInfo=None, CurrentTransformerAssetModel=None, CurrentTransformer=None, **kw_args):
        """Initializes a new 'CurrentTransformerAsset' instance.

        @param typeCT: Type of CT as categorized by the utility's asset management standards and practices. 
        @param CurrentTransformerInfo:
        @param CurrentTransformerAssetModel:
        @param CurrentTransformer:
        """
        #: Type of CT as categorized by the utility's asset management standards and practices.
        self.typeCT = typeCT

        self._CurrentTransformerInfo = None
        self.CurrentTransformerInfo = CurrentTransformerInfo

        self._CurrentTransformerAssetModel = None
        self.CurrentTransformerAssetModel = CurrentTransformerAssetModel

        self._CurrentTransformer = None
        self.CurrentTransformer = CurrentTransformer

        super(CurrentTransformerAsset, self).__init__(**kw_args)

    def getCurrentTransformerInfo(self):
        
        return self._CurrentTransformerInfo

    def setCurrentTransformerInfo(self, value):
        if self._CurrentTransformerInfo is not None:
            filtered = [x for x in self.CurrentTransformerInfo.CurrentTransformerAssets if x != self]
            self._CurrentTransformerInfo._CurrentTransformerAssets = filtered

        self._CurrentTransformerInfo = value
        if self._CurrentTransformerInfo is not None:
            self._CurrentTransformerInfo._CurrentTransformerAssets.append(self)

    CurrentTransformerInfo = property(getCurrentTransformerInfo, setCurrentTransformerInfo)

    def getCurrentTransformerAssetModel(self):
        
        return self._CurrentTransformerAssetModel

    def setCurrentTransformerAssetModel(self, value):
        if self._CurrentTransformerAssetModel is not None:
            filtered = [x for x in self.CurrentTransformerAssetModel.CurrentTransformerAssets if x != self]
            self._CurrentTransformerAssetModel._CurrentTransformerAssets = filtered

        self._CurrentTransformerAssetModel = value
        if self._CurrentTransformerAssetModel is not None:
            self._CurrentTransformerAssetModel._CurrentTransformerAssets.append(self)

    CurrentTransformerAssetModel = property(getCurrentTransformerAssetModel, setCurrentTransformerAssetModel)

    def getCurrentTransformer(self):
        
        return self._CurrentTransformer

    def setCurrentTransformer(self, value):
        if self._CurrentTransformer is not None:
            self._CurrentTransformer._CurrentTransformerAsset = None

        self._CurrentTransformer = value
        if self._CurrentTransformer is not None:
            self._CurrentTransformer._CurrentTransformerAsset = self

    CurrentTransformer = property(getCurrentTransformer, setCurrentTransformer)

