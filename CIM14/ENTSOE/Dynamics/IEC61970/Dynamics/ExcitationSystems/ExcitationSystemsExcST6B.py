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

class ExcitationSystemsExcST6B(CorePowerSystemResource):

    def __init__(self, vamin=0.0, vrmin=0.0, km=0.0, ts=0.0, kg=0.0, tr=0.0, kcl=0.0, klr=0.0, vrmax=0.0, ilr=0.0, kpa=0.0, tg=0.0, vamax=0.0, oelin=0.0, kff=0.0, vmult=0.0, kia=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcST6B' instance.

        @param vamin: 
        @param vrmin: 
        @param km: 
        @param ts: 
        @param kg: 
        @param tr: 
        @param kcl: 
        @param klr: 
        @param vrmax: 
        @param ilr: 
        @param kpa: 
        @param tg: 
        @param vamax: 
        @param oelin: 
        @param kff: 
        @param vmult: 
        @param kia: 
        """

        self.vamin = vamin


        self.vrmin = vrmin


        self.km = km


        self.ts = ts


        self.kg = kg


        self.tr = tr


        self.kcl = kcl


        self.klr = klr


        self.vrmax = vrmax


        self.ilr = ilr


        self.kpa = kpa


        self.tg = tg


        self.vamax = vamax


        self.oelin = oelin


        self.kff = kff


        self.vmult = vmult


        self.kia = kia

        super(ExcitationSystemsExcST6B, self).__init__(*args, **kw_args)

    _attrs = ["vamin", "vrmin", "km", "ts", "kg", "tr", "kcl", "klr", "vrmax", "ilr", "kpa", "tg", "vamax", "oelin", "kff", "vmult", "kia"]
    _attr_types = {"vamin": float, "vrmin": float, "km": float, "ts": float, "kg": float, "tr": float, "kcl": float, "klr": float, "vrmax": float, "ilr": float, "kpa": float, "tg": float, "vamax": float, "oelin": float, "kff": float, "vmult": float, "kia": float}
    _defaults = {"vamin": 0.0, "vrmin": 0.0, "km": 0.0, "ts": 0.0, "kg": 0.0, "tr": 0.0, "kcl": 0.0, "klr": 0.0, "vrmax": 0.0, "ilr": 0.0, "kpa": 0.0, "tg": 0.0, "vamax": 0.0, "oelin": 0.0, "kff": 0.0, "vmult": 0.0, "kia": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

