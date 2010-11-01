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

from CIM14v13.IEC61968.Common.ActivityRecord import ActivityRecord

class EndDeviceEvent(ActivityRecord):
    """Event detected by a DeviceFunction associated with EndDeviceAsset.
    """

    def __init__(self, userID='', DeviceFunction=None, MeterReading=None, *args, **kw_args):
        """Initializes a new 'EndDeviceEvent' instance.

        @param userID: (if user initiated) ID of user who initiated this end device event. 
        @param DeviceFunction: Device function that reported this end device event.
        @param MeterReading: Set of measured values to which this event applies.
        """
        #: (if user initiated) ID of user who initiated this end device event. 
        self.userID = userID

        self._DeviceFunction = None
        self.DeviceFunction = DeviceFunction

        self._MeterReading = None
        self.MeterReading = MeterReading

        super(EndDeviceEvent, self).__init__(*args, **kw_args)

    def getDeviceFunction(self):
        """Device function that reported this end device event.
        """
        return self._DeviceFunction

    def setDeviceFunction(self, value):
        if self._DeviceFunction is not None:
            filtered = [x for x in self.DeviceFunction.EndDeviceEvents if x != self]
            self._DeviceFunction._EndDeviceEvents = filtered

        self._DeviceFunction = value
        if self._DeviceFunction is not None:
            self._DeviceFunction._EndDeviceEvents.append(self)

    DeviceFunction = property(getDeviceFunction, setDeviceFunction)

    def getMeterReading(self):
        """Set of measured values to which this event applies.
        """
        return self._MeterReading

    def setMeterReading(self, value):
        if self._MeterReading is not None:
            filtered = [x for x in self.MeterReading.EndDeviceEvents if x != self]
            self._MeterReading._EndDeviceEvents = filtered

        self._MeterReading = value
        if self._MeterReading is not None:
            self._MeterReading._EndDeviceEvents.append(self)

    MeterReading = property(getMeterReading, setMeterReading)

