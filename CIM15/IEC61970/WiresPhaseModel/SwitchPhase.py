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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class SwitchPhase(PowerSystemResource):
    """Single phase of a multi-phase switch when its attributes might be different per phase.Single phase of a multi-phase switch when its attributes might be different per phase.
    """

    def __init__(self, phaseSide1="C", phaseSide2="C", normalOpen=False, Switch=None, *args, **kw_args):
        """Initialises a new 'SwitchPhase' instance.

        @param phaseSide1: Phase of this SwitchPhase on the &ldquo;from&rdquo; (Switch.Terminal.sequenceNumber=1) side. Should be a phase contained in that terminal&rsquo;s Terminal.phases attribute. Values are: "C", "N", "s1", "B", "s2", "A"
        @param phaseSide2: Phase of this SwitchPhase on the &ldquo;to&rdquo; (Switch.Terminal.sequenceNumber=2) side.  Should be a phase contained in that terminal&rsquo;s Terminal.phases attribute. Values are: "C", "N", "s1", "B", "s2", "A"
        @param normalOpen: Used in cases when no Measurement for the status value is present. If the SwitchPhase has a status measurement the Discrete.normalValue is expected to match with this value. 
        @param Switch:
        """
        #: Phase of this SwitchPhase on the &ldquo;from&rdquo; (Switch.Terminal.sequenceNumber=1) side. Should be a phase contained in that terminal&rsquo;s Terminal.phases attribute. Values are: "C", "N", "s1", "B", "s2", "A"
        self.phaseSide1 = phaseSide1

        #: Phase of this SwitchPhase on the &ldquo;to&rdquo; (Switch.Terminal.sequenceNumber=2) side.  Should be a phase contained in that terminal&rsquo;s Terminal.phases attribute. Values are: "C", "N", "s1", "B", "s2", "A"
        self.phaseSide2 = phaseSide2

        #: Used in cases when no Measurement for the status value is present. If the SwitchPhase has a status measurement the Discrete.normalValue is expected to match with this value.
        self.normalOpen = normalOpen

        self._Switch = None
        self.Switch = Switch

        super(SwitchPhase, self).__init__(*args, **kw_args)

    _attrs = ["phaseSide1", "phaseSide2", "normalOpen"]
    _attr_types = {"phaseSide1": str, "phaseSide2": str, "normalOpen": bool}
    _defaults = {"phaseSide1": "C", "phaseSide2": "C", "normalOpen": False}
    _enums = {"phaseSide1": "SinglePhaseKind", "phaseSide2": "SinglePhaseKind"}
    _refs = ["Switch"]
    _many_refs = []

    def getSwitch(self):
        
        return self._Switch

    def setSwitch(self, value):
        if self._Switch is not None:
            filtered = [x for x in self.Switch.SwitchPhases if x != self]
            self._Switch._SwitchPhases = filtered

        self._Switch = value
        if self._Switch is not None:
            if self not in self._Switch._SwitchPhases:
                self._Switch._SwitchPhases.append(self)

    Switch = property(getSwitch, setSwitch)

