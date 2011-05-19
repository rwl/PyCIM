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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class HydroPump(PowerSystemResource):
    """A synchronous motor-driven pump, typically associated with a pumped storage plantA synchronous motor-driven pump, typically associated with a pumped storage plant
    """

    def __init__(self, pumpDischAtMaxHead=0.0, pumpDischAtMinHead=0.0, pumpPowerAtMinHead=0.0, pumpPowerAtMaxHead=0.0, HydroPowerPlant=None, HydroPumpOpSchedule=None, SynchronousMachine=None, *args, **kw_args):
        """Initialises a new 'HydroPump' instance.

        @param pumpDischAtMaxHead: The pumping discharge under maximum head conditions, usually at full gate 
        @param pumpDischAtMinHead: The pumping discharge under minimum head conditions, usually at full gate 
        @param pumpPowerAtMinHead: The pumping power under minimum head conditions, usually at full gate. 
        @param pumpPowerAtMaxHead: The pumping power under maximum head conditions, usually at full gate 
        @param HydroPowerPlant: The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        @param HydroPumpOpSchedule: The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        @param SynchronousMachine: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        #: The pumping discharge under maximum head conditions, usually at full gate
        self.pumpDischAtMaxHead = pumpDischAtMaxHead

        #: The pumping discharge under minimum head conditions, usually at full gate
        self.pumpDischAtMinHead = pumpDischAtMinHead

        #: The pumping power under minimum head conditions, usually at full gate.
        self.pumpPowerAtMinHead = pumpPowerAtMinHead

        #: The pumping power under maximum head conditions, usually at full gate
        self.pumpPowerAtMaxHead = pumpPowerAtMaxHead

        self._HydroPowerPlant = None
        self.HydroPowerPlant = HydroPowerPlant

        self._HydroPumpOpSchedule = None
        self.HydroPumpOpSchedule = HydroPumpOpSchedule

        self._SynchronousMachine = None
        self.SynchronousMachine = SynchronousMachine

        super(HydroPump, self).__init__(*args, **kw_args)

    _attrs = ["pumpDischAtMaxHead", "pumpDischAtMinHead", "pumpPowerAtMinHead", "pumpPowerAtMaxHead"]
    _attr_types = {"pumpDischAtMaxHead": float, "pumpDischAtMinHead": float, "pumpPowerAtMinHead": float, "pumpPowerAtMaxHead": float}
    _defaults = {"pumpDischAtMaxHead": 0.0, "pumpDischAtMinHead": 0.0, "pumpPowerAtMinHead": 0.0, "pumpPowerAtMaxHead": 0.0}
    _enums = {}
    _refs = ["HydroPowerPlant", "HydroPumpOpSchedule", "SynchronousMachine"]
    _many_refs = []

    def getHydroPowerPlant(self):
        """The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        """
        return self._HydroPowerPlant

    def setHydroPowerPlant(self, value):
        if self._HydroPowerPlant is not None:
            filtered = [x for x in self.HydroPowerPlant.HydroPumps if x != self]
            self._HydroPowerPlant._HydroPumps = filtered

        self._HydroPowerPlant = value
        if self._HydroPowerPlant is not None:
            if self not in self._HydroPowerPlant._HydroPumps:
                self._HydroPowerPlant._HydroPumps.append(self)

    HydroPowerPlant = property(getHydroPowerPlant, setHydroPowerPlant)

    def getHydroPumpOpSchedule(self):
        """The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """
        return self._HydroPumpOpSchedule

    def setHydroPumpOpSchedule(self, value):
        if self._HydroPumpOpSchedule is not None:
            self._HydroPumpOpSchedule._HydroPump = None

        self._HydroPumpOpSchedule = value
        if self._HydroPumpOpSchedule is not None:
            self._HydroPumpOpSchedule.HydroPump = None
            self._HydroPumpOpSchedule._HydroPump = self

    HydroPumpOpSchedule = property(getHydroPumpOpSchedule, setHydroPumpOpSchedule)

    def getSynchronousMachine(self):
        """The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        return self._SynchronousMachine

    def setSynchronousMachine(self, value):
        if self._SynchronousMachine is not None:
            self._SynchronousMachine._HydroPump = None

        self._SynchronousMachine = value
        if self._SynchronousMachine is not None:
            self._SynchronousMachine.HydroPump = None
            self._SynchronousMachine._HydroPump = self

    SynchronousMachine = property(getSynchronousMachine, setSynchronousMachine)

