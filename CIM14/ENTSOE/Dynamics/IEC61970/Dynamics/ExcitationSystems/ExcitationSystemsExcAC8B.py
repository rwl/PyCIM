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

class ExcitationSystemsExcAC8B(CorePowerSystemResource):

    def __init__(self, kdr=0.0, tr=0.0, e1=0.0, e2=0.0, kir=0.0, kc=0.0, vrmax=0.0, ka=0.0, se2=0.0, tdr=0.0, kpr=0.0, vemin=0.0, kd=0.0, te=0.0, se1=0.0, ke=0.0, vfemax=0.0, ta=0.0, vrmin=0.0, vtmult=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcAC8B' instance.

        @param kdr: 
        @param tr: 
        @param e1: 
        @param e2: 
        @param kir: 
        @param kc: 
        @param vrmax: 
        @param ka: 
        @param se2: 
        @param tdr: 
        @param kpr: 
        @param vemin: 
        @param kd: 
        @param te: 
        @param se1: 
        @param ke: 
        @param vfemax: 
        @param ta: 
        @param vrmin: 
        @param vtmult: 
        """

        self.kdr = kdr


        self.tr = tr


        self.e1 = e1


        self.e2 = e2


        self.kir = kir


        self.kc = kc


        self.vrmax = vrmax


        self.ka = ka


        self.se2 = se2


        self.tdr = tdr


        self.kpr = kpr


        self.vemin = vemin


        self.kd = kd


        self.te = te


        self.se1 = se1


        self.ke = ke


        self.vfemax = vfemax


        self.ta = ta


        self.vrmin = vrmin


        self.vtmult = vtmult

        super(ExcitationSystemsExcAC8B, self).__init__(*args, **kw_args)

    _attrs = ["kdr", "tr", "e1", "e2", "kir", "kc", "vrmax", "ka", "se2", "tdr", "kpr", "vemin", "kd", "te", "se1", "ke", "vfemax", "ta", "vrmin", "vtmult"]
    _attr_types = {"kdr": float, "tr": float, "e1": float, "e2": float, "kir": float, "kc": float, "vrmax": float, "ka": float, "se2": float, "tdr": float, "kpr": float, "vemin": float, "kd": float, "te": float, "se1": float, "ke": float, "vfemax": float, "ta": float, "vrmin": float, "vtmult": float}
    _defaults = {"kdr": 0.0, "tr": 0.0, "e1": 0.0, "e2": 0.0, "kir": 0.0, "kc": 0.0, "vrmax": 0.0, "ka": 0.0, "se2": 0.0, "tdr": 0.0, "kpr": 0.0, "vemin": 0.0, "kd": 0.0, "te": 0.0, "se1": 0.0, "ke": 0.0, "vfemax": 0.0, "ta": 0.0, "vrmin": 0.0, "vtmult": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

