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

from CIM14v13.IEC61968.Informative.InfTypeAsset.ElectricalTypeAsset import ElectricalTypeAsset

class RecloserTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic recloser asset that may be used for design purposes.
    """

    def __init__(self, RecloserInfo=None, RecloserAssetModels=None, *args, **kw_args):
        """Initializes a new 'RecloserTypeAsset' instance.

        @param RecloserInfo:
        @param RecloserAssetModels:
        """
        self._RecloserInfo = None
        self.RecloserInfo = RecloserInfo

        self._RecloserAssetModels = []
        self.RecloserAssetModels = [] if RecloserAssetModels is None else RecloserAssetModels

        super(RecloserTypeAsset, self).__init__(*args, **kw_args)

    def getRecloserInfo(self):
        
        return self._RecloserInfo

    def setRecloserInfo(self, value):
        if self._RecloserInfo is not None:
            self._RecloserInfo._RecloserTypeAsset = None

        self._RecloserInfo = value
        if self._RecloserInfo is not None:
            self._RecloserInfo._RecloserTypeAsset = self

    RecloserInfo = property(getRecloserInfo, setRecloserInfo)

    def getRecloserAssetModels(self):
        
        return self._RecloserAssetModels

    def setRecloserAssetModels(self, value):
        for x in self._RecloserAssetModels:
            x._RecloserTypeAsset = None
        for y in value:
            y._RecloserTypeAsset = self
        self._RecloserAssetModels = value

    RecloserAssetModels = property(getRecloserAssetModels, setRecloserAssetModels)

    def addRecloserAssetModels(self, *RecloserAssetModels):
        for obj in RecloserAssetModels:
            obj._RecloserTypeAsset = self
            self._RecloserAssetModels.append(obj)

    def removeRecloserAssetModels(self, *RecloserAssetModels):
        for obj in RecloserAssetModels:
            obj._RecloserTypeAsset = None
            self._RecloserAssetModels.remove(obj)

