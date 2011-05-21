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

class ExcitationSystemsExcDC4B(CorePowerSystemResource):

    def __init__(self, vrmin=0.0, uelin=0.0, ki=0.0, kp=0.0, e2=0.0, oelin=0.0, vrmax=0.0, kf=0.0, te=0.0, ke=0.0, vemin=0.0, tf=0.0, kd=0.0, se2=0.0, ta=0.0, tr=0.0, ka=0.0, se1=0.0, td=0.0, e1=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcDC4B' instance.

        @param vrmin: 
        @param uelin: 
        @param ki: 
        @param kp: 
        @param e2: 
        @param oelin: 
        @param vrmax: 
        @param kf: 
        @param te: 
        @param ke: 
        @param vemin: 
        @param tf: 
        @param kd: 
        @param se2: 
        @param ta: 
        @param tr: 
        @param ka: 
        @param se1: 
        @param td: 
        @param e1: 
        """

        self.vrmin = vrmin


        self.uelin = uelin


        self.ki = ki


        self.kp = kp


        self.e2 = e2


        self.oelin = oelin


        self.vrmax = vrmax


        self.kf = kf


        self.te = te


        self.ke = ke


        self.vemin = vemin


        self.tf = tf


        self.kd = kd


        self.se2 = se2


        self.ta = ta


        self.tr = tr


        self.ka = ka


        self.se1 = se1


        self.td = td


        self.e1 = e1

        super(ExcitationSystemsExcDC4B, self).__init__(*args, **kw_args)

    _attrs = ["vrmin", "uelin", "ki", "kp", "e2", "oelin", "vrmax", "kf", "te", "ke", "vemin", "tf", "kd", "se2", "ta", "tr", "ka", "se1", "td", "e1"]
    _attr_types = {"vrmin": float, "uelin": float, "ki": float, "kp": float, "e2": float, "oelin": float, "vrmax": float, "kf": float, "te": float, "ke": float, "vemin": float, "tf": float, "kd": float, "se2": float, "ta": float, "tr": float, "ka": float, "se1": float, "td": float, "e1": float}
    _defaults = {"vrmin": 0.0, "uelin": 0.0, "ki": 0.0, "kp": 0.0, "e2": 0.0, "oelin": 0.0, "vrmax": 0.0, "kf": 0.0, "te": 0.0, "ke": 0.0, "vemin": 0.0, "tf": 0.0, "kd": 0.0, "se2": 0.0, "ta": 0.0, "tr": 0.0, "ka": 0.0, "se1": 0.0, "td": 0.0, "e1": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

