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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class AssetFunction(IdentifiedObject):
    """Function performed by an asset.
    """

    def __init__(self, configID='', programID='', firmwareID='', password='', hardwareID='', Asset=None, **kw_args):
        """Initializes a new 'AssetFunction' instance.

        @param configID: Configuration specified for this function. 
        @param programID: Name of program. 
        @param firmwareID: Firmware version. 
        @param password: Password needed to access this function. 
        @param hardwareID: Hardware version. 
        @param Asset:
        """
        #: Configuration specified for this function.
        self.configID = configID

        #: Name of program.
        self.programID = programID

        #: Firmware version.
        self.firmwareID = firmwareID

        #: Password needed to access this function.
        self.password = password

        #: Hardware version.
        self.hardwareID = hardwareID

        self._Asset = None
        self.Asset = Asset

        super(AssetFunction, self).__init__(**kw_args)

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

