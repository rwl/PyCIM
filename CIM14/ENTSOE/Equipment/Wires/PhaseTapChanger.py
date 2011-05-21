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

from CIM14.ENTSOE.Equipment.Wires.TapChanger import TapChanger

class PhaseTapChanger(TapChanger):
    """A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.-  The attribute ltcflag specifies whether or not a TapChanger has load tap changing capabilities.  If the ltcFlag is true, the attributes “highStep”, “lowStep”, “neutralStep”, “normalStep” and 'stepPhaseShiftIncrement' are all required. -  The attributes voltageStepIncrementOutOfPhase, windingConnectionAngle, xStepMax, and xStepMin are not required.
    """

    def __init__(self, nominalVoltageOutOfPhase=0.0, windingConnectionAngle=0.0, phaseTapChangerType="asymmetrical", xStepMin=0.0, xStepMax=0.0, stepPhaseShiftIncrement=0.0, voltageStepIncrementOutOfPhase=0.0, TransformerWinding=None, *args, **kw_args):
        """Initialises a new 'PhaseTapChanger' instance.

        @param nominalVoltageOutOfPhase: Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage. 
        @param windingConnectionAngle: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees. 
        @param phaseTapChangerType: The type of phase shifter construction. Values are: "asymmetrical", "symmetrical", "unknown"
        @param xStepMin: The reactance at the minimum tap step. 
        @param xStepMax: The reactance at the maximum tap step. 
        @param stepPhaseShiftIncrement: Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accurately computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. 
        @param voltageStepIncrementOutOfPhase: The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding. 
        @param TransformerWinding: The transformer winding to which the phase tap changer belongs.
        """
        #: Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage.
        self.nominalVoltageOutOfPhase = nominalVoltageOutOfPhase

        #: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.
        self.windingConnectionAngle = windingConnectionAngle

        #: The type of phase shifter construction. Values are: "asymmetrical", "symmetrical", "unknown"
        self.phaseTapChangerType = phaseTapChangerType

        #: The reactance at the minimum tap step.
        self.xStepMin = xStepMin

        #: The reactance at the maximum tap step.
        self.xStepMax = xStepMax

        #: Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accurately computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.
        self.stepPhaseShiftIncrement = stepPhaseShiftIncrement

        #: The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.
        self.voltageStepIncrementOutOfPhase = voltageStepIncrementOutOfPhase

        self._TransformerWinding = None
        self.TransformerWinding = TransformerWinding

        super(PhaseTapChanger, self).__init__(*args, **kw_args)

    _attrs = ["nominalVoltageOutOfPhase", "windingConnectionAngle", "phaseTapChangerType", "xStepMin", "xStepMax", "stepPhaseShiftIncrement", "voltageStepIncrementOutOfPhase"]
    _attr_types = {"nominalVoltageOutOfPhase": float, "windingConnectionAngle": float, "phaseTapChangerType": str, "xStepMin": float, "xStepMax": float, "stepPhaseShiftIncrement": float, "voltageStepIncrementOutOfPhase": float}
    _defaults = {"nominalVoltageOutOfPhase": 0.0, "windingConnectionAngle": 0.0, "phaseTapChangerType": "asymmetrical", "xStepMin": 0.0, "xStepMax": 0.0, "stepPhaseShiftIncrement": 0.0, "voltageStepIncrementOutOfPhase": 0.0}
    _enums = {"phaseTapChangerType": "PhaseTapChangerKind"}
    _refs = ["TransformerWinding"]
    _many_refs = []

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

