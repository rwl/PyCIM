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

from CIM14.Dynamics.TurbineGovernors.TurbineGovernor import TurbineGovernor

class GovSteam1(TurbineGovernor):
    """IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)
    """

    def __init__(self, gv1=0.0, pgv3=0.0, uo=0.0, k1=0.0, mwbase=0.0, k8=0.0, uc=0.0, gv5=0.0, k7=0.0, gv4=0.0, k=0.0, gv2=0.0, db2=0.0, pgv4=0.0, t6=0.0, k2=0.0, db1=0.0, t5=0.0, k5=0.0, pgv2=0.0, pgv1=0.0, t3=0.0, t1=0.0, k6=0.0, gv3=0.0, eps=0.0, gv6=0.0, t4=0.0, pgv6=0.0, pmin=0.0, k4=0.0, pgv5=0.0, pmax=0.0, t7=0.0, k3=0.0, t2=0.0, **kw_args):
        """Initializes a new 'GovSteam1' instance.

        @param gv1: Nonlinear gain valve position point 1 
        @param pgv3: Nonlinear gain power value point 3 
        @param uo: Maximum valve opening velocity (&gt; 0.) 
        @param k1: Fraction of HP shaft power after first boiler pass 
        @param mwbase: Base for power values (&gt; 0.) 
        @param k8: Fraction of LP shaft power after fourth boiler pass 
        @param uc: Maximum valve closing velocity, p.u./sec (&lt; 0.) 
        @param gv5: Nonlinear gain valve position point 5 
        @param k7: Fraction of HP shaft power after fourth boiler pass 
        @param gv4: Nonlinear gain valve position point 4 
        @param k: Governor gain (reciprocal of droop) (&gt; 0.) 
        @param gv2: Nonlinear gain valve position point 2 
        @param db2: Unintentional deadband 
        @param pgv4: Nonlinear gain power value point 4 
        @param t6: Time constant of third boiler pass 
        @param k2: Fraction of LP shaft power after first boiler pass 
        @param db1: Intentional deadband width 
        @param t5: Time constant of second boiler pass 
        @param k5: Fraction of HP shaft power after third boiler pass 
        @param pgv2: Nonlinear gain power value point 2 
        @param pgv1: Nonlinear gain power value point 1 
        @param t3: Valve positioner time constant (&gt; 0.) 
        @param t1: Governor lag time constant 
        @param k6: Fraction of LP shaft power after third boiler pass 
        @param gv3: Nonlinear gain valve position point 3 
        @param eps: Intentional db hysteresis 
        @param gv6: Nonlinear gain valve position point 6 
        @param t4: Inlet piping/steam bowl time constant 
        @param pgv6: Nonlinear gain power value point 6 
        @param pmin: Minimum valve opening (&gt;= 0.) 
        @param k4: Fraction of LP shaft power after second boiler pass 
        @param pgv5: Nonlinear gain power value point 5 
        @param pmax: Maximum valve opening (&gt; Pmin) 
        @param t7: Time constant of fourth boiler pas 
        @param k3: Fraction of HP shaft power after second boiler pass 
        @param t2: Governor lead time constant 
        """
        #: Nonlinear gain valve position point 1
        self.gv1 = gv1

        #: Nonlinear gain power value point 3
        self.pgv3 = pgv3

        #: Maximum valve opening velocity (&gt; 0.)
        self.uo = uo

        #: Fraction of HP shaft power after first boiler pass
        self.k1 = k1

        #: Base for power values (&gt; 0.)
        self.mwbase = mwbase

        #: Fraction of LP shaft power after fourth boiler pass
        self.k8 = k8

        #: Maximum valve closing velocity, p.u./sec (&lt; 0.)
        self.uc = uc

        #: Nonlinear gain valve position point 5
        self.gv5 = gv5

        #: Fraction of HP shaft power after fourth boiler pass
        self.k7 = k7

        #: Nonlinear gain valve position point 4
        self.gv4 = gv4

        #: Governor gain (reciprocal of droop) (&gt; 0.)
        self.k = k

        #: Nonlinear gain valve position point 2
        self.gv2 = gv2

        #: Unintentional deadband
        self.db2 = db2

        #: Nonlinear gain power value point 4
        self.pgv4 = pgv4

        #: Time constant of third boiler pass
        self.t6 = t6

        #: Fraction of LP shaft power after first boiler pass
        self.k2 = k2

        #: Intentional deadband width
        self.db1 = db1

        #: Time constant of second boiler pass
        self.t5 = t5

        #: Fraction of HP shaft power after third boiler pass
        self.k5 = k5

        #: Nonlinear gain power value point 2
        self.pgv2 = pgv2

        #: Nonlinear gain power value point 1
        self.pgv1 = pgv1

        #: Valve positioner time constant (&gt; 0.)
        self.t3 = t3

        #: Governor lag time constant
        self.t1 = t1

        #: Fraction of LP shaft power after third boiler pass
        self.k6 = k6

        #: Nonlinear gain valve position point 3
        self.gv3 = gv3

        #: Intentional db hysteresis
        self.eps = eps

        #: Nonlinear gain valve position point 6
        self.gv6 = gv6

        #: Inlet piping/steam bowl time constant
        self.t4 = t4

        #: Nonlinear gain power value point 6
        self.pgv6 = pgv6

        #: Minimum valve opening (&gt;= 0.)
        self.pmin = pmin

        #: Fraction of LP shaft power after second boiler pass
        self.k4 = k4

        #: Nonlinear gain power value point 5
        self.pgv5 = pgv5

        #: Maximum valve opening (&gt; Pmin)
        self.pmax = pmax

        #: Time constant of fourth boiler pas
        self.t7 = t7

        #: Fraction of HP shaft power after second boiler pass
        self.k3 = k3

        #: Governor lead time constant
        self.t2 = t2

        super(GovSteam1, self).__init__(**kw_args)

