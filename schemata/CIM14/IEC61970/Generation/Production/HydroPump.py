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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class HydroPump(PowerSystemResource):
    """A synchronous motor-driven pump, typically associated with a pumped storage plant
    """

    def __init__(self, pumpPowerAtMaxHead=0.0, pumpPowerAtMinHead=0.0, pumpDischAtMinHead=0.0, pumpDischAtMaxHead=0.0, SynchronousMachine=None, HydroPumpOpSchedule=None, HydroPowerPlant=None, **kw_args):
        """Initializes a new 'HydroPump' instance.

        @param pumpPowerAtMaxHead: The pumping power under maximum head conditions, usually at full gate 
        @param pumpPowerAtMinHead: The pumping power under minimum head conditions, usually at full gate. 
        @param pumpDischAtMinHead: The pumping discharge (m3/sec) under minimum head conditions, usually at full gate 
        @param pumpDischAtMaxHead: The pumping discharge (m3/sec) under maximum head conditions, usually at full gate 
        @param SynchronousMachine: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        @param HydroPumpOpSchedule: The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        @param HydroPowerPlant: The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        """
        #: The pumping power under maximum head conditions, usually at full gate
        self.pumpPowerAtMaxHead = pumpPowerAtMaxHead

        #: The pumping power under minimum head conditions, usually at full gate.
        self.pumpPowerAtMinHead = pumpPowerAtMinHead

        #: The pumping discharge (m3/sec) under minimum head conditions, usually at full gate
        self.pumpDischAtMinHead = pumpDischAtMinHead

        #: The pumping discharge (m3/sec) under maximum head conditions, usually at full gate
        self.pumpDischAtMaxHead = pumpDischAtMaxHead

        self._SynchronousMachine = None
        self.SynchronousMachine = SynchronousMachine

        self._HydroPumpOpSchedule = None
        self.HydroPumpOpSchedule = HydroPumpOpSchedule

        self._HydroPowerPlant = None
        self.HydroPowerPlant = HydroPowerPlant

        super(HydroPump, self).__init__(**kw_args)

    def getSynchronousMachine(self):
        """The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        return self._SynchronousMachine

    def setSynchronousMachine(self, value):
        if self._SynchronousMachine is not None:
            self._SynchronousMachine._HydroPump = None

        self._SynchronousMachine = value
        if self._SynchronousMachine is not None:
            self._SynchronousMachine._HydroPump = self

    SynchronousMachine = property(getSynchronousMachine, setSynchronousMachine)

    def getHydroPumpOpSchedule(self):
        """The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """
        return self._HydroPumpOpSchedule

    def setHydroPumpOpSchedule(self, value):
        if self._HydroPumpOpSchedule is not None:
            self._HydroPumpOpSchedule._HydroPump = None

        self._HydroPumpOpSchedule = value
        if self._HydroPumpOpSchedule is not None:
            self._HydroPumpOpSchedule._HydroPump = self

    HydroPumpOpSchedule = property(getHydroPumpOpSchedule, setHydroPumpOpSchedule)

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
            self._HydroPowerPlant._HydroPumps.append(self)

    HydroPowerPlant = property(getHydroPowerPlant, setHydroPowerPlant)

