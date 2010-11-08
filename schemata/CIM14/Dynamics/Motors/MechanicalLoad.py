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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class MechanicalLoad(PowerSystemResource):
    """A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.
    """

    def __init__(self, rotatingMachine0=None, *args, **kw_args):
        """Initialises a new 'MechanicalLoad' instance.

        @param rotatingMachine0:
        """
        self._rotatingMachine0 = []
        self.rotatingMachine0 = [] if rotatingMachine0 is None else rotatingMachine0

        super(MechanicalLoad, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["rotatingMachine0"]
    _many_refs = ["rotatingMachine0"]

    def getrotatingMachine0(self):
        
        return self._rotatingMachine0

    def setrotatingMachine0(self, value):
        for p in self._rotatingMachine0:
            filtered = [q for q in p.mechanicalLoad0 if q != self]
            self._rotatingMachine0._mechanicalLoad0 = filtered
        for r in value:
            if self not in r._mechanicalLoad0:
                r._mechanicalLoad0.append(self)
        self._rotatingMachine0 = value

    rotatingMachine0 = property(getrotatingMachine0, setrotatingMachine0)

    def addrotatingMachine0(self, *rotatingMachine0):
        for obj in rotatingMachine0:
            if self not in obj._mechanicalLoad0:
                obj._mechanicalLoad0.append(self)
            self._rotatingMachine0.append(obj)

    def removerotatingMachine0(self, *rotatingMachine0):
        for obj in rotatingMachine0:
            if self in obj._mechanicalLoad0:
                obj._mechanicalLoad0.remove(self)
            self._rotatingMachine0.remove(obj)

