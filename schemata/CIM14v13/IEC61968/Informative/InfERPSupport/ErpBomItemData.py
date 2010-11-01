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

class ErpBomItemData(IdentifiedObject):
    """An individual item on a bill of materials.
    """

    def __init__(self, DesignLocation=None, ErpBOM=None, TypeAsset=None, *args, **kw_args):
        """Initializes a new 'ErpBomItemData' instance.

        @param DesignLocation:
        @param ErpBOM:
        @param TypeAsset:
        """
        self._DesignLocation = None
        self.DesignLocation = DesignLocation

        self._ErpBOM = None
        self.ErpBOM = ErpBOM

        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        super(ErpBomItemData, self).__init__(*args, **kw_args)

    def getDesignLocation(self):
        
        return self._DesignLocation

    def setDesignLocation(self, value):
        if self._DesignLocation is not None:
            filtered = [x for x in self.DesignLocation.ErpBomItemDatas if x != self]
            self._DesignLocation._ErpBomItemDatas = filtered

        self._DesignLocation = value
        if self._DesignLocation is not None:
            self._DesignLocation._ErpBomItemDatas.append(self)

    DesignLocation = property(getDesignLocation, setDesignLocation)

    def getErpBOM(self):
        
        return self._ErpBOM

    def setErpBOM(self, value):
        if self._ErpBOM is not None:
            filtered = [x for x in self.ErpBOM.ErpBomItemDatas if x != self]
            self._ErpBOM._ErpBomItemDatas = filtered

        self._ErpBOM = value
        if self._ErpBOM is not None:
            self._ErpBOM._ErpBomItemDatas.append(self)

    ErpBOM = property(getErpBOM, setErpBOM)

    def getTypeAsset(self):
        
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            filtered = [x for x in self.TypeAsset.ErpBomItemDatas if x != self]
            self._TypeAsset._ErpBomItemDatas = filtered

        self._TypeAsset = value
        if self._TypeAsset is not None:
            self._TypeAsset._ErpBomItemDatas.append(self)

    TypeAsset = property(getTypeAsset, setTypeAsset)

