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

class RemotePoint(IdentifiedObject):
    """For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.
    """

    def __init__(self, RemoteUnit=None, *args, **kw_args):
        """Initialises a new 'RemotePoint' instance.

        @param RemoteUnit: Remote unit this point belongs to.
        """
        self._RemoteUnit = None
        self.RemoteUnit = RemoteUnit

        super(RemotePoint, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RemoteUnit"]
    _many_refs = []

    def getRemoteUnit(self):
        """Remote unit this point belongs to.
        """
        return self._RemoteUnit

    def setRemoteUnit(self, value):
        if self._RemoteUnit is not None:
            filtered = [x for x in self.RemoteUnit.RemotePoints if x != self]
            self._RemoteUnit._RemotePoints = filtered

        self._RemoteUnit = value
        if self._RemoteUnit is not None:
            self._RemoteUnit._RemotePoints.append(self)

    RemoteUnit = property(getRemoteUnit, setRemoteUnit)

