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

class ExcitationSystemsExcAC4A(CorePowerSystemResource):

    def __init__(self, tb=0.0, ta=0.0, tc=0.0, vrmin=0.0, vimax=0.0, vrmax=0.0, tr=0.0, kc=0.0, vimin=0.0, ka=0.0, *args, **kw_args):
        """Initialises a new 'ExcitationSystemsExcAC4A' instance.

        @param tb: 
        @param ta: 
        @param tc: 
        @param vrmin: 
        @param vimax: 
        @param vrmax: 
        @param tr: 
        @param kc: 
        @param vimin: 
        @param ka: 
        """

        self.tb = tb


        self.ta = ta


        self.tc = tc


        self.vrmin = vrmin


        self.vimax = vimax


        self.vrmax = vrmax


        self.tr = tr


        self.kc = kc


        self.vimin = vimin


        self.ka = ka

        super(ExcitationSystemsExcAC4A, self).__init__(*args, **kw_args)

    _attrs = ["tb", "ta", "tc", "vrmin", "vimax", "vrmax", "tr", "kc", "vimin", "ka"]
    _attr_types = {"tb": float, "ta": float, "tc": float, "vrmin": float, "vimax": float, "vrmax": float, "tr": float, "kc": float, "vimin": float, "ka": float}
    _defaults = {"tb": 0.0, "ta": 0.0, "tc": 0.0, "vrmin": 0.0, "vimax": 0.0, "vrmax": 0.0, "tr": 0.0, "kc": 0.0, "vimin": 0.0, "ka": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

