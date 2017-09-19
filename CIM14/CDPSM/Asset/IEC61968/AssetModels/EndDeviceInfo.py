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

from CIM15.CDPSM.Asset.IEC61968.Assets.AssetInfo import AssetInfo

class EndDeviceInfo(AssetInfo):
    """End device data.
    """

    def __init__(self, ratedCurrent=0.0, ratedVoltage=0.0, phaseCount=0, *args, **kw_args):
        """Initialises a new 'EndDeviceInfo' instance.

        @param ratedCurrent: Rated current. 
        @param ratedVoltage: Rated voltage. 
        @param phaseCount: Number of potential phases the end device supports, typically 0, 1 or 3. 
        """
        #: Rated current.
        self.ratedCurrent = ratedCurrent

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        #: Number of potential phases the end device supports, typically 0, 1 or 3.
        self.phaseCount = phaseCount

        super(EndDeviceInfo, self).__init__(*args, **kw_args)

    _attrs = ["ratedCurrent", "ratedVoltage", "phaseCount"]
    _attr_types = {"ratedCurrent": float, "ratedVoltage": float, "phaseCount": int}
    _defaults = {"ratedCurrent": 0.0, "ratedVoltage": 0.0, "phaseCount": 0}
    _enums = {}
    _refs = []
    _many_refs = []

