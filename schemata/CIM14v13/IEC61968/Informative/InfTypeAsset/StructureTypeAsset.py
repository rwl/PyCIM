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

from CIM14v13.IEC61968.Informative.InfTypeAsset.TypeAsset import TypeAsset

class StructureTypeAsset(TypeAsset):
    """A Type of Structural Asset with properties common to a large number of asset models.
    """

    def __init__(self, ratedVoltage=0.0, MountConnections=None, **kw_args):
        """Initializes a new 'StructureTypeAsset' instance.

        @param ratedVoltage: Maximum rated voltage of the equipment that can be mounted on/contained within the structure. 
        @param MountConnections:
        """
        #: Maximum rated voltage of the equipment that can be mounted on/contained within the structure.
        self.ratedVoltage = ratedVoltage

        self._MountConnections = []
        self.MountConnections = [] if MountConnections is None else MountConnections

        super(StructureTypeAsset, self).__init__(**kw_args)

    def getMountConnections(self):
        
        return self._MountConnections

    def setMountConnections(self, value):
        for p in self._MountConnections:
            filtered = [q for q in p.StructureTypeAssets if q != self]
            self._MountConnections._StructureTypeAssets = filtered
        for r in value:
            if self not in r._StructureTypeAssets:
                r._StructureTypeAssets.append(self)
        self._MountConnections = value

    MountConnections = property(getMountConnections, setMountConnections)

    def addMountConnections(self, *MountConnections):
        for obj in MountConnections:
            if self not in obj._StructureTypeAssets:
                obj._StructureTypeAssets.append(self)
            self._MountConnections.append(obj)

    def removeMountConnections(self, *MountConnections):
        for obj in MountConnections:
            if self in obj._StructureTypeAssets:
                obj._StructureTypeAssets.remove(self)
            self._MountConnections.remove(obj)

