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

class Seal(IdentifiedObject):
    """Physically controls access to AssetContainers.
    """

    def __init__(self, condition='locked', kind='other', sealNumber='', appliedDateTime='', AssetContainer=None, *args, **kw_args):
        """Initializes a new 'Seal' instance.

        @param condition: Condition of seal. Values are: "locked", "open", "missing", "broken", "other"
        @param kind: Kind of seal. Values are: "other", "steel", "lock", "lead"
        @param sealNumber: (reserved word) Seal number. 
        @param appliedDateTime: Date and time this seal has been applied. 
        @param AssetContainer: Asset container to which this seal is applied.
        """
        #: Condition of seal. Values are: "locked", "open", "missing", "broken", "other"
        self.condition = condition

        #: Kind of seal. Values are: "other", "steel", "lock", "lead"
        self.kind = kind

        #: (reserved word) Seal number. 
        self.sealNumber = sealNumber

        #: Date and time this seal has been applied. 
        self.appliedDateTime = appliedDateTime

        self._AssetContainer = None
        self.AssetContainer = AssetContainer

        super(Seal, self).__init__(*args, **kw_args)

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

