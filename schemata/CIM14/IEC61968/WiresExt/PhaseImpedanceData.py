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

from CIM14.Element import Element

class PhaseImpedanceData(Element):
    """Triplet of resistance, reactance, and susceptance matrix element values.
    """

    def __init__(self, r=0.0, x=0.0, sequenceNumber=0, b=0.0, PhaseImpedance=None, **kw_args):
        """Initializes a new 'PhaseImpedanceData' instance.

        @param r: Resistance matrix element value, per length of unit. 
        @param x: Reactance matrix element value, per length of unit. 
        @param sequenceNumber: Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2. 
        @param b: Susceptance matrix element value, per length of unit. 
        @param PhaseImpedance: Conductor phase impedance to which this data belongs.
        """
        #: Resistance matrix element value, per length of unit.
        self.r = r

        #: Reactance matrix element value, per length of unit.
        self.x = x

        #: Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2.
        self.sequenceNumber = sequenceNumber

        #: Susceptance matrix element value, per length of unit.
        self.b = b

        self._PhaseImpedance = None
        self.PhaseImpedance = PhaseImpedance

        super(PhaseImpedanceData, self).__init__(**kw_args)

    def getPhaseImpedance(self):
        """Conductor phase impedance to which this data belongs.
        """
        return self._PhaseImpedance

    def setPhaseImpedance(self, value):
        if self._PhaseImpedance is not None:
            filtered = [x for x in self.PhaseImpedance.PhaseImpedanceData if x != self]
            self._PhaseImpedance._PhaseImpedanceData = filtered

        self._PhaseImpedance = value
        if self._PhaseImpedance is not None:
            self._PhaseImpedance._PhaseImpedanceData.append(self)

    PhaseImpedance = property(getPhaseImpedance, setPhaseImpedance)

