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

from CIM14.IEC61970.Dynamics.ExcitationSystems.ExcitationSystem import ExcitationSystem

class ExcST4B(ExcitationSystem):
    """IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally.
    """

    def __init__(self, kp=0.0, kim=0.0, vbmax=0.0, kc=0.0, kpr=0.0, xl=0.0, vgmax=0.0, vmmin=0.0, kg=0.0, vmmax=0.0, tr=0.0, ta=0.0, kpm=0.0, angp=0.0, vrmin=0.0, kir=0.0, vrmax=0.0, ki=0.0, *args, **kw_args):
        """Initialises a new 'ExcST4B' instance.

        @param kp: Potential source gain (&gt; 0.) 
        @param kim: Integral gain of inner loop regulator 
        @param vbmax: Maximum excitation voltage (&gt; 0.) 
        @param kc: Exciter regulation factor (&gt;= 0.) 
        @param kpr: AVR proportional gain 
        @param xl: P-bar leakage reactance (&gt;= 0.) 
        @param vgmax: Maximum inner loop feedback gain (&gt;= 0.) 
        @param vmmin: Minimum inner loop regulator output 
        @param kg: Inner loop feedback gain (&gt;= 0.) 
        @param vmmax: Maximum inner loop regulator output 
        @param tr: Voltage transducer time constant (&gt;= 0.) 
        @param ta: AVR time constant (&gt;= 0.) 
        @param kpm: Prop. gain of inner loop regulator 
        @param angp: Phase angle of potential source 
        @param vrmin: Minimum AVR output (&lt; 0.) 
        @param kir: AVR Integral gain 
        @param vrmax: Maximum AVR output (&gt; 0.) 
        @param ki: Current source gain (&gt;= 0.) 
        """
        #: Potential source gain (&gt; 0.)
        self.kp = kp

        #: Integral gain of inner loop regulator
        self.kim = kim

        #: Maximum excitation voltage (&gt; 0.)
        self.vbmax = vbmax

        #: Exciter regulation factor (&gt;= 0.)
        self.kc = kc

        #: AVR proportional gain
        self.kpr = kpr

        #: P-bar leakage reactance (&gt;= 0.)
        self.xl = xl

        #: Maximum inner loop feedback gain (&gt;= 0.)
        self.vgmax = vgmax

        #: Minimum inner loop regulator output
        self.vmmin = vmmin

        #: Inner loop feedback gain (&gt;= 0.)
        self.kg = kg

        #: Maximum inner loop regulator output
        self.vmmax = vmmax

        #: Voltage transducer time constant (&gt;= 0.)
        self.tr = tr

        #: AVR time constant (&gt;= 0.)
        self.ta = ta

        #: Prop. gain of inner loop regulator
        self.kpm = kpm

        #: Phase angle of potential source
        self.angp = angp

        #: Minimum AVR output (&lt; 0.)
        self.vrmin = vrmin

        #: AVR Integral gain
        self.kir = kir

        #: Maximum AVR output (&gt; 0.)
        self.vrmax = vrmax

        #: Current source gain (&gt;= 0.)
        self.ki = ki

        super(ExcST4B, self).__init__(*args, **kw_args)

    _attrs = ["kp", "kim", "vbmax", "kc", "kpr", "xl", "vgmax", "vmmin", "kg", "vmmax", "tr", "ta", "kpm", "angp", "vrmin", "kir", "vrmax", "ki"]
    _attr_types = {"kp": float, "kim": float, "vbmax": float, "kc": float, "kpr": float, "xl": float, "vgmax": float, "vmmin": float, "kg": float, "vmmax": float, "tr": float, "ta": float, "kpm": float, "angp": float, "vrmin": float, "kir": float, "vrmax": float, "ki": float}
    _defaults = {"kp": 0.0, "kim": 0.0, "vbmax": 0.0, "kc": 0.0, "kpr": 0.0, "xl": 0.0, "vgmax": 0.0, "vmmin": 0.0, "kg": 0.0, "vmmax": 0.0, "tr": 0.0, "ta": 0.0, "kpm": 0.0, "angp": 0.0, "vrmin": 0.0, "kir": 0.0, "vrmax": 0.0, "ki": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

