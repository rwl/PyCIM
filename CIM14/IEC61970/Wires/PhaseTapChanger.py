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

from CIM14.IEC61970.Wires.TapChanger import TapChanger

class PhaseTapChanger(TapChanger):
    """A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.
    """

    def __init__(self, phaseTapChangerType="asymmetrical", nominalVoltageOutOfPhase=0.0, xStepMin=0.0, stepPhaseShiftIncrement=0.0, windingConnectionAngle=0.0, xStepMax=0.0, voltageStepIncrementOutOfPhase=0.0, PhaseVariationCurve=None, Winding=None, TransformerWinding=None, *args, **kw_args):
        """Initialises a new 'PhaseTapChanger' instance.

        @param phaseTapChangerType: The type of phase shifter construction. Values are: "asymmetrical", "unknown", "symmetrical"
        @param nominalVoltageOutOfPhase: Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage. 
        @param xStepMin: The reactance at the minimum tap step. 
        @param stepPhaseShiftIncrement: Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accurately computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. 
        @param windingConnectionAngle: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees. 
        @param xStepMax: The reactance at the maximum tap step. 
        @param voltageStepIncrementOutOfPhase: The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding. 
        @param PhaseVariationCurve: A PhaseTapChanger can have an associated PhaseVariationCurve to define phase shift variations with tap step changes.
        @param Winding: Transformer winding to which this phase tap changer belongs.
        @param TransformerWinding: The transformer winding to which the phase tap changer belongs.
        """
        #: The type of phase shifter construction. Values are: "asymmetrical", "unknown", "symmetrical"
        self.phaseTapChangerType = phaseTapChangerType

        #: Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage.
        self.nominalVoltageOutOfPhase = nominalVoltageOutOfPhase

        #: The reactance at the minimum tap step.
        self.xStepMin = xStepMin

        #: Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accurately computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.
        self.stepPhaseShiftIncrement = stepPhaseShiftIncrement

        #: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.
        self.windingConnectionAngle = windingConnectionAngle

        #: The reactance at the maximum tap step.
        self.xStepMax = xStepMax

        #: The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.
        self.voltageStepIncrementOutOfPhase = voltageStepIncrementOutOfPhase

        self._PhaseVariationCurve = None
        self.PhaseVariationCurve = PhaseVariationCurve

        self._Winding = None
        self.Winding = Winding

        self._TransformerWinding = None
        self.TransformerWinding = TransformerWinding

        super(PhaseTapChanger, self).__init__(*args, **kw_args)

    _attrs = ["phaseTapChangerType", "nominalVoltageOutOfPhase", "xStepMin", "stepPhaseShiftIncrement", "windingConnectionAngle", "xStepMax", "voltageStepIncrementOutOfPhase"]
    _attr_types = {"phaseTapChangerType": str, "nominalVoltageOutOfPhase": float, "xStepMin": float, "stepPhaseShiftIncrement": float, "windingConnectionAngle": float, "xStepMax": float, "voltageStepIncrementOutOfPhase": float}
    _defaults = {"phaseTapChangerType": "asymmetrical", "nominalVoltageOutOfPhase": 0.0, "xStepMin": 0.0, "stepPhaseShiftIncrement": 0.0, "windingConnectionAngle": 0.0, "xStepMax": 0.0, "voltageStepIncrementOutOfPhase": 0.0}
    _enums = {"phaseTapChangerType": "PhaseTapChangerKind"}
    _refs = ["PhaseVariationCurve", "Winding", "TransformerWinding"]
    _many_refs = []

    def getPhaseVariationCurve(self):
        """A PhaseTapChanger can have an associated PhaseVariationCurve to define phase shift variations with tap step changes.
        """
        return self._PhaseVariationCurve

    def setPhaseVariationCurve(self, value):
        if self._PhaseVariationCurve is not None:
            self._PhaseVariationCurve._PhaseTapChanger = None

        self._PhaseVariationCurve = value
        if self._PhaseVariationCurve is not None:
            self._PhaseVariationCurve.PhaseTapChanger = None
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
            self._Winding.PhaseTapChanger = None
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
            self._TransformerWinding.PhaseTapChanger = None
            self._TransformerWinding._PhaseTapChanger = self

    TransformerWinding = property(getTransformerWinding, setTransformerWinding)

