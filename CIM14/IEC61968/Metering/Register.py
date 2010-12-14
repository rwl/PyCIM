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

class Register(IdentifiedObject):
    """Display for quantity that is metered on an end device such as a meter.
    """

    def __init__(self, leftDigitCount=0, rightDigitCount=0, ReadingType=None, DeviceFunction=None, *args, **kw_args):
        """Initialises a new 'Register' instance.

        @param leftDigitCount: Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5. 
        @param rightDigitCount: Number of digits (dials on a mechanical meter) to the right of the decimal place. 
        @param ReadingType: Reading type for values displayed by this register.
        @param DeviceFunction: Device function metering quantities displayed by this register.
        """
        #: Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5.
        self.leftDigitCount = leftDigitCount

        #: Number of digits (dials on a mechanical meter) to the right of the decimal place.
        self.rightDigitCount = rightDigitCount

        self._ReadingType = None
        self.ReadingType = ReadingType

        self._DeviceFunction = None
        self.DeviceFunction = DeviceFunction

        super(Register, self).__init__(*args, **kw_args)

    _attrs = ["leftDigitCount", "rightDigitCount"]
    _attr_types = {"leftDigitCount": int, "rightDigitCount": int}
    _defaults = {"leftDigitCount": 0, "rightDigitCount": 0}
    _enums = {}
    _refs = ["ReadingType", "DeviceFunction"]
    _many_refs = []

    def getReadingType(self):
        """Reading type for values displayed by this register.
        """
        return self._ReadingType

    def setReadingType(self, value):
        if self._ReadingType is not None:
            self._ReadingType._Register = None

        self._ReadingType = value
        if self._ReadingType is not None:
            self._ReadingType.Register = None
            self._ReadingType._Register = self

    ReadingType = property(getReadingType, setReadingType)

    def getDeviceFunction(self):
        """Device function metering quantities displayed by this register.
        """
        return self._DeviceFunction

    def setDeviceFunction(self, value):
        if self._DeviceFunction is not None:
            filtered = [x for x in self.DeviceFunction.Registers if x != self]
            self._DeviceFunction._Registers = filtered

        self._DeviceFunction = value
        if self._DeviceFunction is not None:
            if self not in self._DeviceFunction._Registers:
                self._DeviceFunction._Registers.append(self)

    DeviceFunction = property(getDeviceFunction, setDeviceFunction)

