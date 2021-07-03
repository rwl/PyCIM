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

from CIM16.IEC61970.Wires.Connector import Connector

class BusbarSection(Connector):
    """A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
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

