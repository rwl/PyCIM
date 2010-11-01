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

class ErpIssueInventory(IdentifiedObject):
    """Can be used to request an application to process an issue or request information about an issue.
    """

    def __init__(self, status=None, TypeMaterial=None, TypeAsset=None, *args, **kw_args):
        """Initializes a new 'ErpIssueInventory' instance.

        @param status:
        @param TypeMaterial:
        @param TypeAsset:
        """
        self.status = status

        self._TypeMaterial = None
        self.TypeMaterial = TypeMaterial

        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        super(ErpIssueInventory, self).__init__(*args, **kw_args)

    status = None

    def getTypeMaterial(self):
        
        return self._TypeMaterial

    def setTypeMaterial(self, value):
        if self._TypeMaterial is not None:
            filtered = [x for x in self.TypeMaterial.ErpIssueInventories if x != self]
            self._TypeMaterial._ErpIssueInventories = filtered

        self._TypeMaterial = value
        if self._TypeMaterial is not None:
            self._TypeMaterial._ErpIssueInventories.append(self)

    TypeMaterial = property(getTypeMaterial, setTypeMaterial)

    def getTypeAsset(self):
        
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            filtered = [x for x in self.TypeAsset.ErpInventoryIssues if x != self]
            self._TypeAsset._ErpInventoryIssues = filtered

        self._TypeAsset = value
        if self._TypeAsset is not None:
            self._TypeAsset._ErpInventoryIssues.append(self)

    TypeAsset = property(getTypeAsset, setTypeAsset)

