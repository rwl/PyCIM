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

class ExcAC3A(ExcitationSystem):
    """IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators.
    """

    def __init__(self, kf=0.0, e2=0.0, te=0.0, ka=0.0, kr=0.0, tc=0.0, efdn=0.0, ke=0.0, e1=0.0, kd=0.0, se2=0.0, vamax=0.0, tr=0.0, vamin=0.0, tf=0.0, vemin=0.0, kn=0.0, vfemax=0.0, tb=0.0, se1=0.0, kc=0.0, ta=0.0, *args, **kw_args):
        """Initialises a new 'ExcAC3A' instance.

        @param kf: Low level rate feedback gain (&gt;= 0.) 
        @param e2: Field voltage value 2.     (&gt; 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param ka: AVR gain (&gt; 0.) 
        @param kr: Field self-excitation feedback gain (&gt; 0.) 
        @param tc: TGR lead time constant 
        @param efdn: Rate feedback gain break level (&gt; 0.) 
        @param ke: Exciter field resistance constant 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param kd: Exciter internal reactance (&gt;= 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        @param vamax: Maximum AVR output (&gt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param vamin: Minimum AVR output (&lt; 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        @param vemin: Minimum field voltage limit (&lt;= 0.) 
        @param kn: High level rate feedback gain (&gt;= 0.) 
        @param vfemax: Exciter field current limit parameter (&gt;= 0.) 
        @param tb: TGR lag time constant (&gt;= 0.) 
        @param se1: Saturation factor at e1   (&gt;= 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param ta: AVR time constant (&gt; 0.) 
        """
        #: Low level rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Field voltage value 2.     (&gt; 0.)
        self.e2 = e2

        #: Exciter time constant (&gt; 0.)
        self.te = te

        #: AVR gain (&gt; 0.)
        self.ka = ka

        #: Field self-excitation feedback gain (&gt; 0.)
        self.kr = kr

        #: TGR lead time constant
        self.tc = tc

        #: Rate feedback gain break level (&gt; 0.)
        self.efdn = efdn

        #: Exciter field resistance constant
        self.ke = ke

        #: Field voltage value 1     (&gt; 0.)
        self.e1 = e1

        #: Exciter internal reactance (&gt;= 0.)
        self.kd = kd

        #: Saturation factor at e2   (&gt;= 0.)
        self.se2 = se2

        #: Maximum AVR output (&gt; 0.)
        self.vamax = vamax

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Minimum AVR output (&lt; 0.)
        self.vamin = vamin

        #: Rate feedback time constant (&gt; 0.)
        self.tf = tf

        #: Minimum field voltage limit (&lt;= 0.)
        self.vemin = vemin

        #: High level rate feedback gain (&gt;= 0.)
        self.kn = kn

        #: Exciter field current limit parameter (&gt;= 0.)
        self.vfemax = vfemax

        #: TGR lag time constant (&gt;= 0.)
        self.tb = tb

        #: Saturation factor at e1   (&gt;= 0.)
        self.se1 = se1

        #: Rectifier regulation factor (&gt;= 0.)
        self.kc = kc

        #: AVR time constant (&gt; 0.)
        self.ta = ta

        super(ExcAC3A, self).__init__(*args, **kw_args)

    _attrs = ["kf", "e2", "te", "ka", "kr", "tc", "efdn", "ke", "e1", "kd", "se2", "vamax", "tr", "vamin", "tf", "vemin", "kn", "vfemax", "tb", "se1", "kc", "ta"]
    _attr_types = {"kf": float, "e2": float, "te": float, "ka": float, "kr": float, "tc": float, "efdn": float, "ke": float, "e1": float, "kd": float, "se2": float, "vamax": float, "tr": float, "vamin": float, "tf": float, "vemin": float, "kn": float, "vfemax": float, "tb": float, "se1": float, "kc": float, "ta": float}
    _defaults = {"kf": 0.0, "e2": 0.0, "te": 0.0, "ka": 0.0, "kr": 0.0, "tc": 0.0, "efdn": 0.0, "ke": 0.0, "e1": 0.0, "kd": 0.0, "se2": 0.0, "vamax": 0.0, "tr": 0.0, "vamin": 0.0, "tf": 0.0, "vemin": 0.0, "kn": 0.0, "vfemax": 0.0, "tb": 0.0, "se1": 0.0, "kc": 0.0, "ta": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

