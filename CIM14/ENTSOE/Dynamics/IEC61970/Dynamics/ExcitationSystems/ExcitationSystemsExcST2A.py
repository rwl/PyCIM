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

class ExcitationSystemsExcST2A(CorePowerSystemResource):

    def __init__(self, vrmin=0.0, tc=0.0, tb=0.0, ta=0.0, ka=0.0, ke=0.0, uelin=0.0, kc=0.0, te=0.0, ki=0.0, kf=0.0, tf=0.0, vrmax=0.0, efdmax=0.0, tr=0.0, kp=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcST2A' instance.

        @param vrmin: 
        @param tc: 
        @param tb: 
        @param ta: 
        @param ka: 
        @param ke: 
        @param uelin: 
        @param kc: 
        @param te: 
        @param ki: 
        @param kf: 
        @param tf: 
        @param vrmax: 
        @param efdmax: 
        @param tr: 
        @param kp: 
        """

        self.vrmin = vrmin


        self.tc = tc


        self.tb = tb


        self.ta = ta


        self.ka = ka


        self.ke = ke


        self.uelin = uelin


        self.kc = kc


        self.te = te


        self.ki = ki


        self.kf = kf


        self.tf = tf


        self.vrmax = vrmax


        self.efdmax = efdmax


        self.tr = tr


        self.kp = kp

        super(ExcitationSystemsExcST2A, self).__init__(*args, **kw_args)

    _attrs = ["vrmin", "tc", "tb", "ta", "ka", "ke", "uelin", "kc", "te", "ki", "kf", "tf", "vrmax", "efdmax", "tr", "kp"]
    _attr_types = {"vrmin": float, "tc": float, "tb": float, "ta": float, "ka": float, "ke": float, "uelin": float, "kc": float, "te": float, "ki": float, "kf": float, "tf": float, "vrmax": float, "efdmax": float, "tr": float, "kp": float}
    _defaults = {"vrmin": 0.0, "tc": 0.0, "tb": 0.0, "ta": 0.0, "ka": 0.0, "ke": 0.0, "uelin": 0.0, "kc": 0.0, "te": 0.0, "ki": 0.0, "kf": 0.0, "tf": 0.0, "vrmax": 0.0, "efdmax": 0.0, "tr": 0.0, "kp": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

