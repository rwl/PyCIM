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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CorePowerSystemResource import CorePowerSystemResource

class TurbineGovernorsGovSteam0(CorePowerSystemResource):

    def __init__(self, t2=0.0, t3=0.0, t1=0.0, vmax=0.0, dt=0.0, r=0.0, vmin=0.0, mwbase=0.0, *args, **kw_args):
        """Initialises a new 'TurbineGovernorsGovSteam0' instance.

        @param t2: 
        @param t3: 
        @param t1: 
        @param vmax: 
        @param dt: 
        @param r: 
        @param vmin: 
        @param mwbase: 
        """

        self.t2 = t2


        self.t3 = t3


        self.t1 = t1


        self.vmax = vmax


        self.dt = dt


        self.r = r


        self.vmin = vmin


        self.mwbase = mwbase

        super(TurbineGovernorsGovSteam0, self).__init__(*args, **kw_args)

    _attrs = ["t2", "t3", "t1", "vmax", "dt", "r", "vmin", "mwbase"]
    _attr_types = {"t2": float, "t3": float, "t1": float, "vmax": float, "dt": float, "r": float, "vmin": float, "mwbase": float}
    _defaults = {"t2": 0.0, "t3": 0.0, "t1": 0.0, "vmax": 0.0, "dt": 0.0, "r": 0.0, "vmin": 0.0, "mwbase": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

