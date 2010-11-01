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

from CIM14v13.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class RegulationSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    def __init__(self, lineDropCompensation=False, lineDropX=0.0, lineDropR=0.0, RegulatingControl=None, VoltageControlZones=None, *args, **kw_args):
        """Initializes a new 'RegulationSchedule' instance.

        @param lineDropCompensation: Flag to indicate that line drop compensation is to be applied 
        @param lineDropX: Line drop reactance. 
        @param lineDropR: Line drop resistance. 
        @param RegulatingControl: Regulating controls that have this Schedule.
        @param VoltageControlZones: A VoltageControlZone may have a  voltage regulation schedule.
        """
        #: Flag to indicate that line drop compensation is to be applied 
        self.lineDropCompensation = lineDropCompensation

        #: Line drop reactance. 
        self.lineDropX = lineDropX

        #: Line drop resistance. 
        self.lineDropR = lineDropR

        self._RegulatingControl = None
        self.RegulatingControl = RegulatingControl

        self._VoltageControlZones = []
        self.VoltageControlZones = [] if VoltageControlZones is None else VoltageControlZones

        super(RegulationSchedule, self).__init__(*args, **kw_args)

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
            self._RegulatingControl._RegulationSchedule.append(self)

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

    def getVoltageControlZones(self):
        """A VoltageControlZone may have a  voltage regulation schedule.
        """
        return self._VoltageControlZones

    def setVoltageControlZones(self, value):
        for x in self._VoltageControlZones:
            x._RegulationSchedule = None
        for y in value:
            y._RegulationSchedule = self
        self._VoltageControlZones = value

    VoltageControlZones = property(getVoltageControlZones, setVoltageControlZones)

    def addVoltageControlZones(self, *VoltageControlZones):
        for obj in VoltageControlZones:
            obj._RegulationSchedule = self
            self._VoltageControlZones.append(obj)

    def removeVoltageControlZones(self, *VoltageControlZones):
        for obj in VoltageControlZones:
            obj._RegulationSchedule = None
            self._VoltageControlZones.remove(obj)

