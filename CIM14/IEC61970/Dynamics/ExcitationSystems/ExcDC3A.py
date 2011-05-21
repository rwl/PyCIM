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

from CIM14.IEC61970.Dynamics.ExcitationSystems.ExcitationSystem import ExcitationSystem

class ExcDC3A(ExcitationSystem):
    """IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.
    """

    def __init__(self, e1=0.0, vrmax=0.0, te=0.0, ke=0.0, tr=0.0, se2=0.0, trh=0.0, vrmin=0.0, exclim=0.0, e2=0.0, kv=0.0, se1=0.0, *args, **kw_args):
        """Initialises a new 'ExcDC3A' instance.

        @param e1: Field voltage value 1    (&gt; 0.) 
        @param vrmax: Maximum control element output (&gt; 0.) 
        @param te: Exciter field time constant (&gt; 0.) 
        @param ke: Exciter field resistance line slope 
        @param tr: Filter  time constant (&gt;= 0.) 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param trh: Rheostat full range travel time (&gt; 0.) 
        @param vrmin: Minimum control element output (&lt;= 0.) 
        @param exclim: If not 0, apply lower limit of 0. to exciter output 
        @param e2: Field voltage value 2.     (&gt; 0.) 
        @param kv: Voltage error threshold min/max control action (&gt; 0.) 
        @param se1: Saturation factor at e1 (&gt;= 0.) 
        """
        #: Field voltage value 1    (&gt; 0.)
        self.e1 = e1

        #: Maximum control element output (&gt; 0.)
        self.vrmax = vrmax

        #: Exciter field time constant (&gt; 0.)
        self.te = te

        #: Exciter field resistance line slope
        self.ke = ke

        #: Filter  time constant (&gt;= 0.)
        self.tr = tr

        #: Saturation factor at e2  (&gt;= 0.)
        self.se2 = se2

        #: Rheostat full range travel time (&gt; 0.)
        self.trh = trh

        #: Minimum control element output (&lt;= 0.)
        self.vrmin = vrmin

        #: If not 0, apply lower limit of 0. to exciter output
        self.exclim = exclim

        #: Field voltage value 2.     (&gt; 0.)
        self.e2 = e2

        #: Voltage error threshold min/max control action (&gt; 0.)
        self.kv = kv

        #: Saturation factor at e1 (&gt;= 0.)
        self.se1 = se1

        super(ExcDC3A, self).__init__(*args, **kw_args)

    _attrs = ["e1", "vrmax", "te", "ke", "tr", "se2", "trh", "vrmin", "exclim", "e2", "kv", "se1"]
    _attr_types = {"e1": float, "vrmax": float, "te": float, "ke": float, "tr": float, "se2": float, "trh": float, "vrmin": float, "exclim": float, "e2": float, "kv": float, "se1": float}
    _defaults = {"e1": 0.0, "vrmax": 0.0, "te": 0.0, "ke": 0.0, "tr": 0.0, "se2": 0.0, "trh": 0.0, "vrmin": 0.0, "exclim": 0.0, "e2": 0.0, "kv": 0.0, "se1": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

