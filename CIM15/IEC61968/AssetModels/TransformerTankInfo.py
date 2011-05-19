# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61968.Assets.AssetInfo import AssetInfo

class TransformerTankInfo(AssetInfo):
    """Set of transformer tank data, from an equipment library.Set of transformer tank data, from an equipment library.
    """

    def __init__(self, TransformerAssets=None, TransformerEndInfos=None, PowerTransformerInfo=None, TransformerAssetModels=None, TransformerTanks=None, *args, **kw_args):
        """Initialises a new 'TransformerTankInfo' instance.

        @param TransformerAssets:
        @param TransformerEndInfos: Data for all the ends described by this transformer tank data.
        @param PowerTransformerInfo: Power transformer data that this tank description is part of.
        @param TransformerAssetModels:
        @param TransformerTanks: All transformer tanks that can be described with this transformer tank data.
        """
        self._TransformerAssets = []
        self.TransformerAssets = [] if TransformerAssets is None else TransformerAssets

        self._TransformerEndInfos = []
        self.TransformerEndInfos = [] if TransformerEndInfos is None else TransformerEndInfos

        self._PowerTransformerInfo = None
        self.PowerTransformerInfo = PowerTransformerInfo

        self._TransformerAssetModels = []
        self.TransformerAssetModels = [] if TransformerAssetModels is None else TransformerAssetModels

        self._TransformerTanks = []
        self.TransformerTanks = [] if TransformerTanks is None else TransformerTanks

        super(TransformerTankInfo, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TransformerAssets", "TransformerEndInfos", "PowerTransformerInfo", "TransformerAssetModels", "TransformerTanks"]
    _many_refs = ["TransformerAssets", "TransformerEndInfos", "TransformerAssetModels", "TransformerTanks"]

    def getTransformerAssets(self):
        
        return self._TransformerAssets

    def setTransformerAssets(self, value):
        for x in self._TransformerAssets:
            x.TransformerInfo = None
        for y in value:
            y._TransformerInfo = self
        self._TransformerAssets = value

    TransformerAssets = property(getTransformerAssets, setTransformerAssets)

    def addTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            obj.TransformerInfo = self

    def removeTransformerAssets(self, *TransformerAssets):
        for obj in TransformerAssets:
            obj.TransformerInfo = None

    def getTransformerEndInfos(self):
        """Data for all the ends described by this transformer tank data.
        """
        return self._TransformerEndInfos

    def setTransformerEndInfos(self, value):
        for x in self._TransformerEndInfos:
            x.TransformerTankInfo = None
        for y in value:
            y._TransformerTankInfo = self
        self._TransformerEndInfos = value

    TransformerEndInfos = property(getTransformerEndInfos, setTransformerEndInfos)

    def addTransformerEndInfos(self, *TransformerEndInfos):
        for obj in TransformerEndInfos:
            obj.TransformerTankInfo = self

    def removeTransformerEndInfos(self, *TransformerEndInfos):
        for obj in TransformerEndInfos:
            obj.TransformerTankInfo = None

    def getPowerTransformerInfo(self):
        """Power transformer data that this tank description is part of.
        """
        return self._PowerTransformerInfo

    def setPowerTransformerInfo(self, value):
        if self._PowerTransformerInfo is not None:
            filtered = [x for x in self.PowerTransformerInfo.TransformerTankInfo if x != self]
            self._PowerTransformerInfo._TransformerTankInfo = filtered

        self._PowerTransformerInfo = value
        if self._PowerTransformerInfo is not None:
            if self not in self._PowerTransformerInfo._TransformerTankInfo:
                self._PowerTransformerInfo._TransformerTankInfo.append(self)

    PowerTransformerInfo = property(getPowerTransformerInfo, setPowerTransformerInfo)

    def getTransformerAssetModels(self):
        
        return self._TransformerAssetModels

    def setTransformerAssetModels(self, value):
        for x in self._TransformerAssetModels:
            x.TransformerInfo = None
        for y in value:
            y._TransformerInfo = self
        self._TransformerAssetModels = value

    TransformerAssetModels = property(getTransformerAssetModels, setTransformerAssetModels)

    def addTransformerAssetModels(self, *TransformerAssetModels):
        for obj in TransformerAssetModels:
            obj.TransformerInfo = self

    def removeTransformerAssetModels(self, *TransformerAssetModels):
        for obj in TransformerAssetModels:
            obj.TransformerInfo = None

    def getTransformerTanks(self):
        """All transformer tanks that can be described with this transformer tank data.
        """
        return self._TransformerTanks

    def setTransformerTanks(self, value):
        for x in self._TransformerTanks:
            x.TransformerTankInfo = None
        for y in value:
            y._TransformerTankInfo = self
        self._TransformerTanks = value

    TransformerTanks = property(getTransformerTanks, setTransformerTanks)

    def addTransformerTanks(self, *TransformerTanks):
        for obj in TransformerTanks:
            obj.TransformerTankInfo = self

    def removeTransformerTanks(self, *TransformerTanks):
        for obj in TransformerTanks:
            obj.TransformerTankInfo = None

