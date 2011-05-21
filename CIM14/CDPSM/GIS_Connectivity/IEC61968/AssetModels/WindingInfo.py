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

from CIM14.CDPSM.GIS_Connectivity.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WindingInfo(IdentifiedObject):
    """Winding data.
    """

    def __init__(self, ratedS=0.0, ratedU=0.0, connectionKind="I", WindingTests=None, ToWindingSpecs=None, Windings=None, *args, **kw_args):
        """Initialises a new 'WindingInfo' instance.

        @param ratedS: Normal apparent power rating of this winding. 
        @param ratedU: Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings. 
        @param connectionKind: Kind of connection of this winding. Values are: "I", "Z", "Yn", "Y", "A", "D", "Zn"
        @param WindingTests: All winding tests during which voltage or current was applied to this winding.
        @param ToWindingSpecs: Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.
        @param Windings: All windings described by this winding data.
        """
        #: Normal apparent power rating of this winding.
        self.ratedS = ratedS

        #: Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.
        self.ratedU = ratedU

        #: Kind of connection of this winding. Values are: "I", "Z", "Yn", "Y", "A", "D", "Zn"
        self.connectionKind = connectionKind

        self._WindingTests = []
        self.WindingTests = [] if WindingTests is None else WindingTests

        self._ToWindingSpecs = []
        self.ToWindingSpecs = [] if ToWindingSpecs is None else ToWindingSpecs

        self._Windings = []
        self.Windings = [] if Windings is None else Windings

        super(WindingInfo, self).__init__(*args, **kw_args)

    _attrs = ["ratedS", "ratedU", "connectionKind"]
    _attr_types = {"ratedS": float, "ratedU": float, "connectionKind": str}
    _defaults = {"ratedS": 0.0, "ratedU": 0.0, "connectionKind": "I"}
    _enums = {"connectionKind": "WindingConnection"}
    _refs = ["WindingTests", "ToWindingSpecs", "Windings"]
    _many_refs = ["WindingTests", "ToWindingSpecs", "Windings"]

    def getWindingTests(self):
        """All winding tests during which voltage or current was applied to this winding.
        """
        return self._WindingTests

    def setWindingTests(self, value):
        for x in self._WindingTests:
            x.FromWinding = None
        for y in value:
            y._FromWinding = self
        self._WindingTests = value

    WindingTests = property(getWindingTests, setWindingTests)

    def addWindingTests(self, *WindingTests):
        for obj in WindingTests:
            obj.FromWinding = self

    def removeWindingTests(self, *WindingTests):
        for obj in WindingTests:
            obj.FromWinding = None

    def getToWindingSpecs(self):
        """Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.
        """
        return self._ToWindingSpecs

    def setToWindingSpecs(self, value):
        for x in self._ToWindingSpecs:
            x.ToWinding = None
        for y in value:
            y._ToWinding = self
        self._ToWindingSpecs = value

    ToWindingSpecs = property(getToWindingSpecs, setToWindingSpecs)

    def addToWindingSpecs(self, *ToWindingSpecs):
        for obj in ToWindingSpecs:
            obj.ToWinding = self

    def removeToWindingSpecs(self, *ToWindingSpecs):
        for obj in ToWindingSpecs:
            obj.ToWinding = None

    def getWindings(self):
        """All windings described by this winding data.
        """
        return self._Windings

    def setWindings(self, value):
        for x in self._Windings:
            x.WindingInfo = None
        for y in value:
            y._WindingInfo = self
        self._Windings = value

    Windings = property(getWindings, setWindings)

    def addWindings(self, *Windings):
        for obj in Windings:
            obj.WindingInfo = self

    def removeWindings(self, *Windings):
        for obj in Windings:
            obj.WindingInfo = None

