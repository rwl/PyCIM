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

class ExcitationSystemsExcDC2A(CorePowerSystemResource):

    def __init__(self, te=0.0, tf=0.0, ka=0.0, tc=0.0, vrmin=0.0, ta=0.0, tb=0.0, vrmax=0.0, kf=0.0, ke=0.0, uelin=0.0, se1=0.0, tr=0.0, se2=0.0, exclim=0.0, e2=0.0, e1=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcDC2A' instance.

        @param te: 
        @param tf: 
        @param ka: 
        @param tc: 
        @param vrmin: 
        @param ta: 
        @param tb: 
        @param vrmax: 
        @param kf: 
        @param ke: 
        @param uelin: 
        @param se1: 
        @param tr: 
        @param se2: 
        @param exclim: 
        @param e2: 
        @param e1: 
        """

        self.te = te


        self.tf = tf


        self.ka = ka


        self.tc = tc


        self.vrmin = vrmin


        self.ta = ta


        self.tb = tb


        self.vrmax = vrmax


        self.kf = kf


        self.ke = ke


        self.uelin = uelin


        self.se1 = se1


        self.tr = tr


        self.se2 = se2


        self.exclim = exclim


        self.e2 = e2


        self.e1 = e1

        super(ExcitationSystemsExcDC2A, self).__init__(*args, **kw_args)

    _attrs = ["te", "tf", "ka", "tc", "vrmin", "ta", "tb", "vrmax", "kf", "ke", "uelin", "se1", "tr", "se2", "exclim", "e2", "e1"]
    _attr_types = {"te": float, "tf": float, "ka": float, "tc": float, "vrmin": float, "ta": float, "tb": float, "vrmax": float, "kf": float, "ke": float, "uelin": float, "se1": float, "tr": float, "se2": float, "exclim": float, "e2": float, "e1": float}
    _defaults = {"te": 0.0, "tf": 0.0, "ka": 0.0, "tc": 0.0, "vrmin": 0.0, "ta": 0.0, "tb": 0.0, "vrmax": 0.0, "kf": 0.0, "ke": 0.0, "uelin": 0.0, "se1": 0.0, "tr": 0.0, "se2": 0.0, "exclim": 0.0, "e2": 0.0, "e1": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

