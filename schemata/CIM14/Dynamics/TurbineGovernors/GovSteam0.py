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

class GovSteam0(TurbineGovernor):
    """A simplified steam turbine-governor model.
    """

    def __init__(self, t2=0.0, t1=0.0, vmin=0.0, dt=0.0, vmax=0.0, mwbase=0.0, r=0.0, t3=0.0, **kw_args):
        """Initializes a new 'GovSteam0' instance.

        @param t2: Numerator time constant of T2/T3 block 
        @param t1: Steam bowl time constant 
        @param vmin: Minimum valve position, p.u. of mwcap 
        @param dt: Turbine damping coefficient 
        @param vmax: Maximum valve position, p.u. of mwcap 
        @param mwbase: Base for power values  (&gt; 0.) 
        @param r: Permanent droop 
        @param t3: Reheater time constant 
        """
        #: Numerator time constant of T2/T3 block
        self.t2 = t2

        #: Steam bowl time constant
        self.t1 = t1

        #: Minimum valve position, p.u. of mwcap
        self.vmin = vmin

        #: Turbine damping coefficient
        self.dt = dt

        #: Maximum valve position, p.u. of mwcap
        self.vmax = vmax

        #: Base for power values  (&gt; 0.)
        self.mwbase = mwbase

        #: Permanent droop
        self.r = r

        #: Reheater time constant
        self.t3 = t3

        super(GovSteam0, self).__init__(**kw_args)

