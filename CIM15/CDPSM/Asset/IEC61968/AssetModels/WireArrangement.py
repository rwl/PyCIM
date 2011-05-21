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

class WireArrangement(IdentifiedObject):
    """Identification, spacing and configuration of the wires of a conductor, with reference to their type.
    """

    def __init__(self, mountingPointY=0.0, position=0, mountingPointX=0.0, WireType=None, ConductorInfo=None, *args, **kw_args):
        """Initialises a new 'WireArrangement' instance.

        @param mountingPointY: Height above ground of the first wire. 
        @param position: Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC. 
        @param mountingPointX: Signed horizontal distance from the first wire to a common reference point. 
        @param WireType: Wire type used for this wire arrangement.
        @param ConductorInfo: Conductor data this wire arrangement belongs to.
        """
        #: Height above ground of the first wire.
        self.mountingPointY = mountingPointY

        #: Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.
        self.position = position

        #: Signed horizontal distance from the first wire to a common reference point.
        self.mountingPointX = mountingPointX

        self._WireType = None
        self.WireType = WireType

        self._ConductorInfo = None
        self.ConductorInfo = ConductorInfo

        super(WireArrangement, self).__init__(*args, **kw_args)

    _attrs = ["mountingPointY", "position", "mountingPointX"]
    _attr_types = {"mountingPointY": float, "position": int, "mountingPointX": float}
    _defaults = {"mountingPointY": 0.0, "position": 0, "mountingPointX": 0.0}
    _enums = {}
    _refs = ["WireType", "ConductorInfo"]
    _many_refs = []

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
            if self not in self._WireType._WireArrangements:
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
            if self not in self._ConductorInfo._WireArrangements:
                self._ConductorInfo._WireArrangements.append(self)

    ConductorInfo = property(getConductorInfo, setConductorInfo)

