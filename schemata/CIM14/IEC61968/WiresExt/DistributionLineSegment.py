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

from CIM14.IEC61970.Wires.ACLineSegment import ACLineSegment

class DistributionLineSegment(ACLineSegment):
    """Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.
    """

    def __init__(self, ConductorInfo=None, PhaseImpedance=None, SequenceImpedance=None, **kw_args):
        """Initializes a new 'DistributionLineSegment' instance.

        @param ConductorInfo: Conductor data of this conductor segment.
        @param PhaseImpedance: Phase impedance of this conductor segment; used for unbalanced model.
        @param SequenceImpedance: Sequence impedance of this conductor segment; used for balanced model.
        """
        self._ConductorInfo = None
        self.ConductorInfo = ConductorInfo

        self._PhaseImpedance = None
        self.PhaseImpedance = PhaseImpedance

        self._SequenceImpedance = None
        self.SequenceImpedance = SequenceImpedance

        super(DistributionLineSegment, self).__init__(**kw_args)

    def getConductorInfo(self):
        """Conductor data of this conductor segment.
        """
        return self._ConductorInfo

    def setConductorInfo(self, value):
        if self._ConductorInfo is not None:
            filtered = [x for x in self.ConductorInfo.ConductorSegments if x != self]
            self._ConductorInfo._ConductorSegments = filtered

        self._ConductorInfo = value
        if self._ConductorInfo is not None:
            self._ConductorInfo._ConductorSegments.append(self)

    ConductorInfo = property(getConductorInfo, setConductorInfo)

    def getPhaseImpedance(self):
        """Phase impedance of this conductor segment; used for unbalanced model.
        """
        return self._PhaseImpedance

    def setPhaseImpedance(self, value):
        if self._PhaseImpedance is not None:
            filtered = [x for x in self.PhaseImpedance.ConductorSegments if x != self]
            self._PhaseImpedance._ConductorSegments = filtered

        self._PhaseImpedance = value
        if self._PhaseImpedance is not None:
            self._PhaseImpedance._ConductorSegments.append(self)

    PhaseImpedance = property(getPhaseImpedance, setPhaseImpedance)

    def getSequenceImpedance(self):
        """Sequence impedance of this conductor segment; used for balanced model.
        """
        return self._SequenceImpedance

    def setSequenceImpedance(self, value):
        if self._SequenceImpedance is not None:
            filtered = [x for x in self.SequenceImpedance.ConductorSegments if x != self]
            self._SequenceImpedance._ConductorSegments = filtered

        self._SequenceImpedance = value
        if self._SequenceImpedance is not None:
            self._SequenceImpedance._ConductorSegments.append(self)

    SequenceImpedance = property(getSequenceImpedance, setSequenceImpedance)

