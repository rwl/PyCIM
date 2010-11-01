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

class SteamSendoutSchedule(RegularIntervalSchedule):
    """The cogeneration plant's steam sendout schedule in volume per time unit.
    """

    def __init__(self, CogenerationPlant=None, *args, **kw_args):
        """Initializes a new 'SteamSendoutSchedule' instance.

        @param CogenerationPlant: A cogeneration plant has a steam sendout schedule
        """
        self._CogenerationPlant = None
        self.CogenerationPlant = CogenerationPlant

        super(SteamSendoutSchedule, self).__init__(*args, **kw_args)

    def getCogenerationPlant(self):
        """A cogeneration plant has a steam sendout schedule
        """
        return self._CogenerationPlant

    def setCogenerationPlant(self, value):
        if self._CogenerationPlant is not None:
            self._CogenerationPlant._SteamSendoutSchedule = None

        self._CogenerationPlant = value
        if self._CogenerationPlant is not None:
            self._CogenerationPlant._SteamSendoutSchedule = self

    CogenerationPlant = property(getCogenerationPlant, setCogenerationPlant)

