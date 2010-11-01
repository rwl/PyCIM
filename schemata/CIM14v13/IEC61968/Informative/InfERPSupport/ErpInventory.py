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

class ErpInventory(IdentifiedObject):
    """Utility inventory-related information about an item or part (and not for description of the item and its attributes). It is used by ERP applications to enable the synchronization of Inventory data that exists on separate Item Master databases. This data is not the master data that describes the attributes of the item such as dimensions, weight, or unit of measure - it describes the item as it exists at a specific location.
    """

    def __init__(self, Asset=None, status=None, *args, **kw_args):
        """Initializes a new 'ErpInventory' instance.

        @param Asset:
        @param status:
        """
        self._Asset = None
        self.Asset = Asset

        self.status = status

        super(ErpInventory, self).__init__(*args, **kw_args)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            self._Asset._ErpInventory = None

        self._Asset = value
        if self._Asset is not None:
            self._Asset._ErpInventory = self

    Asset = property(getAsset, setAsset)

    status = None

