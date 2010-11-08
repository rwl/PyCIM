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

from CIM14.IEC61968.AssetModels.CableInfo import CableInfo

class ConcentricNeutralCableInfo(CableInfo):
    """Concentric neutral cable data.
    """

    def __init__(self, diameterOverNeutral=0.0, neutralStrandCount=0, WireType=None, *args, **kw_args):
        """Initialises a new 'ConcentricNeutralCableInfo' instance.

        @param diameterOverNeutral: Diameter over the concentric neutral strands. 
        @param neutralStrandCount: Number of concentric neutral strands. 
        @param WireType: Wire type used for this concentric neutral cable.
        """
        #: Diameter over the concentric neutral strands.
        self.diameterOverNeutral = diameterOverNeutral

        #: Number of concentric neutral strands.
        self.neutralStrandCount = neutralStrandCount

        self._WireType = None
        self.WireType = WireType

        super(ConcentricNeutralCableInfo, self).__init__(*args, **kw_args)

    _attrs = ["diameterOverNeutral", "neutralStrandCount"]
    _attr_types = {"diameterOverNeutral": float, "neutralStrandCount": int}
    _defaults = {"diameterOverNeutral": 0.0, "neutralStrandCount": 0}
    _enums = {}
    _refs = ["WireType"]
    _many_refs = []

    def getWireType(self):
        """Wire type used for this concentric neutral cable.
        """
        return self._WireType

    def setWireType(self, value):
        if self._WireType is not None:
            filtered = [x for x in self.WireType.ConcentricNeutralCableInfos if x != self]
            self._WireType._ConcentricNeutralCableInfos = filtered

        self._WireType = value
        if self._WireType is not None:
            self._WireType._ConcentricNeutralCableInfos.append(self)

    WireType = property(getWireType, setWireType)

