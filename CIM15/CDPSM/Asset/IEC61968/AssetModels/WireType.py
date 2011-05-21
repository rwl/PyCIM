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

from CIM15.CDPSM.Asset.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WireType(IdentifiedObject):
    """Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    def __init__(self, rDC20=0.0, coreRadius=0.0, rAC75=0.0, material="aluminum", ratedCurrent=0.0, strandCount=0, rAC25=0.0, rAC50=0.0, radius=0.0, gmr=0.0, coreStrandCount=0, sizeDescription='', WireArrangements=None, *args, **kw_args):
        """Initialises a new 'WireType' instance.

        @param rDC20: DC resistance per unit length of the conductor at 20 oC. 
        @param coreRadius: (if there is a different core material) Radius of the central core. 
        @param rAC75: AC resistance per unit length of the conductor at 75 oC. 
        @param material: Wire material. Values are: "aluminum", "copper", "other", "steel", "acsr"
        @param ratedCurrent: Current carrying capacity of the wire under stated thermal conditions. 
        @param strandCount: Number of strands in the wire. 
        @param rAC25: AC resistance per unit length of the conductor at 25 oC. 
        @param rAC50: AC resistance per unit length of the conductor at 50 oC. 
        @param radius: Outside radius of the wire. 
        @param gmr: Geometric mean radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor. 
        @param coreStrandCount: (if used) Number of strands in the steel core. 
        @param sizeDescription: Describes the wire guage or cross section (e.g., 4/0, #2, 336.5). 
        @param WireArrangements: All wire arrangements using this wire type.
        """
        #: DC resistance per unit length of the conductor at 20 oC.
        self.rDC20 = rDC20

        #: (if there is a different core material) Radius of the central core.
        self.coreRadius = coreRadius

        #: AC resistance per unit length of the conductor at 75 oC.
        self.rAC75 = rAC75

        #: Wire material. Values are: "aluminum", "copper", "other", "steel", "acsr"
        self.material = material

        #: Current carrying capacity of the wire under stated thermal conditions.
        self.ratedCurrent = ratedCurrent

        #: Number of strands in the wire.
        self.strandCount = strandCount

        #: AC resistance per unit length of the conductor at 25 oC.
        self.rAC25 = rAC25

        #: AC resistance per unit length of the conductor at 50 oC.
        self.rAC50 = rAC50

        #: Outside radius of the wire.
        self.radius = radius

        #: Geometric mean radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
        self.gmr = gmr

        #: (if used) Number of strands in the steel core.
        self.coreStrandCount = coreStrandCount

        #: Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).
        self.sizeDescription = sizeDescription

        self._WireArrangements = []
        self.WireArrangements = [] if WireArrangements is None else WireArrangements

        super(WireType, self).__init__(*args, **kw_args)

    _attrs = ["rDC20", "coreRadius", "rAC75", "material", "ratedCurrent", "strandCount", "rAC25", "rAC50", "radius", "gmr", "coreStrandCount", "sizeDescription"]
    _attr_types = {"rDC20": float, "coreRadius": float, "rAC75": float, "material": str, "ratedCurrent": float, "strandCount": int, "rAC25": float, "rAC50": float, "radius": float, "gmr": float, "coreStrandCount": int, "sizeDescription": str}
    _defaults = {"rDC20": 0.0, "coreRadius": 0.0, "rAC75": 0.0, "material": "aluminum", "ratedCurrent": 0.0, "strandCount": 0, "rAC25": 0.0, "rAC50": 0.0, "radius": 0.0, "gmr": 0.0, "coreStrandCount": 0, "sizeDescription": ''}
    _enums = {"material": "ConductorMaterialKind"}
    _refs = ["WireArrangements"]
    _many_refs = ["WireArrangements"]

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

