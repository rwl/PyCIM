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

from CIM16.CDPSM.Connectivity.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Bay(EquipmentContainer):
    """A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """

    def __init__(self, VoltageLevel=None, Substation=None, *args, **kw_args):
        """Initialises a new 'Bay' instance.

        @param VoltageLevel: The association is used in the naming hierarchy.
        @param Substation: The association is used in the naming hierarchy.
        """
        self._VoltageLevel = None
        self.VoltageLevel = VoltageLevel

        self._Substation = None
        self.Substation = Substation

        super(Bay, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["VoltageLevel", "Substation"]
    _many_refs = []

    def getVoltageLevel(self):
        """The association is used in the naming hierarchy.
        """
        return self._VoltageLevel

    def setVoltageLevel(self, value):
        if self._VoltageLevel is not None:
            filtered = [x for x in self.VoltageLevel.Bays if x != self]
            self._VoltageLevel._Bays = filtered

        self._VoltageLevel = value
        if self._VoltageLevel is not None:
            if self not in self._VoltageLevel._Bays:
                self._VoltageLevel._Bays.append(self)

    VoltageLevel = property(getVoltageLevel, setVoltageLevel)

    def getSubstation(self):
        """The association is used in the naming hierarchy.
        """
        return self._Substation

    def setSubstation(self, value):
        if self._Substation is not None:
            filtered = [x for x in self.Substation.Bays if x != self]
            self._Substation._Bays = filtered

        self._Substation = value
        if self._Substation is not None:
            if self not in self._Substation._Bays:
                self._Substation._Bays.append(self)

    Substation = property(getSubstation, setSubstation)

