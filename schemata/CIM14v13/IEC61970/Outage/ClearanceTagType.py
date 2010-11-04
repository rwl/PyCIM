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

class ClearanceTagType(IdentifiedObject):
    """Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """

    def __init__(self, ClearanceTags=None, **kw_args):
        """Initializes a new 'ClearanceTagType' instance.

        @param ClearanceTags: The ClearanceTags currently being defined for this type.
        """
        self._ClearanceTags = []
        self.ClearanceTags = [] if ClearanceTags is None else ClearanceTags

        super(ClearanceTagType, self).__init__(**kw_args)

    def getClearanceTags(self):
        """The ClearanceTags currently being defined for this type.
        """
        return self._ClearanceTags

    def setClearanceTags(self, value):
        for x in self._ClearanceTags:
            x._ClearanceTagType = None
        for y in value:
            y._ClearanceTagType = self
        self._ClearanceTags = value

    ClearanceTags = property(getClearanceTags, setClearanceTags)

    def addClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj._ClearanceTagType = self
            self._ClearanceTags.append(obj)

    def removeClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj._ClearanceTagType = None
            self._ClearanceTags.remove(obj)

