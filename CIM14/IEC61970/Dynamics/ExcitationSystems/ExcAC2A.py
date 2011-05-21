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

class ExcAC2A(ExcitationSystem):
    """IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.
    """

    def __init__(self, vrmin=0.0, vamin=0.0, kh=0.0, vrmax=0.0, tb=0.0, e1=0.0, se1=0.0, te=0.0, kf=0.0, tc=0.0, e2=0.0, ke=0.0, tr=0.0, tf=0.0, ta=0.0, kc=0.0, kd=0.0, se2=0.0, vfemax=0.0, vamax=0.0, kb=0.0, ka=0.0, *args, **kw_args):
        """Initialises a new 'ExcAC2A' instance.

        @param vrmin: Minimum exciter control signal (&lt; 0.) 
        @param vamin: Minimum AVR output (&lt; 0.) 
        @param kh: Exciter field current feedback gain (&gt;= 0.) 
        @param vrmax: Maximum exciter control signal (&gt; 0.) 
        @param tb: TGR lag time constant (&gt;= 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param tc: TGR lead time constant 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param ke: Exciter field resistance constant 
        @param tr: Filter time constant (&gt;= 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        @param ta: AVR time constant (&gt; 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param kd: Exciter internal reactance (&gt;= 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        @param vfemax: Exciter field current limit parameter (&gt;= 0.) 
        @param vamax: Maximum AVR output (&gt; 0.) 
        @param kb: Exciter field current controller gain (&gt; 0.) 
        @param ka: AVR gain (&gt; 0.) 
        """
        #: Minimum exciter control signal (&lt; 0.)
        self.vrmin = vrmin

        #: Minimum AVR output (&lt; 0.)
        self.vamin = vamin

        #: Exciter field current feedback gain (&gt;= 0.)
        self.kh = kh

        #: Maximum exciter control signal (&gt; 0.)
        self.vrmax = vrmax

        #: TGR lag time constant (&gt;= 0.)
        self.tb = tb

        #: Field voltage value 1     (&gt; 0.)
        self.e1 = e1

        #: Saturation factor at e1  (&gt;= 0.)
        self.se1 = se1

        #: Exciter time constant (&gt; 0.)
        self.te = te

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: TGR lead time constant
        self.tc = tc

        #: Field voltage value 2.    (&gt; 0.)
        self.e2 = e2

        #: Exciter field resistance constant
        self.ke = ke

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Rate feedback time constant (&gt; 0.)
        self.tf = tf

        #: AVR time constant (&gt; 0.)
        self.ta = ta

        #: Rectifier regulation factor (&gt;= 0.)
        self.kc = kc

        #: Exciter internal reactance (&gt;= 0.)
        self.kd = kd

        #: Saturation factor at e2   (&gt;= 0.)
        self.se2 = se2

        #: Exciter field current limit parameter (&gt;= 0.)
        self.vfemax = vfemax

        #: Maximum AVR output (&gt; 0.)
        self.vamax = vamax

        #: Exciter field current controller gain (&gt; 0.)
        self.kb = kb

        #: AVR gain (&gt; 0.)
        self.ka = ka

        super(ExcAC2A, self).__init__(*args, **kw_args)

    _attrs = ["vrmin", "vamin", "kh", "vrmax", "tb", "e1", "se1", "te", "kf", "tc", "e2", "ke", "tr", "tf", "ta", "kc", "kd", "se2", "vfemax", "vamax", "kb", "ka"]
    _attr_types = {"vrmin": float, "vamin": float, "kh": float, "vrmax": float, "tb": float, "e1": float, "se1": float, "te": float, "kf": float, "tc": float, "e2": float, "ke": float, "tr": float, "tf": float, "ta": float, "kc": float, "kd": float, "se2": float, "vfemax": float, "vamax": float, "kb": float, "ka": float}
    _defaults = {"vrmin": 0.0, "vamin": 0.0, "kh": 0.0, "vrmax": 0.0, "tb": 0.0, "e1": 0.0, "se1": 0.0, "te": 0.0, "kf": 0.0, "tc": 0.0, "e2": 0.0, "ke": 0.0, "tr": 0.0, "tf": 0.0, "ta": 0.0, "kc": 0.0, "kd": 0.0, "se2": 0.0, "vfemax": 0.0, "vamax": 0.0, "kb": 0.0, "ka": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

