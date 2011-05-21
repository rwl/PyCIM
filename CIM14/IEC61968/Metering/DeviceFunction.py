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

from CIM14.IEC61968.Assets.AssetFunction import AssetFunction

class DeviceFunction(AssetFunction):
    """Function performed by a device such as a meter, communication equipment, controllers, etc.
    """

    def __init__(self, disabled=False, EndDeviceAsset=None, Registers=None, EndDeviceEvents=None, *args, **kw_args):
        """Initialises a new 'DeviceFunction' instance.

        @param disabled: True if the device function is disabled (deactivated). Default is false (i.e., function is enabled). 
        @param EndDeviceAsset: End device asset that performs this function.
        @param Registers: All registers for quantities metered by this device function.
        @param EndDeviceEvents: All events reported by this device function.
        """
        #: True if the device function is disabled (deactivated). Default is false (i.e., function is enabled).
        self.disabled = disabled

        self._EndDeviceAsset = None
        self.EndDeviceAsset = EndDeviceAsset

        self._Registers = []
        self.Registers = [] if Registers is None else Registers

        self._EndDeviceEvents = []
        self.EndDeviceEvents = [] if EndDeviceEvents is None else EndDeviceEvents

        super(DeviceFunction, self).__init__(*args, **kw_args)

    _attrs = ["disabled"]
    _attr_types = {"disabled": bool}
    _defaults = {"disabled": False}
    _enums = {}
    _refs = ["EndDeviceAsset", "Registers", "EndDeviceEvents"]
    _many_refs = ["Registers", "EndDeviceEvents"]

    def getEndDeviceAsset(self):
        """End device asset that performs this function.
        """
        return self._EndDeviceAsset

    def setEndDeviceAsset(self, value):
        if self._EndDeviceAsset is not None:
            filtered = [x for x in self.EndDeviceAsset.DeviceFunctions if x != self]
            self._EndDeviceAsset._DeviceFunctions = filtered

        self._EndDeviceAsset = value
        if self._EndDeviceAsset is not None:
            if self not in self._EndDeviceAsset._DeviceFunctions:
                self._EndDeviceAsset._DeviceFunctions.append(self)

    EndDeviceAsset = property(getEndDeviceAsset, setEndDeviceAsset)

    def getRegisters(self):
        """All registers for quantities metered by this device function.
        """
        return self._Registers

    def setRegisters(self, value):
        for x in self._Registers:
            x.DeviceFunction = None
        for y in value:
            y._DeviceFunction = self
        self._Registers = value

    Registers = property(getRegisters, setRegisters)

    def addRegisters(self, *Registers):
        for obj in Registers:
            obj.DeviceFunction = self

    def removeRegisters(self, *Registers):
        for obj in Registers:
            obj.DeviceFunction = None

    def getEndDeviceEvents(self):
        """All events reported by this device function.
        """
        return self._EndDeviceEvents

    def setEndDeviceEvents(self, value):
        for x in self._EndDeviceEvents:
            x.DeviceFunction = None
        for y in value:
            y._DeviceFunction = self
        self._EndDeviceEvents = value

    EndDeviceEvents = property(getEndDeviceEvents, setEndDeviceEvents)

    def addEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj.DeviceFunction = self

    def removeEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj.DeviceFunction = None

