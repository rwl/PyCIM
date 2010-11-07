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

class ModelingAuthoritySet(IdentifiedObject):
    """A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.
    """

    def __init__(self, ModelingAuthority=None, IdentifiedObjects=None, **kw_args):
        """Initializes a new 'ModelingAuthoritySet' instance.

        @param ModelingAuthority: A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        @param IdentifiedObjects: An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        self._ModelingAuthority = None
        self.ModelingAuthority = ModelingAuthority

        self._IdentifiedObjects = []
        self.IdentifiedObjects = [] if IdentifiedObjects is None else IdentifiedObjects

        super(ModelingAuthoritySet, self).__init__(**kw_args)

    def getModelingAuthority(self):
        """A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        return self._ModelingAuthority

    def setModelingAuthority(self, value):
        if self._ModelingAuthority is not None:
            filtered = [x for x in self.ModelingAuthority.ModelingAuthoritySets if x != self]
            self._ModelingAuthority._ModelingAuthoritySets = filtered

        self._ModelingAuthority = value
        if self._ModelingAuthority is not None:
            self._ModelingAuthority._ModelingAuthoritySets.append(self)

    ModelingAuthority = property(getModelingAuthority, setModelingAuthority)

    def getIdentifiedObjects(self):
        """An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.
        """
        return self._IdentifiedObjects

    def setIdentifiedObjects(self, value):
        for x in self._IdentifiedObjects:
            x._ModelingAuthoritySet = None
        for y in value:
            y._ModelingAuthoritySet = self
        self._IdentifiedObjects = value

    IdentifiedObjects = property(getIdentifiedObjects, setIdentifiedObjects)

    def addIdentifiedObjects(self, *IdentifiedObjects):
        for obj in IdentifiedObjects:
            obj._ModelingAuthoritySet = self
            self._IdentifiedObjects.append(obj)

    def removeIdentifiedObjects(self, *IdentifiedObjects):
        for obj in IdentifiedObjects:
            obj._ModelingAuthoritySet = None
            self._IdentifiedObjects.remove(obj)

