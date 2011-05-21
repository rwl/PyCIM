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

class ExcAC1A(ExcitationSystem):
    """IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.
    """

    def __init__(self, vrmin=0.0, tr=0.0, vrmax=0.0, ta=0.0, kf=0.0, te=0.0, ka=0.0, vamax=0.0, tb=0.0, e1=0.0, kd=0.0, se1=0.0, vamin=0.0, ke=0.0, kc=0.0, tf=0.0, tc=0.0, e2=0.0, se2=0.0, *args, **kw_args):
        """Initialises a new 'ExcAC1A' instance.

        @param vrmin: Minimum exciter control signal  (&lt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param vrmax: Maximum exciter control signal (&gt; 0.) 
        @param ta: AVR time constant (&gt; 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param ka: AVR gain (&gt; 0.) 
        @param vamax: Maximum AVR output (&gt; 0.) 
        @param tb: TGR lag time constant (&gt;= 0.) 
        @param e1: Field voltage value 1    (&gt; 0.) 
        @param kd: Exciter internal reactance  (&gt;= 0.) 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param vamin: Minimum AVR output (&lt; 0.) 
        @param ke: Exciter field resistance constant 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        @param tc: TGR lead time constant 
        @param e2: Field voltage value 2.   (&gt; 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        """
        #: Minimum exciter control signal  (&lt; 0.)
        self.vrmin = vrmin

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Maximum exciter control signal (&gt; 0.)
        self.vrmax = vrmax

        #: AVR time constant (&gt; 0.)
        self.ta = ta

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Exciter time constant (&gt; 0.)
        self.te = te

        #: AVR gain (&gt; 0.)
        self.ka = ka

        #: Maximum AVR output (&gt; 0.)
        self.vamax = vamax

        #: TGR lag time constant (&gt;= 0.)
        self.tb = tb

        #: Field voltage value 1    (&gt; 0.)
        self.e1 = e1

        #: Exciter internal reactance  (&gt;= 0.)
        self.kd = kd

        #: Saturation factor at e1  (&gt;= 0.)
        self.se1 = se1

        #: Minimum AVR output (&lt; 0.)
        self.vamin = vamin

        #: Exciter field resistance constant
        self.ke = ke

        #: Rectifier regulation factor (&gt;= 0.)
        self.kc = kc

        #: Rate feedback time constant (&gt; 0.)
        self.tf = tf

        #: TGR lead time constant
        self.tc = tc

        #: Field voltage value 2.   (&gt; 0.)
        self.e2 = e2

        #: Saturation factor at e2   (&gt;= 0.)
        self.se2 = se2

        super(ExcAC1A, self).__init__(*args, **kw_args)

    _attrs = ["vrmin", "tr", "vrmax", "ta", "kf", "te", "ka", "vamax", "tb", "e1", "kd", "se1", "vamin", "ke", "kc", "tf", "tc", "e2", "se2"]
    _attr_types = {"vrmin": float, "tr": float, "vrmax": float, "ta": float, "kf": float, "te": float, "ka": float, "vamax": float, "tb": float, "e1": float, "kd": float, "se1": float, "vamin": float, "ke": float, "kc": float, "tf": float, "tc": float, "e2": float, "se2": float}
    _defaults = {"vrmin": 0.0, "tr": 0.0, "vrmax": 0.0, "ta": 0.0, "kf": 0.0, "te": 0.0, "ka": 0.0, "vamax": 0.0, "tb": 0.0, "e1": 0.0, "kd": 0.0, "se1": 0.0, "vamin": 0.0, "ke": 0.0, "kc": 0.0, "tf": 0.0, "tc": 0.0, "e2": 0.0, "se2": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

