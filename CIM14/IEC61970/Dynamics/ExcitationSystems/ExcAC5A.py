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

class ExcAC5A(ExcitationSystem):
    """IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.
    """

    def __init__(self, ka=0.0, e1=0.0, kf=0.0, te=0.0, vrmin=0.0, vrmax=0.0, se2=0.0, tf3=0.0, e2=0.0, ke=0.0, tr=0.0, se1=0.0, tf2=0.0, tf1=0.0, ta=0.0, *args, **kw_args):
        """Initialises a new 'ExcAC5A' instance.

        @param ka: Gain  (&gt; 0.) 
        @param e1: Field voltage value 1      (&gt; 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param te: Exciter time constant, sec. (&gt; 0.) 
        @param vrmin: Minimum controller output (&lt;  0.) 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param se2: Saturation factor at e2 (&gt;= 0.) 
        @param tf3: Rate feedback lead time constant 
        @param e2: Field voltage value 2.  (&gt; 0.) 
        @param ke: Exciter field resistance line slope 
        @param tr: Filter time constant (&gt;= 0.) 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param tf2: Rate feedback lag time constant (&gt;= 0.) 
        @param tf1: Rate feedback lag time constant (&gt; 0.) 
        @param ta: Time constant (&gt; 0.) 
        """
        #: Gain  (&gt; 0.)
        self.ka = ka

        #: Field voltage value 1      (&gt; 0.)
        self.e1 = e1

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Exciter time constant, sec. (&gt; 0.)
        self.te = te

        #: Minimum controller output (&lt;  0.)
        self.vrmin = vrmin

        #: Maximum controller output (&gt; 0.)
        self.vrmax = vrmax

        #: Saturation factor at e2 (&gt;= 0.)
        self.se2 = se2

        #: Rate feedback lead time constant
        self.tf3 = tf3

        #: Field voltage value 2.  (&gt; 0.)
        self.e2 = e2

        #: Exciter field resistance line slope
        self.ke = ke

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Saturation factor at e1  (&gt;= 0.)
        self.se1 = se1

        #: Rate feedback lag time constant (&gt;= 0.)
        self.tf2 = tf2

        #: Rate feedback lag time constant (&gt; 0.)
        self.tf1 = tf1

        #: Time constant (&gt; 0.)
        self.ta = ta

        super(ExcAC5A, self).__init__(*args, **kw_args)

    _attrs = ["ka", "e1", "kf", "te", "vrmin", "vrmax", "se2", "tf3", "e2", "ke", "tr", "se1", "tf2", "tf1", "ta"]
    _attr_types = {"ka": float, "e1": float, "kf": float, "te": float, "vrmin": float, "vrmax": float, "se2": float, "tf3": float, "e2": float, "ke": float, "tr": float, "se1": float, "tf2": float, "tf1": float, "ta": float}
    _defaults = {"ka": 0.0, "e1": 0.0, "kf": 0.0, "te": 0.0, "vrmin": 0.0, "vrmax": 0.0, "se2": 0.0, "tf3": 0.0, "e2": 0.0, "ke": 0.0, "tr": 0.0, "se1": 0.0, "tf2": 0.0, "tf1": 0.0, "ta": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

