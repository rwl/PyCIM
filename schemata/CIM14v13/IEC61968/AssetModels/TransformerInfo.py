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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerInfo(IdentifiedObject):
    """Set of transformer data, from an equipment library.
    """

    def __init__(self, Transformers=None, TransformerAssets=None, WindingInfos=None, TransformerAssetModels=None, **kw_args):
        """Initializes a new 'TransformerInfo' instance.

        @param Transformers: All transformers that can be described with this transformer data.
        @param TransformerAssets:
        @param WindingInfos: Data for all the windings described by this transformer data.
        @param TransformerAssetModels:
        """
        self._Transformers = []
        self.Transformers = [] if Transformers is None else Transformers

        self._TransformerAssets = []
        self.TransformerAssets = [] if TransformerAssets is None else TransformerAssets

        self._WindingInfos = []
        self.WindingInfos = [] if WindingInfos is None else WindingInfos

        self._TransformerAssetModels = []
        self.TransformerAssetModels = [] if TransformerAssetModels is None else TransformerAssetModels

        super(TransformerInfo, self).__init__(**kw_args)

    def getTransformers(self):
        """All transformers that can be described with this transformer data.
        """
        return self._Transformers

    def setTransformers(self, value):
        for x in self._Transformers:
            x._TransformerInfo = None
        for y in value:
            y._TransformerInfo = self
        self._Transformers = value

    Transformers = property(getTransformers, setTransformers)

    def addTransformers(self, *Transformers):
        for obj in Transformers:
            obj._TransformerInfo = self
            self._Transformers.append(obj)

    def removeTransformers(self, *Transformers):
        for obj in Transformers:
            obj._TransformerInfo = None
            self._Transformers.remove(obj)

    def getTransformerAssets(self):
        
        return self._TransformerAssets

    def setTransformerAssets(self, value):
        for x in self._TransformerAssets:
            x._TransformerInfo = None
        for y in value:
            y._TransformerInfo = self
        self._TransformerAssets = value

    TransformerAssets = property(getTransformerAssets, setTransformerAssets)

    def addTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            obj._TransformerInfo = self
            self._TransformerAssets.append(obj)

    def removeTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            obj._TransformerInfo = None
            self._TransformerAssets.remove(obj)

    def getWindingInfos(self):
        """Data for all the windings described by this transformer data.
        """
        return self._WindingInfos

    def setWindingInfos(self, value):
        for x in self._WindingInfos:
            x._TransformerInfo = None
        for y in value:
            y._TransformerInfo = self
        self._WindingInfos = value

    WindingInfos = property(getWindingInfos, setWindingInfos)

    def addWindingInfos(self, *WindingInfos):
        for obj in WindingInfos:
            obj._TransformerInfo = self
            self._WindingInfos.append(obj)

    def removeWindingInfos(self, *WindingInfos):
        for obj in WindingInfos:
            obj._TransformerInfo = None
            self._WindingInfos.remove(obj)

    def getTransformerAssetModels(self):
        
        return self._TransformerAssetModels

    def setTransformerAssetModels(self, value):
        for x in self._TransformerAssetModels:
            x._TransformerInfo = None
        for y in value:
            y._TransformerInfo = self
        self._TransformerAssetModels = value

    TransformerAssetModels = property(getTransformerAssetModels, setTransformerAssetModels)

    def addTransformerAssetModels(self, *TransformerAssetModels):
        for obj in TransformerAssetModels:
            obj._TransformerInfo = self
            self._TransformerAssetModels.append(obj)

    def removeTransformerAssetModels(self, *TransformerAssetModels):
        for obj in TransformerAssetModels:
            obj._TransformerInfo = None
            self._TransformerAssetModels.remove(obj)

