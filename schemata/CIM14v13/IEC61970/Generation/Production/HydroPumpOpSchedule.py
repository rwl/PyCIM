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

from CIM14v13.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule

class HydroPumpOpSchedule(RegularIntervalSchedule):
    """The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)
    """

    def __init__(self, HydroPump=None, **kw_args):
        """Initializes a new 'HydroPumpOpSchedule' instance.

        @param HydroPump: The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """
        self._HydroPump = None
        self.HydroPump = HydroPump

        super(HydroPumpOpSchedule, self).__init__(**kw_args)

    def getHydroPump(self):
        """The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """
        return self._HydroPump

    def setHydroPump(self, value):
        if self._HydroPump is not None:
            self._HydroPump._HydroPumpOpSchedule = None

        self._HydroPump = value
        if self._HydroPump is not None:
            self._HydroPump._HydroPumpOpSchedule = self

    HydroPump = property(getHydroPump, setHydroPump)

