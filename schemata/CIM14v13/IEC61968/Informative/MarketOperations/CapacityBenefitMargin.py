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

from CIM14v13.IEC61968.Informative.EnergyScheduling.Profile import Profile

class CapacityBenefitMargin(Profile):
    """Capacity Benefit Margin (CBM) is defined as that amount of transmission transfer capability reserved by load serving entities to ensure access to generation from interconnected systems to meet generation reliability requirements. Reservation fo CBM by a load serving entity allows that entity to reduce its installed generating capacity below that which may otherwise have been necessary without interconnections to meet its generation reliability requirements.  CBM is modeled as a profile with values in different time periods which are represented by the profile data.
    """

    def __init__(self, Season=None, Flowgate=None, *args, **kw_args):
        """Initializes a new 'CapacityBenefitMargin' instance.

        @param Season: Capacity Benefit Margin may differ based on the season
        @param Flowgate: A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data
        """
        self._Season = None
        self.Season = Season

        self._Flowgate = []
        self.Flowgate = [] if Flowgate is None else Flowgate

        super(CapacityBenefitMargin, self).__init__(*args, **kw_args)

    def getSeason(self):
        """Capacity Benefit Margin may differ based on the season
        """
        return self._Season

    def setSeason(self, value):
        if self._Season is not None:
            filtered = [x for x in self.Season.CapacityBenefitMargin if x != self]
            self._Season._CapacityBenefitMargin = filtered

        self._Season = value
        if self._Season is not None:
            self._Season._CapacityBenefitMargin.append(self)

    Season = property(getSeason, setSeason)

    def getFlowgate(self):
        """A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data
        """
        return self._Flowgate

    def setFlowgate(self, value):
        for p in self._Flowgate:
            filtered = [q for q in p.CapacityBenefitMargin if q != self]
            self._Flowgate._CapacityBenefitMargin = filtered
        for r in value:
            if self not in r._CapacityBenefitMargin:
                r._CapacityBenefitMargin.append(self)
        self._Flowgate = value

    Flowgate = property(getFlowgate, setFlowgate)

    def addFlowgate(self, *Flowgate):
        for obj in Flowgate:
            if self not in obj._CapacityBenefitMargin:
                obj._CapacityBenefitMargin.append(self)
            self._Flowgate.append(obj)

    def removeFlowgate(self, *Flowgate):
        for obj in Flowgate:
            if self in obj._CapacityBenefitMargin:
                obj._CapacityBenefitMargin.remove(self)
            self._Flowgate.remove(obj)

