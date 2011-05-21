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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CorePowerSystemResource import CorePowerSystemResource

class ExcitationSystemsExcAC5A(CorePowerSystemResource):

    def __init__(self, ta=0.0, vrmax=0.0, ka=0.0, vrmin=0.0, tr=0.0, tf1=0.0, ke=0.0, tf2=0.0, te=0.0, kf=0.0, e1=0.0, tf3=0.0, e2=0.0, se1=0.0, se2=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcAC5A' instance.

        @param ta: 
        @param vrmax: 
        @param ka: 
        @param vrmin: 
        @param tr: 
        @param tf1: 
        @param ke: 
        @param tf2: 
        @param te: 
        @param kf: 
        @param e1: 
        @param tf3: 
        @param e2: 
        @param se1: 
        @param se2: 
        """

        self.ta = ta


        self.vrmax = vrmax


        self.ka = ka


        self.vrmin = vrmin


        self.tr = tr


        self.tf1 = tf1


        self.ke = ke


        self.tf2 = tf2


        self.te = te


        self.kf = kf


        self.e1 = e1


        self.tf3 = tf3


        self.e2 = e2


        self.se1 = se1


        self.se2 = se2

        super(ExcitationSystemsExcAC5A, self).__init__(*args, **kw_args)

    _attrs = ["ta", "vrmax", "ka", "vrmin", "tr", "tf1", "ke", "tf2", "te", "kf", "e1", "tf3", "e2", "se1", "se2"]
    _attr_types = {"ta": float, "vrmax": float, "ka": float, "vrmin": float, "tr": float, "tf1": float, "ke": float, "tf2": float, "te": float, "kf": float, "e1": float, "tf3": float, "e2": float, "se1": float, "se2": float}
    _defaults = {"ta": 0.0, "vrmax": 0.0, "ka": 0.0, "vrmin": 0.0, "tr": 0.0, "tf1": 0.0, "ke": 0.0, "tf2": 0.0, "te": 0.0, "kf": 0.0, "e1": 0.0, "tf3": 0.0, "e2": 0.0, "se1": 0.0, "se2": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

