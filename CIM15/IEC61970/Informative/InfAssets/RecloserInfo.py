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

from CIM15.IEC61970.Informative.InfAssets.SwitchInfo import SwitchInfo

class RecloserInfo(SwitchInfo):
    """Properties of recloser assets.Properties of recloser assets.
    """

    def __init__(self, groundTripNormalEnabled=False, groundTripCapable=False, recloseLockoutCount=0, phaseTripRating=0.0, groundTripRating=0.0, *args, **kw_args):
        """Initialises a new 'RecloserInfo' instance.

        @param groundTripNormalEnabled: True if normal status of ground trip is enabled. 
        @param groundTripCapable: True if device has ground trip capability. 
        @param recloseLockoutCount: Total number of phase reclose operations. 
        @param phaseTripRating: Phase trip rating. 
        @param groundTripRating: Ground trip rating. 
        """
        #: True if normal status of ground trip is enabled.
        self.groundTripNormalEnabled = groundTripNormalEnabled

        #: True if device has ground trip capability.
        self.groundTripCapable = groundTripCapable

        #: Total number of phase reclose operations.
        self.recloseLockoutCount = recloseLockoutCount

        #: Phase trip rating.
        self.phaseTripRating = phaseTripRating

        #: Ground trip rating.
        self.groundTripRating = groundTripRating

        super(RecloserInfo, self).__init__(*args, **kw_args)

    _attrs = ["groundTripNormalEnabled", "groundTripCapable", "recloseLockoutCount", "phaseTripRating", "groundTripRating"]
    _attr_types = {"groundTripNormalEnabled": bool, "groundTripCapable": bool, "recloseLockoutCount": int, "phaseTripRating": float, "groundTripRating": float}
    _defaults = {"groundTripNormalEnabled": False, "groundTripCapable": False, "recloseLockoutCount": 0, "phaseTripRating": 0.0, "groundTripRating": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

