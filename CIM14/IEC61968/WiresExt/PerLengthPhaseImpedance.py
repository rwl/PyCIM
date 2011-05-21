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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PerLengthPhaseImpedance(IdentifiedObject):
    """Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.
    """

    def __init__(self, conductorCount=0, ConductorSegments=None, PhaseImpedanceData=None, *args, **kw_args):
        """Initialises a new 'PerLengthPhaseImpedance' instance.

        @param conductorCount: Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix. 
        @param ConductorSegments: All conductor segments described by this phase impedance.
        @param PhaseImpedanceData: All data that belong to this conductor phase impedance.
        """
        #: Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix.
        self.conductorCount = conductorCount

        self._ConductorSegments = []
        self.ConductorSegments = [] if ConductorSegments is None else ConductorSegments

        self._PhaseImpedanceData = []
        self.PhaseImpedanceData = [] if PhaseImpedanceData is None else PhaseImpedanceData

        super(PerLengthPhaseImpedance, self).__init__(*args, **kw_args)

    _attrs = ["conductorCount"]
    _attr_types = {"conductorCount": int}
    _defaults = {"conductorCount": 0}
    _enums = {}
    _refs = ["ConductorSegments", "PhaseImpedanceData"]
    _many_refs = ["ConductorSegments", "PhaseImpedanceData"]

    def getConductorSegments(self):
        """All conductor segments described by this phase impedance.
        """
        return self._ConductorSegments

    def setConductorSegments(self, value):
        for x in self._ConductorSegments:
            x.PhaseImpedance = None
        for y in value:
            y._PhaseImpedance = self
        self._ConductorSegments = value

    ConductorSegments = property(getConductorSegments, setConductorSegments)

    def addConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj.PhaseImpedance = self

    def removeConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj.PhaseImpedance = None

    def getPhaseImpedanceData(self):
        """All data that belong to this conductor phase impedance.
        """
        return self._PhaseImpedanceData

    def setPhaseImpedanceData(self, value):
        for x in self._PhaseImpedanceData:
            x.PhaseImpedance = None
        for y in value:
            y._PhaseImpedance = self
        self._PhaseImpedanceData = value

    PhaseImpedanceData = property(getPhaseImpedanceData, setPhaseImpedanceData)

    def addPhaseImpedanceData(self, *PhaseImpedanceData):
        for obj in PhaseImpedanceData:
            obj.PhaseImpedance = self

    def removePhaseImpedanceData(self, *PhaseImpedanceData):
        for obj in PhaseImpedanceData:
            obj.PhaseImpedance = None

