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

class TurbineGovernorsGovHydro1(CorePowerSystemResource):

    def __init__(self, rperm=0.0, tg=0.0, tf=0.0, mwbase=0.0, gmax=0.0, at=0.0, gmin=0.0, qnl=0.0, velm=0.0, tw=0.0, dturb=0.0, rtemp=0.0, tr=0.0, *args, **kw_args):
        """Initialises a new 'TurbineGovernorsGovHydro1' instance.

        @param rperm: 
        @param tg: 
        @param tf: 
        @param mwbase: 
        @param gmax: 
        @param at: 
        @param gmin: 
        @param qnl: 
        @param velm: 
        @param tw: 
        @param dturb: 
        @param rtemp: 
        @param tr: 
        """

        self.rperm = rperm


        self.tg = tg


        self.tf = tf


        self.mwbase = mwbase


        self.gmax = gmax


        self.at = at


        self.gmin = gmin


        self.qnl = qnl


        self.velm = velm


        self.tw = tw


        self.dturb = dturb


        self.rtemp = rtemp


        self.tr = tr

        super(TurbineGovernorsGovHydro1, self).__init__(*args, **kw_args)

    _attrs = ["rperm", "tg", "tf", "mwbase", "gmax", "at", "gmin", "qnl", "velm", "tw", "dturb", "rtemp", "tr"]
    _attr_types = {"rperm": float, "tg": float, "tf": float, "mwbase": float, "gmax": float, "at": float, "gmin": float, "qnl": float, "velm": float, "tw": float, "dturb": float, "rtemp": float, "tr": float}
    _defaults = {"rperm": 0.0, "tg": 0.0, "tf": 0.0, "mwbase": 0.0, "gmax": 0.0, "at": 0.0, "gmin": 0.0, "qnl": 0.0, "velm": 0.0, "tw": 0.0, "dturb": 0.0, "rtemp": 0.0, "tr": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

