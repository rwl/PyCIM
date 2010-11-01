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

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel

class ToolAssetModel(AssetModel):
    """Documentation for a type of a tool of a particular product model made by a manufacturer.
    """

    def __init__(self, Tools=None, ToolTypeAsset=None, *args, **kw_args):
        """Initializes a new 'ToolAssetModel' instance.

        @param Tools:
        @param ToolTypeAsset:
        """
        self._Tools = []
        self.Tools = [] if Tools is None else Tools

        self._ToolTypeAsset = None
        self.ToolTypeAsset = ToolTypeAsset

        super(ToolAssetModel, self).__init__(*args, **kw_args)

    def getTools(self):
        
        return self._Tools

    def setTools(self, value):
        for x in self._Tools:
            x._ToolAssetModel = None
        for y in value:
            y._ToolAssetModel = self
        self._Tools = value

    Tools = property(getTools, setTools)

    def addTools(self, *Tools):
        for obj in Tools:
            obj._ToolAssetModel = self
            self._Tools.append(obj)

    def removeTools(self, *Tools):
        for obj in Tools:
            obj._ToolAssetModel = None
            self._Tools.remove(obj)

    def getToolTypeAsset(self):
        
        return self._ToolTypeAsset

    def setToolTypeAsset(self, value):
        if self._ToolTypeAsset is not None:
            filtered = [x for x in self.ToolTypeAsset.ToolAssetModels if x != self]
            self._ToolTypeAsset._ToolAssetModels = filtered

        self._ToolTypeAsset = value
        if self._ToolTypeAsset is not None:
            self._ToolTypeAsset._ToolAssetModels.append(self)

    ToolTypeAsset = property(getToolTypeAsset, setToolTypeAsset)

