# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.Dynamics.ExcitationSystems.ExcitationSystem import ExcitationSystem

class ExcDC4B(ExcitationSystem):
    """IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model.
    """

    def __init__(self, e1=0.0, se2=0.0, tf=0.0, oelin=0.0, ki=0.0, ta=0.0, vrmax=0.0, tr=0.0, kf=0.0, vrmin=0.0, te=0.0, ka=0.0, kp=0.0, td=0.0, kd=0.0, vemin=0.0, ke=0.0, se1=0.0, e2=0.0, uelin=0.0, **kw_args):
        """Initializes a new 'ExcDC4B' instance.

        @param e1: Field voltage value 1     (&gt; 0.) 
        @param se2: Saturation factor at e2 (&gt;= 0.) 
        @param tf: Rate feedback time constant (&gt;= 0.) 
        @param oelin: OEL input: if &lt; 2, LV gate; if = 2, subtract from error signal 
        @param ki: Integral gain (&gt;= 0.) 
        @param ta: Time constant (&gt; 0.) 
        @param vrmax: Maximum controller output 
        @param tr: Filter time constant (&gt;= 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param vrmin: Minimum controller output (&lt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param kp: Proportional gain (&gt;= 0.) 
        @param td: Derivative time constant (&gt; 0. If kd &gt; 0.) 
        @param kd: Derivative gain (&gt;= 0.) 
        @param vemin: Exciter minimum output  (&lt;= 0.) 
        @param ke: Exciter field resistance line slope 
        @param se1: Saturation factor at e1   (&gt;= 0.) 
        @param e2: Field voltage value 2.   (&gt; 0.) 
        @param uelin: UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        """
        #: Field voltage value 1     (&gt; 0.)
        self.e1 = e1

        #: Saturation factor at e2 (&gt;= 0.)
        self.se2 = se2

        #: Rate feedback time constant (&gt;= 0.)
        self.tf = tf

        #: OEL input: if &lt; 2, LV gate; if = 2, subtract from error signal
        self.oelin = oelin

        #: Integral gain (&gt;= 0.)
        self.ki = ki

        #: Time constant (&gt; 0.)
        self.ta = ta

        #: Maximum controller output
        self.vrmax = vrmax

        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Rate feedback gain (&gt;= 0.)
        self.kf = kf

        #: Minimum controller output (&lt;= 0.)
        self.vrmin = vrmin

        #: Exciter time constant (&gt; 0.)
        self.te = te

        #: Gain (&gt; 0.)
        self.ka = ka

        #: Proportional gain (&gt;= 0.)
        self.kp = kp

        #: Derivative time constant (&gt; 0. If kd &gt; 0.)
        self.td = td

        #: Derivative gain (&gt;= 0.)
        self.kd = kd

        #: Exciter minimum output  (&lt;= 0.)
        self.vemin = vemin

        #: Exciter field resistance line slope
        self.ke = ke

        #: Saturation factor at e1   (&gt;= 0.)
        self.se1 = se1

        #: Field voltage value 2.   (&gt; 0.)
        self.e2 = e2

        #: UEL input: if &lt; 2, HV gate; if = 2, add to error signal
        self.uelin = uelin

        super(ExcDC4B, self).__init__(**kw_args)

