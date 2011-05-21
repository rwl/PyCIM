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

class TurbineGovernorsGovHydro2(CorePowerSystemResource):

    def __init__(self, bturb=0.0, rtemp=0.0, tw=0.0, rperm=0.0, gv1=0.0, gv2=0.0, tr=0.0, aturb=0.0, tp=0.0, uo=0.0, gv6=0.0, gv5=0.0, pgv5=0.0, gv4=0.0, pgv6=0.0, gv3=0.0, pgv2=0.0, pgv1=0.0, db1=0.0, pgv4=0.0, kturb=0.0, db2=0.0, tg=0.0, pmax=0.0, pgv3=0.0, mwbase=0.0, uc=0.0, pmin=0.0, eps=0.0, *args, **kw_args):
        """Initialises a new 'TurbineGovernorsGovHydro2' instance.

        @param bturb: 
        @param rtemp: 
        @param tw: 
        @param rperm: 
        @param gv1: 
        @param gv2: 
        @param tr: 
        @param aturb: 
        @param tp: 
        @param uo: 
        @param gv6: 
        @param gv5: 
        @param pgv5: 
        @param gv4: 
        @param pgv6: 
        @param gv3: 
        @param pgv2: 
        @param pgv1: 
        @param db1: 
        @param pgv4: 
        @param kturb: 
        @param db2: 
        @param tg: 
        @param pmax: 
        @param pgv3: 
        @param mwbase: 
        @param uc: 
        @param pmin: 
        @param eps: 
        """

        self.bturb = bturb


        self.rtemp = rtemp


        self.tw = tw


        self.rperm = rperm


        self.gv1 = gv1


        self.gv2 = gv2


        self.tr = tr


        self.aturb = aturb


        self.tp = tp


        self.uo = uo


        self.gv6 = gv6


        self.gv5 = gv5


        self.pgv5 = pgv5


        self.gv4 = gv4


        self.pgv6 = pgv6


        self.gv3 = gv3


        self.pgv2 = pgv2


        self.pgv1 = pgv1


        self.db1 = db1


        self.pgv4 = pgv4


        self.kturb = kturb


        self.db2 = db2


        self.tg = tg


        self.pmax = pmax


        self.pgv3 = pgv3


        self.mwbase = mwbase


        self.uc = uc


        self.pmin = pmin


        self.eps = eps

        super(TurbineGovernorsGovHydro2, self).__init__(*args, **kw_args)

    _attrs = ["bturb", "rtemp", "tw", "rperm", "gv1", "gv2", "tr", "aturb", "tp", "uo", "gv6", "gv5", "pgv5", "gv4", "pgv6", "gv3", "pgv2", "pgv1", "db1", "pgv4", "kturb", "db2", "tg", "pmax", "pgv3", "mwbase", "uc", "pmin", "eps"]
    _attr_types = {"bturb": float, "rtemp": float, "tw": float, "rperm": float, "gv1": float, "gv2": float, "tr": float, "aturb": float, "tp": float, "uo": float, "gv6": float, "gv5": float, "pgv5": float, "gv4": float, "pgv6": float, "gv3": float, "pgv2": float, "pgv1": float, "db1": float, "pgv4": float, "kturb": float, "db2": float, "tg": float, "pmax": float, "pgv3": float, "mwbase": float, "uc": float, "pmin": float, "eps": float}
    _defaults = {"bturb": 0.0, "rtemp": 0.0, "tw": 0.0, "rperm": 0.0, "gv1": 0.0, "gv2": 0.0, "tr": 0.0, "aturb": 0.0, "tp": 0.0, "uo": 0.0, "gv6": 0.0, "gv5": 0.0, "pgv5": 0.0, "gv4": 0.0, "pgv6": 0.0, "gv3": 0.0, "pgv2": 0.0, "pgv1": 0.0, "db1": 0.0, "pgv4": 0.0, "kturb": 0.0, "db2": 0.0, "tg": 0.0, "pmax": 0.0, "pgv3": 0.0, "mwbase": 0.0, "uc": 0.0, "pmin": 0.0, "eps": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

