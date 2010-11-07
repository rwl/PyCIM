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

from CIM14.IEC61968.Assets.AssetFunction import AssetFunction

class DeviceFunction(AssetFunction):
    """Function performed by a device such as a meter, communication equipment, controllers, etc.
    """

    def __init__(self, disabled=False, EndDeviceAsset=None, Registers=None, EndDeviceEvents=None, **kw_args):
        """Initializes a new 'DeviceFunction' instance.

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

        super(DeviceFunction, self).__init__(**kw_args)

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
            self._EndDeviceAsset._DeviceFunctions.append(self)

    EndDeviceAsset = property(getEndDeviceAsset, setEndDeviceAsset)

    def getRegisters(self):
        """All registers for quantities metered by this device function.
        """
        return self._Registers

    def setRegisters(self, value):
        for x in self._Registers:
            x._DeviceFunction = None
        for y in value:
            y._DeviceFunction = self
        self._Registers = value

    Registers = property(getRegisters, setRegisters)

    def addRegisters(self, *Registers):
        for obj in Registers:
            obj._DeviceFunction = self
            self._Registers.append(obj)

    def removeRegisters(self, *Registers):
        for obj in Registers:
            obj._DeviceFunction = None
            self._Registers.remove(obj)

    def getEndDeviceEvents(self):
        """All events reported by this device function.
        """
        return self._EndDeviceEvents

    def setEndDeviceEvents(self, value):
        for x in self._EndDeviceEvents:
            x._DeviceFunction = None
        for y in value:
            y._DeviceFunction = self
        self._EndDeviceEvents = value

    EndDeviceEvents = property(getEndDeviceEvents, setEndDeviceEvents)

    def addEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj._DeviceFunction = self
            self._EndDeviceEvents.append(obj)

    def removeEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj._DeviceFunction = None
            self._EndDeviceEvents.remove(obj)

