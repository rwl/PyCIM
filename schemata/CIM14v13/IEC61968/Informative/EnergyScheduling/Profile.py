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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Profile(IdentifiedObject):
    """A profile is a simpler curve type.
    """

    def __init__(self, ProfileDatas=None, **kw_args):
        """Initializes a new 'Profile' instance.

        @param ProfileDatas: A profile has profile data associated with it.
        """
        self._ProfileDatas = []
        self.ProfileDatas = [] if ProfileDatas is None else ProfileDatas

        super(Profile, self).__init__(**kw_args)

    def getProfileDatas(self):
        """A profile has profile data associated with it.
        """
        return self._ProfileDatas

    def setProfileDatas(self, value):
        for p in self._ProfileDatas:
            filtered = [q for q in p.Profile if q != self]
            self._ProfileDatas._Profile = filtered
        for r in value:
            if self not in r._Profile:
                r._Profile.append(self)
        self._ProfileDatas = value

    ProfileDatas = property(getProfileDatas, setProfileDatas)

    def addProfileDatas(self, *ProfileDatas):
        for obj in ProfileDatas:
            if self not in obj._Profile:
                obj._Profile.append(self)
            self._ProfileDatas.append(obj)

    def removeProfileDatas(self, *ProfileDatas):
        for obj in ProfileDatas:
            if self in obj._Profile:
                obj._Profile.remove(self)
            self._ProfileDatas.remove(obj)

