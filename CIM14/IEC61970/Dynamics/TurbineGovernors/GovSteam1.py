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

from CIM14.IEC61970.Dynamics.TurbineGovernors.TurbineGovernor import TurbineGovernor

class GovSteam1(TurbineGovernor):
    """IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)
    """

    def __init__(self, gv1=0.0, pgv3=0.0, uo=0.0, k1=0.0, mwbase=0.0, k8=0.0, uc=0.0, gv5=0.0, k7=0.0, gv4=0.0, k=0.0, gv2=0.0, db2=0.0, pgv4=0.0, t6=0.0, k2=0.0, db1=0.0, t5=0.0, k5=0.0, pgv2=0.0, pgv1=0.0, t3=0.0, t1=0.0, k6=0.0, gv3=0.0, eps=0.0, gv6=0.0, t4=0.0, pgv6=0.0, pmin=0.0, k4=0.0, pgv5=0.0, pmax=0.0, t7=0.0, k3=0.0, t2=0.0, *args, **kw_args):
        """Initialises a new 'GovSteam1' instance.

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

        super(GovSteam1, self).__init__(*args, **kw_args)

    _attrs = ["gv1", "pgv3", "uo", "k1", "mwbase", "k8", "uc", "gv5", "k7", "gv4", "k", "gv2", "db2", "pgv4", "t6", "k2", "db1", "t5", "k5", "pgv2", "pgv1", "t3", "t1", "k6", "gv3", "eps", "gv6", "t4", "pgv6", "pmin", "k4", "pgv5", "pmax", "t7", "k3", "t2"]
    _attr_types = {"gv1": float, "pgv3": float, "uo": float, "k1": float, "mwbase": float, "k8": float, "uc": float, "gv5": float, "k7": float, "gv4": float, "k": float, "gv2": float, "db2": float, "pgv4": float, "t6": float, "k2": float, "db1": float, "t5": float, "k5": float, "pgv2": float, "pgv1": float, "t3": float, "t1": float, "k6": float, "gv3": float, "eps": float, "gv6": float, "t4": float, "pgv6": float, "pmin": float, "k4": float, "pgv5": float, "pmax": float, "t7": float, "k3": float, "t2": float}
    _defaults = {"gv1": 0.0, "pgv3": 0.0, "uo": 0.0, "k1": 0.0, "mwbase": 0.0, "k8": 0.0, "uc": 0.0, "gv5": 0.0, "k7": 0.0, "gv4": 0.0, "k": 0.0, "gv2": 0.0, "db2": 0.0, "pgv4": 0.0, "t6": 0.0, "k2": 0.0, "db1": 0.0, "t5": 0.0, "k5": 0.0, "pgv2": 0.0, "pgv1": 0.0, "t3": 0.0, "t1": 0.0, "k6": 0.0, "gv3": 0.0, "eps": 0.0, "gv6": 0.0, "t4": 0.0, "pgv6": 0.0, "pmin": 0.0, "k4": 0.0, "pgv5": 0.0, "pmax": 0.0, "t7": 0.0, "k3": 0.0, "t2": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

