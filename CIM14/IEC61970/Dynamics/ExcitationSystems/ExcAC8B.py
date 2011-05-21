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

class ExcAC8B(ExcitationSystem):
    """IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>.
    """

    def __init__(self, vfemax=0.0, vrmin=0.0, ta=0.0, tdr=0.0, vtmult=0.0, ka=0.0, kdr=0.0, se1=0.0, e1=0.0, vemin=0.0, te=0.0, ke=0.0, se2=0.0, tr=0.0, kir=0.0, kpr=0.0, vrmax=0.0, kd=0.0, e2=0.0, kc=0.0, *args, **kw_args):
        """Initialises a new 'ExcAC8B' instance.

        @param vfemax: Exciter field current limit parameter 
        @param vrmin: Minimum controller output (&lt;= 0.) 
        @param ta: Amplifier time constant  (&gt;= 0.) 
        @param tdr: Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.) 
        @param vtmult: if not 0, multiply vrmax and vrmin by terminal voltage 
        @param ka: Amplifier gain (&gt; 0.) 
        @param kdr: Voltage Regulator Derivative Gain (&gt;= 0.) 
        @param se1: Saturation factor at e1 (&gt;= 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param vemin: Minimum exciter ouput voltage (&lt;= 0.) 
        @param te: Exciter field time constant (&gt; 0.) 
        @param ke: Exciter field proportional constant 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param tr: Voltage transducer time constant (&gt;= 0.) 
        @param kir: Voltage Regulator Integral Gain (&gt;= 0.) 
        @param kpr: Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.) 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param kd: Exciter regulation factor (&gt;= 0.) 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        """
        #: Exciter field current limit parameter
        self.vfemax = vfemax

        #: Minimum controller output (&lt;= 0.)
        self.vrmin = vrmin

        #: Amplifier time constant  (&gt;= 0.)
        self.ta = ta

        #: Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.)
        self.tdr = tdr

        #: if not 0, multiply vrmax and vrmin by terminal voltage
        self.vtmult = vtmult

        #: Amplifier gain (&gt; 0.)
        self.ka = ka

        #: Voltage Regulator Derivative Gain (&gt;= 0.)
        self.kdr = kdr

        #: Saturation factor at e1 (&gt;= 0.)
        self.se1 = se1

        #: Field voltage value 1     (&gt; 0.)
        self.e1 = e1

        #: Minimum exciter ouput voltage (&lt;= 0.)
        self.vemin = vemin

        #: Exciter field time constant (&gt; 0.)
        self.te = te

        #: Exciter field proportional constant
        self.ke = ke

        #: Saturation factor at e2  (&gt;= 0.)
        self.se2 = se2

        #: Voltage transducer time constant (&gt;= 0.)
        self.tr = tr

        #: Voltage Regulator Integral Gain (&gt;= 0.)
        self.kir = kir

        #: Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.)
        self.kpr = kpr

        #: Maximum controller output (&gt; 0.)
        self.vrmax = vrmax

        #: Exciter regulation factor (&gt;= 0.)
        self.kd = kd

        #: Field voltage value 2.    (&gt; 0.)
        self.e2 = e2

        #: Rectifier regulation factor (&gt;= 0.)
        self.kc = kc

        super(ExcAC8B, self).__init__(*args, **kw_args)

    _attrs = ["vfemax", "vrmin", "ta", "tdr", "vtmult", "ka", "kdr", "se1", "e1", "vemin", "te", "ke", "se2", "tr", "kir", "kpr", "vrmax", "kd", "e2", "kc"]
    _attr_types = {"vfemax": float, "vrmin": float, "ta": float, "tdr": float, "vtmult": float, "ka": float, "kdr": float, "se1": float, "e1": float, "vemin": float, "te": float, "ke": float, "se2": float, "tr": float, "kir": float, "kpr": float, "vrmax": float, "kd": float, "e2": float, "kc": float}
    _defaults = {"vfemax": 0.0, "vrmin": 0.0, "ta": 0.0, "tdr": 0.0, "vtmult": 0.0, "ka": 0.0, "kdr": 0.0, "se1": 0.0, "e1": 0.0, "vemin": 0.0, "te": 0.0, "ke": 0.0, "se2": 0.0, "tr": 0.0, "kir": 0.0, "kpr": 0.0, "vrmax": 0.0, "kd": 0.0, "e2": 0.0, "kc": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

