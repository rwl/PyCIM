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

class ExcitationSystemsExcST3A(CorePowerSystemResource):

    def __init__(self, vrmin=0.0, kc=0.0, ka=0.0, vbmax=0.0, vimin=0.0, xl=0.0, vgmax=0.0, angp=0.0, vmmin=0.0, vrmax=0.0, kp=0.0, km=0.0, vimax=0.0, tr=0.0, vmmax=0.0, ki=0.0, tm=0.0, ta=0.0, tb=0.0, kg=0.0, tc=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcST3A' instance.

        @param vrmin: 
        @param kc: 
        @param ka: 
        @param vbmax: 
        @param vimin: 
        @param xl: 
        @param vgmax: 
        @param angp: 
        @param vmmin: 
        @param vrmax: 
        @param kp: 
        @param km: 
        @param vimax: 
        @param tr: 
        @param vmmax: 
        @param ki: 
        @param tm: 
        @param ta: 
        @param tb: 
        @param kg: 
        @param tc: 
        """

        self.vrmin = vrmin


        self.kc = kc


        self.ka = ka


        self.vbmax = vbmax


        self.vimin = vimin


        self.xl = xl


        self.vgmax = vgmax


        self.angp = angp


        self.vmmin = vmmin


        self.vrmax = vrmax


        self.kp = kp


        self.km = km


        self.vimax = vimax


        self.tr = tr


        self.vmmax = vmmax


        self.ki = ki


        self.tm = tm


        self.ta = ta


        self.tb = tb


        self.kg = kg


        self.tc = tc

        super(ExcitationSystemsExcST3A, self).__init__(*args, **kw_args)

    _attrs = ["vrmin", "kc", "ka", "vbmax", "vimin", "xl", "vgmax", "angp", "vmmin", "vrmax", "kp", "km", "vimax", "tr", "vmmax", "ki", "tm", "ta", "tb", "kg", "tc"]
    _attr_types = {"vrmin": float, "kc": float, "ka": float, "vbmax": float, "vimin": float, "xl": float, "vgmax": float, "angp": float, "vmmin": float, "vrmax": float, "kp": float, "km": float, "vimax": float, "tr": float, "vmmax": float, "ki": float, "tm": float, "ta": float, "tb": float, "kg": float, "tc": float}
    _defaults = {"vrmin": 0.0, "kc": 0.0, "ka": 0.0, "vbmax": 0.0, "vimin": 0.0, "xl": 0.0, "vgmax": 0.0, "angp": 0.0, "vmmin": 0.0, "vrmax": 0.0, "kp": 0.0, "km": 0.0, "vimax": 0.0, "tr": 0.0, "vmmax": 0.0, "ki": 0.0, "tm": 0.0, "ta": 0.0, "tb": 0.0, "kg": 0.0, "tc": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

