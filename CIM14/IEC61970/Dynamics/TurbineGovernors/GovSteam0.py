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

class GovSteam0(TurbineGovernor):
    """A simplified steam turbine-governor model.
    """

    def __init__(self, t2=0.0, t1=0.0, vmin=0.0, dt=0.0, vmax=0.0, mwbase=0.0, r=0.0, t3=0.0, *args, **kw_args):
        """Initialises a new 'GovSteam0' instance.

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

        super(GovSteam0, self).__init__(*args, **kw_args)

    _attrs = ["t2", "t1", "vmin", "dt", "vmax", "mwbase", "r", "t3"]
    _attr_types = {"t2": float, "t1": float, "vmin": float, "dt": float, "vmax": float, "mwbase": float, "r": float, "t3": float}
    _defaults = {"t2": 0.0, "t1": 0.0, "vmin": 0.0, "dt": 0.0, "vmax": 0.0, "mwbase": 0.0, "r": 0.0, "t3": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

