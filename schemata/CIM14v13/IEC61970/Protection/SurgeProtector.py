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

from CIM14v13.IEC61970.Core.Equipment import Equipment

class SurgeProtector(Equipment):
    """Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the said equipment against transient voltage spikes caused by lightning or switching activity.
    """

    def __init__(self, SurgeProtectorTypeAsset=None, SurgeProtectorAsset=None, **kw_args):
        """Initializes a new 'SurgeProtector' instance.

        @param SurgeProtectorTypeAsset:
        @param SurgeProtectorAsset:
        """
        self._SurgeProtectorTypeAsset = None
        self.SurgeProtectorTypeAsset = SurgeProtectorTypeAsset

        self._SurgeProtectorAsset = None
        self.SurgeProtectorAsset = SurgeProtectorAsset

        super(SurgeProtector, self).__init__(**kw_args)

    def getSurgeProtectorTypeAsset(self):
        
        return self._SurgeProtectorTypeAsset

    def setSurgeProtectorTypeAsset(self, value):
        if self._SurgeProtectorTypeAsset is not None:
            filtered = [x for x in self.SurgeProtectorTypeAsset.SurgeProtectors if x != self]
            self._SurgeProtectorTypeAsset._SurgeProtectors = filtered

        self._SurgeProtectorTypeAsset = value
        if self._SurgeProtectorTypeAsset is not None:
            self._SurgeProtectorTypeAsset._SurgeProtectors.append(self)

    SurgeProtectorTypeAsset = property(getSurgeProtectorTypeAsset, setSurgeProtectorTypeAsset)

    def getSurgeProtectorAsset(self):
        
        return self._SurgeProtectorAsset

    def setSurgeProtectorAsset(self, value):
        if self._SurgeProtectorAsset is not None:
            self._SurgeProtectorAsset._SurgeProtector = None

        self._SurgeProtectorAsset = value
        if self._SurgeProtectorAsset is not None:
            self._SurgeProtectorAsset._SurgeProtector = self

    SurgeProtectorAsset = property(getSurgeProtectorAsset, setSurgeProtectorAsset)

