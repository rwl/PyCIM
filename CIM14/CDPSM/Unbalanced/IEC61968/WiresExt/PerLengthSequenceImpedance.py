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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PerLengthSequenceImpedance(IdentifiedObject):
    """Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.
    """

    def __init__(self, x=0.0, r0=0.0, x0=0.0, b0ch=0.0, r=0.0, bch=0.0, ConductorSegments=None, *args, **kw_args):
        """Initialises a new 'PerLengthSequenceImpedance' instance.

        @param x: Positive sequence series reactance, per unit of length. 
        @param r0: Zero sequence series resistance, per unit of length. 
        @param x0: Zero sequence series reactance, per unit of length. 
        @param b0ch: Zero sequence shunt (charging) susceptance, per unit of length. 
        @param r: Positive sequence series resistance, per unit of length. 
        @param bch: Positive sequence shunt (charging) susceptance, per unit of length. 
        @param ConductorSegments: All conductor segments described by this sequence impedance.
        """
        #: Positive sequence series reactance, per unit of length.
        self.x = x

        #: Zero sequence series resistance, per unit of length.
        self.r0 = r0

        #: Zero sequence series reactance, per unit of length.
        self.x0 = x0

        #: Zero sequence shunt (charging) susceptance, per unit of length.
        self.b0ch = b0ch

        #: Positive sequence series resistance, per unit of length.
        self.r = r

        #: Positive sequence shunt (charging) susceptance, per unit of length.
        self.bch = bch

        self._ConductorSegments = []
        self.ConductorSegments = [] if ConductorSegments is None else ConductorSegments

        super(PerLengthSequenceImpedance, self).__init__(*args, **kw_args)

    _attrs = ["x", "r0", "x0", "b0ch", "r", "bch"]
    _attr_types = {"x": float, "r0": float, "x0": float, "b0ch": float, "r": float, "bch": float}
    _defaults = {"x": 0.0, "r0": 0.0, "x0": 0.0, "b0ch": 0.0, "r": 0.0, "bch": 0.0}
    _enums = {}
    _refs = ["ConductorSegments"]
    _many_refs = ["ConductorSegments"]

    def getConductorSegments(self):
        """All conductor segments described by this sequence impedance.
        """
        return self._ConductorSegments

    def setConductorSegments(self, value):
        for x in self._ConductorSegments:
            x.SequenceImpedance = None
        for y in value:
            y._SequenceImpedance = self
        self._ConductorSegments = value

    ConductorSegments = property(getConductorSegments, setConductorSegments)

    def addConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj.SequenceImpedance = self

    def removeConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj.SequenceImpedance = None

