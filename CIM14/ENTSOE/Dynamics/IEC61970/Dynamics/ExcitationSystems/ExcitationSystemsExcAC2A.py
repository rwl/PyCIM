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

class ExcitationSystemsExcAC2A(CorePowerSystemResource):

    def __init__(self, tb=0.0, e1=0.0, ta=0.0, vrmin=0.0, e2=0.0, vfemax=0.0, vrmax=0.0, ka=0.0, se1=0.0, se2=0.0, kf=0.0, kh=0.0, kc=0.0, vamin=0.0, kb=0.0, ke=0.0, tr=0.0, kd=0.0, te=0.0, tc=0.0, vamax=0.0, tf=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcAC2A' instance.

        @param tb: 
        @param e1: 
        @param ta: 
        @param vrmin: 
        @param e2: 
        @param vfemax: 
        @param vrmax: 
        @param ka: 
        @param se1: 
        @param se2: 
        @param kf: 
        @param kh: 
        @param kc: 
        @param vamin: 
        @param kb: 
        @param ke: 
        @param tr: 
        @param kd: 
        @param te: 
        @param tc: 
        @param vamax: 
        @param tf: 
        """

        self.tb = tb


        self.e1 = e1


        self.ta = ta


        self.vrmin = vrmin


        self.e2 = e2


        self.vfemax = vfemax


        self.vrmax = vrmax


        self.ka = ka


        self.se1 = se1


        self.se2 = se2


        self.kf = kf


        self.kh = kh


        self.kc = kc


        self.vamin = vamin


        self.kb = kb


        self.ke = ke


        self.tr = tr


        self.kd = kd


        self.te = te


        self.tc = tc


        self.vamax = vamax


        self.tf = tf

        super(ExcitationSystemsExcAC2A, self).__init__(*args, **kw_args)

    _attrs = ["tb", "e1", "ta", "vrmin", "e2", "vfemax", "vrmax", "ka", "se1", "se2", "kf", "kh", "kc", "vamin", "kb", "ke", "tr", "kd", "te", "tc", "vamax", "tf"]
    _attr_types = {"tb": float, "e1": float, "ta": float, "vrmin": float, "e2": float, "vfemax": float, "vrmax": float, "ka": float, "se1": float, "se2": float, "kf": float, "kh": float, "kc": float, "vamin": float, "kb": float, "ke": float, "tr": float, "kd": float, "te": float, "tc": float, "vamax": float, "tf": float}
    _defaults = {"tb": 0.0, "e1": 0.0, "ta": 0.0, "vrmin": 0.0, "e2": 0.0, "vfemax": 0.0, "vrmax": 0.0, "ka": 0.0, "se1": 0.0, "se2": 0.0, "kf": 0.0, "kh": 0.0, "kc": 0.0, "vamin": 0.0, "kb": 0.0, "ke": 0.0, "tr": 0.0, "kd": 0.0, "te": 0.0, "tc": 0.0, "vamax": 0.0, "tf": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

