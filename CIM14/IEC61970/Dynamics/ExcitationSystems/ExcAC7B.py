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

class ExcAC7B(ExcitationSystem):
    """IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate.
    """

    def __init__(self, kir=0.0, kpr=0.0, vfemax=0.0, te=0.0, vemin=0.0, ke=0.0, kp=0.0, kd=0.0, kdr=0.0, kf3=0.0, e1=0.0, tdr=0.0, se2=0.0, kf1=0.0, e2=0.0, kc=0.0, vamin=0.0, se1=0.0, vrmin=0.0, tf=0.0, vrmax=0.0, kf2=0.0, kl=0.0, kpa=0.0, kia=0.0, tr=0.0, vamax=0.0, *args, **kw_args):
        """Initialises a new 'ExcAC7B' instance.

        @param kir: Regulator integral gain (&gt;= 0.) 
        @param kpr: Regulator proportional gain (&gt; 0. if kir = 0.) 
        @param vfemax: Exciter field current limit parameter 
        @param te: Exciter time constant, sec. (&gt; 0.) 
        @param vemin: Minimum exciter ouput voltage (&lt;= 0.) 
        @param ke: Exciter field resistance constant 
        @param kp: Exciter field voltage source gain (&gt; 0.) 
        @param kd: Exciter internal reactance (&gt;= 0.) 
        @param kdr: Regulator derivative gain (&gt;= 0.) 
        @param kf3: Rate feedback gain (&gt;= 0.) 
        @param e1: Field voltage value 1   (&gt; 0.) 
        @param tdr: Derivative gain washout time constant (&gt;= 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        @param kf1: Field voltage feedback gain (&gt;= 0.) 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param vamin: Minimum amplifier output (&lt; 0.) 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param vrmin: Minimum regulator output (&lt; 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        @param vrmax: Maximum regulator output (&gt; 0.) 
        @param kf2: Exciter field current feedback gain (&gt;= 0.) 
        @param kl: Exciter field voltage lower limit parameter 
        @param kpa: Amplifier proportional gain (&gt; 0. if kia = 0.) 
        @param kia: Amplifier integral gain (&gt;= 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param vamax: Maximum amplifier output (&gt; 0.) 
        """
        #: Regulator integral gain (&gt;= 0.)
        self.kir = kir

        #: Regulator proportional gain (&gt; 0. if kir = 0.)
        self.kpr = kpr

        #: Exciter field current limit parameter
        self.vfemax = vfemax

        #: Exciter time constant, sec. (&gt; 0.)
        self.te = te

        #: Minimum exciter ouput voltage (&lt;= 0.)
        self.vemin = vemin

        #: Exciter field resistance constant
        self.ke = ke

        #: Exciter field voltage source gain (&gt; 0.)
        self.kp = kp

        #: Exciter internal reactance (&gt;= 0.)
        self.kd = kd

        #: Regulator derivative gain (&gt;= 0.)
        self.kdr = kdr

        #: Rate feedback gain (&gt;= 0.)
        self.kf3 = kf3

        #: Field voltage value 1   (&gt; 0.)
        self.e1 = e1

        #: Derivative gain washout time constant (&gt;= 0.)
        self.tdr = tdr

        #: Saturation factor at e2   (&gt;= 0.)
        self.se2 = se2

        #: Field voltage feedback gain (&gt;= 0.)
        self.kf1 = kf1

        #: Field voltage value 2.    (&gt; 0.)
        self.e2 = e2

        #: Rectifier regulation factor (&gt;= 0.)
        self.kc = kc

        #: Minimum amplifier output (&lt; 0.)
        self.vamin = vamin

        #: Saturation factor at e1  (&gt;= 0.)
        self.se1 = se1

        #: Minimum regulator output (&lt; 0.)
        self.vrmin = vrmin

        #: Rate feedback time constant (&gt; 0.)
        self.tf = tf

        #: Maximum regulator output (&gt; 0.)
        self.vrmax = vrmax

        #: Exciter field current feedback gain (&gt;= 0.)
        self.kf2 = kf2

        #: Exciter field voltage lower limit parameter
        self.kl = kl

        #: Amplifier proportional gain (&gt; 0. if kia = 0.)
        self.kpa = kpa

        #: Amplifier integral gain (&gt;= 0.)
        self.kia = kia

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Maximum amplifier output (&gt; 0.)
        self.vamax = vamax

        super(ExcAC7B, self).__init__(*args, **kw_args)

    _attrs = ["kir", "kpr", "vfemax", "te", "vemin", "ke", "kp", "kd", "kdr", "kf3", "e1", "tdr", "se2", "kf1", "e2", "kc", "vamin", "se1", "vrmin", "tf", "vrmax", "kf2", "kl", "kpa", "kia", "tr", "vamax"]
    _attr_types = {"kir": float, "kpr": float, "vfemax": float, "te": float, "vemin": float, "ke": float, "kp": float, "kd": float, "kdr": float, "kf3": float, "e1": float, "tdr": float, "se2": float, "kf1": float, "e2": float, "kc": float, "vamin": float, "se1": float, "vrmin": float, "tf": float, "vrmax": float, "kf2": float, "kl": float, "kpa": float, "kia": float, "tr": float, "vamax": float}
    _defaults = {"kir": 0.0, "kpr": 0.0, "vfemax": 0.0, "te": 0.0, "vemin": 0.0, "ke": 0.0, "kp": 0.0, "kd": 0.0, "kdr": 0.0, "kf3": 0.0, "e1": 0.0, "tdr": 0.0, "se2": 0.0, "kf1": 0.0, "e2": 0.0, "kc": 0.0, "vamin": 0.0, "se1": 0.0, "vrmin": 0.0, "tf": 0.0, "vrmax": 0.0, "kf2": 0.0, "kl": 0.0, "kpa": 0.0, "kia": 0.0, "tr": 0.0, "vamax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

