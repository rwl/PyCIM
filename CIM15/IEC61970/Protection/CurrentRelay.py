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

from CIM15.IEC61970.Protection.ProtectionEquipment import ProtectionEquipment

class CurrentRelay(ProtectionEquipment):
    """A device that checks current flow values in any direction or designated directionA device that checks current flow values in any direction or designated direction
    """

    def __init__(self, currentLimit3=0.0, currentLimit2=0.0, currentLimit1=0.0, inverseTimeFlag=False, timeDelay3=0.0, timeDelay2=0.0, timeDelay1=0.0, *args, **kw_args):
        """Initialises a new 'CurrentRelay' instance.

        @param currentLimit3: Current limit #3 for inverse time pickup 
        @param currentLimit2: Current limit #2 for inverse time pickup 
        @param currentLimit1: Current limit #1 for inverse time pickup 
        @param inverseTimeFlag: Set true if the current relay has inverse time characteristic. 
        @param timeDelay3: Inverse time delay #3 for current limit #3 
        @param timeDelay2: Inverse time delay #2 for current limit #2 
        @param timeDelay1: Inverse time delay #1 for current limit #1 
        """
        #: Current limit #3 for inverse time pickup
        self.currentLimit3 = currentLimit3

        #: Current limit #2 for inverse time pickup
        self.currentLimit2 = currentLimit2

        #: Current limit #1 for inverse time pickup
        self.currentLimit1 = currentLimit1

        #: Set true if the current relay has inverse time characteristic.
        self.inverseTimeFlag = inverseTimeFlag

        #: Inverse time delay #3 for current limit #3
        self.timeDelay3 = timeDelay3

        #: Inverse time delay #2 for current limit #2
        self.timeDelay2 = timeDelay2

        #: Inverse time delay #1 for current limit #1
        self.timeDelay1 = timeDelay1

        super(CurrentRelay, self).__init__(*args, **kw_args)

    _attrs = ["currentLimit3", "currentLimit2", "currentLimit1", "inverseTimeFlag", "timeDelay3", "timeDelay2", "timeDelay1"]
    _attr_types = {"currentLimit3": float, "currentLimit2": float, "currentLimit1": float, "inverseTimeFlag": bool, "timeDelay3": float, "timeDelay2": float, "timeDelay1": float}
    _defaults = {"currentLimit3": 0.0, "currentLimit2": 0.0, "currentLimit1": 0.0, "inverseTimeFlag": False, "timeDelay3": 0.0, "timeDelay2": 0.0, "timeDelay1": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

