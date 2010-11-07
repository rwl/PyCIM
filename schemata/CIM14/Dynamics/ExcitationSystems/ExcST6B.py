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

class ExcST6B(ExcitationSystem):
    """IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.
    """

    def __init__(self, tr=0.0, ilr=0.0, vrmin=0.0, vmult=0.0, vrmax=0.0, oelin=0.0, klr=0.0, kg=0.0, kpa=0.0, vamax=0.0, ts=0.0, kcl=0.0, tg=0.0, vamin=0.0, kia=0.0, kff=0.0, km=0.0, **kw_args):
        """Initializes a new 'ExcST6B' instance.

        @param tr: Filter time constant (&gt;= 0.) 
        @param ilr: Field current limiter setpoint (&gt; 0.) 
        @param vrmin: Minimum regulator output (&lt; 0.) 
        @param vmult: If non-zero, multiply regulator output by terminal voltage 
        @param vrmax: Maximum regulator output (&gt; 0.) 
        @param oelin: OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input 
        @param klr: Field current limiter gain (&gt; 0.) 
        @param kg: Feedback gain (&gt;= 0.) 
        @param kpa: Regulator proportional gain (&gt; 0.) 
        @param vamax: PI maximum output. (&gt; 0.) 
        @param ts: Rectifier firing time constant (not in IEEE model) (&gt;= 0.) 
        @param kcl: Field current limiter conversion factor (&gt; 0.) 
        @param tg: Feedback time constant (&gt;= 0.) 
        @param vamin: PI minimum output (&lt; 0.) 
        @param kia: Regulator integral gain (&gt; 0.) 
        @param kff: Feedforward gain 
        @param km: Main gain 
        """
        #: Filter time constant (&gt;= 0.)
        self.tr = tr

        #: Field current limiter setpoint (&gt; 0.)
        self.ilr = ilr

        #: Minimum regulator output (&lt; 0.)
        self.vrmin = vrmin

        #: If non-zero, multiply regulator output by terminal voltage
        self.vmult = vmult

        #: Maximum regulator output (&gt; 0.)
        self.vrmax = vrmax

        #: OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input
        self.oelin = oelin

        #: Field current limiter gain (&gt; 0.)
        self.klr = klr

        #: Feedback gain (&gt;= 0.)
        self.kg = kg

        #: Regulator proportional gain (&gt; 0.)
        self.kpa = kpa

        #: PI maximum output. (&gt; 0.)
        self.vamax = vamax

        #: Rectifier firing time constant (not in IEEE model) (&gt;= 0.)
        self.ts = ts

        #: Field current limiter conversion factor (&gt; 0.)
        self.kcl = kcl

        #: Feedback time constant (&gt;= 0.)
        self.tg = tg

        #: PI minimum output (&lt; 0.)
        self.vamin = vamin

        #: Regulator integral gain (&gt; 0.)
        self.kia = kia

        #: Feedforward gain
        self.kff = kff

        #: Main gain
        self.km = km

        super(ExcST6B, self).__init__(**kw_args)

