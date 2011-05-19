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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class VoltageControlZone(PowerSystemResource):
    """An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """

    def __init__(self, RegulationSchedule=None, BusbarSection=None, *args, **kw_args):
        """Initialises a new 'VoltageControlZone' instance.

        @param RegulationSchedule: A VoltageControlZone may have a  voltage regulation schedule.
        @param BusbarSection: A VoltageControlZone is controlled by a designated BusbarSection.
        """
        self._RegulationSchedule = None
        self.RegulationSchedule = RegulationSchedule

        self._BusbarSection = None
        self.BusbarSection = BusbarSection

        super(VoltageControlZone, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RegulationSchedule", "BusbarSection"]
    _many_refs = []

    def getRegulationSchedule(self):
        """A VoltageControlZone may have a  voltage regulation schedule.
        """
        return self._RegulationSchedule

    def setRegulationSchedule(self, value):
        if self._RegulationSchedule is not None:
            filtered = [x for x in self.RegulationSchedule.VoltageControlZones if x != self]
            self._RegulationSchedule._VoltageControlZones = filtered

        self._RegulationSchedule = value
        if self._RegulationSchedule is not None:
            if self not in self._RegulationSchedule._VoltageControlZones:
                self._RegulationSchedule._VoltageControlZones.append(self)

    RegulationSchedule = property(getRegulationSchedule, setRegulationSchedule)

    def getBusbarSection(self):
        """A VoltageControlZone is controlled by a designated BusbarSection.
        """
        return self._BusbarSection

    def setBusbarSection(self, value):
        if self._BusbarSection is not None:
            self._BusbarSection._VoltageControlZone = None

        self._BusbarSection = value
        if self._BusbarSection is not None:
            self._BusbarSection.VoltageControlZone = None
            self._BusbarSection._VoltageControlZone = self

    BusbarSection = property(getBusbarSection, setBusbarSection)

