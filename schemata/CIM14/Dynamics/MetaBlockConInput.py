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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class MetaBlockConInput(IdentifiedObject):
    """If model the association to MeasurementType, the it means take the input from the associated PSR or Terminal in the static model.
    """

    def __init__(self, MetaBlockConSignal=None, MemberOf_MetaBlockConnection=None, Unit=None, **kw_args):
        """Initializes a new 'MetaBlockConInput' instance.

        @param MetaBlockConSignal:
        @param MemberOf_MetaBlockConnection:
        @param Unit:
        """
        self._MetaBlockConSignal = None
        self.MetaBlockConSignal = MetaBlockConSignal

        self._MemberOf_MetaBlockConnection = None
        self.MemberOf_MetaBlockConnection = MemberOf_MetaBlockConnection

        self._Unit = None
        self.Unit = Unit

        super(MetaBlockConInput, self).__init__(**kw_args)

    def getMetaBlockConSignal(self):
        
        return self._MetaBlockConSignal

    def setMetaBlockConSignal(self, value):
        if self._MetaBlockConSignal is not None:
            self._MetaBlockConSignal._MetaBlockConInput = None

        self._MetaBlockConSignal = value
        if self._MetaBlockConSignal is not None:
            self._MetaBlockConSignal._MetaBlockConInput = self

    MetaBlockConSignal = property(getMetaBlockConSignal, setMetaBlockConSignal)

    def getMemberOf_MetaBlockConnection(self):
        
        return self._MemberOf_MetaBlockConnection

    def setMemberOf_MetaBlockConnection(self, value):
        if self._MemberOf_MetaBlockConnection is not None:
            filtered = [x for x in self.MemberOf_MetaBlockConnection.MetaBlockConInput if x != self]
            self._MemberOf_MetaBlockConnection._MetaBlockConInput = filtered

        self._MemberOf_MetaBlockConnection = value
        if self._MemberOf_MetaBlockConnection is not None:
            self._MemberOf_MetaBlockConnection._MetaBlockConInput.append(self)

    MemberOf_MetaBlockConnection = property(getMemberOf_MetaBlockConnection, setMemberOf_MetaBlockConnection)

    def getUnit(self):
        
        return self._Unit

    def setUnit(self, value):
        if self._Unit is not None:
            filtered = [x for x in self.Unit.MetaBlockConInput if x != self]
            self._Unit._MetaBlockConInput = filtered

        self._Unit = value
        if self._Unit is not None:
            self._Unit._MetaBlockConInput.append(self)

    Unit = property(getUnit, setUnit)

