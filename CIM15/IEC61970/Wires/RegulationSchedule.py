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

from CIM15.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class RegulationSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a controlled variable, e.g., busbar voltage.A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    def __init__(self, RegulatingControl=None, VoltageControlZones=None, *args, **kw_args):
        """Initialises a new 'RegulationSchedule' instance.

        @param RegulatingControl: Regulating controls that have this Schedule.
        @param VoltageControlZones: A VoltageControlZone may have a  voltage regulation schedule.
        """
        self._RegulatingControl = None
        self.RegulatingControl = RegulatingControl

        self._VoltageControlZones = []
        self.VoltageControlZones = [] if VoltageControlZones is None else VoltageControlZones

        super(RegulationSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RegulatingControl", "VoltageControlZones"]
    _many_refs = ["VoltageControlZones"]

    def getRegulatingControl(self):
        """Regulating controls that have this Schedule.
        """
        return self._RegulatingControl

    def setRegulatingControl(self, value):
        if self._RegulatingControl is not None:
            filtered = [x for x in self.RegulatingControl.RegulationSchedule if x != self]
            self._RegulatingControl._RegulationSchedule = filtered

        self._RegulatingControl = value
        if self._RegulatingControl is not None:
            if self not in self._RegulatingControl._RegulationSchedule:
                self._RegulatingControl._RegulationSchedule.append(self)

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

    def getVoltageControlZones(self):
        """A VoltageControlZone may have a  voltage regulation schedule.
        """
        return self._VoltageControlZones

    def setVoltageControlZones(self, value):
        for x in self._VoltageControlZones:
            x.RegulationSchedule = None
        for y in value:
            y._RegulationSchedule = self
        self._VoltageControlZones = value

    VoltageControlZones = property(getVoltageControlZones, setVoltageControlZones)

    def addVoltageControlZones(self, *VoltageControlZones):
        for obj in VoltageControlZones:
            obj.RegulationSchedule = self

    def removeVoltageControlZones(self, *VoltageControlZones):
        for obj in VoltageControlZones:
            obj.RegulationSchedule = None

