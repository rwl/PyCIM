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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WireType(IdentifiedObject):
    """Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    def __init__(self, rAC75=0.0, coreRadius=0.0, coreStrandCount=0, rAC25=0.0, radius=0.0, gmr=0.0, rDC20=0.0, rAC50=0.0, material="steel", sizeDescription='', strandCount=0, ratedCurrent=0.0, ConcentricNeutralCableInfos=None, WireArrangements=None, *args, **kw_args):
        """Initialises a new 'WireType' instance.

        @param rAC75: AC resistance per unit length of the conductor at 75 degrees C. 
        @param coreRadius: (if there is a different core material) Radius of the central core. 
        @param coreStrandCount: (if used) Number of strands in the steel core. 
        @param rAC25: AC resistance per unit length of the conductor at 25 degrees C. 
        @param radius: Outside radius of the wire. 
        @param gmr: Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor. 
        @param rDC20: DC resistance per unit length of the conductor at 20 degrees C. 
        @param rAC50: AC resistance per unit length of the conductor at 50 degrees C. 
        @param material: Wire material. Values are: "steel", "other", "aluminum", "copper", "acsr"
        @param sizeDescription: Describes the wire guage or cross section (e.g., 4/0, #2, 336.5). 
        @param strandCount: Number of strands in the wire. 
        @param ratedCurrent: Current carrying capacity of the wire under stated thermal conditions. 
        @param ConcentricNeutralCableInfos: All concentric neutral cables using this wire type.
        @param WireArrangements: All wire arrangements using this wire type.
        """
        #: AC resistance per unit length of the conductor at 75 degrees C.
        self.rAC75 = rAC75

        #: (if there is a different core material) Radius of the central core.
        self.coreRadius = coreRadius

        #: (if used) Number of strands in the steel core.
        self.coreStrandCount = coreStrandCount

        #: AC resistance per unit length of the conductor at 25 degrees C.
        self.rAC25 = rAC25

        #: Outside radius of the wire.
        self.radius = radius

        #: Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
        self.gmr = gmr

        #: DC resistance per unit length of the conductor at 20 degrees C.
        self.rDC20 = rDC20

        #: AC resistance per unit length of the conductor at 50 degrees C.
        self.rAC50 = rAC50

        #: Wire material. Values are: "steel", "other", "aluminum", "copper", "acsr"
        self.material = material

        #: Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).
        self.sizeDescription = sizeDescription

        #: Number of strands in the wire.
        self.strandCount = strandCount

        #: Current carrying capacity of the wire under stated thermal conditions.
        self.ratedCurrent = ratedCurrent

        self._ConcentricNeutralCableInfos = []
        self.ConcentricNeutralCableInfos = [] if ConcentricNeutralCableInfos is None else ConcentricNeutralCableInfos

        self._WireArrangements = []
        self.WireArrangements = [] if WireArrangements is None else WireArrangements

        super(WireType, self).__init__(*args, **kw_args)

    _attrs = ["rAC75", "coreRadius", "coreStrandCount", "rAC25", "radius", "gmr", "rDC20", "rAC50", "material", "sizeDescription", "strandCount", "ratedCurrent"]
    _attr_types = {"rAC75": float, "coreRadius": float, "coreStrandCount": int, "rAC25": float, "radius": float, "gmr": float, "rDC20": float, "rAC50": float, "material": str, "sizeDescription": str, "strandCount": int, "ratedCurrent": float}
    _defaults = {"rAC75": 0.0, "coreRadius": 0.0, "coreStrandCount": 0, "rAC25": 0.0, "radius": 0.0, "gmr": 0.0, "rDC20": 0.0, "rAC50": 0.0, "material": "steel", "sizeDescription": '', "strandCount": 0, "ratedCurrent": 0.0}
    _enums = {"material": "ConductorMaterialKind"}
    _refs = ["ConcentricNeutralCableInfos", "WireArrangements"]
    _many_refs = ["ConcentricNeutralCableInfos", "WireArrangements"]

    def getConcentricNeutralCableInfos(self):
        """All concentric neutral cables using this wire type.
        """
        return self._ConcentricNeutralCableInfos

    def setConcentricNeutralCableInfos(self, value):
        for x in self._ConcentricNeutralCableInfos:
            x.WireType = None
        for y in value:
            y._WireType = self
        self._ConcentricNeutralCableInfos = value

    ConcentricNeutralCableInfos = property(getConcentricNeutralCableInfos, setConcentricNeutralCableInfos)

    def addConcentricNeutralCableInfos(self, *ConcentricNeutralCableInfos):
        for obj in ConcentricNeutralCableInfos:
            obj.WireType = self

    def removeConcentricNeutralCableInfos(self, *ConcentricNeutralCableInfos):
        for obj in ConcentricNeutralCableInfos:
            obj.WireType = None

    def getWireArrangements(self):
        """All wire arrangements using this wire type.
        """
        return self._WireArrangements

    def setWireArrangements(self, value):
        for x in self._WireArrangements:
            x.WireType = None
        for y in value:
            y._WireType = self
        self._WireArrangements = value

    WireArrangements = property(getWireArrangements, setWireArrangements)

    def addWireArrangements(self, *WireArrangements):
        for obj in WireArrangements:
            obj.WireType = self

    def removeWireArrangements(self, *WireArrangements):
        for obj in WireArrangements:
            obj.WireType = None

