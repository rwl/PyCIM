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

class ExcitationSystemsExcST7B(CorePowerSystemResource):

    def __init__(self, tg=0.0, kpa=0.0, vmin=0.0, vrmax=0.0, kl=0.0, tr=0.0, kh=0.0, ts=0.0, vrmin=0.0, oelin=0.0, uelin=0.0, tia=0.0, tb=0.0, tc=0.0, tf=0.0, kia=0.0, vmax=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcST7B' instance.

        @param tg: 
        @param kpa: 
        @param vmin: 
        @param vrmax: 
        @param kl: 
        @param tr: 
        @param kh: 
        @param ts: 
        @param vrmin: 
        @param oelin: 
        @param uelin: 
        @param tia: 
        @param tb: 
        @param tc: 
        @param tf: 
        @param kia: 
        @param vmax: 
        """

        self.tg = tg


        self.kpa = kpa


        self.vmin = vmin


        self.vrmax = vrmax


        self.kl = kl


        self.tr = tr


        self.kh = kh


        self.ts = ts


        self.vrmin = vrmin


        self.oelin = oelin


        self.uelin = uelin


        self.tia = tia


        self.tb = tb


        self.tc = tc


        self.tf = tf


        self.kia = kia


        self.vmax = vmax

        super(ExcitationSystemsExcST7B, self).__init__(*args, **kw_args)

    _attrs = ["tg", "kpa", "vmin", "vrmax", "kl", "tr", "kh", "ts", "vrmin", "oelin", "uelin", "tia", "tb", "tc", "tf", "kia", "vmax"]
    _attr_types = {"tg": float, "kpa": float, "vmin": float, "vrmax": float, "kl": float, "tr": float, "kh": float, "ts": float, "vrmin": float, "oelin": float, "uelin": float, "tia": float, "tb": float, "tc": float, "tf": float, "kia": float, "vmax": float}
    _defaults = {"tg": 0.0, "kpa": 0.0, "vmin": 0.0, "vrmax": 0.0, "kl": 0.0, "tr": 0.0, "kh": 0.0, "ts": 0.0, "vrmin": 0.0, "oelin": 0.0, "uelin": 0.0, "tia": 0.0, "tb": 0.0, "tc": 0.0, "tf": 0.0, "kia": 0.0, "vmax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

