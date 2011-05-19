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

from CIM15.IEC61968.Assets.AssetInfo import AssetInfo

class EndDeviceInfo(AssetInfo):
    """End device data.End device data.
    """

    def __init__(self, phaseCount=0, ratedCurrent=0.0, ratedVoltage=0.0, EndDevices=None, *args, **kw_args):
        """Initialises a new 'EndDeviceInfo' instance.

        @param phaseCount: Number of potential phases the end device supports, typically 0, 1 or 3. 
        @param ratedCurrent: Rated current. 
        @param ratedVoltage: Rated voltage. 
        @param EndDevices: All end devices described with this data.
        """
        #: Number of potential phases the end device supports, typically 0, 1 or 3.
        self.phaseCount = phaseCount

        #: Rated current.
        self.ratedCurrent = ratedCurrent

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        self._EndDevices = []
        self.EndDevices = [] if EndDevices is None else EndDevices

        super(EndDeviceInfo, self).__init__(*args, **kw_args)

    _attrs = ["phaseCount", "ratedCurrent", "ratedVoltage"]
    _attr_types = {"phaseCount": int, "ratedCurrent": float, "ratedVoltage": float}
    _defaults = {"phaseCount": 0, "ratedCurrent": 0.0, "ratedVoltage": 0.0}
    _enums = {}
    _refs = ["EndDevices"]
    _many_refs = ["EndDevices"]

    def getEndDevices(self):
        """All end devices described with this data.
        """
        return self._EndDevices

    def setEndDevices(self, value):
        for x in self._EndDevices:
            x.EndDeviceInfo = None
        for y in value:
            y._EndDeviceInfo = self
        self._EndDevices = value

    EndDevices = property(getEndDevices, setEndDevices)

    def addEndDevices(self, *EndDevices):
        for obj in EndDevices:
            obj.EndDeviceInfo = self

    def removeEndDevices(self, *EndDevices):
        for obj in EndDevices:
            obj.EndDeviceInfo = None

