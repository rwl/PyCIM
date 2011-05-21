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

class ExcST2A(ExcitationSystem):
    """IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.
    """

    def __init__(self, te=0.0, ka=0.0, tb=0.0, tf=0.0, kf=0.0, ke=0.0, tr=0.0, tc=0.0, ta=0.0, kc=0.0, ki=0.0, kp=0.0, uelin=0.0, vrmax=0.0, efdmax=0.0, vrmin=0.0, *args, **kw_args):
        """Initialises a new 'ExcST2A' instance.

        @param te: Transformer saturation control time constant (&gt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param tb: Time constant (&gt;=0.) 
        @param tf: Rate feedback time constant (&gt;= 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param ke: Time constant feedback 
        @param tr: Filter time constant (&gt;= 0.) 
        @param tc: Time constant 
        @param ta: Time constant (&gt; 0.) 
        @param kc: Rectifier loading factor (&gt;= 0.) 
        @param ki: Current source gain (&gt;= 0.) 
        @param kp: Potential source gain (&gt;= 0.) 
        @param uelin: UEL input: if = 1, HV gate; if = 2, add to error signal 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param efdmax: Maximum field voltage (&gt;=0.) 
        @param vrmin: Minimum controller output (&lt; 0.) 
        """
        #: Transformer saturation control time constant (&gt; 0.)
        self.te = te

        #: Gain (&gt; 0.)
        self.ka = ka

        #: Time constant (&gt;=0.)
        self.tb = tb

        #: Rate feedback time constant (&gt;= 0.)
        self.tf = tf

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Time constant feedback
        self.ke = ke

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Time constant
        self.tc = tc

        #: Time constant (&gt; 0.)
        self.ta = ta

        #: Rectifier loading factor (&gt;= 0.)
        self.kc = kc

        #: Current source gain (&gt;= 0.)
        self.ki = ki

        #: Potential source gain (&gt;= 0.)
        self.kp = kp

        #: UEL input: if = 1, HV gate; if = 2, add to error signal
        self.uelin = uelin

        #: Maximum controller output (&gt; 0.)
        self.vrmax = vrmax

        #: Maximum field voltage (&gt;=0.)
        self.efdmax = efdmax

        #: Minimum controller output (&lt; 0.)
        self.vrmin = vrmin

        super(ExcST2A, self).__init__(*args, **kw_args)

    _attrs = ["te", "ka", "tb", "tf", "kf", "ke", "tr", "tc", "ta", "kc", "ki", "kp", "uelin", "vrmax", "efdmax", "vrmin"]
    _attr_types = {"te": float, "ka": float, "tb": float, "tf": float, "kf": float, "ke": float, "tr": float, "tc": float, "ta": float, "kc": float, "ki": float, "kp": float, "uelin": float, "vrmax": float, "efdmax": float, "vrmin": float}
    _defaults = {"te": 0.0, "ka": 0.0, "tb": 0.0, "tf": 0.0, "kf": 0.0, "ke": 0.0, "tr": 0.0, "tc": 0.0, "ta": 0.0, "kc": 0.0, "ki": 0.0, "kp": 0.0, "uelin": 0.0, "vrmax": 0.0, "efdmax": 0.0, "vrmin": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

