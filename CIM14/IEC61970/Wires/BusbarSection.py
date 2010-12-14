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

from CIM14.IEC61970.Wires.Connector import Connector

class BusbarSection(Connector):
    """A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """

    def __init__(self, VoltageControlZone=None, *args, **kw_args):
        """Initialises a new 'BusbarSection' instance.

        @param VoltageControlZone: A VoltageControlZone is controlled by a designated BusbarSection.
        """
        self._VoltageControlZone = None
        self.VoltageControlZone = VoltageControlZone

        super(BusbarSection, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["VoltageControlZone"]
    _many_refs = []

    def getVoltageControlZone(self):
        """A VoltageControlZone is controlled by a designated BusbarSection.
        """
        return self._VoltageControlZone

    def setVoltageControlZone(self, value):
        if self._VoltageControlZone is not None:
            self._VoltageControlZone._BusbarSection = None

        self._VoltageControlZone = value
        if self._VoltageControlZone is not None:
            self._VoltageControlZone.BusbarSection = None
            self._VoltageControlZone._BusbarSection = self

    VoltageControlZone = property(getVoltageControlZone, setVoltageControlZone)

