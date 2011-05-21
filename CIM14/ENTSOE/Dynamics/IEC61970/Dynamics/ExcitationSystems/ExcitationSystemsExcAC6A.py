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

class ExcitationSystemsExcAC6A(CorePowerSystemResource):

    def __init__(self, vamax=0.0, vfelim=0.0, tr=0.0, e2=0.0, e1=0.0, vamin=0.0, vhmax=0.0, vrmax=0.0, se1=0.0, se2=0.0, vrmin=0.0, te=0.0, kh=0.0, tb=0.0, tc=0.0, ta=0.0, ka=0.0, kc=0.0, tj=0.0, tk=0.0, ke=0.0, th=0.0, kd=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcAC6A' instance.

        @param vamax: 
        @param vfelim: 
        @param tr: 
        @param e2: 
        @param e1: 
        @param vamin: 
        @param vhmax: 
        @param vrmax: 
        @param se1: 
        @param se2: 
        @param vrmin: 
        @param te: 
        @param kh: 
        @param tb: 
        @param tc: 
        @param ta: 
        @param ka: 
        @param kc: 
        @param tj: 
        @param tk: 
        @param ke: 
        @param th: 
        @param kd: 
        """

        self.vamax = vamax


        self.vfelim = vfelim


        self.tr = tr


        self.e2 = e2


        self.e1 = e1


        self.vamin = vamin


        self.vhmax = vhmax


        self.vrmax = vrmax


        self.se1 = se1


        self.se2 = se2


        self.vrmin = vrmin


        self.te = te


        self.kh = kh


        self.tb = tb


        self.tc = tc


        self.ta = ta


        self.ka = ka


        self.kc = kc


        self.tj = tj


        self.tk = tk


        self.ke = ke


        self.th = th


        self.kd = kd

        super(ExcitationSystemsExcAC6A, self).__init__(*args, **kw_args)

    _attrs = ["vamax", "vfelim", "tr", "e2", "e1", "vamin", "vhmax", "vrmax", "se1", "se2", "vrmin", "te", "kh", "tb", "tc", "ta", "ka", "kc", "tj", "tk", "ke", "th", "kd"]
    _attr_types = {"vamax": float, "vfelim": float, "tr": float, "e2": float, "e1": float, "vamin": float, "vhmax": float, "vrmax": float, "se1": float, "se2": float, "vrmin": float, "te": float, "kh": float, "tb": float, "tc": float, "ta": float, "ka": float, "kc": float, "tj": float, "tk": float, "ke": float, "th": float, "kd": float}
    _defaults = {"vamax": 0.0, "vfelim": 0.0, "tr": 0.0, "e2": 0.0, "e1": 0.0, "vamin": 0.0, "vhmax": 0.0, "vrmax": 0.0, "se1": 0.0, "se2": 0.0, "vrmin": 0.0, "te": 0.0, "kh": 0.0, "tb": 0.0, "tc": 0.0, "ta": 0.0, "ka": 0.0, "kc": 0.0, "tj": 0.0, "tk": 0.0, "ke": 0.0, "th": 0.0, "kd": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

