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

class ExcitationSystemsExcDC1A(CorePowerSystemResource):

    def __init__(self, exclim=0.0, vrmin=0.0, tc=0.0, ta=0.0, tb=0.0, ka=0.0, ke=0.0, se2=0.0, te=0.0, se1=0.0, tf=0.0, kf=0.0, uelin=0.0, tr=0.0, e1=0.0, vrmax=0.0, e2=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcDC1A' instance.

        @param exclim: 
        @param vrmin: 
        @param tc: 
        @param ta: 
        @param tb: 
        @param ka: 
        @param ke: 
        @param se2: 
        @param te: 
        @param se1: 
        @param tf: 
        @param kf: 
        @param uelin: 
        @param tr: 
        @param e1: 
        @param vrmax: 
        @param e2: 
        """

        self.exclim = exclim


        self.vrmin = vrmin


        self.tc = tc


        self.ta = ta


        self.tb = tb


        self.ka = ka


        self.ke = ke


        self.se2 = se2


        self.te = te


        self.se1 = se1


        self.tf = tf


        self.kf = kf


        self.uelin = uelin


        self.tr = tr


        self.e1 = e1


        self.vrmax = vrmax


        self.e2 = e2

        super(ExcitationSystemsExcDC1A, self).__init__(*args, **kw_args)

    _attrs = ["exclim", "vrmin", "tc", "ta", "tb", "ka", "ke", "se2", "te", "se1", "tf", "kf", "uelin", "tr", "e1", "vrmax", "e2"]
    _attr_types = {"exclim": float, "vrmin": float, "tc": float, "ta": float, "tb": float, "ka": float, "ke": float, "se2": float, "te": float, "se1": float, "tf": float, "kf": float, "uelin": float, "tr": float, "e1": float, "vrmax": float, "e2": float}
    _defaults = {"exclim": 0.0, "vrmin": 0.0, "tc": 0.0, "ta": 0.0, "tb": 0.0, "ka": 0.0, "ke": 0.0, "se2": 0.0, "te": 0.0, "se1": 0.0, "tf": 0.0, "kf": 0.0, "uelin": 0.0, "tr": 0.0, "e1": 0.0, "vrmax": 0.0, "e2": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

