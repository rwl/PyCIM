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

class TapSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a tap step.
    """

    def __init__(self, lineDropX=0.0, lineDropCompensation=False, lineDropR=0.0, TapChanger=None, **kw_args):
        """Initializes a new 'TapSchedule' instance.

        @param lineDropX: Line drop reactance. 
        @param lineDropCompensation: Flag to indicate that line drop compensation is to be applied 
        @param lineDropR: Line drop resistance. 
        @param TapChanger: A TapSchedule is associated with a TapChanger.
        """
        #: Line drop reactance.
        self.lineDropX = lineDropX

        #: Flag to indicate that line drop compensation is to be applied
        self.lineDropCompensation = lineDropCompensation

        #: Line drop resistance.
        self.lineDropR = lineDropR

        self._TapChanger = None
        self.TapChanger = TapChanger

        super(TapSchedule, self).__init__(**kw_args)

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
            self._TapChanger._TapSchedules.append(self)

    TapChanger = property(getTapChanger, setTapChanger)

