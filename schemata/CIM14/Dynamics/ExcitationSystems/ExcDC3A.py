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

class ExcDC3A(ExcitationSystem):
    """IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.
    """

    def __init__(self, e1=0.0, vrmax=0.0, te=0.0, ke=0.0, tr=0.0, se2=0.0, trh=0.0, vrmin=0.0, exclim=0.0, e2=0.0, kv=0.0, se1=0.0, **kw_args):
        """Initializes a new 'ExcDC3A' instance.

        @param e1: Field voltage value 1    (&gt; 0.) 
        @param vrmax: Maximum control element output (&gt; 0.) 
        @param te: Exciter field time constant (&gt; 0.) 
        @param ke: Exciter field resistance line slope 
        @param tr: Filter  time constant (&gt;= 0.) 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param trh: Rheostat full range travel time (&gt; 0.) 
        @param vrmin: Minimum control element output (&lt;= 0.) 
        @param exclim: If not 0, apply lower limit of 0. to exciter output 
        @param e2: Field voltage value 2.     (&gt; 0.) 
        @param kv: Voltage error threshold min/max control action (&gt; 0.) 
        @param se1: Saturation factor at e1 (&gt;= 0.) 
        """
        #: Field voltage value 1    (&gt; 0.)
        self.e1 = e1

        #: Maximum control element output (&gt; 0.)
        self.vrmax = vrmax

        #: Exciter field time constant (&gt; 0.)
        self.te = te

        #: Exciter field resistance line slope
        self.ke = ke

        #: Filter  time constant (&gt;= 0.)
        self.tr = tr

        #: Saturation factor at e2  (&gt;= 0.)
        self.se2 = se2

        #: Rheostat full range travel time (&gt; 0.)
        self.trh = trh

        #: Minimum control element output (&lt;= 0.)
        self.vrmin = vrmin

        #: If not 0, apply lower limit of 0. to exciter output
        self.exclim = exclim

        #: Field voltage value 2.     (&gt; 0.)
        self.e2 = e2

        #: Voltage error threshold min/max control action (&gt; 0.)
        self.kv = kv

        #: Saturation factor at e1 (&gt;= 0.)
        self.se1 = se1

        super(ExcDC3A, self).__init__(**kw_args)

