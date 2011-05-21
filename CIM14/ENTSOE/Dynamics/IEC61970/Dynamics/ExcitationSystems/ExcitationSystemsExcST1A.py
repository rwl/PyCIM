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

class ExcitationSystemsExcST1A(CorePowerSystemResource):

    def __init__(self, vrmin=0.0, kc=0.0, vimin=0.0, uelin=0.0, tf=0.0, kf=0.0, tc1=0.0, pssin=0.0, tc=0.0, tb=0.0, ka=0.0, ta=0.0, tr=0.0, ilr=0.0, vamin=0.0, klr=0.0, tb1=0.0, vamax=0.0, vrmax=0.0, vimax=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcST1A' instance.

        @param vrmin: 
        @param kc: 
        @param vimin: 
        @param uelin: 
        @param tf: 
        @param kf: 
        @param tc1: 
        @param pssin: 
        @param tc: 
        @param tb: 
        @param ka: 
        @param ta: 
        @param tr: 
        @param ilr: 
        @param vamin: 
        @param klr: 
        @param tb1: 
        @param vamax: 
        @param vrmax: 
        @param vimax: 
        """

        self.vrmin = vrmin


        self.kc = kc


        self.vimin = vimin


        self.uelin = uelin


        self.tf = tf


        self.kf = kf


        self.tc1 = tc1


        self.pssin = pssin


        self.tc = tc


        self.tb = tb


        self.ka = ka


        self.ta = ta


        self.tr = tr


        self.ilr = ilr


        self.vamin = vamin


        self.klr = klr


        self.tb1 = tb1


        self.vamax = vamax


        self.vrmax = vrmax


        self.vimax = vimax

        super(ExcitationSystemsExcST1A, self).__init__(*args, **kw_args)

    _attrs = ["vrmin", "kc", "vimin", "uelin", "tf", "kf", "tc1", "pssin", "tc", "tb", "ka", "ta", "tr", "ilr", "vamin", "klr", "tb1", "vamax", "vrmax", "vimax"]
    _attr_types = {"vrmin": float, "kc": float, "vimin": float, "uelin": float, "tf": float, "kf": float, "tc1": float, "pssin": float, "tc": float, "tb": float, "ka": float, "ta": float, "tr": float, "ilr": float, "vamin": float, "klr": float, "tb1": float, "vamax": float, "vrmax": float, "vimax": float}
    _defaults = {"vrmin": 0.0, "kc": 0.0, "vimin": 0.0, "uelin": 0.0, "tf": 0.0, "kf": 0.0, "tc1": 0.0, "pssin": 0.0, "tc": 0.0, "tb": 0.0, "ka": 0.0, "ta": 0.0, "tr": 0.0, "ilr": 0.0, "vamin": 0.0, "klr": 0.0, "tb1": 0.0, "vamax": 0.0, "vrmax": 0.0, "vimax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

