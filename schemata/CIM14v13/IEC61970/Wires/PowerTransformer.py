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

from CIM14v13.IEC61970.Core.Equipment import Equipment

class PowerTransformer(Equipment):
    """An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """

    def __init__(self, bmagSat=0.0, magBaseU=0.0, magSatFlux=0.0, TransformerWindings=None, Flowgates=None, HeatExchanger=None, **kw_args):
        """Initializes a new 'PowerTransformer' instance.

        @param bmagSat: Core shunt magnetizing susceptance in the saturation region. 
        @param magBaseU: The reference voltage at which the magnetizing saturation measurements were made 
        @param magSatFlux: Core magnetizing saturation curve knee flux level. 
        @param TransformerWindings: A transformer has windings
        @param Flowgates:
        @param HeatExchanger: A transformer may have a heat exchanger
        """
        #: Core shunt magnetizing susceptance in the saturation region.
        self.bmagSat = bmagSat

        #: The reference voltage at which the magnetizing saturation measurements were made
        self.magBaseU = magBaseU

        #: Core magnetizing saturation curve knee flux level.
        self.magSatFlux = magSatFlux

        self._TransformerWindings = []
        self.TransformerWindings = [] if TransformerWindings is None else TransformerWindings

        self._Flowgates = []
        self.Flowgates = [] if Flowgates is None else Flowgates

        self._HeatExchanger = None
        self.HeatExchanger = HeatExchanger

        super(PowerTransformer, self).__init__(**kw_args)

    def getTransformerWindings(self):
        """A transformer has windings
        """
        return self._TransformerWindings

    def setTransformerWindings(self, value):
        for x in self._TransformerWindings:
            x._PowerTransformer = None
        for y in value:
            y._PowerTransformer = self
        self._TransformerWindings = value

    TransformerWindings = property(getTransformerWindings, setTransformerWindings)

    def addTransformerWindings(self, *TransformerWindings):
        for obj in TransformerWindings:
            obj._PowerTransformer = self
            self._TransformerWindings.append(obj)

    def removeTransformerWindings(self, *TransformerWindings):
        for obj in TransformerWindings:
            obj._PowerTransformer = None
            self._TransformerWindings.remove(obj)

    def getFlowgates(self):
        
        return self._Flowgates

    def setFlowgates(self, value):
        for p in self._Flowgates:
            filtered = [q for q in p.PowerTransormers if q != self]
            self._Flowgates._PowerTransormers = filtered
        for r in value:
            if self not in r._PowerTransormers:
                r._PowerTransormers.append(self)
        self._Flowgates = value

    Flowgates = property(getFlowgates, setFlowgates)

    def addFlowgates(self, *Flowgates):
        for obj in Flowgates:
            if self not in obj._PowerTransormers:
                obj._PowerTransormers.append(self)
            self._Flowgates.append(obj)

    def removeFlowgates(self, *Flowgates):
        for obj in Flowgates:
            if self in obj._PowerTransormers:
                obj._PowerTransormers.remove(self)
            self._Flowgates.remove(obj)

    def getHeatExchanger(self):
        """A transformer may have a heat exchanger
        """
        return self._HeatExchanger

    def setHeatExchanger(self, value):
        if self._HeatExchanger is not None:
            self._HeatExchanger._PowerTransformer = None

        self._HeatExchanger = value
        if self._HeatExchanger is not None:
            self._HeatExchanger._PowerTransformer = self

    HeatExchanger = property(getHeatExchanger, setHeatExchanger)

