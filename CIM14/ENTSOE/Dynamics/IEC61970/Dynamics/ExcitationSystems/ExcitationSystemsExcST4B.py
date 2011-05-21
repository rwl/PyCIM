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

class ExcitationSystemsExcST4B(CorePowerSystemResource):

    def __init__(self, kp=0.0, xl=0.0, vbmax=0.0, ki=0.0, kir=0.0, vrmin=0.0, vmmin=0.0, kim=0.0, ta=0.0, kg=0.0, tr=0.0, kc=0.0, vrmax=0.0, angp=0.0, kpr=0.0, vgmax=0.0, kpm=0.0, vmmax=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcST4B' instance.

        @param kp: 
        @param xl: 
        @param vbmax: 
        @param ki: 
        @param kir: 
        @param vrmin: 
        @param vmmin: 
        @param kim: 
        @param ta: 
        @param kg: 
        @param tr: 
        @param kc: 
        @param vrmax: 
        @param angp: 
        @param kpr: 
        @param vgmax: 
        @param kpm: 
        @param vmmax: 
        """

        self.kp = kp


        self.xl = xl


        self.vbmax = vbmax


        self.ki = ki


        self.kir = kir


        self.vrmin = vrmin


        self.vmmin = vmmin


        self.kim = kim


        self.ta = ta


        self.kg = kg


        self.tr = tr


        self.kc = kc


        self.vrmax = vrmax


        self.angp = angp


        self.kpr = kpr


        self.vgmax = vgmax


        self.kpm = kpm


        self.vmmax = vmmax

        super(ExcitationSystemsExcST4B, self).__init__(*args, **kw_args)

    _attrs = ["kp", "xl", "vbmax", "ki", "kir", "vrmin", "vmmin", "kim", "ta", "kg", "tr", "kc", "vrmax", "angp", "kpr", "vgmax", "kpm", "vmmax"]
    _attr_types = {"kp": float, "xl": float, "vbmax": float, "ki": float, "kir": float, "vrmin": float, "vmmin": float, "kim": float, "ta": float, "kg": float, "tr": float, "kc": float, "vrmax": float, "angp": float, "kpr": float, "vgmax": float, "kpm": float, "vmmax": float}
    _defaults = {"kp": 0.0, "xl": 0.0, "vbmax": 0.0, "ki": 0.0, "kir": 0.0, "vrmin": 0.0, "vmmin": 0.0, "kim": 0.0, "ta": 0.0, "kg": 0.0, "tr": 0.0, "kc": 0.0, "vrmax": 0.0, "angp": 0.0, "kpr": 0.0, "vgmax": 0.0, "kpm": 0.0, "vmmax": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

