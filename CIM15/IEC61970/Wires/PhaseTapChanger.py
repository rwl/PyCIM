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

from CIM15.IEC61970.Wires.TapChanger import TapChanger

class PhaseTapChanger(TapChanger):
    """A PhaseTapChanger controls the phase angle difference across the power transformer and hence the activer power flow through it. A PhaseTapChanger may also impact the voltage magnitude.A PhaseTapChanger controls the phase angle difference across the power transformer and hence the activer power flow through it. A PhaseTapChanger may also impact the voltage magnitude.
    """

    def __init__(self, PhaseTapChangerTabular=None, TransformerEnd=None, *args, **kw_args):
        """Initialises a new 'PhaseTapChanger' instance.

        @param PhaseTapChangerTabular:
        @param TransformerEnd: Transformer end to which this phase tap changer belongs.
        """
        self._PhaseTapChangerTabular = None
        self.PhaseTapChangerTabular = PhaseTapChangerTabular

        self._TransformerEnd = None
        self.TransformerEnd = TransformerEnd

        super(PhaseTapChanger, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PhaseTapChangerTabular", "TransformerEnd"]
    _many_refs = []

    def getPhaseTapChangerTabular(self):
        
        return self._PhaseTapChangerTabular

    def setPhaseTapChangerTabular(self, value):
        if self._PhaseTapChangerTabular is not None:
            filtered = [x for x in self.PhaseTapChangerTabular.PhaseTapChanger if x != self]
            self._PhaseTapChangerTabular._PhaseTapChanger = filtered

        self._PhaseTapChangerTabular = value
        if self._PhaseTapChangerTabular is not None:
            if self not in self._PhaseTapChangerTabular._PhaseTapChanger:
                self._PhaseTapChangerTabular._PhaseTapChanger.append(self)

    PhaseTapChangerTabular = property(getPhaseTapChangerTabular, setPhaseTapChangerTabular)

    def getTransformerEnd(self):
        """Transformer end to which this phase tap changer belongs.
        """
        return self._TransformerEnd

    def setTransformerEnd(self, value):
        if self._TransformerEnd is not None:
            self._TransformerEnd._PhaseTapChanger = None

        self._TransformerEnd = value
        if self._TransformerEnd is not None:
            self._TransformerEnd.PhaseTapChanger = None
            self._TransformerEnd._PhaseTapChanger = self

    TransformerEnd = property(getTransformerEnd, setTransformerEnd)

