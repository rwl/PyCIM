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

class ExcitationSystemsExcAC1A(CorePowerSystemResource):

    def __init__(self, se1=0.0, se2=0.0, e2=0.0, e1=0.0, tr=0.0, vamin=0.0, vamax=0.0, vrmax=0.0, tb=0.0, kd=0.0, tc=0.0, kc=0.0, kf=0.0, ta=0.0, vrmin=0.0, ke=0.0, te=0.0, tf=0.0, ka=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcAC1A' instance.

        @param se1: 
        @param se2: 
        @param e2: 
        @param e1: 
        @param tr: 
        @param vamin: 
        @param vamax: 
        @param vrmax: 
        @param tb: 
        @param kd: 
        @param tc: 
        @param kc: 
        @param kf: 
        @param ta: 
        @param vrmin: 
        @param ke: 
        @param te: 
        @param tf: 
        @param ka: 
        """

        self.se1 = se1


        self.se2 = se2


        self.e2 = e2


        self.e1 = e1


        self.tr = tr


        self.vamin = vamin


        self.vamax = vamax


        self.vrmax = vrmax


        self.tb = tb


        self.kd = kd


        self.tc = tc


        self.kc = kc


        self.kf = kf


        self.ta = ta


        self.vrmin = vrmin


        self.ke = ke


        self.te = te


        self.tf = tf


        self.ka = ka

        super(ExcitationSystemsExcAC1A, self).__init__(*args, **kw_args)

    _attrs = ["se1", "se2", "e2", "e1", "tr", "vamin", "vamax", "vrmax", "tb", "kd", "tc", "kc", "kf", "ta", "vrmin", "ke", "te", "tf", "ka"]
    _attr_types = {"se1": float, "se2": float, "e2": float, "e1": float, "tr": float, "vamin": float, "vamax": float, "vrmax": float, "tb": float, "kd": float, "tc": float, "kc": float, "kf": float, "ta": float, "vrmin": float, "ke": float, "te": float, "tf": float, "ka": float}
    _defaults = {"se1": 0.0, "se2": 0.0, "e2": 0.0, "e1": 0.0, "tr": 0.0, "vamin": 0.0, "vamax": 0.0, "vrmax": 0.0, "tb": 0.0, "kd": 0.0, "tc": 0.0, "kc": 0.0, "kf": 0.0, "ta": 0.0, "vrmin": 0.0, "ke": 0.0, "te": 0.0, "tf": 0.0, "ka": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

