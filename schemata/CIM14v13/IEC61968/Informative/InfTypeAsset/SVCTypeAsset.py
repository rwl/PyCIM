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

from CIM14v13.IEC61968.Informative.InfTypeAsset.FACTSDeviceTypeAsset import FACTSDeviceTypeAsset

class SVCTypeAsset(FACTSDeviceTypeAsset):
    """Documentation for a generic Static Var Compensator (SVC) that may be used for various purposes such as work planning.
    """

    def __init__(self, SvcInfos=None, SVCAssetModels=None, **kw_args):
        """Initializes a new 'SVCTypeAsset' instance.

        @param SvcInfos:
        @param SVCAssetModels:
        """
        self._SvcInfos = []
        self.SvcInfos = [] if SvcInfos is None else SvcInfos

        self._SVCAssetModels = []
        self.SVCAssetModels = [] if SVCAssetModels is None else SVCAssetModels

        super(SVCTypeAsset, self).__init__(**kw_args)

    def getSvcInfos(self):
        
        return self._SvcInfos

    def setSvcInfos(self, value):
        for p in self._SvcInfos:
            filtered = [q for q in p.SVCTypeAssets if q != self]
            self._SvcInfos._SVCTypeAssets = filtered
        for r in value:
            if self not in r._SVCTypeAssets:
                r._SVCTypeAssets.append(self)
        self._SvcInfos = value

    SvcInfos = property(getSvcInfos, setSvcInfos)

    def addSvcInfos(self, *SvcInfos):
        for obj in SvcInfos:
            if self not in obj._SVCTypeAssets:
                obj._SVCTypeAssets.append(self)
            self._SvcInfos.append(obj)

    def removeSvcInfos(self, *SvcInfos):
        for obj in SvcInfos:
            if self in obj._SVCTypeAssets:
                obj._SVCTypeAssets.remove(self)
            self._SvcInfos.remove(obj)

    def getSVCAssetModels(self):
        
        return self._SVCAssetModels

    def setSVCAssetModels(self, value):
        for x in self._SVCAssetModels:
            x._SVCTypeAsset = None
        for y in value:
            y._SVCTypeAsset = self
        self._SVCAssetModels = value

    SVCAssetModels = property(getSVCAssetModels, setSVCAssetModels)

    def addSVCAssetModels(self, *SVCAssetModels):
        for obj in SVCAssetModels:
            obj._SVCTypeAsset = self
            self._SVCAssetModels.append(obj)

    def removeSVCAssetModels(self, *SVCAssetModels):
        for obj in SVCAssetModels:
            obj._SVCTypeAsset = None
            self._SVCAssetModels.remove(obj)

