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

class ExcitationSystemsExcAC7B(CorePowerSystemResource):

    def __init__(self, kd=0.0, kc=0.0, vrmin=0.0, kdr=0.0, vrmax=0.0, kpr=0.0, vemin=0.0, kl=0.0, kf1=0.0, kia=0.0, kf3=0.0, se1=0.0, vfemax=0.0, kf2=0.0, te=0.0, tf=0.0, ke=0.0, kpa=0.0, e2=0.0, se2=0.0, kp=0.0, e1=0.0, kir=0.0, tr=0.0, tdr=0.0, vamin=0.0, vamax=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcAC7B' instance.

        @param kd: 
        @param kc: 
        @param vrmin: 
        @param kdr: 
        @param vrmax: 
        @param kpr: 
        @param vemin: 
        @param kl: 
        @param kf1: 
        @param kia: 
        @param kf3: 
        @param se1: 
        @param vfemax: 
        @param kf2: 
        @param te: 
        @param tf: 
        @param ke: 
        @param kpa: 
        @param e2: 
        @param se2: 
        @param kp: 
        @param e1: 
        @param kir: 
        @param tr: 
        @param tdr: 
        @param vamin: 
        @param vamax: 
        """

        self.kd = kd


        self.kc = kc


        self.vrmin = vrmin


        self.kdr = kdr


        self.vrmax = vrmax


        self.kpr = kpr


        self.vemin = vemin


        self.kl = kl


        self.kf1 = kf1


        self.kia = kia


        self.kf3 = kf3


        self.se1 = se1


        self.vfemax = vfemax


        self.kf2 = kf2


        self.te = te


        self.tf = tf


        self.ke = ke


        self.kpa = kpa


        self.e2 = e2


        self.se2 = se2


        self.kp = kp


        self.e1 = e1


        self.kir = kir


        self.tr = tr


        self.tdr = tdr


        self.vamin = vamin


        self.vamax = vamax

        super(ExcitationSystemsExcAC7B, self).__init__(*args, **kw_args)

    _attrs = ["kd", "kc", "vrmin", "kdr", "vrmax", "kpr", "vemin", "kl", "kf1", "kia", "kf3", "se1", "vfemax", "kf2", "te", "tf", "ke", "kpa", "e2", "se2", "kp", "e1", "kir", "tr", "tdr", "vamin", "vamax"]
    _attr_types = {"kd": float, "kc": float, "vrmin": float, "kdr": float, "vrmax": float, "kpr": float, "vemin": float, "kl": float, "kf1": float, "kia": float, "kf3": float, "se1": float, "vfemax": float, "kf2": float, "te": float, "tf": float, "ke": float, "kpa": float, "e2": float, "se2": float, "kp": float, "e1": float, "kir": float, "tr": float, "tdr": float, "vamin": float, "vamax": float}
    _defaults = {"kd": 0.0, "kc": 0.0, "vrmin": 0.0, "kdr": 0.0, "vrmax": 0.0, "kpr": 0.0, "vemin": 0.0, "kl": 0.0, "kf1": 0.0, "kia": 0.0, "kf3": 0.0, "se1": 0.0, "vfemax": 0.0, "kf2": 0.0, "te": 0.0, "tf": 0.0, "ke": 0.0, "kpa": 0.0, "e2": 0.0, "se2": 0.0, "kp": 0.0, "e1": 0.0, "kir": 0.0, "tr": 0.0, "tdr": 0.0, "vamin": 0.0, "vamax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

