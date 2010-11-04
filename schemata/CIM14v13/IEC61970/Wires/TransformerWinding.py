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

from CIM14v13.IEC61970.Core.ConductingEquipment import ConductingEquipment

class TransformerWinding(ConductingEquipment):
    """A winding is associated with each defined terminal of a transformer (or phase shifter).
    """

    def __init__(self, windingType='tertiary', connectionType='Y', shortTermS=0.0, ratedU=0.0, grounded=False, r0=0.0, ratedS=0.0, emergencyS=0.0, b0=0.0, xground=0.0, g0=0.0, b=0.0, r=0.0, rground=0.0, x=0.0, insulationU=0.0, g=0.0, x0=0.0, To_WindingTest=None, PowerTransformer=None, From_WindingTest=None, RatioTapChanger=None, PhaseTapChanger=None, *args, **kw_args):
        """Initializes a new 'TransformerWinding' instance.

        @param windingType: The type of winding. Values are: "tertiary", "secondary", "primary", "quaternary"
        @param connectionType: The type of connection of the winding. Values are: "Y", "Yn", "Zn", "I", "A", "D", "Z"
        @param shortTermS: Apparent power that the winding can carry for a short period of time. 
        @param ratedU: The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
        @param grounded: Set if the winding is grounded. 
        @param r0: Zero sequence series resistance of the winding. 
        @param ratedS: The normal apparent power rating for the winding 
        @param emergencyS: The apparent power that the winding can carry  under emergency conditions. 
        @param b0: Zero sequence magnetizing branch susceptance. 
        @param xground: Ground reactance path through connected grounding transformer. 
        @param g0: Zero sequence magnetizing branch conductance. 
        @param b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        @param r: Positive sequence series resistance of the winding.  For a two winding transformer, the full resistance of the transformer should be entered on the primary (high voltage) winding. 
        @param rground: Ground resistance path through connected grounding transformer. 
        @param x: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        @param insulationU: Basic insulation level voltage rating 
        @param g: Magnetizing branch conductance (G mag). 
        @param x0: Zero sequence series reactance of the winding. 
        @param To_WindingTest: The winding winding tests for which the transformer winding (terminal) participates as the 'to' end of the test.
        @param PowerTransformer: A transformer has windings
        @param From_WindingTest: The transformer winding tests for which the transformer winding (terminal) participates as the 'from' part of the test.
        @param RatioTapChanger: The ratio tap changer associated with the transformer winding.
        @param PhaseTapChanger: The phase tap changer associated with the transformer winding.
        """
        #: The type of winding.Values are: "tertiary", "secondary", "primary", "quaternary"
        self.windingType = windingType

        #: The type of connection of the winding.Values are: "Y", "Yn", "Zn", "I", "A", "D", "Z"
        self.connectionType = connectionType

        #: Apparent power that the winding can carry for a short period of time.
        self.shortTermS = shortTermS

        #: The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
        self.ratedU = ratedU

        #: Set if the winding is grounded.
        self.grounded = grounded

        #: Zero sequence series resistance of the winding.
        self.r0 = r0

        #: The normal apparent power rating for the winding
        self.ratedS = ratedS

        #: The apparent power that the winding can carry  under emergency conditions.
        self.emergencyS = emergencyS

        #: Zero sequence magnetizing branch susceptance.
        self.b0 = b0

        #: Ground reactance path through connected grounding transformer.
        self.xground = xground

        #: Zero sequence magnetizing branch conductance.
        self.g0 = g0

        #: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
        self.b = b

        #: Positive sequence series resistance of the winding.  For a two winding transformer, the full resistance of the transformer should be entered on the primary (high voltage) winding.
        self.r = r

        #: Ground resistance path through connected grounding transformer.
        self.rground = rground

        #: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.
        self.x = x

        #: Basic insulation level voltage rating
        self.insulationU = insulationU

        #: Magnetizing branch conductance (G mag).
        self.g = g

        #: Zero sequence series reactance of the winding.
        self.x0 = x0

        self._To_WindingTest = []
        self.To_WindingTest = [] if To_WindingTest is None else To_WindingTest

        self._PowerTransformer = None
        self.PowerTransformer = PowerTransformer

        self._From_WindingTest = []
        self.From_WindingTest = [] if From_WindingTest is None else From_WindingTest

        self._RatioTapChanger = None
        self.RatioTapChanger = RatioTapChanger

        self._PhaseTapChanger = None
        self.PhaseTapChanger = PhaseTapChanger

        super(TransformerWinding, self).__init__(*args, **kw_args)

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

