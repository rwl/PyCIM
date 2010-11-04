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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WireType(IdentifiedObject):
    """Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    def __init__(self, material='aluminum', strandCount=0, rAC25=0.0, coreStrandCount=0, ratedCurrent=0.0, sizeDescription='', gmr=0.0, rAC75=0.0, radius=0.0, rDC20=0.0, rAC50=0.0, coreRadius=0.0, WireArrangements=None, ConcentricNeutralCableInfos=None, **kw_args):
        """Initializes a new 'WireType' instance.

        @param material: Wire material. Values are: "aluminum", "steel", "other", "copper", "acsr"
        @param strandCount: Number of strands in the wire. 
        @param rAC25: AC resistance per unit length of the conductor at 25 degrees C. 
        @param coreStrandCount: (if used) Number of strands in the steel core. 
        @param ratedCurrent: Current carrying capacity of the wire under stated thermal conditions. 
        @param sizeDescription: Describes the wire guage or cross section (e.g., 4/0, #2, 336.5). 
        @param gmr: Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor. 
        @param rAC75: AC resistance per unit length of the conductor at 75 degrees C. 
        @param radius: Outside radius of the wire. 
        @param rDC20: DC resistance per unit length of the conductor at 20 degrees C. 
        @param rAC50: AC resistance per unit length of the conductor at 50 degrees C. 
        @param coreRadius: (if there is a different core material) Radius of the central core. 
        @param WireArrangements: All wire arrangements using this wire type.
        @param ConcentricNeutralCableInfos: All concentric neutral cables using this wire type.
        """
        #: Wire material.Values are: "aluminum", "steel", "other", "copper", "acsr"
        self.material = material

        #: Number of strands in the wire.
        self.strandCount = strandCount

        #: AC resistance per unit length of the conductor at 25 degrees C.
        self.rAC25 = rAC25

        #: (if used) Number of strands in the steel core.
        self.coreStrandCount = coreStrandCount

        #: Current carrying capacity of the wire under stated thermal conditions.
        self.ratedCurrent = ratedCurrent

        #: Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).
        self.sizeDescription = sizeDescription

        #: Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
        self.gmr = gmr

        #: AC resistance per unit length of the conductor at 75 degrees C.
        self.rAC75 = rAC75

        #: Outside radius of the wire.
        self.radius = radius

        #: DC resistance per unit length of the conductor at 20 degrees C.
        self.rDC20 = rDC20

        #: AC resistance per unit length of the conductor at 50 degrees C.
        self.rAC50 = rAC50

        #: (if there is a different core material) Radius of the central core.
        self.coreRadius = coreRadius

        self._WireArrangements = []
        self.WireArrangements = [] if WireArrangements is None else WireArrangements

        self._ConcentricNeutralCableInfos = []
        self.ConcentricNeutralCableInfos = [] if ConcentricNeutralCableInfos is None else ConcentricNeutralCableInfos

        super(WireType, self).__init__(**kw_args)

    def getWireArrangements(self):
        """All wire arrangements using this wire type.
        """
        return self._WireArrangements

    def setWireArrangements(self, value):
        for x in self._WireArrangements:
            x._WireType = None
        for y in value:
            y._WireType = self
        self._WireArrangements = value

    WireArrangements = property(getWireArrangements, setWireArrangements)

    def addWireArrangements(self, *WireArrangements):
        for obj in WireArrangements:
            obj._WireType = self
            self._WireArrangements.append(obj)

    def removeWireArrangements(self, *WireArrangements):
        for obj in WireArrangements:
            obj._WireType = None
            self._WireArrangements.remove(obj)

    def getConcentricNeutralCableInfos(self):
        """All concentric neutral cables using this wire type.
        """
        return self._ConcentricNeutralCableInfos

    def setConcentricNeutralCableInfos(self, value):
        for x in self._ConcentricNeutralCableInfos:
            x._WireType = None
        for y in value:
            y._WireType = self
        self._ConcentricNeutralCableInfos = value

    ConcentricNeutralCableInfos = property(getConcentricNeutralCableInfos, setConcentricNeutralCableInfos)

    def addConcentricNeutralCableInfos(self, *ConcentricNeutralCableInfos):
        for obj in ConcentricNeutralCableInfos:
            obj._WireType = self
            self._ConcentricNeutralCableInfos.append(obj)

    def removeConcentricNeutralCableInfos(self, *ConcentricNeutralCableInfos):
        for obj in ConcentricNeutralCableInfos:
            obj._WireType = None
            self._ConcentricNeutralCableInfos.remove(obj)

