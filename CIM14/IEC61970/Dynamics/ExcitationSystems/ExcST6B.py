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

class ExcST6B(ExcitationSystem):
    """IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.
    """

    def __init__(self, tr=0.0, ilr=0.0, vrmin=0.0, vmult=0.0, vrmax=0.0, oelin=0.0, klr=0.0, kg=0.0, kpa=0.0, vamax=0.0, ts=0.0, kcl=0.0, tg=0.0, vamin=0.0, kia=0.0, kff=0.0, km=0.0, *args, **kw_args):
        """Initialises a new 'ExcST6B' instance.

        @param tr: Filter time constant (&gt;= 0.) 
        @param ilr: Field current limiter setpoint (&gt; 0.) 
        @param vrmin: Minimum regulator output (&lt; 0.) 
        @param vmult: If non-zero, multiply regulator output by terminal voltage 
        @param vrmax: Maximum regulator output (&gt; 0.) 
        @param oelin: OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input 
        @param klr: Field current limiter gain (&gt; 0.) 
        @param kg: Feedback gain (&gt;= 0.) 
        @param kpa: Regulator proportional gain (&gt; 0.) 
        @param vamax: PI maximum output. (&gt; 0.) 
        @param ts: Rectifier firing time constant (not in IEEE model) (&gt;= 0.) 
        @param kcl: Field current limiter conversion factor (&gt; 0.) 
        @param tg: Feedback time constant (&gt;= 0.) 
        @param vamin: PI minimum output (&lt; 0.) 
        @param kia: Regulator integral gain (&gt; 0.) 
        @param kff: Feedforward gain 
        @param km: Main gain 
        """
        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Field current limiter setpoint (&gt; 0.)
        self.ilr = ilr

        #: Minimum regulator output (&lt; 0.)
        self.vrmin = vrmin

        #: If non-zero, multiply regulator output by terminal voltage
        self.vmult = vmult

        #: Maximum regulator output (&gt; 0.)
        self.vrmax = vrmax

        #: OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input
        self.oelin = oelin

        #: Field current limiter gain (&gt; 0.)
        self.klr = klr

        #: Feedback gain (&gt;= 0.)
        self.kg = kg

        #: Regulator proportional gain (&gt; 0.)
        self.kpa = kpa

        #: PI maximum output. (&gt; 0.)
        self.vamax = vamax

        #: Rectifier firing time constant (not in IEEE model) (&gt;= 0.)
        self.ts = ts

        #: Field current limiter conversion factor (&gt; 0.)
        self.kcl = kcl

        #: Feedback time constant (&gt;= 0.)
        self.tg = tg

        #: PI minimum output (&lt; 0.)
        self.vamin = vamin

        #: Regulator integral gain (&gt; 0.)
        self.kia = kia

        #: Feedforward gain
        self.kff = kff

        #: Main gain
        self.km = km

        super(ExcST6B, self).__init__(*args, **kw_args)

    _attrs = ["tr", "ilr", "vrmin", "vmult", "vrmax", "oelin", "klr", "kg", "kpa", "vamax", "ts", "kcl", "tg", "vamin", "kia", "kff", "km"]
    _attr_types = {"tr": float, "ilr": float, "vrmin": float, "vmult": float, "vrmax": float, "oelin": float, "klr": float, "kg": float, "kpa": float, "vamax": float, "ts": float, "kcl": float, "tg": float, "vamin": float, "kia": float, "kff": float, "km": float}
    _defaults = {"tr": 0.0, "ilr": 0.0, "vrmin": 0.0, "vmult": 0.0, "vrmax": 0.0, "oelin": 0.0, "klr": 0.0, "kg": 0.0, "kpa": 0.0, "vamax": 0.0, "ts": 0.0, "kcl": 0.0, "tg": 0.0, "vamin": 0.0, "kia": 0.0, "kff": 0.0, "km": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

