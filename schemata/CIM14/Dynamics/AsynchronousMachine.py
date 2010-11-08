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

from CIM14.Dynamics.RotatingMachine import RotatingMachine

class AsynchronousMachine(RotatingMachine):
    """An asynchronous (induction) machine with no external connection to the rotor windings, e.g squirel-cage induction machine.
    """

    def __init__(self, xm=0.0, xs=0.0, xpp=0.0, xlr2=0.0, rr2=0.0, tpo=0.0, rr1=0.0, xp=0.0, tppo=0.0, xlr1=0.0, *args, **kw_args):
        """Initialises a new 'AsynchronousMachine' instance.

        @param xm: Magnetizing reactance 
        @param xs: Synchronous reactance (&gt;= Xp) 
        @param xpp: Sub-transient reactance (unsaturated) (&gt; Xl) 
        @param xlr2: Damper 2 winding leakage reactance 
        @param rr2: Damper 2 winding resistance 
        @param tpo: Transient rotor time constant (&gt; Tppo) 
        @param rr1: Damper 1 winding resistance 
        @param xp: Transient reactance (unsaturated) (&gt; =Xpp) 
        @param tppo: Sub-transient rotor time constant (&gt; 0.) 
        @param xlr1: Damper 1 winding leakage reactance 
        """
        #: Magnetizing reactance
        self.xm = xm

        #: Synchronous reactance (&gt;= Xp)
        self.xs = xs

        #: Sub-transient reactance (unsaturated) (&gt; Xl)
        self.xpp = xpp

        #: Damper 2 winding leakage reactance
        self.xlr2 = xlr2

        #: Damper 2 winding resistance
        self.rr2 = rr2

        #: Transient rotor time constant (&gt; Tppo)
        self.tpo = tpo

        #: Damper 1 winding resistance
        self.rr1 = rr1

        #: Transient reactance (unsaturated) (&gt; =Xpp)
        self.xp = xp

        #: Sub-transient rotor time constant (&gt; 0.)
        self.tppo = tppo

        #: Damper 1 winding leakage reactance
        self.xlr1 = xlr1

        super(AsynchronousMachine, self).__init__(*args, **kw_args)

    _attrs = ["xm", "xs", "xpp", "xlr2", "rr2", "tpo", "rr1", "xp", "tppo", "xlr1"]
    _attr_types = {"xm": float, "xs": float, "xpp": float, "xlr2": float, "rr2": float, "tpo": float, "rr1": float, "xp": float, "tppo": float, "xlr1": float}
    _defaults = {"xm": 0.0, "xs": 0.0, "xpp": 0.0, "xlr2": 0.0, "rr2": 0.0, "tpo": 0.0, "rr1": 0.0, "xp": 0.0, "tppo": 0.0, "xlr1": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

