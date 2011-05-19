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

class TypeAssetCatalogue(IdentifiedObject):
    """Catalogue of generic types of assets (TypeAsset) that may be used for design purposes. It is not associated with a particular manufacturer.Catalogue of generic types of assets (TypeAsset) that may be used for design purposes. It is not associated with a particular manufacturer.
    """

    def __init__(self, TypeAssets=None, status=None, *args, **kw_args):
        """Initialises a new 'TypeAssetCatalogue' instance.

        @param TypeAssets:
        @param status:
        """
        self._TypeAssets = []
        self.TypeAssets = [] if TypeAssets is None else TypeAssets

        self.status = status

        super(TypeAssetCatalogue, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TypeAssets", "status"]
    _many_refs = ["TypeAssets"]

    def getTypeAssets(self):
        
        return self._TypeAssets

    def setTypeAssets(self, value):
        for x in self._TypeAssets:
            x.TypeAssetCatalogue = None
        for y in value:
            y._TypeAssetCatalogue = self
        self._TypeAssets = value

    TypeAssets = property(getTypeAssets, setTypeAssets)

    def addTypeAssets(self, *TypeAssets):
        for obj in TypeAssets:
            obj.TypeAssetCatalogue = self

    def removeTypeAssets(self, *TypeAssets):
        for obj in TypeAssets:
            obj.TypeAssetCatalogue = None

    status = None

