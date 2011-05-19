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

class ErpIssueInventory(IdentifiedObject):
    """Can be used to request an application to process an issue or request information about an issue.Can be used to request an application to process an issue or request information about an issue.
    """

    def __init__(self, TypeAsset=None, status=None, TypeMaterial=None, *args, **kw_args):
        """Initialises a new 'ErpIssueInventory' instance.

        @param TypeAsset:
        @param status:
        @param TypeMaterial:
        """
        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        self.status = status

        self._TypeMaterial = None
        self.TypeMaterial = TypeMaterial

        super(ErpIssueInventory, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TypeAsset", "status", "TypeMaterial"]
    _many_refs = []

    def getTypeAsset(self):
        
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            filtered = [x for x in self.TypeAsset.ErpInventoryIssues if x != self]
            self._TypeAsset._ErpInventoryIssues = filtered

        self._TypeAsset = value
        if self._TypeAsset is not None:
            if self not in self._TypeAsset._ErpInventoryIssues:
                self._TypeAsset._ErpInventoryIssues.append(self)

    TypeAsset = property(getTypeAsset, setTypeAsset)

    status = None

    def getTypeMaterial(self):
        
        return self._TypeMaterial

    def setTypeMaterial(self, value):
        if self._TypeMaterial is not None:
            filtered = [x for x in self.TypeMaterial.ErpIssueInventories if x != self]
            self._TypeMaterial._ErpIssueInventories = filtered

        self._TypeMaterial = value
        if self._TypeMaterial is not None:
            if self not in self._TypeMaterial._ErpIssueInventories:
                self._TypeMaterial._ErpIssueInventories.append(self)

    TypeMaterial = property(getTypeMaterial, setTypeMaterial)

