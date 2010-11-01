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

from CIM14v13.Element import Element

class ProfileData(Element):
    """Data for profile.
    """

    def __init__(self, stopDateTime='', energyLevel=0.0, startDateTime='', capacityLevel=0.0, sequenceNumber=0, Profile=None, *args, **kw_args):
        """Initializes a new 'ProfileData' instance.

        @param stopDateTime: Stop date/time for this profile. 
        @param energyLevel: Energy level for the profile 
        @param startDateTime: Start date/time for this profile. 
        @param capacityLevel: Active power capacity level for the profile. 
        @param sequenceNumber: Sequence to provide item numbering for the profile. { greater than or equal to 1 } 
        @param Profile: A profile has profile data associated with it.
        """
        #: Stop date/time for this profile. 
        self.stopDateTime = stopDateTime

        #: Energy level for the profile 
        self.energyLevel = energyLevel

        #: Start date/time for this profile. 
        self.startDateTime = startDateTime

        #: Active power capacity level for the profile. 
        self.capacityLevel = capacityLevel

        #: Sequence to provide item numbering for the profile. { greater than or equal to 1 } 
        self.sequenceNumber = sequenceNumber

        self._Profile = []
        self.Profile = [] if Profile is None else Profile

        super(ProfileData, self).__init__(*args, **kw_args)

    def getProfile(self):
        """A profile has profile data associated with it.
        """
        return self._Profile

    def setProfile(self, value):
        for p in self._Profile:
            filtered = [q for q in p.ProfileDatas if q != self]
            self._Profile._ProfileDatas = filtered
        for r in value:
            if self not in r._ProfileDatas:
                r._ProfileDatas.append(self)
        self._Profile = value

    Profile = property(getProfile, setProfile)

    def addProfile(self, *Profile):
        for obj in Profile:
            if self not in obj._ProfileDatas:
                obj._ProfileDatas.append(self)
            self._Profile.append(obj)

    def removeProfile(self, *Profile):
        for obj in Profile:
            if self in obj._ProfileDatas:
                obj._ProfileDatas.remove(self)
            self._Profile.remove(obj)

