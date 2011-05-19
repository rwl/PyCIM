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

class SwitchInfo(AssetInfo):
    """Properties of switch assets.Properties of switch assets.
    """

    def __init__(self, dielectricStrength=0.0, gang=False, makingCapacity=0.0, withstandCurrent=0.0, loadBreak=False, minimumCurrent=0.0, interruptingRating=0.0, remote=False, poleCount=0, *args, **kw_args):
        """Initialises a new 'SwitchInfo' instance.

        @param dielectricStrength: The maximum rms voltage that may be applied across an open contact without breaking down the dielectric properties of the switch in the open position. 
        @param gang: True if multi-phase switch controls all phases concurrently. 
        @param makingCapacity: The highest value of current the switch can make at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        @param withstandCurrent: The highest value of current the switch can carry in the closed position at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        @param loadBreak: True if switch has load breaking capabiity. Unless specified false, this is always assumed to be true for breakers and reclosers. 
        @param minimumCurrent: The lowest value of current that the switch can make, carry and break in uninterrupted duty at the rated voltage under specified operating conditions without suffering significant deterioration of its performance. 
        @param interruptingRating: Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage. 
        @param remote: True if device is capable of being operated by remote control. 
        @param poleCount: Number of poles (i.e. of current carrying conductors that are switched). 
        """
        #: The maximum rms voltage that may be applied across an open contact without breaking down the dielectric properties of the switch in the open position.
        self.dielectricStrength = dielectricStrength

        #: True if multi-phase switch controls all phases concurrently.
        self.gang = gang

        #: The highest value of current the switch can make at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
        self.makingCapacity = makingCapacity

        #: The highest value of current the switch can carry in the closed position at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
        self.withstandCurrent = withstandCurrent

        #: True if switch has load breaking capabiity. Unless specified false, this is always assumed to be true for breakers and reclosers.
        self.loadBreak = loadBreak

        #: The lowest value of current that the switch can make, carry and break in uninterrupted duty at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
        self.minimumCurrent = minimumCurrent

        #: Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage.
        self.interruptingRating = interruptingRating

        #: True if device is capable of being operated by remote control.
        self.remote = remote

        #: Number of poles (i.e. of current carrying conductors that are switched).
        self.poleCount = poleCount

        super(SwitchInfo, self).__init__(*args, **kw_args)

    _attrs = ["dielectricStrength", "gang", "makingCapacity", "withstandCurrent", "loadBreak", "minimumCurrent", "interruptingRating", "remote", "poleCount"]
    _attr_types = {"dielectricStrength": float, "gang": bool, "makingCapacity": float, "withstandCurrent": float, "loadBreak": bool, "minimumCurrent": float, "interruptingRating": float, "remote": bool, "poleCount": int}
    _defaults = {"dielectricStrength": 0.0, "gang": False, "makingCapacity": 0.0, "withstandCurrent": 0.0, "loadBreak": False, "minimumCurrent": 0.0, "interruptingRating": 0.0, "remote": False, "poleCount": 0}
    _enums = {}
    _refs = []
    _many_refs = []

