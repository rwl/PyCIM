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

from CIM14v13.IEC61968.Informative.InfAssets.ConductorAsset import ConductorAsset

class OverheadConductorAsset(ConductorAsset):
    """Physical conductor performing the Conductor role that is used in overhead applications.
    """

    def __init__(self, MountingPoint=None, *args, **kw_args):
        """Initializes a new 'OverheadConductorAsset' instance.

        @param MountingPoint:
        """
        self._MountingPoint = None
        self.MountingPoint = MountingPoint

        super(OverheadConductorAsset, self).__init__(*args, **kw_args)

    def getMountingPoint(self):
        
        return self._MountingPoint

    def setMountingPoint(self, value):
        if self._MountingPoint is not None:
            filtered = [x for x in self.MountingPoint.OverheadConductors if x != self]
            self._MountingPoint._OverheadConductors = filtered

        self._MountingPoint = value
        if self._MountingPoint is not None:
            self._MountingPoint._OverheadConductors.append(self)

    MountingPoint = property(getMountingPoint, setMountingPoint)

