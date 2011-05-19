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

from CIM15.IEC61970.StateVariables.StateVariable import StateVariable

class SvTapStep(StateVariable):
    """State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """

    def __init__(self, position=0.0, TapChanger=None, *args, **kw_args):
        """Initialises a new 'SvTapStep' instance.

        @param position: The floating point tap position. To get integer value scale with range and round off. 
        @param TapChanger: The tap changer associated with the tap step state.
        """
        #: The floating point tap position. To get integer value scale with range and round off.
        self.position = position

        self._TapChanger = None
        self.TapChanger = TapChanger

        super(SvTapStep, self).__init__(*args, **kw_args)

    _attrs = ["position"]
    _attr_types = {"position": float}
    _defaults = {"position": 0.0}
    _enums = {}
    _refs = ["TapChanger"]
    _many_refs = []

    def getTapChanger(self):
        """The tap changer associated with the tap step state.
        """
        return self._TapChanger

    def setTapChanger(self, value):
        if self._TapChanger is not None:
            self._TapChanger._SvTapStep = None

        self._TapChanger = value
        if self._TapChanger is not None:
            self._TapChanger.SvTapStep = None
            self._TapChanger._SvTapStep = self

    TapChanger = property(getTapChanger, setTapChanger)

