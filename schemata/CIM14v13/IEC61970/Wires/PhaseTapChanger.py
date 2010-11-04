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

from CIM14v13.IEC61970.Wires.TapChanger import TapChanger

class PhaseTapChanger(TapChanger):
    """A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.
    """

    def __init__(self, phaseTapChangerType='symmetrical', windingConnectionAngle=0.0, stepPhaseShiftIncrement=0.0, xStepMax=0.0, xStepMin=0.0, voltageStepIncrementOutOfPhase=0.0, nominalVoltageOutOfPhase=0.0, PhaseVariationCurve=None, Winding=None, TransformerWinding=None, *args, **kw_args):
        """Initializes a new 'PhaseTapChanger' instance.

        @param phaseTapChangerType: The type of phase shifter construction. Values are: "symmetrical", "unknown", "asymmetrical"
        @param windingConnectionAngle: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees. 
        @param stepPhaseShiftIncrement: Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accurately computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. 
        @param xStepMax: The reactance at the maximum tap step. 
        @param xStepMin: The reactance at the minimum tap step. 
        @param voltageStepIncrementOutOfPhase: The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding. 
        @param nominalVoltageOutOfPhase: Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage. 
        @param PhaseVariationCurve: A PhaseTapChanger can have an associated PhaseVariationCurve to define phase shift variations with tap step changes.
        @param Winding: Transformer winding to which this phase tap changer belongs.
        @param TransformerWinding: The transformer winding to which the phase tap changer belongs.
        """
        #: The type of phase shifter construction.Values are: "symmetrical", "unknown", "asymmetrical"
        self.phaseTapChangerType = phaseTapChangerType

        #: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.
        self.windingConnectionAngle = windingConnectionAngle

        #: Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accurately computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.
        self.stepPhaseShiftIncrement = stepPhaseShiftIncrement

        #: The reactance at the maximum tap step.
        self.xStepMax = xStepMax

        #: The reactance at the minimum tap step.
        self.xStepMin = xStepMin

        #: The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.
        self.voltageStepIncrementOutOfPhase = voltageStepIncrementOutOfPhase

        #: Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage.
        self.nominalVoltageOutOfPhase = nominalVoltageOutOfPhase

        self._PhaseVariationCurve = None
        self.PhaseVariationCurve = PhaseVariationCurve

        self._Winding = None
        self.Winding = Winding

        self._TransformerWinding = None
        self.TransformerWinding = TransformerWinding

        super(PhaseTapChanger, self).__init__(*args, **kw_args)

    def getPhaseVariationCurve(self):
        """A PhaseTapChanger can have an associated PhaseVariationCurve to define phase shift variations with tap step changes.
        """
        return self._PhaseVariationCurve

    def setPhaseVariationCurve(self, value):
        if self._PhaseVariationCurve is not None:
            self._PhaseVariationCurve._PhaseTapChanger = None

        self._PhaseVariationCurve = value
        if self._PhaseVariationCurve is not None:
            self._PhaseVariationCurve._PhaseTapChanger = self

    PhaseVariationCurve = property(getPhaseVariationCurve, setPhaseVariationCurve)

    def getWinding(self):
        """Transformer winding to which this phase tap changer belongs.
        """
        return self._Winding

    def setWinding(self, value):
        if self._Winding is not None:
            self._Winding._PhaseTapChanger = None

        self._Winding = value
        if self._Winding is not None:
            self._Winding._PhaseTapChanger = self

    Winding = property(getWinding, setWinding)

    def getTransformerWinding(self):
        """The transformer winding to which the phase tap changer belongs.
        """
        return self._TransformerWinding

    def setTransformerWinding(self, value):
        if self._TransformerWinding is not None:
            self._TransformerWinding._PhaseTapChanger = None

        self._TransformerWinding = value
        if self._TransformerWinding is not None:
            self._TransformerWinding._PhaseTapChanger = self

    TransformerWinding = property(getTransformerWinding, setTransformerWinding)

