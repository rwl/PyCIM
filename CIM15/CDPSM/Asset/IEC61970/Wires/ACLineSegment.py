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

from CIM15.CDPSM.Asset.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ACLineSegment(IdentifiedObject):
    """A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines, it is sufficient to use ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment. If per lenght impedance data is available from a library of standard types, impedances and admittances can be calculated in one of the following ways: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model.
    """

    def __init__(self, SequenceImpedance=None, ConductorInfo=None, PhaseImpedance=None, *args, **kw_args):
        """Initialises a new 'ACLineSegment' instance.

        @param SequenceImpedance: Sequence impedance of this line segment; used for balanced model.
        @param ConductorInfo: Conductor data for this line segment.
        @param PhaseImpedance: Phase impedance of this line segment; used for unbalanced model.
        """
        self._SequenceImpedance = None
        self.SequenceImpedance = SequenceImpedance

        self._ConductorInfo = None
        self.ConductorInfo = ConductorInfo

        self._PhaseImpedance = None
        self.PhaseImpedance = PhaseImpedance

        super(ACLineSegment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SequenceImpedance", "ConductorInfo", "PhaseImpedance"]
    _many_refs = []

    def getSequenceImpedance(self):
        """Sequence impedance of this line segment; used for balanced model.
        """
        return self._SequenceImpedance

    def setSequenceImpedance(self, value):
        if self._SequenceImpedance is not None:
            filtered = [x for x in self.SequenceImpedance.LineSegments if x != self]
            self._SequenceImpedance._LineSegments = filtered

        self._SequenceImpedance = value
        if self._SequenceImpedance is not None:
            if self not in self._SequenceImpedance._LineSegments:
                self._SequenceImpedance._LineSegments.append(self)

    SequenceImpedance = property(getSequenceImpedance, setSequenceImpedance)

    def getConductorInfo(self):
        """Conductor data for this line segment.
        """
        return self._ConductorInfo

    def setConductorInfo(self, value):
        if self._ConductorInfo is not None:
            filtered = [x for x in self.ConductorInfo.LineSegments if x != self]
            self._ConductorInfo._LineSegments = filtered

        self._ConductorInfo = value
        if self._ConductorInfo is not None:
            if self not in self._ConductorInfo._LineSegments:
                self._ConductorInfo._LineSegments.append(self)

    ConductorInfo = property(getConductorInfo, setConductorInfo)

    def getPhaseImpedance(self):
        """Phase impedance of this line segment; used for unbalanced model.
        """
        return self._PhaseImpedance

    def setPhaseImpedance(self, value):
        if self._PhaseImpedance is not None:
            filtered = [x for x in self.PhaseImpedance.LineSegments if x != self]
            self._PhaseImpedance._LineSegments = filtered

        self._PhaseImpedance = value
        if self._PhaseImpedance is not None:
            if self not in self._PhaseImpedance._LineSegments:
                self._PhaseImpedance._LineSegments.append(self)

    PhaseImpedance = property(getPhaseImpedance, setPhaseImpedance)

