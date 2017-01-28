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

from CIM15.IEC61970.Wires.Conductor import Conductor

class ACLineSegment(Conductor):
    """A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines, it is sufficient to use ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment. If per lenght impedance data is available from a library of standard types, impedances and admittances can be calculated in one of the following ways: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines, it is sufficient to use ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment. If per lenght impedance data is available from a library of standard types, impedances and admittances can be calculated in one of the following ways: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model.
    """

    def __init__(self, g0ch=0.0, r=0.0, x=0.0, gch=0.0, r0=0.0, bch=0.0, b0ch=0.0, x0=0.0, SequenceImpedance=None, ConductorAssets=None, ConductorInfo=None, Cut=None, PhaseImpedance=None, Clamp=None, ACLineSegmentPhases=None, *args, **kw_args):
        """Initialises a new 'ACLineSegment' instance.

        @param g0ch: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param r: Positive sequence series resistance of the entire line section. 
        @param x: Positive sequence series reactance of the entire line section. 
        @param gch: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param r0: Zero sequence series resistance of the entire line section. 
        @param bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
        @param b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param x0: Zero sequence series reactance of the entire line section. 
        @param SequenceImpedance: Sequence impedance of this line segment; used for balanced model.
        @param ConductorAssets:
        @param ConductorInfo: Conductor data for this line segment.
        @param Cut:
        @param PhaseImpedance: Phase impedance of this line segment; used for unbalanced model.
        @param Clamp:
        @param ACLineSegmentPhases: List of ACLineSegmentPhase objects
        """
        #: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.g0ch = g0ch

        #: Positive sequence series resistance of the entire line section.
        self.r = r

        #: Positive sequence series reactance of the entire line section.
        self.x = x

        #: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
        self.gch = gch

        #: Zero sequence series resistance of the entire line section.
        self.r0 = r0

        #: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.
        self.bch = bch

        #: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
        self.b0ch = b0ch

        #: Zero sequence series reactance of the entire line section.
        self.x0 = x0

        self._SequenceImpedance = None
        self.SequenceImpedance = SequenceImpedance

        self._ConductorAssets = []
        self.ConductorAssets = [] if ConductorAssets is None else ConductorAssets

        self._ConductorInfo = None
        self.ConductorInfo = ConductorInfo

        self._Cut = []
        self.Cut = [] if Cut is None else Cut

        self._PhaseImpedance = None
        self.PhaseImpedance = PhaseImpedance

        self._Clamp = []
        self.Clamp = [] if Clamp is None else Clamp

        self._ACLineSegmentPhases = []
        self.ACLineSegmentPhases = [] if ACLineSegmentPhases is None else ACLineSegmentPhases

        super(ACLineSegment, self).__init__(*args, **kw_args)

    _attrs = ["g0ch", "r", "x", "gch", "r0", "bch", "b0ch", "x0"]
    _attr_types = {"g0ch": float, "r": float, "x": float, "gch": float, "r0": float, "bch": float, "b0ch": float, "x0": float}
    _defaults = {"g0ch": 0.0, "r": 0.0, "x": 0.0, "gch": 0.0, "r0": 0.0, "bch": 0.0, "b0ch": 0.0, "x0": 0.0}
    _enums = {}
    _refs = ["SequenceImpedance", "ConductorAssets", "ConductorInfo", "Cut", "PhaseImpedance", "Clamp", "ACLineSegmentPhases"]
    _many_refs = ["ConductorAssets", "Cut", "Clamp", "ACLineSegmentPhases"]

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

    def getConductorAssets(self):
        
        return self._ConductorAssets

    def setConductorAssets(self, value):
        for x in self._ConductorAssets:
            x.ConductorSegment = None
        for y in value:
            y._ConductorSegment = self
        self._ConductorAssets = value

    ConductorAssets = property(getConductorAssets, setConductorAssets)

    def addConductorAssets(self, *ConductorAssets):
        for obj in ConductorAssets:
            obj.ConductorSegment = self

    def removeConductorAssets(self, *ConductorAssets):
        for obj in ConductorAssets:
            obj.ConductorSegment = None

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

    def getCut(self):
        
        return self._Cut

    def setCut(self, value):
        for x in self._Cut:
            x.ACLineSegment = None
        for y in value:
            y._ACLineSegment = self
        self._Cut = value

    Cut = property(getCut, setCut)

    def addCut(self, *Cut):
        for obj in Cut:
            obj.ACLineSegment = self

    def removeCut(self, *Cut):
        for obj in Cut:
            obj.ACLineSegment = None

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

    def getClamp(self):
        
        return self._Clamp

    def setClamp(self, value):
        for x in self._Clamp:
            x.ACLineSegment = None
        for y in value:
            y._ACLineSegment = self
        self._Clamp = value

    Clamp = property(getClamp, setClamp)

    def addClamp(self, *Clamp):
        for obj in Clamp:
            obj.ACLineSegment = self

    def removeClamp(self, *Clamp):
        for obj in Clamp:
            obj.ACLineSegment = None

    def getACLineSegmentPhases(self):
        return self._ACLineSegmentPhases

    def setACLineSegmentPhases(self, value):
        for x in self._ACLineSegmentPhases:
            x.ACLineSegment = None
        for y in value:
            y._ACLineSegment = self
        self._ACLineSegmentPhases = value

    ACLineSegmentPhases = property(getACLineSegmentPhases, setACLineSegmentPhases)

    def addACLineSegmentPhases(self, *ACLineSegmentPhases):
        for obj in ACLineSegmentPhases:
            obj.ACLineSegment = self

    def removeACLineSegmentPhases(self, *ACLineSegmentPhases):
        for obj in ACLineSegmentPhases:
            obj.ACLineSegment = None

