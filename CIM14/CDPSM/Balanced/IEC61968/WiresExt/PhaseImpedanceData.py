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

from CIM14.CDPSM.Balanced.Element import Element

class PhaseImpedanceData(Element):
    """Triplet of resistance, reactance, and susceptance matrix element values.
    """

    def __init__(self, x=0.0, sequenceNumber=0, b=0.0, r=0.0, PhaseImpedance=None, *args, **kw_args):
        """Initialises a new 'PhaseImpedanceData' instance.

        @param x: Reactance matrix element value, per length of unit. 
        @param sequenceNumber: Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2. 
        @param b: Susceptance matrix element value, per length of unit. 
        @param r: Resistance matrix element value, per length of unit. 
        @param PhaseImpedance: Conductor phase impedance to which this data belongs.
        """
        #: Reactance matrix element value, per length of unit.
        self.x = x

        #: Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2.
        self.sequenceNumber = sequenceNumber

        #: Susceptance matrix element value, per length of unit.
        self.b = b

        #: Resistance matrix element value, per length of unit.
        self.r = r

        self._PhaseImpedance = None
        self.PhaseImpedance = PhaseImpedance

        super(PhaseImpedanceData, self).__init__(*args, **kw_args)

    _attrs = ["x", "sequenceNumber", "b", "r"]
    _attr_types = {"x": float, "sequenceNumber": int, "b": float, "r": float}
    _defaults = {"x": 0.0, "sequenceNumber": 0, "b": 0.0, "r": 0.0}
    _enums = {}
    _refs = ["PhaseImpedance"]
    _many_refs = []

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
            if self not in self._PhaseImpedance._PhaseImpedanceData:
                self._PhaseImpedance._PhaseImpedanceData.append(self)

    PhaseImpedance = property(getPhaseImpedance, setPhaseImpedance)

