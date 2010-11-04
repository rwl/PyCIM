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

from CIM14v13.IEC61968.Informative.InfAssetModels.FACTSDeviceAssetModel import FACTSDeviceAssetModel

class SVCAssetModel(FACTSDeviceAssetModel):
    """Documentation for a type of a Static Var Compensator of a particular product model made by a manufacturer.
    """

    def __init__(self, SvcInfo=None, SVCTypeAsset=None, SVCAssets=None, **kw_args):
        """Initializes a new 'SVCAssetModel' instance.

        @param SvcInfo:
        @param SVCTypeAsset:
        @param SVCAssets:
        """
        self._SvcInfo = None
        self.SvcInfo = SvcInfo

        self._SVCTypeAsset = None
        self.SVCTypeAsset = SVCTypeAsset

        self._SVCAssets = []
        self.SVCAssets = [] if SVCAssets is None else SVCAssets

        super(SVCAssetModel, self).__init__(**kw_args)

    def getSvcInfo(self):
        
        return self._SvcInfo

    def setSvcInfo(self, value):
        if self._SvcInfo is not None:
            self._SvcInfo._SVCAssetModel = None

        self._SvcInfo = value
        if self._SvcInfo is not None:
            self._SvcInfo._SVCAssetModel = self

    SvcInfo = property(getSvcInfo, setSvcInfo)

    def getSVCTypeAsset(self):
        
        return self._SVCTypeAsset

    def setSVCTypeAsset(self, value):
        if self._SVCTypeAsset is not None:
            filtered = [x for x in self.SVCTypeAsset.SVCAssetModels if x != self]
            self._SVCTypeAsset._SVCAssetModels = filtered

        self._SVCTypeAsset = value
        if self._SVCTypeAsset is not None:
            self._SVCTypeAsset._SVCAssetModels.append(self)

    SVCTypeAsset = property(getSVCTypeAsset, setSVCTypeAsset)

    def getSVCAssets(self):
        
        return self._SVCAssets

    def setSVCAssets(self, value):
        for x in self._SVCAssets:
            x._SVCAssetModel = None
        for y in value:
            y._SVCAssetModel = self
        self._SVCAssets = value

    SVCAssets = property(getSVCAssets, setSVCAssets)

    def addSVCAssets(self, *SVCAssets):
        for obj in SVCAssets:
            obj._SVCAssetModel = self
            self._SVCAssets.append(obj)

    def removeSVCAssets(self, *SVCAssets):
        for obj in SVCAssets:
            obj._SVCAssetModel = None
            self._SVCAssets.remove(obj)

