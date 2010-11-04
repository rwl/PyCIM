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

from CIM14v13.IEC61968.Informative.InfTypeAsset.TypeAsset import TypeAsset

class ToolTypeAsset(TypeAsset):
    """Documentation for a generic tool that may be used for various purposes such as work planning.
    """

    def __init__(self, ToolAssetModels=None, **kw_args):
        """Initializes a new 'ToolTypeAsset' instance.

        @param ToolAssetModels:
        """
        self._ToolAssetModels = []
        self.ToolAssetModels = [] if ToolAssetModels is None else ToolAssetModels

        super(ToolTypeAsset, self).__init__(**kw_args)

    def getToolAssetModels(self):
        
        return self._ToolAssetModels

    def setToolAssetModels(self, value):
        for x in self._ToolAssetModels:
            x._ToolTypeAsset = None
        for y in value:
            y._ToolTypeAsset = self
        self._ToolAssetModels = value

    ToolAssetModels = property(getToolAssetModels, setToolAssetModels)

    def addToolAssetModels(self, *ToolAssetModels):
        for obj in ToolAssetModels:
            obj._ToolTypeAsset = self
            self._ToolAssetModels.append(obj)

    def removeToolAssetModels(self, *ToolAssetModels):
        for obj in ToolAssetModels:
            obj._ToolTypeAsset = None
            self._ToolAssetModels.remove(obj)

