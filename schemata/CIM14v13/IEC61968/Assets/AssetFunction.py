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

from CIM14v13.IEC61968.Assets.Asset import Asset

class AssetFunction(Asset):
    """Function performed by an asset. Often, function is a module (or a board that plugs into a backplane) that can be replaced or updated without impacting the rest of the asset. Therefore functions are treated as assets because they have life-cycles that are independent of the asset containing the function.
    """

    def __init__(self, hardwareID='', configID='', programID='', password='', firmwareID='', Asset=None, AssetFunctionAssetModel=None, *args, **kw_args):
        """Initializes a new 'AssetFunction' instance.

        @param hardwareID: Hardware version. 
        @param configID: Configuration specified for this function. 
        @param programID: Name of program. 
        @param password: Password needed to access this function. 
        @param firmwareID: Firmware version. 
        @param Asset:
        @param AssetFunctionAssetModel:
        """
        #: Hardware version.
        self.hardwareID = hardwareID

        #: Configuration specified for this function.
        self.configID = configID

        #: Name of program.
        self.programID = programID

        #: Password needed to access this function.
        self.password = password

        #: Firmware version.
        self.firmwareID = firmwareID

        self._Asset = None
        self.Asset = Asset

        self._AssetFunctionAssetModel = None
        self.AssetFunctionAssetModel = AssetFunctionAssetModel

        super(AssetFunction, self).__init__(*args, **kw_args)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.AssetFunctions if x != self]
            self._Asset._AssetFunctions = filtered

        self._Asset = value
        if self._Asset is not None:
            self._Asset._AssetFunctions.append(self)

    Asset = property(getAsset, setAsset)

    def getAssetFunctionAssetModel(self):
        
        return self._AssetFunctionAssetModel

    def setAssetFunctionAssetModel(self, value):
        if self._AssetFunctionAssetModel is not None:
            filtered = [x for x in self.AssetFunctionAssetModel.AssetFunctions if x != self]
            self._AssetFunctionAssetModel._AssetFunctions = filtered

        self._AssetFunctionAssetModel = value
        if self._AssetFunctionAssetModel is not None:
            self._AssetFunctionAssetModel._AssetFunctions.append(self)

    AssetFunctionAssetModel = property(getAssetFunctionAssetModel, setAssetFunctionAssetModel)

