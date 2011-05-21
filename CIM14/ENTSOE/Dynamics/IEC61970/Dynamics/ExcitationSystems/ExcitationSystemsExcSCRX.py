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

class ExcitationSystemsExcSCRX(CorePowerSystemResource):

    def __init__(self, te=0.0, tb=0.0, emax=0.0, cswitch=False, rcrfd=0.0, tatb=0.0, k=0.0, emin=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcSCRX' instance.

        @param te: 
        @param tb: 
        @param emax: 
        @param cswitch: 
        @param rcrfd: 
        @param tatb: 
        @param k: 
        @param emin: 
        """

        self.te = te


        self.tb = tb


        self.emax = emax


        self.cswitch = cswitch


        self.rcrfd = rcrfd


        self.tatb = tatb


        self.k = k


        self.emin = emin

        super(ExcitationSystemsExcSCRX, self).__init__(*args, **kw_args)

    _attrs = ["te", "tb", "emax", "cswitch", "rcrfd", "tatb", "k", "emin"]
    _attr_types = {"te": float, "tb": float, "emax": float, "cswitch": bool, "rcrfd": float, "tatb": float, "k": float, "emin": float}
    _defaults = {"te": 0.0, "tb": 0.0, "emax": 0.0, "cswitch": False, "rcrfd": 0.0, "tatb": 0.0, "k": 0.0, "emin": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

