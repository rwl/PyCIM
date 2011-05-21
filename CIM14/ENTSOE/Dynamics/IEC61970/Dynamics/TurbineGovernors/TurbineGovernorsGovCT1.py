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

class TurbineGovernorsGovCT1(CorePowerSystemResource):

    def __init__(self, rdown=0.0, vmax=0.0, wfnl=0.0, tdgov=0.0, aset=0.0, r=0.0, wfspd=False, kpgov=0.0, minerr=0.0, tsa=0.0, tact=0.0, tsb=0.0, ldref=0.0, kimw=0.0, maxerr=0.0, vmin=0.0, mwbase=0.0, rclose=0.0, tpelec=0.0, rup=0.0, tb=0.0, ka=0.0, ta=0.0, kdgov=0.0, kturb=0.0, db=0.0, teng=0.0, tc=0.0, ropen=0.0, dm=0.0, kiload=0.0, pmwset=0.0, rselect=False, kigov=0.0, kpload=0.0, tfload=0.0, *args, **kw_args):
        """Initialises a new 'TurbineGovernorsGovCT1' instance.

        @param rdown: 
        @param vmax: 
        @param wfnl: 
        @param tdgov: 
        @param aset: 
        @param r: 
        @param wfspd: 
        @param kpgov: 
        @param minerr: 
        @param tsa: 
        @param tact: 
        @param tsb: 
        @param ldref: 
        @param kimw: 
        @param maxerr: 
        @param vmin: 
        @param mwbase: 
        @param rclose: 
        @param tpelec: 
        @param rup: 
        @param tb: 
        @param ka: 
        @param ta: 
        @param kdgov: 
        @param kturb: 
        @param db: 
        @param teng: 
        @param tc: 
        @param ropen: 
        @param dm: 
        @param kiload: 
        @param pmwset: 
        @param rselect: 
        @param kigov: 
        @param kpload: 
        @param tfload: 
        """

        self.rdown = rdown


        self.vmax = vmax


        self.wfnl = wfnl


        self.tdgov = tdgov


        self.aset = aset


        self.r = r


        self.wfspd = wfspd


        self.kpgov = kpgov


        self.minerr = minerr


        self.tsa = tsa


        self.tact = tact


        self.tsb = tsb


        self.ldref = ldref


        self.kimw = kimw


        self.maxerr = maxerr


        self.vmin = vmin


        self.mwbase = mwbase


        self.rclose = rclose


        self.tpelec = tpelec


        self.rup = rup


        self.tb = tb


        self.ka = ka


        self.ta = ta


        self.kdgov = kdgov


        self.kturb = kturb


        self.db = db


        self.teng = teng


        self.tc = tc


        self.ropen = ropen


        self.dm = dm


        self.kiload = kiload


        self.pmwset = pmwset


        self.rselect = rselect


        self.kigov = kigov


        self.kpload = kpload


        self.tfload = tfload

        super(TurbineGovernorsGovCT1, self).__init__(*args, **kw_args)

    _attrs = ["rdown", "vmax", "wfnl", "tdgov", "aset", "r", "wfspd", "kpgov", "minerr", "tsa", "tact", "tsb", "ldref", "kimw", "maxerr", "vmin", "mwbase", "rclose", "tpelec", "rup", "tb", "ka", "ta", "kdgov", "kturb", "db", "teng", "tc", "ropen", "dm", "kiload", "pmwset", "rselect", "kigov", "kpload", "tfload"]
    _attr_types = {"rdown": float, "vmax": float, "wfnl": float, "tdgov": float, "aset": float, "r": float, "wfspd": bool, "kpgov": float, "minerr": float, "tsa": float, "tact": float, "tsb": float, "ldref": float, "kimw": float, "maxerr": float, "vmin": float, "mwbase": float, "rclose": float, "tpelec": float, "rup": float, "tb": float, "ka": float, "ta": float, "kdgov": float, "kturb": float, "db": float, "teng": float, "tc": float, "ropen": float, "dm": float, "kiload": float, "pmwset": float, "rselect": bool, "kigov": float, "kpload": float, "tfload": float}
    _defaults = {"rdown": 0.0, "vmax": 0.0, "wfnl": 0.0, "tdgov": 0.0, "aset": 0.0, "r": 0.0, "wfspd": False, "kpgov": 0.0, "minerr": 0.0, "tsa": 0.0, "tact": 0.0, "tsb": 0.0, "ldref": 0.0, "kimw": 0.0, "maxerr": 0.0, "vmin": 0.0, "mwbase": 0.0, "rclose": 0.0, "tpelec": 0.0, "rup": 0.0, "tb": 0.0, "ka": 0.0, "ta": 0.0, "kdgov": 0.0, "kturb": 0.0, "db": 0.0, "teng": 0.0, "tc": 0.0, "ropen": 0.0, "dm": 0.0, "kiload": 0.0, "pmwset": 0.0, "rselect": False, "kigov": 0.0, "kpload": 0.0, "tfload": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

