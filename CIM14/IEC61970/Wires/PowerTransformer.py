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

from CIM14.IEC61970.Core.Equipment import Equipment

class PowerTransformer(Equipment):
    """An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """

    def __init__(self, magSatFlux=0.0, magBaseU=0.0, bmagSat=0.0, TransformerWindings=None, HeatExchanger=None, *args, **kw_args):
        """Initialises a new 'PowerTransformer' instance.

        @param magSatFlux: Core magnetizing saturation curve knee flux level. 
        @param magBaseU: The reference voltage at which the magnetizing saturation measurements were made 
        @param bmagSat: Core shunt magnetizing susceptance in the saturation region. 
        @param TransformerWindings: A transformer has windings
        @param HeatExchanger: A transformer may have a heat exchanger
        """
        #: Core magnetizing saturation curve knee flux level.
        self.magSatFlux = magSatFlux

        #: The reference voltage at which the magnetizing saturation measurements were made
        self.magBaseU = magBaseU

        #: Core shunt magnetizing susceptance in the saturation region.
        self.bmagSat = bmagSat

        self._TransformerWindings = []
        self.TransformerWindings = [] if TransformerWindings is None else TransformerWindings

        self._HeatExchanger = None
        self.HeatExchanger = HeatExchanger

        super(PowerTransformer, self).__init__(*args, **kw_args)

    _attrs = ["magSatFlux", "magBaseU", "bmagSat"]
    _attr_types = {"magSatFlux": float, "magBaseU": float, "bmagSat": float}
    _defaults = {"magSatFlux": 0.0, "magBaseU": 0.0, "bmagSat": 0.0}
    _enums = {}
    _refs = ["TransformerWindings", "HeatExchanger"]
    _many_refs = ["TransformerWindings"]

    def getTransformerWindings(self):
        """A transformer has windings
        """
        return self._TransformerWindings

    def setTransformerWindings(self, value):
        for x in self._TransformerWindings:
            x.PowerTransformer = None
        for y in value:
            y._PowerTransformer = self
        self._TransformerWindings = value

    TransformerWindings = property(getTransformerWindings, setTransformerWindings)

    def addTransformerWindings(self, *TransformerWindings):
        for obj in TransformerWindings:
            obj.PowerTransformer = self

    def removeTransformerWindings(self, *TransformerWindings):
        for obj in TransformerWindings:
            obj.PowerTransformer = None

    def getHeatExchanger(self):
        """A transformer may have a heat exchanger
        """
        return self._HeatExchanger

    def setHeatExchanger(self, value):
        if self._HeatExchanger is not None:
            self._HeatExchanger._PowerTransformer = None

        self._HeatExchanger = value
        if self._HeatExchanger is not None:
            self._HeatExchanger.PowerTransformer = None
            self._HeatExchanger._PowerTransformer = self

    HeatExchanger = property(getHeatExchanger, setHeatExchanger)

