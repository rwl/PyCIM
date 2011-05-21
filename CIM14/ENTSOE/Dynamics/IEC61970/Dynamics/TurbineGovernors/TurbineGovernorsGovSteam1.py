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

class TurbineGovernorsGovSteam1(CorePowerSystemResource):

    def __init__(self, eps=0.0, uc=0.0, mwbase=0.0, pmin=0.0, k3=0.0, k=0.0, k2=0.0, k1=0.0, pgv1=0.0, k7=0.0, k6=0.0, pmax=0.0, k5=0.0, k4=0.0, gv6=0.0, t6=0.0, pgv6=0.0, t7=0.0, gv5=0.0, k8=0.0, gv1=0.0, t1=0.0, t2=0.0, pgv3=0.0, db1=0.0, t3=0.0, uo=0.0, pgv2=0.0, gv4=0.0, pgv5=0.0, t4=0.0, gv2=0.0, gv3=0.0, t5=0.0, pgv4=0.0, db2=0.0, *args, **kw_args):
        """Initialises a new 'TurbineGovernorsGovSteam1' instance.

        @param eps: 
        @param uc: 
        @param mwbase: 
        @param pmin: 
        @param k3: 
        @param k: 
        @param k2: 
        @param k1: 
        @param pgv1: 
        @param k7: 
        @param k6: 
        @param pmax: 
        @param k5: 
        @param k4: 
        @param gv6: 
        @param t6: 
        @param pgv6: 
        @param t7: 
        @param gv5: 
        @param k8: 
        @param gv1: 
        @param t1: 
        @param t2: 
        @param pgv3: 
        @param db1: 
        @param t3: 
        @param uo: 
        @param pgv2: 
        @param gv4: 
        @param pgv5: 
        @param t4: 
        @param gv2: 
        @param gv3: 
        @param t5: 
        @param pgv4: 
        @param db2: 
        """

        self.eps = eps


        self.uc = uc


        self.mwbase = mwbase


        self.pmin = pmin


        self.k3 = k3


        self.k = k


        self.k2 = k2


        self.k1 = k1


        self.pgv1 = pgv1


        self.k7 = k7


        self.k6 = k6


        self.pmax = pmax


        self.k5 = k5


        self.k4 = k4


        self.gv6 = gv6


        self.t6 = t6


        self.pgv6 = pgv6


        self.t7 = t7


        self.gv5 = gv5


        self.k8 = k8


        self.gv1 = gv1


        self.t1 = t1


        self.t2 = t2


        self.pgv3 = pgv3


        self.db1 = db1


        self.t3 = t3


        self.uo = uo


        self.pgv2 = pgv2


        self.gv4 = gv4


        self.pgv5 = pgv5


        self.t4 = t4


        self.gv2 = gv2


        self.gv3 = gv3


        self.t5 = t5


        self.pgv4 = pgv4


        self.db2 = db2

        super(TurbineGovernorsGovSteam1, self).__init__(*args, **kw_args)

    _attrs = ["eps", "uc", "mwbase", "pmin", "k3", "k", "k2", "k1", "pgv1", "k7", "k6", "pmax", "k5", "k4", "gv6", "t6", "pgv6", "t7", "gv5", "k8", "gv1", "t1", "t2", "pgv3", "db1", "t3", "uo", "pgv2", "gv4", "pgv5", "t4", "gv2", "gv3", "t5", "pgv4", "db2"]
    _attr_types = {"eps": float, "uc": float, "mwbase": float, "pmin": float, "k3": float, "k": float, "k2": float, "k1": float, "pgv1": float, "k7": float, "k6": float, "pmax": float, "k5": float, "k4": float, "gv6": float, "t6": float, "pgv6": float, "t7": float, "gv5": float, "k8": float, "gv1": float, "t1": float, "t2": float, "pgv3": float, "db1": float, "t3": float, "uo": float, "pgv2": float, "gv4": float, "pgv5": float, "t4": float, "gv2": float, "gv3": float, "t5": float, "pgv4": float, "db2": float}
    _defaults = {"eps": 0.0, "uc": 0.0, "mwbase": 0.0, "pmin": 0.0, "k3": 0.0, "k": 0.0, "k2": 0.0, "k1": 0.0, "pgv1": 0.0, "k7": 0.0, "k6": 0.0, "pmax": 0.0, "k5": 0.0, "k4": 0.0, "gv6": 0.0, "t6": 0.0, "pgv6": 0.0, "t7": 0.0, "gv5": 0.0, "k8": 0.0, "gv1": 0.0, "t1": 0.0, "t2": 0.0, "pgv3": 0.0, "db1": 0.0, "t3": 0.0, "uo": 0.0, "pgv2": 0.0, "gv4": 0.0, "pgv5": 0.0, "t4": 0.0, "gv2": 0.0, "gv3": 0.0, "t5": 0.0, "pgv4": 0.0, "db2": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

