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

class ExcitationSystemsExcAC3A(CorePowerSystemResource):

    def __init__(self, ta=0.0, ka=0.0, kd=0.0, se1=0.0, kc=0.0, se2=0.0, te=0.0, tf=0.0, tb=0.0, tc=0.0, vamax=0.0, kf=0.0, vemin=0.0, ke=0.0, vfemax=0.0, tr=0.0, e2=0.0, e1=0.0, kn=0.0, vamin=0.0, kr=0.0, efdn=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcAC3A' instance.

        @param ta: 
        @param ka: 
        @param kd: 
        @param se1: 
        @param kc: 
        @param se2: 
        @param te: 
        @param tf: 
        @param tb: 
        @param tc: 
        @param vamax: 
        @param kf: 
        @param vemin: 
        @param ke: 
        @param vfemax: 
        @param tr: 
        @param e2: 
        @param e1: 
        @param kn: 
        @param vamin: 
        @param kr: 
        @param efdn: 
        """

        self.ta = ta


        self.ka = ka


        self.kd = kd


        self.se1 = se1


        self.kc = kc


        self.se2 = se2


        self.te = te


        self.tf = tf


        self.tb = tb


        self.tc = tc


        self.vamax = vamax


        self.kf = kf


        self.vemin = vemin


        self.ke = ke


        self.vfemax = vfemax


        self.tr = tr


        self.e2 = e2


        self.e1 = e1


        self.kn = kn


        self.vamin = vamin


        self.kr = kr


        self.efdn = efdn

        super(ExcitationSystemsExcAC3A, self).__init__(*args, **kw_args)

    _attrs = ["ta", "ka", "kd", "se1", "kc", "se2", "te", "tf", "tb", "tc", "vamax", "kf", "vemin", "ke", "vfemax", "tr", "e2", "e1", "kn", "vamin", "kr", "efdn"]
    _attr_types = {"ta": float, "ka": float, "kd": float, "se1": float, "kc": float, "se2": float, "te": float, "tf": float, "tb": float, "tc": float, "vamax": float, "kf": float, "vemin": float, "ke": float, "vfemax": float, "tr": float, "e2": float, "e1": float, "kn": float, "vamin": float, "kr": float, "efdn": float}
    _defaults = {"ta": 0.0, "ka": 0.0, "kd": 0.0, "se1": 0.0, "kc": 0.0, "se2": 0.0, "te": 0.0, "tf": 0.0, "tb": 0.0, "tc": 0.0, "vamax": 0.0, "kf": 0.0, "vemin": 0.0, "ke": 0.0, "vfemax": 0.0, "tr": 0.0, "e2": 0.0, "e1": 0.0, "kn": 0.0, "vamin": 0.0, "kr": 0.0, "efdn": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

