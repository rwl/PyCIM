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

