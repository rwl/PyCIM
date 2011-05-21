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

class ExcST3A(ExcitationSystem):
    """IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A.
    """

    def __init__(self, kp=0.0, angp=0.0, xl=0.0, tc=0.0, tb=0.0, ki=0.0, vbmax=0.0, kc=0.0, vrmax=0.0, vimax=0.0, vgmax=0.0, km=0.0, vmmax=0.0, ka=0.0, tr=0.0, vrmin=0.0, kg=0.0, vimin=0.0, vmmin=0.0, tm=0.0, ta=0.0, *args, **kw_args):
        """Initialises a new 'ExcST3A' instance.

        @param kp: Potential source gain (&gt; 0.) 
        @param angp: Phase angle of potential source 
        @param xl: P-bar reactance (&gt;= 0.) 
        @param tc: AVR lead time constant 
        @param tb: AVR lag time constant (&gt;= 0.) 
        @param ki: Current source gain (&gt;= 0.) 
        @param vbmax: Maximum excitation voltage (&gt; 0.) 
        @param kc: Exciter regulation factor (&gt;= 0.) 
        @param vrmax: Maximum AVR output (&gt; 0.) 
        @param vimax: Maximum error (&gt; 0.) 
        @param vgmax: Maximum inner loop feedback voltage (&gt;= 0.) 
        @param km: Inner loop forward gain (&gt; 0.) 
        @param vmmax: Maximum inner loop output (&gt; 0.) 
        @param ka: AVR gain (&gt; 0.) 
        @param tr: Voltage transducer time constant (&gt;= 0.) 
        @param vrmin: Minimum AVR output (&lt; 0.) 
        @param kg: Inner loop feedback gain (&gt;= 0.) 
        @param vimin: Minimum error (&lt; 0.) 
        @param vmmin: Minimum inner loop output (&lt;= 0.) 
        @param tm: Inner loop time constant (&gt; 0.) 
        @param ta: AVR time constant (&gt;= 0.) 
        """
        #: Potential source gain (&gt; 0.)
        self.kp = kp

        #: Phase angle of potential source
        self.angp = angp

        #: P-bar reactance (&gt;= 0.)
        self.xl = xl

        #: AVR lead time constant
        self.tc = tc

        #: AVR lag time constant (&gt;= 0.)
        self.tb = tb

        #: Current source gain (&gt;= 0.)
        self.ki = ki

        #: Maximum excitation voltage (&gt; 0.)
        self.vbmax = vbmax

        #: Exciter regulation factor (&gt;= 0.)
        self.kc = kc

        #: Maximum AVR output (&gt; 0.)
        self.vrmax = vrmax

        #: Maximum error (&gt; 0.)
        self.vimax = vimax

        #: Maximum inner loop feedback voltage (&gt;= 0.)
        self.vgmax = vgmax

        #: Inner loop forward gain (&gt; 0.)
        self.km = km

        #: Maximum inner loop output (&gt; 0.)
        self.vmmax = vmmax

        #: AVR gain (&gt; 0.)
        self.ka = ka

        #: Voltage transducer time constant (&gt;= 0.)
        self.tr = tr

        #: Minimum AVR output (&lt; 0.)
        self.vrmin = vrmin

        #: Inner loop feedback gain (&gt;= 0.)
        self.kg = kg

        #: Minimum error (&lt; 0.)
        self.vimin = vimin

        #: Minimum inner loop output (&lt;= 0.)
        self.vmmin = vmmin

        #: Inner loop time constant (&gt; 0.)
        self.tm = tm

        #: AVR time constant (&gt;= 0.)
        self.ta = ta

        super(ExcST3A, self).__init__(*args, **kw_args)

    _attrs = ["kp", "angp", "xl", "tc", "tb", "ki", "vbmax", "kc", "vrmax", "vimax", "vgmax", "km", "vmmax", "ka", "tr", "vrmin", "kg", "vimin", "vmmin", "tm", "ta"]
    _attr_types = {"kp": float, "angp": float, "xl": float, "tc": float, "tb": float, "ki": float, "vbmax": float, "kc": float, "vrmax": float, "vimax": float, "vgmax": float, "km": float, "vmmax": float, "ka": float, "tr": float, "vrmin": float, "kg": float, "vimin": float, "vmmin": float, "tm": float, "ta": float}
    _defaults = {"kp": 0.0, "angp": 0.0, "xl": 0.0, "tc": 0.0, "tb": 0.0, "ki": 0.0, "vbmax": 0.0, "kc": 0.0, "vrmax": 0.0, "vimax": 0.0, "vgmax": 0.0, "km": 0.0, "vmmax": 0.0, "ka": 0.0, "tr": 0.0, "vrmin": 0.0, "kg": 0.0, "vimin": 0.0, "vmmin": 0.0, "tm": 0.0, "ta": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

