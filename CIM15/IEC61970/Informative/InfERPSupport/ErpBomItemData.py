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

class ErpBomItemData(IdentifiedObject):
    """An individual item on a bill of materials.An individual item on a bill of materials.
    """

    def __init__(self, TypeAsset=None, ErpBOM=None, DesignLocation=None, *args, **kw_args):
        """Initialises a new 'ErpBomItemData' instance.

        @param TypeAsset:
        @param ErpBOM:
        @param DesignLocation:
        """
        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        self._ErpBOM = None
        self.ErpBOM = ErpBOM

        self._DesignLocation = None
        self.DesignLocation = DesignLocation

        super(ErpBomItemData, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TypeAsset", "ErpBOM", "DesignLocation"]
    _many_refs = []

    def getTypeAsset(self):
        
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            filtered = [x for x in self.TypeAsset.ErpBomItemDatas if x != self]
            self._TypeAsset._ErpBomItemDatas = filtered

        self._TypeAsset = value
        if self._TypeAsset is not None:
            if self not in self._TypeAsset._ErpBomItemDatas:
                self._TypeAsset._ErpBomItemDatas.append(self)

    TypeAsset = property(getTypeAsset, setTypeAsset)

    def getErpBOM(self):
        
        return self._ErpBOM

    def setErpBOM(self, value):
        if self._ErpBOM is not None:
            filtered = [x for x in self.ErpBOM.ErpBomItemDatas if x != self]
            self._ErpBOM._ErpBomItemDatas = filtered

        self._ErpBOM = value
        if self._ErpBOM is not None:
            if self not in self._ErpBOM._ErpBomItemDatas:
                self._ErpBOM._ErpBomItemDatas.append(self)

    ErpBOM = property(getErpBOM, setErpBOM)

    def getDesignLocation(self):
        
        return self._DesignLocation

    def setDesignLocation(self, value):
        if self._DesignLocation is not None:
            filtered = [x for x in self.DesignLocation.ErpBomItemDatas if x != self]
            self._DesignLocation._ErpBomItemDatas = filtered

        self._DesignLocation = value
        if self._DesignLocation is not None:
            if self not in self._DesignLocation._ErpBomItemDatas:
                self._DesignLocation._ErpBomItemDatas.append(self)

    DesignLocation = property(getDesignLocation, setDesignLocation)

