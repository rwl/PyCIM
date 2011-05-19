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

from CIM15.IEC61968.Assets.AssetFunction import AssetFunction

class EndDeviceFunction(AssetFunction):
    """Function performed by an end device such as a meter, communication equipment, controllers, etc.Function performed by an end device such as a meter, communication equipment, controllers, etc.
    """

    def __init__(self, enabled=False, supported=False, Registers=None, ComEquipment=None, EndDeviceEvents=None, EndDevice=None, *args, **kw_args):
        """Initialises a new 'EndDeviceFunction' instance.

        @param enabled: True if the function is enabled (current operating status; makes sense only if 'supported'=true). 
        @param supported: True if the function is supported (inherent property of the device). 
        @param Registers: All registers for quantities metered by this end device function.
        @param ComEquipment: Communication equipment performing this device function.
        @param EndDeviceEvents: All events reported by this end device function.
        @param EndDevice: End device that performs this function.
        """
        #: True if the function is enabled (current operating status; makes sense only if 'supported'=true).
        self.enabled = enabled

        #: True if the function is supported (inherent property of the device).
        self.supported = supported

        self._Registers = []
        self.Registers = [] if Registers is None else Registers

        self._ComEquipment = None
        self.ComEquipment = ComEquipment

        self._EndDeviceEvents = []
        self.EndDeviceEvents = [] if EndDeviceEvents is None else EndDeviceEvents

        self._EndDevice = None
        self.EndDevice = EndDevice

        super(EndDeviceFunction, self).__init__(*args, **kw_args)

    _attrs = ["enabled", "supported"]
    _attr_types = {"enabled": bool, "supported": bool}
    _defaults = {"enabled": False, "supported": False}
    _enums = {}
    _refs = ["Registers", "ComEquipment", "EndDeviceEvents", "EndDevice"]
    _many_refs = ["Registers", "EndDeviceEvents"]

    def getRegisters(self):
        """All registers for quantities metered by this end device function.
        """
        return self._Registers

    def setRegisters(self, value):
        for x in self._Registers:
            x.EndDeviceFunction = None
        for y in value:
            y._EndDeviceFunction = self
        self._Registers = value

    Registers = property(getRegisters, setRegisters)

    def addRegisters(self, *Registers):
        for obj in Registers:
            obj.EndDeviceFunction = self

    def removeRegisters(self, *Registers):
        for obj in Registers:
            obj.EndDeviceFunction = None

    def getComEquipment(self):
        """Communication equipment performing this device function.
        """
        return self._ComEquipment

    def setComEquipment(self, value):
        if self._ComEquipment is not None:
            filtered = [x for x in self.ComEquipment.EndDeviceFunctions if x != self]
            self._ComEquipment._EndDeviceFunctions = filtered

        self._ComEquipment = value
        if self._ComEquipment is not None:
            if self not in self._ComEquipment._EndDeviceFunctions:
                self._ComEquipment._EndDeviceFunctions.append(self)

    ComEquipment = property(getComEquipment, setComEquipment)

    def getEndDeviceEvents(self):
        """All events reported by this end device function.
        """
        return self._EndDeviceEvents

    def setEndDeviceEvents(self, value):
        for x in self._EndDeviceEvents:
            x.EndDeviceFunction = None
        for y in value:
            y._EndDeviceFunction = self
        self._EndDeviceEvents = value

    EndDeviceEvents = property(getEndDeviceEvents, setEndDeviceEvents)

    def addEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj.EndDeviceFunction = self

    def removeEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj.EndDeviceFunction = None

    def getEndDevice(self):
        """End device that performs this function.
        """
        return self._EndDevice

    def setEndDevice(self, value):
        if self._EndDevice is not None:
            filtered = [x for x in self.EndDevice.EndDeviceFunctions if x != self]
            self._EndDevice._EndDeviceFunctions = filtered

        self._EndDevice = value
        if self._EndDevice is not None:
            if self not in self._EndDevice._EndDeviceFunctions:
                self._EndDevice._EndDeviceFunctions.append(self)

    EndDevice = property(getEndDevice, setEndDevice)

