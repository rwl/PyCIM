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

from CIM14.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class TapSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a tap step.
    """

    def __init__(self, lineDropCompensation=False, lineDropR=0.0, lineDropX=0.0, TapChanger=None, *args, **kw_args):
        """Initialises a new 'TapSchedule' instance.

        @param lineDropCompensation: Flag to indicate that line drop compensation is to be applied 
        @param lineDropR: Line drop resistance. 
        @param lineDropX: Line drop reactance. 
        @param TapChanger: A TapSchedule is associated with a TapChanger.
        """
        #: Flag to indicate that line drop compensation is to be applied
        self.lineDropCompensation = lineDropCompensation

        #: Line drop resistance.
        self.lineDropR = lineDropR

        #: Line drop reactance.
        self.lineDropX = lineDropX

        self._TapChanger = None
        self.TapChanger = TapChanger

        super(TapSchedule, self).__init__(*args, **kw_args)

    _attrs = ["lineDropCompensation", "lineDropR", "lineDropX"]
    _attr_types = {"lineDropCompensation": bool, "lineDropR": float, "lineDropX": float}
    _defaults = {"lineDropCompensation": False, "lineDropR": 0.0, "lineDropX": 0.0}
    _enums = {}
    _refs = ["TapChanger"]
    _many_refs = []

    def getTapChanger(self):
        """A TapSchedule is associated with a TapChanger.
        """
        return self._TapChanger

    def setTapChanger(self, value):
        if self._TapChanger is not None:
            filtered = [x for x in self.TapChanger.TapSchedules if x != self]
            self._TapChanger._TapSchedules = filtered

        self._TapChanger = value
        if self._TapChanger is not None:
            if self not in self._TapChanger._TapSchedules:
                self._TapChanger._TapSchedules.append(self)

    TapChanger = property(getTapChanger, setTapChanger)

