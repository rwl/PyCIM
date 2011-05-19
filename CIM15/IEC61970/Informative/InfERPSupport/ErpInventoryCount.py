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

class ErpInventoryCount(IdentifiedObject):
    """This is related to Inventory physical counts organized by AssetModel. Note that a count of a type of asset can be accomplished by the association inherited by AssetModel (from Document) to Asset. It enables ERP applications to transfer an inventory count between ERP and the actual physical inventory location. This count may be a cycle count or a physical count.This is related to Inventory physical counts organized by AssetModel. Note that a count of a type of asset can be accomplished by the association inherited by AssetModel (from Document) to Asset. It enables ERP applications to transfer an inventory count between ERP and the actual physical inventory location. This count may be a cycle count or a physical count.
    """

    def __init__(self, status=None, MaterialItem=None, AssetModel=None, *args, **kw_args):
        """Initialises a new 'ErpInventoryCount' instance.

        @param status:
        @param MaterialItem:
        @param AssetModel:
        """
        self.status = status

        self._MaterialItem = None
        self.MaterialItem = MaterialItem

        self._AssetModel = None
        self.AssetModel = AssetModel

        super(ErpInventoryCount, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["status", "MaterialItem", "AssetModel"]
    _many_refs = []

    status = None

    def getMaterialItem(self):
        
        return self._MaterialItem

    def setMaterialItem(self, value):
        if self._MaterialItem is not None:
            filtered = [x for x in self.MaterialItem.ErpInventoryCounts if x != self]
            self._MaterialItem._ErpInventoryCounts = filtered

        self._MaterialItem = value
        if self._MaterialItem is not None:
            if self not in self._MaterialItem._ErpInventoryCounts:
                self._MaterialItem._ErpInventoryCounts.append(self)

    MaterialItem = property(getMaterialItem, setMaterialItem)

    def getAssetModel(self):
        
        return self._AssetModel

    def setAssetModel(self, value):
        if self._AssetModel is not None:
            filtered = [x for x in self.AssetModel.ErpInventoryCounts if x != self]
            self._AssetModel._ErpInventoryCounts = filtered

        self._AssetModel = value
        if self._AssetModel is not None:
            if self not in self._AssetModel._ErpInventoryCounts:
                self._AssetModel._ErpInventoryCounts.append(self)

    AssetModel = property(getAssetModel, setAssetModel)

