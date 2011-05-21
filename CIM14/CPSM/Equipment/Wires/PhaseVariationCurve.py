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

from CIM14.CPSM.Equipment.Core.Curve import Curve

class PhaseVariationCurve(Curve):
    """A Phase Variation Curve describes the phase shift in relationship to tap step changes.  The tap step is represented using the xValue and the phase shift using y1value.Unit Symbol for this is Percent
    """

    def __init__(self, PhaseTapChanger=None, *args, **kw_args):
        """Initialises a new 'PhaseVariationCurve' instance.

        @param PhaseTapChanger: A PhaseVariationCurve defines phase shift changes for a PhaseTapChanger.
        """
        self._PhaseTapChanger = None
        self.PhaseTapChanger = PhaseTapChanger

        super(PhaseVariationCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PhaseTapChanger"]
    _many_refs = []

    def getPhaseTapChanger(self):
        """A PhaseVariationCurve defines phase shift changes for a PhaseTapChanger.
        """
        return self._PhaseTapChanger

    def setPhaseTapChanger(self, value):
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger._PhaseVariationCurve = None

        self._PhaseTapChanger = value
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger.PhaseVariationCurve = None
            self._PhaseTapChanger._PhaseVariationCurve = self

    PhaseTapChanger = property(getPhaseTapChanger, setPhaseTapChanger)

