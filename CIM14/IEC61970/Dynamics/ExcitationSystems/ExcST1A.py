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

class ExcST1A(ExcitationSystem):
    """IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.
    """

    def __init__(self, ta=0.0, vimin=0.0, vamin=0.0, kf=0.0, vrmin=0.0, ka=0.0, tb=0.0, vamax=0.0, tb1=0.0, uelin=0.0, kc=0.0, tc1=0.0, tf=0.0, klr=0.0, vimax=0.0, tc=0.0, pssin=0.0, vrmax=0.0, tr=0.0, ilr=0.0, *args, **kw_args):
        """Initialises a new 'ExcST1A' instance.

        @param ta: Time constant (&gt;= 0.) 
        @param vimin: Minimum error (&lt; 0.) 
        @param vamin: Minimum control element output (&lt; 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param vrmin: Excitation voltage lower limit (&lt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param tb: Lag time constant (&gt;= 0.) 
        @param vamax: Maximum control element output (&gt; 0.) 
        @param tb1: Lag time constant (&gt;= 0.) 
        @param uelin: = 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal 
        @param kc: Excitation system regulation factor (&gt;= 0.) 
        @param tc1: Lead time constant 
        @param tf: Rate feedback time constant (&gt;= 0.) 
        @param klr: Gain on field current limit 
        @param vimax: Maximum error (&gt; 0.) 
        @param tc: Lead time constant 
        @param pssin: = 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output 
        @param vrmax: Excitation voltage upper limit (&gt; 0.) 
        @param tr: Voltage transducer time constant (&gt;= 0.) 
        @param ilr: Maximum field current 
        """
        #: Time constant (&gt;= 0.)
        self.ta = ta

        #: Minimum error (&lt; 0.)
        self.vimin = vimin

        #: Minimum control element output (&lt; 0.)
        self.vamin = vamin

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Excitation voltage lower limit (&lt; 0.)
        self.vrmin = vrmin

        #: Gain (&gt; 0.)
        self.ka = ka

        #: Lag time constant (&gt;= 0.)
        self.tb = tb

        #: Maximum control element output (&gt; 0.)
        self.vamax = vamax

        #: Lag time constant (&gt;= 0.)
        self.tb1 = tb1

        #: = 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal
        self.uelin = uelin

        #: Excitation system regulation factor (&gt;= 0.)
        self.kc = kc

        #: Lead time constant
        self.tc1 = tc1

        #: Rate feedback time constant (&gt;= 0.)
        self.tf = tf

        #: Gain on field current limit
        self.klr = klr

        #: Maximum error (&gt; 0.)
        self.vimax = vimax

        #: Lead time constant
        self.tc = tc

        #: = 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output
        self.pssin = pssin

        #: Excitation voltage upper limit (&gt; 0.)
        self.vrmax = vrmax

        #: Voltage transducer time constant (&gt;= 0.)
        self.tr = tr

        #: Maximum field current
        self.ilr = ilr

        super(ExcST1A, self).__init__(*args, **kw_args)

    _attrs = ["ta", "vimin", "vamin", "kf", "vrmin", "ka", "tb", "vamax", "tb1", "uelin", "kc", "tc1", "tf", "klr", "vimax", "tc", "pssin", "vrmax", "tr", "ilr"]
    _attr_types = {"ta": float, "vimin": float, "vamin": float, "kf": float, "vrmin": float, "ka": float, "tb": float, "vamax": float, "tb1": float, "uelin": float, "kc": float, "tc1": float, "tf": float, "klr": float, "vimax": float, "tc": float, "pssin": float, "vrmax": float, "tr": float, "ilr": float}
    _defaults = {"ta": 0.0, "vimin": 0.0, "vamin": 0.0, "kf": 0.0, "vrmin": 0.0, "ka": 0.0, "tb": 0.0, "vamax": 0.0, "tb1": 0.0, "uelin": 0.0, "kc": 0.0, "tc1": 0.0, "tf": 0.0, "klr": 0.0, "vimax": 0.0, "tc": 0.0, "pssin": 0.0, "vrmax": 0.0, "tr": 0.0, "ilr": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

