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

class ModelingAuthority(IdentifiedObject):
    """A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.
    """

    def __init__(self, ModelingAuthoritySets=None, **kw_args):
        """Initializes a new 'ModelingAuthority' instance.

        @param ModelingAuthoritySets: A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        self._ModelingAuthoritySets = []
        self.ModelingAuthoritySets = [] if ModelingAuthoritySets is None else ModelingAuthoritySets

        super(ModelingAuthority, self).__init__(**kw_args)

    def getModelingAuthoritySets(self):
        """A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.
        """
        return self._ModelingAuthoritySets

    def setModelingAuthoritySets(self, value):
        for x in self._ModelingAuthoritySets:
            x._ModelingAuthority = None
        for y in value:
            y._ModelingAuthority = self
        self._ModelingAuthoritySets = value

    ModelingAuthoritySets = property(getModelingAuthoritySets, setModelingAuthoritySets)

    def addModelingAuthoritySets(self, *ModelingAuthoritySets):
        for obj in ModelingAuthoritySets:
            obj._ModelingAuthority = self
            self._ModelingAuthoritySets.append(obj)

    def removeModelingAuthoritySets(self, *ModelingAuthoritySets):
        for obj in ModelingAuthoritySets:
            obj._ModelingAuthority = None
            self._ModelingAuthoritySets.remove(obj)

