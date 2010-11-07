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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WireArrangement(IdentifiedObject):
    """Identification, spacing and configuration of the wires of a Conductor, with reference to their type.
    """

    def __init__(self, position=0, mountingPointX=0.0, mountingPointY=0.0, WireType=None, ConductorInfo=None, **kw_args):
        """Initializes a new 'WireArrangement' instance.

        @param position: Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC. 
        @param mountingPointX: Signed horizontal distance from the first wire to a common reference point. 
        @param mountingPointY: Height above ground of the first wire. 
        @param WireType: Wire type used for this wire arrangement.
        @param ConductorInfo: Conductor data this wire arrangement belongs to.
        """
        #: Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.
        self.position = position

        #: Signed horizontal distance from the first wire to a common reference point.
        self.mountingPointX = mountingPointX

        #: Height above ground of the first wire.
        self.mountingPointY = mountingPointY

        self._WireType = None
        self.WireType = WireType

        self._ConductorInfo = None
        self.ConductorInfo = ConductorInfo

        super(WireArrangement, self).__init__(**kw_args)

    def getWireType(self):
        """Wire type used for this wire arrangement.
        """
        return self._WireType

    def setWireType(self, value):
        if self._WireType is not None:
            filtered = [x for x in self.WireType.WireArrangements if x != self]
            self._WireType._WireArrangements = filtered

        self._WireType = value
        if self._WireType is not None:
            self._WireType._WireArrangements.append(self)

    WireType = property(getWireType, setWireType)

    def getConductorInfo(self):
        """Conductor data this wire arrangement belongs to.
        """
        return self._ConductorInfo

    def setConductorInfo(self, value):
        if self._ConductorInfo is not None:
            filtered = [x for x in self.ConductorInfo.WireArrangements if x != self]
            self._ConductorInfo._WireArrangements = filtered

        self._ConductorInfo = value
        if self._ConductorInfo is not None:
            self._ConductorInfo._WireArrangements.append(self)

    ConductorInfo = property(getConductorInfo, setConductorInfo)

