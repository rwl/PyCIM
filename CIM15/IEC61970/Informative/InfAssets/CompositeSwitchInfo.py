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

class CompositeSwitchInfo(AssetInfo):
    """Properties of a composite switch.Properties of a composite switch.
    """

    def __init__(self, kind="throwOver", phaseCode="s12N", remote=False, switchStateCount=0, ratedVoltage=0.0, ganged=False, phaseCount=0, initOpMode='', interruptingRating=0.0, *args, **kw_args):
        """Initialises a new 'CompositeSwitchInfo' instance.

        @param kind: Kind of composite switch. Values are: "throwOver", "regulatorBypass", "escoThrowOver", "ral", "other", "gral", "ugMultiSwitch"
        @param phaseCode: Phases carried, if applicable. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param remote: True if device is capable of being operated by remote control. 
        @param switchStateCount: Number of switch states represented by the composite switch. 
        @param ratedVoltage: Rated voltage. 
        @param ganged: True if multi-phase switch controls all phases concurrently. 
        @param phaseCount: Supported number of phases, typically 0, 1 or 3. 
        @param initOpMode: Initial operating mode, with the following values: Automatic, Manual. 
        @param interruptingRating: Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage. 
        """
        #: Kind of composite switch. Values are: "throwOver", "regulatorBypass", "escoThrowOver", "ral", "other", "gral", "ugMultiSwitch"
        self.kind = kind

        #: Phases carried, if applicable. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.phaseCode = phaseCode

        #: True if device is capable of being operated by remote control.
        self.remote = remote

        #: Number of switch states represented by the composite switch.
        self.switchStateCount = switchStateCount

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        #: True if multi-phase switch controls all phases concurrently.
        self.ganged = ganged

        #: Supported number of phases, typically 0, 1 or 3.
        self.phaseCount = phaseCount

        #: Initial operating mode, with the following values: Automatic, Manual.
        self.initOpMode = initOpMode

        #: Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage.
        self.interruptingRating = interruptingRating

        super(CompositeSwitchInfo, self).__init__(*args, **kw_args)

    _attrs = ["kind", "phaseCode", "remote", "switchStateCount", "ratedVoltage", "ganged", "phaseCount", "initOpMode", "interruptingRating"]
    _attr_types = {"kind": str, "phaseCode": str, "remote": bool, "switchStateCount": int, "ratedVoltage": float, "ganged": bool, "phaseCount": int, "initOpMode": str, "interruptingRating": float}
    _defaults = {"kind": "throwOver", "phaseCode": "s12N", "remote": False, "switchStateCount": 0, "ratedVoltage": 0.0, "ganged": False, "phaseCount": 0, "initOpMode": '', "interruptingRating": 0.0}
    _enums = {"kind": "CompositeSwitchKind", "phaseCode": "PhaseCode"}
    _refs = []
    _many_refs = []

