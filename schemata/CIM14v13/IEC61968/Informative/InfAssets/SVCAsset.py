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

from CIM14v13.IEC61968.Informative.InfAssets.FACTSDeviceAsset import FACTSDeviceAsset

class SVCAsset(FACTSDeviceAsset):
    """Physical asset performing StaticVarCompensator function.
    """

    def __init__(self, SvcInfo=None, SVCAssetModel=None, *args, **kw_args):
        """Initializes a new 'SVCAsset' instance.

        @param SvcInfo:
        @param SVCAssetModel:
        """
        self._SvcInfo = None
        self.SvcInfo = SvcInfo

        self._SVCAssetModel = None
        self.SVCAssetModel = SVCAssetModel

        super(SVCAsset, self).__init__(*args, **kw_args)

    def getSvcInfo(self):
        
        return self._SvcInfo

    def setSvcInfo(self, value):
        if self._SvcInfo is not None:
            self._SvcInfo._SVCAsset = None

        self._SvcInfo = value
        if self._SvcInfo is not None:
            self._SvcInfo._SVCAsset = self

    SvcInfo = property(getSvcInfo, setSvcInfo)

    def getSVCAssetModel(self):
        
        return self._SVCAssetModel

    def setSVCAssetModel(self, value):
        if self._SVCAssetModel is not None:
            filtered = [x for x in self.SVCAssetModel.SVCAssets if x != self]
            self._SVCAssetModel._SVCAssets = filtered

        self._SVCAssetModel = value
        if self._SVCAssetModel is not None:
            self._SVCAssetModel._SVCAssets.append(self)

    SVCAssetModel = property(getSVCAssetModel, setSVCAssetModel)

