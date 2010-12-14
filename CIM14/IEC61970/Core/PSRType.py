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

class PSRType(IdentifiedObject):
    """Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.
    """

    def __init__(self, PowerSystemResources=None, *args, **kw_args):
        """Initialises a new 'PSRType' instance.

        @param PowerSystemResources: Power system resources classified with this PSRType.
        """
        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        super(PSRType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PowerSystemResources"]
    _many_refs = ["PowerSystemResources"]

    def getPowerSystemResources(self):
        """Power system resources classified with this PSRType.
        """
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for x in self._PowerSystemResources:
            x.PSRType = None
        for y in value:
            y._PSRType = self
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            obj.PSRType = self

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            obj.PSRType = None

