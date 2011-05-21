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

class ExcAC4A(ExcitationSystem):
    """IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.
    """

    def __init__(self, ka=0.0, vimin=0.0, tb=0.0, tr=0.0, tc=0.0, ta=0.0, kc=0.0, vrmin=0.0, vrmax=0.0, vimax=0.0, *args, **kw_args):
        """Initialises a new 'ExcAC4A' instance.

        @param ka: Gain (&gt; 0.) 
        @param vimin: Minimum error signal (&lt; 0.) 
        @param tb: Lag time constant (&gt;= 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param tc: Lead time constant 
        @param ta: Time constant (&gt; 0.) 
        @param kc: Excitation system regulation (&gt;= 0.) 
        @param vrmin: Minimum controller output (&lt; 0.) 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param vimax: Maximum error signal ( &gt; 0.) 
        """
        #: Gain (&gt; 0.)
        self.ka = ka

        #: Minimum error signal (&lt; 0.)
        self.vimin = vimin

        #: Lag time constant (&gt;= 0.)
        self.tb = tb

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Lead time constant
        self.tc = tc

        #: Time constant (&gt; 0.)
        self.ta = ta

        #: Excitation system regulation (&gt;= 0.)
        self.kc = kc

        #: Minimum controller output (&lt; 0.)
        self.vrmin = vrmin

        #: Maximum controller output (&gt; 0.)
        self.vrmax = vrmax

        #: Maximum error signal ( &gt; 0.)
        self.vimax = vimax

        super(ExcAC4A, self).__init__(*args, **kw_args)

    _attrs = ["ka", "vimin", "tb", "tr", "tc", "ta", "kc", "vrmin", "vrmax", "vimax"]
    _attr_types = {"ka": float, "vimin": float, "tb": float, "tr": float, "tc": float, "ta": float, "kc": float, "vrmin": float, "vrmax": float, "vimax": float}
    _defaults = {"ka": 0.0, "vimin": 0.0, "tb": 0.0, "tr": 0.0, "tc": 0.0, "ta": 0.0, "kc": 0.0, "vrmin": 0.0, "vrmax": 0.0, "vimax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

