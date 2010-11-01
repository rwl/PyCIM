# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61968.Assets.Asset import Asset

class BushingAsset(Asset):
    """Physical bushing that insulates and protects from abrasion a conductor that passes through it. It is associated with a specific Terminal, which is in turn associated with a ConductingEquipment.
    """

    def __init__(self, c2Capacitance=0.0, c1PowerFactor=0.0, c2PowerFactor=0.0, c1Capacitance=0.0, Terminal=None, BushingInsulationPFs=None, BushingModel=None, *args, **kw_args):
        """Initializes a new 'BushingAsset' instance.

        @param c2Capacitance: Factory measured capacitance measured between the power factor tap and ground. 
        @param c1PowerFactor: Factory measured insulation power factor, measured between the power factor tap and the bushing conductor. 
        @param c2PowerFactor: Factory measured insulation power factor, measured between the power factor tap and ground. 
        @param c1Capacitance: Factory measured capacitance, measured between the power factor tap and the bushing conductor. 
        @param Terminal:
        @param BushingInsulationPFs:
        @param BushingModel:
        """
        #: Factory measured capacitance measured between the power factor tap and ground. 
        self.c2Capacitance = c2Capacitance

        #: Factory measured insulation power factor, measured between the power factor tap and the bushing conductor. 
        self.c1PowerFactor = c1PowerFactor

        #: Factory measured insulation power factor, measured between the power factor tap and ground. 
        self.c2PowerFactor = c2PowerFactor

        #: Factory measured capacitance, measured between the power factor tap and the bushing conductor. 
        self.c1Capacitance = c1Capacitance

        self._Terminal = None
        self.Terminal = Terminal

        self._BushingInsulationPFs = []
        self.BushingInsulationPFs = [] if BushingInsulationPFs is None else BushingInsulationPFs

        self._BushingModel = None
        self.BushingModel = BushingModel

        super(BushingAsset, self).__init__(*args, **kw_args)

    def getTerminal(self):
        
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            self._Terminal._BushingAsset = None

        self._Terminal = value
        if self._Terminal is not None:
            self._Terminal._BushingAsset = self

    Terminal = property(getTerminal, setTerminal)

    def getBushingInsulationPFs(self):
        
        return self._BushingInsulationPFs

    def setBushingInsulationPFs(self, value):
        for x in self._BushingInsulationPFs:
            x._BushingAsset = None
        for y in value:
            y._BushingAsset = self
        self._BushingInsulationPFs = value

    BushingInsulationPFs = property(getBushingInsulationPFs, setBushingInsulationPFs)

    def addBushingInsulationPFs(self, *BushingInsulationPFs):
        for obj in BushingInsulationPFs:
            obj._BushingAsset = self
            self._BushingInsulationPFs.append(obj)

    def removeBushingInsulationPFs(self, *BushingInsulationPFs):
        for obj in BushingInsulationPFs:
            obj._BushingAsset = None
            self._BushingInsulationPFs.remove(obj)

    def getBushingModel(self):
        
        return self._BushingModel

    def setBushingModel(self, value):
        if self._BushingModel is not None:
            self._BushingModel._BushingAsset = None

        self._BushingModel = value
        if self._BushingModel is not None:
            self._BushingModel._BushingAsset = self

    BushingModel = property(getBushingModel, setBushingModel)

