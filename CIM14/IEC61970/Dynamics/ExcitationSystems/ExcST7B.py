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

class ExcST7B(ExcitationSystem):
    """IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).
    """

    def __init__(self, oelin=0.0, vmax=0.0, tb=0.0, kia=0.0, kpa=0.0, kh=0.0, vrmin=0.0, ts=0.0, tia=0.0, tg=0.0, tr=0.0, tf=0.0, vrmax=0.0, uelin=0.0, kl=0.0, vmin=0.0, tc=0.0, *args, **kw_args):
        """Initialises a new 'ExcST7B' instance.

        @param oelin: OEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL input 
        @param vmax: Maximum voltage reference signal (&gt; 0.) 
        @param tb: Lead-lag denominator time constant (&gt;= 0.) 
        @param kia: Feedback gain (&gt;= 0.) 
        @param kpa: Regulator proportional gain (&gt; 0.) 
        @param kh: High-value gate feedback gain (&gt;= 0.) 
        @param vrmin: Minimum field voltage output (&lt; 0.) 
        @param ts: Rectifier firing time constant (&gt;= 0.) (not in IEEE model) 
        @param tia: Feedback time constant (&gt;= 0.) 
        @param tg: Input lead-lag numerator time constant (&gt;= 0.) 
        @param tr: Filter time constant 
        @param tf: Input lead-lag denominator time constant (&gt;= 0.) 
        @param vrmax: Maximum field voltage output (&gt; 0.) 
        @param uelin: UEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL input 
        @param kl: Low-value gate feedback gain (&gt;= 0.) 
        @param vmin: Minimum voltage reference signal (&gt; 0.) 
        @param tc: Lead-lag numerator time constant (&gt;= 0.) 
        """
        #: OEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL input
        self.oelin = oelin

        #: Maximum voltage reference signal (&gt; 0.)
        self.vmax = vmax

        #: Lead-lag denominator time constant (&gt;= 0.)
        self.tb = tb

        #: Feedback gain (&gt;= 0.)
        self.kia = kia

        #: Regulator proportional gain (&gt; 0.)
        self.kpa = kpa

        #: High-value gate feedback gain (&gt;= 0.)
        self.kh = kh

        #: Minimum field voltage output (&lt; 0.)
        self.vrmin = vrmin

        #: Rectifier firing time constant (&gt;= 0.) (not in IEEE model)
        self.ts = ts

        #: Feedback time constant (&gt;= 0.)
        self.tia = tia

        #: Input lead-lag numerator time constant (&gt;= 0.)
        self.tg = tg

        #: Filter time constant
        self.tr = tr

        #: Input lead-lag denominator time constant (&gt;= 0.)
        self.tf = tf

        #: Maximum field voltage output (&gt; 0.)
        self.vrmax = vrmax

        #: UEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL input
        self.uelin = uelin

        #: Low-value gate feedback gain (&gt;= 0.)
        self.kl = kl

        #: Minimum voltage reference signal (&gt; 0.)
        self.vmin = vmin

        #: Lead-lag numerator time constant (&gt;= 0.)
        self.tc = tc

        super(ExcST7B, self).__init__(*args, **kw_args)

    _attrs = ["oelin", "vmax", "tb", "kia", "kpa", "kh", "vrmin", "ts", "tia", "tg", "tr", "tf", "vrmax", "uelin", "kl", "vmin", "tc"]
    _attr_types = {"oelin": float, "vmax": float, "tb": float, "kia": float, "kpa": float, "kh": float, "vrmin": float, "ts": float, "tia": float, "tg": float, "tr": float, "tf": float, "vrmax": float, "uelin": float, "kl": float, "vmin": float, "tc": float}
    _defaults = {"oelin": 0.0, "vmax": 0.0, "tb": 0.0, "kia": 0.0, "kpa": 0.0, "kh": 0.0, "vrmin": 0.0, "ts": 0.0, "tia": 0.0, "tg": 0.0, "tr": 0.0, "tf": 0.0, "vrmax": 0.0, "uelin": 0.0, "kl": 0.0, "vmin": 0.0, "tc": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

