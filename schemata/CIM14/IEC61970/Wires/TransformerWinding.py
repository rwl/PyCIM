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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class TransformerWinding(ConductingEquipment):
    """A winding is associated with each defined terminal of a transformer (or phase shifter).
    """

    def __init__(self, connectionType="Yn", windingType="primary", x=0.0, grounded=False, g=0.0, r=0.0, x0=0.0, ratedU=0.0, ratedS=0.0, emergencyS=0.0, rground=0.0, shortTermS=0.0, r0=0.0, g0=0.0, insulationU=0.0, b=0.0, b0=0.0, xground=0.0, From_WindingTest=None, To_WindingTest=None, RatioTapChanger=None, PowerTransformer=None, PhaseTapChanger=None, *args, **kw_args):
        """Initialises a new 'TransformerWinding' instance.

        @param connectionType: The type of connection of the winding. Values are: "Yn", "Y", "D", "I", "Z", "A", "Zn"
        @param windingType: The type of winding. Values are: "primary", "quaternary", "secondary", "tertiary"
        @param x: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        @param grounded: Set if the winding is grounded. 
        @param g: Magnetizing branch conductance (G mag). 
        @param r: Positive sequence series resistance of the winding.  For a two winding transformer, the full resistance of the transformer should be entered on the primary (high voltage) winding. 
        @param x0: Zero sequence series reactance of the winding. 
        @param ratedU: The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
        @param ratedS: The normal apparent power rating for the winding 
        @param emergencyS: The apparent power that the winding can carry  under emergency conditions. 
        @param rground: Ground resistance path through connected grounding transformer. 
        @param shortTermS: Apparent power that the winding can carry for a short period of time. 
        @param r0: Zero sequence series resistance of the winding. 
        @param g0: Zero sequence magnetizing branch conductance. 
        @param insulationU: Basic insulation level voltage rating 
        @param b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        @param b0: Zero sequence magnetizing branch susceptance. 
        @param xground: Ground reactance path through connected grounding transformer. 
        @param From_WindingTest: The transformer winding tests for which the transformer winding (terminal) participates as the 'from' part of the test.
        @param To_WindingTest: The winding winding tests for which the transformer winding (terminal) participates as the 'to' end of the test.
        @param RatioTapChanger: The ratio tap changer associated with the transformer winding.
        @param PowerTransformer: A transformer has windings
        @param PhaseTapChanger: The phase tap changer associated with the transformer winding.
        """
        #: The type of connection of the winding. Values are: "Yn", "Y", "D", "I", "Z", "A", "Zn"
        self.connectionType = connectionType

        #: The type of winding. Values are: "primary", "quaternary", "secondary", "tertiary"
        self.windingType = windingType

        #: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.
        self.x = x

        #: Set if the winding is grounded.
        self.grounded = grounded

        #: Magnetizing branch conductance (G mag).
        self.g = g

        #: Positive sequence series resistance of the winding.  For a two winding transformer, the full resistance of the transformer should be entered on the primary (high voltage) winding.
        self.r = r

        #: Zero sequence series reactance of the winding.
        self.x0 = x0

        #: The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
        self.ratedU = ratedU

        #: The normal apparent power rating for the winding
        self.ratedS = ratedS

        #: The apparent power that the winding can carry  under emergency conditions.
        self.emergencyS = emergencyS

        #: Ground resistance path through connected grounding transformer.
        self.rground = rground

        #: Apparent power that the winding can carry for a short period of time.
        self.shortTermS = shortTermS

        #: Zero sequence series resistance of the winding.
        self.r0 = r0

        #: Zero sequence magnetizing branch conductance.
        self.g0 = g0

        #: Basic insulation level voltage rating
        self.insulationU = insulationU

        #: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
        self.b = b

        #: Zero sequence magnetizing branch susceptance.
        self.b0 = b0

        #: Ground reactance path through connected grounding transformer.
        self.xground = xground

        self._From_WindingTest = []
        self.From_WindingTest = [] if From_WindingTest is None else From_WindingTest

        self._To_WindingTest = []
        self.To_WindingTest = [] if To_WindingTest is None else To_WindingTest

        self._RatioTapChanger = None
        self.RatioTapChanger = RatioTapChanger

        self._PowerTransformer = None
        self.PowerTransformer = PowerTransformer

        self._PhaseTapChanger = None
        self.PhaseTapChanger = PhaseTapChanger

        super(TransformerWinding, self).__init__(*args, **kw_args)

    _attrs = ["connectionType", "windingType", "x", "grounded", "g", "r", "x0", "ratedU", "ratedS", "emergencyS", "rground", "shortTermS", "r0", "g0", "insulationU", "b", "b0", "xground"]
    _attr_types = {"connectionType": str, "windingType": str, "x": float, "grounded": bool, "g": float, "r": float, "x0": float, "ratedU": float, "ratedS": float, "emergencyS": float, "rground": float, "shortTermS": float, "r0": float, "g0": float, "insulationU": float, "b": float, "b0": float, "xground": float}
    _defaults = {"connectionType": "Yn", "windingType": "primary", "x": 0.0, "grounded": False, "g": 0.0, "r": 0.0, "x0": 0.0, "ratedU": 0.0, "ratedS": 0.0, "emergencyS": 0.0, "rground": 0.0, "shortTermS": 0.0, "r0": 0.0, "g0": 0.0, "insulationU": 0.0, "b": 0.0, "b0": 0.0, "xground": 0.0}
    _enums = {"connectionType": "WindingConnection", "windingType": "WindingType"}
    _refs = ["From_WindingTest", "To_WindingTest", "RatioTapChanger", "PowerTransformer", "PhaseTapChanger"]
    _many_refs = ["From_WindingTest", "To_WindingTest"]

    def getFrom_WindingTest(self):
        """The transformer winding tests for which the transformer winding (terminal) participates as the 'from' part of the test.
        """
        return self._From_WindingTest

    def setFrom_WindingTest(self, value):
        for x in self._From_WindingTest:
            x._From_TransformerWinding = None
        for y in value:
            y._From_TransformerWinding = self
        self._From_WindingTest = value

    From_WindingTest = property(getFrom_WindingTest, setFrom_WindingTest)

    def addFrom_WindingTest(self, *From_WindingTest):
        for obj in From_WindingTest:
            obj._From_TransformerWinding = self
            self._From_WindingTest.append(obj)

    def removeFrom_WindingTest(self, *From_WindingTest):
        for obj in From_WindingTest:
            obj._From_TransformerWinding = None
            self._From_WindingTest.remove(obj)

    def getTo_WindingTest(self):
        """The winding winding tests for which the transformer winding (terminal) participates as the 'to' end of the test.
        """
        return self._To_WindingTest

    def setTo_WindingTest(self, value):
        for x in self._To_WindingTest:
            x._To_TransformerWinding = None
        for y in value:
            y._To_TransformerWinding = self
        self._To_WindingTest = value

    To_WindingTest = property(getTo_WindingTest, setTo_WindingTest)

    def addTo_WindingTest(self, *To_WindingTest):
        for obj in To_WindingTest:
            obj._To_TransformerWinding = self
            self._To_WindingTest.append(obj)

    def removeTo_WindingTest(self, *To_WindingTest):
        for obj in To_WindingTest:
            obj._To_TransformerWinding = None
            self._To_WindingTest.remove(obj)

    def getRatioTapChanger(self):
        """The ratio tap changer associated with the transformer winding.
        """
        return self._RatioTapChanger

    def setRatioTapChanger(self, value):
        if self._RatioTapChanger is not None:
            self._RatioTapChanger._TransformerWinding = None

        self._RatioTapChanger = value
        if self._RatioTapChanger is not None:
            self._RatioTapChanger._TransformerWinding = self

    RatioTapChanger = property(getRatioTapChanger, setRatioTapChanger)

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
            self._PowerTransformer._TransformerWindings.append(self)

    PowerTransformer = property(getPowerTransformer, setPowerTransformer)

    def getPhaseTapChanger(self):
        """The phase tap changer associated with the transformer winding.
        """
        return self._PhaseTapChanger

    def setPhaseTapChanger(self, value):
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger._TransformerWinding = None

        self._PhaseTapChanger = value
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger._TransformerWinding = self

    PhaseTapChanger = property(getPhaseTapChanger, setPhaseTapChanger)

