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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class AssetInfo(IdentifiedObject):
    """Set of attributes of an asset, representing typical data-sheet information of a physical device, that can be instantiated and shared in different data exchange contexts: - as attributes of an asset instance (installed or in stock) - as attributes of an asset model (product by a manufacturer) - as attributes of a type asset (generic type of an asset as used in designs/extension planning).Set of attributes of an asset, representing typical data-sheet information of a physical device, that can be instantiated and shared in different data exchange contexts: - as attributes of an asset instance (installed or in stock) - as attributes of an asset model (product by a manufacturer) - as attributes of a type asset (generic type of an asset as used in designs/extension planning).
    """

    def __init__(self, Assets=None, DimensionsInfo=None, AssetModel=None, *args, **kw_args):
        """Initialises a new 'AssetInfo' instance.

        @param Assets: All assets described by this data.
        @param DimensionsInfo:
        @param AssetModel: Asset model described by this data.
        """
        self._Assets = None
        self.Assets = Assets

        self._DimensionsInfo = None
        self.DimensionsInfo = DimensionsInfo

        self._AssetModel = None
        self.AssetModel = AssetModel

        super(AssetInfo, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Assets", "DimensionsInfo", "AssetModel"]
    _many_refs = []

    def getAssets(self):
        """All assets described by this data.
        """
        return self._Assets

    def setAssets(self, value):
        if self._Assets is not None:
            self._Assets._AssetInfo = None

        self._Assets = value
        if self._Assets is not None:
            self._Assets.AssetInfo = None
            self._Assets._AssetInfo = self

    Assets = property(getAssets, setAssets)

    def getDimensionsInfo(self):
        
        return self._DimensionsInfo

    def setDimensionsInfo(self, value):
        if self._DimensionsInfo is not None:
            filtered = [x for x in self.DimensionsInfo.AssetInfos if x != self]
            self._DimensionsInfo._AssetInfos = filtered

        self._DimensionsInfo = value
        if self._DimensionsInfo is not None:
            if self not in self._DimensionsInfo._AssetInfos:
                self._DimensionsInfo._AssetInfos.append(self)

    DimensionsInfo = property(getDimensionsInfo, setDimensionsInfo)

    def getAssetModel(self):
        """Asset model described by this data.
        """
        return self._AssetModel

    def setAssetModel(self, value):
        if self._AssetModel is not None:
            self._AssetModel._AssetInfo = None

        self._AssetModel = value
        if self._AssetModel is not None:
            self._AssetModel.AssetInfo = None
            self._AssetModel._AssetInfo = self

    AssetModel = property(getAssetModel, setAssetModel)

