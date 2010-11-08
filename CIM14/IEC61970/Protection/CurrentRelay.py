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

from CIM14.IEC61970.Protection.ProtectionEquipment import ProtectionEquipment

class CurrentRelay(ProtectionEquipment):
    """A device that checks current flow values in any direction or designated direction
    """

    def __init__(self, currentLimit1=0.0, timeDelay3=0.0, timeDelay2=0.0, currentLimit3=0.0, currentLimit2=0.0, inverseTimeFlag=False, timeDelay1=0.0, *args, **kw_args):
        """Initialises a new 'CurrentRelay' instance.

        @param currentLimit1: Current limit #1 for inverse time pickup 
        @param timeDelay3: Inverse time delay #3 for current limit #3 
        @param timeDelay2: Inverse time delay #2 for current limit #2 
        @param currentLimit3: Current limit #3 for inverse time pickup 
        @param currentLimit2: Current limit #2 for inverse time pickup 
        @param inverseTimeFlag: Set true if the current relay has inverse time characteristic. 
        @param timeDelay1: Inverse time delay #1 for current limit #1 
        """
        #: Current limit #1 for inverse time pickup
        self.currentLimit1 = currentLimit1

        #: Inverse time delay #3 for current limit #3
        self.timeDelay3 = timeDelay3

        #: Inverse time delay #2 for current limit #2
        self.timeDelay2 = timeDelay2

        #: Current limit #3 for inverse time pickup
        self.currentLimit3 = currentLimit3

        #: Current limit #2 for inverse time pickup
        self.currentLimit2 = currentLimit2

        #: Set true if the current relay has inverse time characteristic.
        self.inverseTimeFlag = inverseTimeFlag

        #: Inverse time delay #1 for current limit #1
        self.timeDelay1 = timeDelay1

        super(CurrentRelay, self).__init__(*args, **kw_args)

    _attrs = ["currentLimit1", "timeDelay3", "timeDelay2", "currentLimit3", "currentLimit2", "inverseTimeFlag", "timeDelay1"]
    _attr_types = {"currentLimit1": float, "timeDelay3": float, "timeDelay2": float, "currentLimit3": float, "currentLimit2": float, "inverseTimeFlag": bool, "timeDelay1": float}
    _defaults = {"currentLimit1": 0.0, "timeDelay3": 0.0, "timeDelay2": 0.0, "currentLimit3": 0.0, "currentLimit2": 0.0, "inverseTimeFlag": False, "timeDelay1": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

