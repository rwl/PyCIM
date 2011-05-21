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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class AssetFunction(IdentifiedObject):
    """Function performed by an asset.
    """

    def __init__(self, configID='', programID='', firmwareID='', password='', hardwareID='', Asset=None, *args, **kw_args):
        """Initialises a new 'AssetFunction' instance.

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

        super(AssetFunction, self).__init__(*args, **kw_args)

    _attrs = ["configID", "programID", "firmwareID", "password", "hardwareID"]
    _attr_types = {"configID": str, "programID": str, "firmwareID": str, "password": str, "hardwareID": str}
    _defaults = {"configID": '', "programID": '', "firmwareID": '', "password": '', "hardwareID": ''}
    _enums = {}
    _refs = ["Asset"]
    _many_refs = []

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.AssetFunctions if x != self]
            self._Asset._AssetFunctions = filtered

        self._Asset = value
        if self._Asset is not None:
            if self not in self._Asset._AssetFunctions:
                self._Asset._AssetFunctions.append(self)

    Asset = property(getAsset, setAsset)

