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

from CIM16.IEC61970.Core.IdentifiedObject import IdentifiedObject

class AssetModel(IdentifiedObject):
    """Model of an asset, either a product of a specific manufacturer or a generic asset model or material item. Data-sheet characteristics are available through the associated AssetInfo subclass and can be shared with asset or power system resource instances.Model of an asset, either a product of a specific manufacturer or a generic asset model or material item. Data-sheet characteristics are available through the associated AssetInfo subclass and can be shared with asset or power system resource instances.
    """

    def __init__(self, AssetInfo=None, ErpInventoryCounts=None, *args, **kw_args):
        """Initialises a new 'AssetModel' instance.

        @param AssetInfo: Data applicable to this asset model.
        @param ErpInventoryCounts:
        """
        self._AssetInfo = None
        self.AssetInfo = AssetInfo

        self._ErpInventoryCounts = []
        self.ErpInventoryCounts = [] if ErpInventoryCounts is None else ErpInventoryCounts

        super(AssetModel, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["AssetInfo", "ErpInventoryCounts"]
    _many_refs = ["ErpInventoryCounts"]

    def getAssetInfo(self):
        """Data applicable to this asset model.
        """
        return self._AssetInfo

    def setAssetInfo(self, value):
        if self._AssetInfo is not None:
            self._AssetInfo._AssetModel = None

        self._AssetInfo = value
        if self._AssetInfo is not None:
            self._AssetInfo.AssetModel = None
            self._AssetInfo._AssetModel = self

    AssetInfo = property(getAssetInfo, setAssetInfo)

    def getErpInventoryCounts(self):
        
        return self._ErpInventoryCounts

    def setErpInventoryCounts(self, value):
        for x in self._ErpInventoryCounts:
            x.AssetModel = None
        for y in value:
            y._AssetModel = self
        self._ErpInventoryCounts = value

    ErpInventoryCounts = property(getErpInventoryCounts, setErpInventoryCounts)

    def addErpInventoryCounts(self, *ErpInventoryCounts):
        for obj in ErpInventoryCounts:
            obj.AssetModel = self

    def removeErpInventoryCounts(self, *ErpInventoryCounts):
        for obj in ErpInventoryCounts:
            obj.AssetModel = None

