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

from CIM15.CDPSM.Balanced.IEC61970.Wires.TransformerEnd import TransformerEnd

class PowerTransformerEnd(TransformerEnd):
    """A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impdedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star equivalentas follows 1) for a two Terminal PowerTransformer the high voltage PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage PowerTransformerEnd has zero values for r, r0, x, and x0. 2) for a three Terminal PowerTransformer the three PowerTransformerEnds represents a star equivalent with each leg in the star represented by r, r0, x, and x0 values. 3) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.
    """

    def __init__(self, g0=0.0, ratedS=0.0, b0=0.0, r0=0.0, connectionKind="Z", b=0.0, r=0.0, ratedU=0.0, x0=0.0, x=0.0, g=0.0, *args, **kw_args):
        """Initialises a new 'PowerTransformerEnd' instance.

        @param g0: Zero sequence magnetizing branch conductance (star-model). 
        @param ratedS: Normal apparent power rating. 
        @param b0: Zero sequence magnetizing branch susceptance. 
        @param r0: Zero sequence series resistance (star-model) of the transformer end. 
        @param connectionKind: Kind of connection. Values are: "Z", "A", "Yn", "Y", "Zn", "D", "I"
        @param b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        @param r: Resistance (star-model) of the transformer end. 
        @param ratedU: Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. 
        @param x0: Zero sequence series reactance of the transformer end. 
        @param x: Positive sequence series reactance (star-model) of the transformer end. 
        @param g: Magnetizing branch conductance (G mag). 
        """
        #: Zero sequence magnetizing branch conductance (star-model).
        self.g0 = g0

        #: Normal apparent power rating.
        self.ratedS = ratedS

        #: Zero sequence magnetizing branch susceptance.
        self.b0 = b0

        #: Zero sequence series resistance (star-model) of the transformer end.
        self.r0 = r0

        #: Kind of connection. Values are: "Z", "A", "Yn", "Y", "Zn", "D", "I"
        self.connectionKind = connectionKind

        #: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
        self.b = b

        #: Resistance (star-model) of the transformer end.
        self.r = r

        #: Rated voltage: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.
        self.ratedU = ratedU

        #: Zero sequence series reactance of the transformer end.
        self.x0 = x0

        #: Positive sequence series reactance (star-model) of the transformer end.
        self.x = x

        #: Magnetizing branch conductance (G mag).
        self.g = g

        super(PowerTransformerEnd, self).__init__(*args, **kw_args)

    _attrs = ["g0", "ratedS", "b0", "r0", "connectionKind", "b", "r", "ratedU", "x0", "x", "g"]
    _attr_types = {"g0": float, "ratedS": float, "b0": float, "r0": float, "connectionKind": str, "b": float, "r": float, "ratedU": float, "x0": float, "x": float, "g": float}
    _defaults = {"g0": 0.0, "ratedS": 0.0, "b0": 0.0, "r0": 0.0, "connectionKind": "Z", "b": 0.0, "r": 0.0, "ratedU": 0.0, "x0": 0.0, "x": 0.0, "g": 0.0}
    _enums = {"connectionKind": "WindingConnection"}
    _refs = []
    _many_refs = []

