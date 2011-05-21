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

from CIM14.CPSM.Equipment.Core.ConductingEquipment import ConductingEquipment

class TransformerWinding(ConductingEquipment):
    """A winding is associated with each defined terminal of a transformer (or phase shifter).-  [R5.4], [R5.6], and [R5.10] are satisfied by navigation to ConnectivityNode and Substation -  Each TransformerWinging must be contained by a PowerTransformer.  Because a TransformerWinding (or any other object) can not be contained by more than one parent, a TransformerWinding can not have an association to an EquipmentContainer (Substation, VoltageLevel, etc). -  The attributes ratedS, b0, g0, r0, x0, rground, xground, and connectionType are not required. 
    """

    def __init__(self, x=0.0, x0=0.0, b0=0.0, g0=0.0, rground=0.0, b=0.0, connectionType="I", ratedS=0.0, r=0.0, r0=0.0, ratedU=0.0, xground=0.0, windingType="tertiary", RatioTapChanger=None, PhaseTapChanger=None, PowerTransformer=None, *args, **kw_args):
        """Initialises a new 'TransformerWinding' instance.

        @param x: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        @param x0: Zero sequence series reactance of the winding. 
        @param b0: Zero sequence magnetizing branch susceptance. 
        @param g0: Zero sequence magnetizing branch conductance. 
        @param rground: Ground resistance path through connected grounding transformer. 
        @param b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        @param connectionType: The type of connection of the winding. Values are: "I", "Yn", "Z", "Y", "A", "D", "Zn"
        @param ratedS: The normal apparent power rating for the winding 
        @param r: Positive sequence series resistance of the winding.  For a two winding transformer, the full resistance of the transformer should be entered on the primary (high voltage) winding. 
        @param r0: Zero sequence series resistance of the winding. 
        @param ratedU: The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
        @param xground: Ground reactance path through connected grounding transformer. 
        @param windingType: The type of winding. Values are: "tertiary", "primary", "secondary"
        @param RatioTapChanger: The ratio tap changer associated with the transformer winding.
        @param PhaseTapChanger: The phase tap changer associated with the transformer winding.
        @param PowerTransformer: A transformer has windings
        """
        #: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.
        self.x = x

        #: Zero sequence series reactance of the winding.
        self.x0 = x0

        #: Zero sequence magnetizing branch susceptance.
        self.b0 = b0

        #: Zero sequence magnetizing branch conductance.
        self.g0 = g0

        #: Ground resistance path through connected grounding transformer.
        self.rground = rground

        #: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
        self.b = b

        #: The type of connection of the winding. Values are: "I", "Yn", "Z", "Y", "A", "D", "Zn"
        self.connectionType = connectionType

        #: The normal apparent power rating for the winding
        self.ratedS = ratedS

        #: Positive sequence series resistance of the winding.  For a two winding transformer, the full resistance of the transformer should be entered on the primary (high voltage) winding.
        self.r = r

        #: Zero sequence series resistance of the winding.
        self.r0 = r0

        #: The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
        self.ratedU = ratedU

        #: Ground reactance path through connected grounding transformer.
        self.xground = xground

        #: The type of winding. Values are: "tertiary", "primary", "secondary"
        self.windingType = windingType

        self._RatioTapChanger = None
        self.RatioTapChanger = RatioTapChanger

        self._PhaseTapChanger = None
        self.PhaseTapChanger = PhaseTapChanger

        self._PowerTransformer = None
        self.PowerTransformer = PowerTransformer

        super(TransformerWinding, self).__init__(*args, **kw_args)

    _attrs = ["x", "x0", "b0", "g0", "rground", "b", "connectionType", "ratedS", "r", "r0", "ratedU", "xground", "windingType"]
    _attr_types = {"x": float, "x0": float, "b0": float, "g0": float, "rground": float, "b": float, "connectionType": str, "ratedS": float, "r": float, "r0": float, "ratedU": float, "xground": float, "windingType": str}
    _defaults = {"x": 0.0, "x0": 0.0, "b0": 0.0, "g0": 0.0, "rground": 0.0, "b": 0.0, "connectionType": "I", "ratedS": 0.0, "r": 0.0, "r0": 0.0, "ratedU": 0.0, "xground": 0.0, "windingType": "tertiary"}
    _enums = {"connectionType": "WindingConnection", "windingType": "WindingType"}
    _refs = ["RatioTapChanger", "PhaseTapChanger", "PowerTransformer"]
    _many_refs = []

    def getRatioTapChanger(self):
        """The ratio tap changer associated with the transformer winding.
        """
        return self._RatioTapChanger

    def setRatioTapChanger(self, value):
        if self._RatioTapChanger is not None:
            self._RatioTapChanger._TransformerWinding = None

        self._RatioTapChanger = value
        if self._RatioTapChanger is not None:
            self._RatioTapChanger.TransformerWinding = None
            self._RatioTapChanger._TransformerWinding = self

    RatioTapChanger = property(getRatioTapChanger, setRatioTapChanger)

    def getPhaseTapChanger(self):
        """The phase tap changer associated with the transformer winding.
        """
        return self._PhaseTapChanger

    def setPhaseTapChanger(self, value):
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger._TransformerWinding = None

        self._PhaseTapChanger = value
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger.TransformerWinding = None
            self._PhaseTapChanger._TransformerWinding = self

    PhaseTapChanger = property(getPhaseTapChanger, setPhaseTapChanger)

    def getPowerTransformer(self):
        """A transformer has windings
        """
        return self._PowerTransformer

    def setPowerTransformer(self, value):
        if self._PowerTransformer is not None:
            filtered = [x for x in self.PowerTransformer.TransformerWindings if x != self]
            self._PowerTransformer._TransformerWindings = filtered

        self._PowerTransformer = value
        if self._PowerTransformer is not None:
            if self not in self._PowerTransformer._TransformerWindings:
                self._PowerTransformer._TransformerWindings.append(self)

    PowerTransformer = property(getPowerTransformer, setPowerTransformer)

