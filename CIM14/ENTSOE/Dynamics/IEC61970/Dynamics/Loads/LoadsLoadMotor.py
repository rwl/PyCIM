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

class LoadsLoadMotor(CorePowerSystemResource):

    def __init__(self, lfac=0.0, ra=0.0, d=0.0, ls=0.0, tppo=0.0, tbkr=0.0, lpp=0.0, tpo=0.0, lp=0.0, h=0.0, vt=0.0, pfrac=0.0, tv=0.0, *args, **kw_args):
        """Initialises a new 'LoadsLoadMotor' instance.

        @param lfac: 
        @param ra: 
        @param d: 
        @param ls: 
        @param tppo: 
        @param tbkr: 
        @param lpp: 
        @param tpo: 
        @param lp: 
        @param h: 
        @param vt: 
        @param pfrac: 
        @param tv: 
        """

        self.lfac = lfac


        self.ra = ra


        self.d = d


        self.ls = ls


        self.tppo = tppo


        self.tbkr = tbkr


        self.lpp = lpp


        self.tpo = tpo


        self.lp = lp


        self.h = h


        self.vt = vt


        self.pfrac = pfrac


        self.tv = tv

        super(LoadsLoadMotor, self).__init__(*args, **kw_args)

    _attrs = ["lfac", "ra", "d", "ls", "tppo", "tbkr", "lpp", "tpo", "lp", "h", "vt", "pfrac", "tv"]
    _attr_types = {"lfac": float, "ra": float, "d": float, "ls": float, "tppo": float, "tbkr": float, "lpp": float, "tpo": float, "lp": float, "h": float, "vt": float, "pfrac": float, "tv": float}
    _defaults = {"lfac": 0.0, "ra": 0.0, "d": 0.0, "ls": 0.0, "tppo": 0.0, "tbkr": 0.0, "lpp": 0.0, "tpo": 0.0, "lp": 0.0, "h": 0.0, "vt": 0.0, "pfrac": 0.0, "tv": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

