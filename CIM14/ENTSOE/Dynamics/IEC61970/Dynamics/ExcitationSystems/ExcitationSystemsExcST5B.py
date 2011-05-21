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

class ExcitationSystemsExcST5B(CorePowerSystemResource):

    def __init__(self, toc2=0.0, toc1=0.0, tc1=0.0, vrmin=0.0, tc2=0.0, kc=0.0, tb2=0.0, tob1=0.0, vrmax=0.0, tob2=0.0, tb1=0.0, tub1=0.0, tub2=0.0, tuc1=0.0, tuc2=0.0, kr=0.0, tr=0.0, t1=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcST5B' instance.

        @param toc2: 
        @param toc1: 
        @param tc1: 
        @param vrmin: 
        @param tc2: 
        @param kc: 
        @param tb2: 
        @param tob1: 
        @param vrmax: 
        @param tob2: 
        @param tb1: 
        @param tub1: 
        @param tub2: 
        @param tuc1: 
        @param tuc2: 
        @param kr: 
        @param tr: 
        @param t1: 
        """

        self.toc2 = toc2


        self.toc1 = toc1


        self.tc1 = tc1


        self.vrmin = vrmin


        self.tc2 = tc2


        self.kc = kc


        self.tb2 = tb2


        self.tob1 = tob1


        self.vrmax = vrmax


        self.tob2 = tob2


        self.tb1 = tb1


        self.tub1 = tub1


        self.tub2 = tub2


        self.tuc1 = tuc1


        self.tuc2 = tuc2


        self.kr = kr


        self.tr = tr


        self.t1 = t1

        super(ExcitationSystemsExcST5B, self).__init__(*args, **kw_args)

    _attrs = ["toc2", "toc1", "tc1", "vrmin", "tc2", "kc", "tb2", "tob1", "vrmax", "tob2", "tb1", "tub1", "tub2", "tuc1", "tuc2", "kr", "tr", "t1"]
    _attr_types = {"toc2": float, "toc1": float, "tc1": float, "vrmin": float, "tc2": float, "kc": float, "tb2": float, "tob1": float, "vrmax": float, "tob2": float, "tb1": float, "tub1": float, "tub2": float, "tuc1": float, "tuc2": float, "kr": float, "tr": float, "t1": float}
    _defaults = {"toc2": 0.0, "toc1": 0.0, "tc1": 0.0, "vrmin": 0.0, "tc2": 0.0, "kc": 0.0, "tb2": 0.0, "tob1": 0.0, "vrmax": 0.0, "tob2": 0.0, "tb1": 0.0, "tub1": 0.0, "tub2": 0.0, "tuc1": 0.0, "tuc2": 0.0, "kr": 0.0, "tr": 0.0, "t1": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

