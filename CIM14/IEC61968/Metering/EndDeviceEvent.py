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

from CIM14.IEC61968.Common.ActivityRecord import ActivityRecord

class EndDeviceEvent(ActivityRecord):
    """Event detected by a DeviceFunction associated with EndDeviceAsset.
    """

    def __init__(self, userID='', MeterReading=None, DeviceFunction=None, *args, **kw_args):
        """Initialises a new 'EndDeviceEvent' instance.

        @param userID: (if user initiated) ID of user who initiated this end device event. 
        @param MeterReading: Set of measured values to which this event applies.
        @param DeviceFunction: Device function that reported this end device event.
        """
        #: (if user initiated) ID of user who initiated this end device event.
        self.userID = userID

        self._MeterReading = None
        self.MeterReading = MeterReading

        self._DeviceFunction = None
        self.DeviceFunction = DeviceFunction

        super(EndDeviceEvent, self).__init__(*args, **kw_args)

    _attrs = ["userID"]
    _attr_types = {"userID": str}
    _defaults = {"userID": ''}
    _enums = {}
    _refs = ["MeterReading", "DeviceFunction"]
    _many_refs = []

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
            if self not in self._MeterReading._EndDeviceEvents:
                self._MeterReading._EndDeviceEvents.append(self)

    MeterReading = property(getMeterReading, setMeterReading)

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
            if self not in self._DeviceFunction._EndDeviceEvents:
                self._DeviceFunction._EndDeviceEvents.append(self)

    DeviceFunction = property(getDeviceFunction, setDeviceFunction)

