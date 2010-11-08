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

class Seal(IdentifiedObject):
    """Physically controls access to AssetContainers.
    """

    def __init__(self, kind="other", condition="open", sealNumber='', appliedDateTime='', AssetContainer=None, *args, **kw_args):
        """Initialises a new 'Seal' instance.

        @param kind: Kind of seal. Values are: "other", "lead", "steel", "lock"
        @param condition: Condition of seal. Values are: "open", "broken", "missing", "other", "locked"
        @param sealNumber: (reserved word) Seal number. 
        @param appliedDateTime: Date and time this seal has been applied. 
        @param AssetContainer: Asset container to which this seal is applied.
        """
        #: Kind of seal. Values are: "other", "lead", "steel", "lock"
        self.kind = kind

        #: Condition of seal. Values are: "open", "broken", "missing", "other", "locked"
        self.condition = condition

        #: (reserved word) Seal number.
        self.sealNumber = sealNumber

        #: Date and time this seal has been applied.
        self.appliedDateTime = appliedDateTime

        self._AssetContainer = None
        self.AssetContainer = AssetContainer

        super(Seal, self).__init__(*args, **kw_args)

    _attrs = ["kind", "condition", "sealNumber", "appliedDateTime"]
    _attr_types = {"kind": str, "condition": str, "sealNumber": str, "appliedDateTime": str}
    _defaults = {"kind": "other", "condition": "open", "sealNumber": '', "appliedDateTime": ''}
    _enums = {"kind": "SealKind", "condition": "SealConditionKind"}
    _refs = ["AssetContainer"]
    _many_refs = []

    def getAssetContainer(self):
        """Asset container to which this seal is applied.
        """
        return self._AssetContainer

    def setAssetContainer(self, value):
        if self._AssetContainer is not None:
            filtered = [x for x in self.AssetContainer.Seals if x != self]
            self._AssetContainer._Seals = filtered

        self._AssetContainer = value
        if self._AssetContainer is not None:
            self._AssetContainer._Seals.append(self)

    AssetContainer = property(getAssetContainer, setAssetContainer)

