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

from CIM15.IEC61968.Assets.Asset import Asset

class Bushing(Asset):
    """Bushing asset.Bushing asset.
    """

    def __init__(self, c2PowerFactor=0.0, c2Capacitance=0.0, c1PowerFactor=0.0, insulationKind="solidPorcelain", c1Capacitance=0.0, Terminal=None, BushingInsulationPFs=None, *args, **kw_args):
        """Initialises a new 'Bushing' instance.

        @param c2PowerFactor: Factory measured insulation power factor, measured between the power factor tap and ground. 
        @param c2Capacitance: Factory measured capacitance measured between the power factor tap and ground. 
        @param c1PowerFactor: Factory measured insulation power factor, measured between the power factor tap and the bushing conductor. 
        @param insulationKind: Kind of insulation. Values are: "solidPorcelain", "compound", "other", "paperoil"
        @param c1Capacitance: Factory measured capacitance, measured between the power factor tap and the bushing conductor. 
        @param Terminal:
        @param BushingInsulationPFs:
        """
        #: Factory measured insulation power factor, measured between the power factor tap and ground.
        self.c2PowerFactor = c2PowerFactor

        #: Factory measured capacitance measured between the power factor tap and ground.
        self.c2Capacitance = c2Capacitance

        #: Factory measured insulation power factor, measured between the power factor tap and the bushing conductor.
        self.c1PowerFactor = c1PowerFactor

        #: Kind of insulation. Values are: "solidPorcelain", "compound", "other", "paperoil"
        self.insulationKind = insulationKind

        #: Factory measured capacitance, measured between the power factor tap and the bushing conductor.
        self.c1Capacitance = c1Capacitance

        self._Terminal = None
        self.Terminal = Terminal

        self._BushingInsulationPFs = []
        self.BushingInsulationPFs = [] if BushingInsulationPFs is None else BushingInsulationPFs

        super(Bushing, self).__init__(*args, **kw_args)

    _attrs = ["c2PowerFactor", "c2Capacitance", "c1PowerFactor", "insulationKind", "c1Capacitance"]
    _attr_types = {"c2PowerFactor": float, "c2Capacitance": float, "c1PowerFactor": float, "insulationKind": str, "c1Capacitance": float}
    _defaults = {"c2PowerFactor": 0.0, "c2Capacitance": 0.0, "c1PowerFactor": 0.0, "insulationKind": "solidPorcelain", "c1Capacitance": 0.0}
    _enums = {"insulationKind": "BushingInsulationKind"}
    _refs = ["Terminal", "BushingInsulationPFs"]
    _many_refs = ["BushingInsulationPFs"]

    def getTerminal(self):
        
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            self._Terminal._BushingInfo = None

        self._Terminal = value
        if self._Terminal is not None:
            self._Terminal.BushingInfo = None
            self._Terminal._BushingInfo = self

    Terminal = property(getTerminal, setTerminal)

    def getBushingInsulationPFs(self):
        
        return self._BushingInsulationPFs

    def setBushingInsulationPFs(self, value):
        for x in self._BushingInsulationPFs:
            x.BushingInfo = None
        for y in value:
            y._BushingInfo = self
        self._BushingInsulationPFs = value

    BushingInsulationPFs = property(getBushingInsulationPFs, setBushingInsulationPFs)

    def addBushingInsulationPFs(self, *BushingInsulationPFs):
        for obj in BushingInsulationPFs:
            obj.BushingInfo = self

    def removeBushingInsulationPFs(self, *BushingInsulationPFs):
        for obj in BushingInsulationPFs:
            obj.BushingInfo = None

