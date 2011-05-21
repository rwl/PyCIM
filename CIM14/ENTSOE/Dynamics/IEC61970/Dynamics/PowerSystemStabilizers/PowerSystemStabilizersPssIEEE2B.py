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

class PowerSystemStabilizersPssIEEE2B(CorePowerSystemResource):

    def __init__(self, t10=0.0, a=0.0, ks1=0.0, ks3=0.0, t11=0.0, ks2=0.0, vstmin=0.0, vsi1max=0.0, vsi2max=0.0, tb=0.0, t2=0.0, ta=0.0, t1=0.0, t4=0.0, n=0, t3=0.0, m=0, j1=0, t6=0.0, j2=0, t8=0.0, vsi1min=0.0, t7=0.0, t9=0.0, ks4=0.0, tw2=0.0, tw1=0.0, tw4=0.0, vsi2min=0.0, tw3=0.0, vstmax=0.0, *args, **kw_args):
        """Initialises a new 'PowerSystemStabilizersPssIEEE2B' instance.

        @param t10: 
        @param a: 
        @param ks1: 
        @param ks3: 
        @param t11: 
        @param ks2: 
        @param vstmin: 
        @param vsi1max: 
        @param vsi2max: 
        @param tb: 
        @param t2: 
        @param ta: 
        @param t1: 
        @param t4: 
        @param n: 
        @param t3: 
        @param m: 
        @param j1: 
        @param t6: 
        @param j2: 
        @param t8: 
        @param vsi1min: 
        @param t7: 
        @param t9: 
        @param ks4: 
        @param tw2: 
        @param tw1: 
        @param tw4: 
        @param vsi2min: 
        @param tw3: 
        @param vstmax: 
        """

        self.t10 = t10


        self.a = a


        self.ks1 = ks1


        self.ks3 = ks3


        self.t11 = t11


        self.ks2 = ks2


        self.vstmin = vstmin


        self.vsi1max = vsi1max


        self.vsi2max = vsi2max


        self.tb = tb


        self.t2 = t2


        self.ta = ta


        self.t1 = t1


        self.t4 = t4


        self.n = n


        self.t3 = t3


        self.m = m


        self.j1 = j1


        self.t6 = t6


        self.j2 = j2


        self.t8 = t8


        self.vsi1min = vsi1min


        self.t7 = t7


        self.t9 = t9


        self.ks4 = ks4


        self.tw2 = tw2


        self.tw1 = tw1


        self.tw4 = tw4


        self.vsi2min = vsi2min


        self.tw3 = tw3


        self.vstmax = vstmax

        super(PowerSystemStabilizersPssIEEE2B, self).__init__(*args, **kw_args)

    _attrs = ["t10", "a", "ks1", "ks3", "t11", "ks2", "vstmin", "vsi1max", "vsi2max", "tb", "t2", "ta", "t1", "t4", "n", "t3", "m", "j1", "t6", "j2", "t8", "vsi1min", "t7", "t9", "ks4", "tw2", "tw1", "tw4", "vsi2min", "tw3", "vstmax"]
    _attr_types = {"t10": float, "a": float, "ks1": float, "ks3": float, "t11": float, "ks2": float, "vstmin": float, "vsi1max": float, "vsi2max": float, "tb": float, "t2": float, "ta": float, "t1": float, "t4": float, "n": int, "t3": float, "m": int, "j1": int, "t6": float, "j2": int, "t8": float, "vsi1min": float, "t7": float, "t9": float, "ks4": float, "tw2": float, "tw1": float, "tw4": float, "vsi2min": float, "tw3": float, "vstmax": float}
    _defaults = {"t10": 0.0, "a": 0.0, "ks1": 0.0, "ks3": 0.0, "t11": 0.0, "ks2": 0.0, "vstmin": 0.0, "vsi1max": 0.0, "vsi2max": 0.0, "tb": 0.0, "t2": 0.0, "ta": 0.0, "t1": 0.0, "t4": 0.0, "n": 0, "t3": 0.0, "m": 0, "j1": 0, "t6": 0.0, "j2": 0, "t8": 0.0, "vsi1min": 0.0, "t7": 0.0, "t9": 0.0, "ks4": 0.0, "tw2": 0.0, "tw1": 0.0, "tw4": 0.0, "vsi2min": 0.0, "tw3": 0.0, "vstmax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

