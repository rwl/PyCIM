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

class RecloserAsset(ElectricalAsset):
    """Physical recloser performing a reclosing function, which is modeled through Breaker.
    """

    def __init__(self, RecloserAssetModel=None, RecloserInfo=None, *args, **kw_args):
        """Initializes a new 'RecloserAsset' instance.

        @param RecloserAssetModel:
        @param RecloserInfo:
        """
        self._RecloserAssetModel = None
        self.RecloserAssetModel = RecloserAssetModel

        self._RecloserInfo = None
        self.RecloserInfo = RecloserInfo

        super(RecloserAsset, self).__init__(*args, **kw_args)

    def getRecloserAssetModel(self):
        
        return self._RecloserAssetModel

    def setRecloserAssetModel(self, value):
        if self._RecloserAssetModel is not None:
            filtered = [x for x in self.RecloserAssetModel.RecloserAssets if x != self]
            self._RecloserAssetModel._RecloserAssets = filtered

        self._RecloserAssetModel = value
        if self._RecloserAssetModel is not None:
            self._RecloserAssetModel._RecloserAssets.append(self)

    RecloserAssetModel = property(getRecloserAssetModel, setRecloserAssetModel)

    def getRecloserInfo(self):
        
        return self._RecloserInfo

    def setRecloserInfo(self, value):
        if self._RecloserInfo is not None:
            filtered = [x for x in self.RecloserInfo.RecloserAssets if x != self]
            self._RecloserInfo._RecloserAssets = filtered

        self._RecloserInfo = value
        if self._RecloserInfo is not None:
            self._RecloserInfo._RecloserAssets.append(self)

    RecloserInfo = property(getRecloserInfo, setRecloserInfo)

