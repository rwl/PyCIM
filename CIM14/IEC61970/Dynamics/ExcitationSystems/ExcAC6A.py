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

class ExcAC6A(ExcitationSystem):
    """IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update.
    """

    def __init__(self, te=0.0, ka=0.0, vhmax=0.0, kh=0.0, tk=0.0, ke=0.0, se1=0.0, tr=0.0, vrmin=0.0, vrmax=0.0, tc=0.0, e2=0.0, tj=0.0, kc=0.0, vfelim=0.0, ta=0.0, th=0.0, kd=0.0, vamax=0.0, tb=0.0, e1=0.0, vamin=0.0, se2=0.0, *args, **kw_args):
        """Initialises a new 'ExcAC6A' instance.

        @param te: Exciter time constant (&gt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param vhmax: Maximum field current limiter signal (&gt; 0.) 
        @param kh: Exciter field current limiter gain (&gt;= 0.) 
        @param tk: Lag time constant (&gt;= 0.) 
        @param ke: Exciter field resistance constant 
        @param se1: Saturation factor at e1 (&gt;= 0.) 
        @param tr: Filter time constant 
        @param vrmin: Minimum exciter control signal (&lt; 0.) 
        @param vrmax: Maximum exciter control signal (&gt; 0.) 
        @param tc: Lead time constant 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param tj: Field current limiter time constant (&gt;= 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param vfelim: Exciter field current limit reference (&gt; 0.) 
        @param ta: Time constant (&gt;= 0.) 
        @param th: Field current limiter time constant (&gt; 0.) 
        @param kd: Exciter internal reactance (&gt;= 0.) 
        @param vamax: Maximum controller element output (&gt; 0.) 
        @param tb: Time constant (&gt;= 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param vamin: Minimum controller element output (&lt; 0.) 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        """
        #: Exciter time constant (&gt; 0.)
        self.te = te

        #: Gain (&gt; 0.)
        self.ka = ka

        #: Maximum field current limiter signal (&gt; 0.)
        self.vhmax = vhmax

        #: Exciter field current limiter gain (&gt;= 0.)
        self.kh = kh

        #: Lag time constant (&gt;= 0.)
        self.tk = tk

        #: Exciter field resistance constant
        self.ke = ke

        #: Saturation factor at e1 (&gt;= 0.)
        self.se1 = se1

        #: Filter time constant
        self.tr = tr

        #: Minimum exciter control signal (&lt; 0.)
        self.vrmin = vrmin

        #: Maximum exciter control signal (&gt; 0.)
        self.vrmax = vrmax

        #: Lead time constant
        self.tc = tc

        #: Field voltage value 2.    (&gt; 0.)
        self.e2 = e2

        #: Field current limiter time constant (&gt;= 0.)
        self.tj = tj

        #: Rectifier regulation factor (&gt;= 0.)
        self.kc = kc

        #: Exciter field current limit reference (&gt; 0.)
        self.vfelim = vfelim

        #: Time constant (&gt;= 0.)
        self.ta = ta

        #: Field current limiter time constant (&gt; 0.)
        self.th = th

        #: Exciter internal reactance (&gt;= 0.)
        self.kd = kd

        #: Maximum controller element output (&gt; 0.)
        self.vamax = vamax

        #: Time constant (&gt;= 0.)
        self.tb = tb

        #: Field voltage value 1     (&gt; 0.)
        self.e1 = e1

        #: Minimum controller element output (&lt; 0.)
        self.vamin = vamin

        #: Saturation factor at e2  (&gt;= 0.)
        self.se2 = se2

        super(ExcAC6A, self).__init__(*args, **kw_args)

    _attrs = ["te", "ka", "vhmax", "kh", "tk", "ke", "se1", "tr", "vrmin", "vrmax", "tc", "e2", "tj", "kc", "vfelim", "ta", "th", "kd", "vamax", "tb", "e1", "vamin", "se2"]
    _attr_types = {"te": float, "ka": float, "vhmax": float, "kh": float, "tk": float, "ke": float, "se1": float, "tr": float, "vrmin": float, "vrmax": float, "tc": float, "e2": float, "tj": float, "kc": float, "vfelim": float, "ta": float, "th": float, "kd": float, "vamax": float, "tb": float, "e1": float, "vamin": float, "se2": float}
    _defaults = {"te": 0.0, "ka": 0.0, "vhmax": 0.0, "kh": 0.0, "tk": 0.0, "ke": 0.0, "se1": 0.0, "tr": 0.0, "vrmin": 0.0, "vrmax": 0.0, "tc": 0.0, "e2": 0.0, "tj": 0.0, "kc": 0.0, "vfelim": 0.0, "ta": 0.0, "th": 0.0, "kd": 0.0, "vamax": 0.0, "tb": 0.0, "e1": 0.0, "vamin": 0.0, "se2": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

