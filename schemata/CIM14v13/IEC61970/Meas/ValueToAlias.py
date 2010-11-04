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

class ValueToAlias(IdentifiedObject):
    """Describes the translation of one particular value into a name, e.g. 1->'Open'
    """

    def __init__(self, value=0, ValueAliasSet=None, *args, **kw_args):
        """Initializes a new 'ValueToAlias' instance.

        @param value: The value that is mapped 
        @param ValueAliasSet: The ValueAliasSet having the ValueToAlias mappings
        """
        #: The value that is mapped
        self.value = value

        self._ValueAliasSet = None
        self.ValueAliasSet = ValueAliasSet

        super(ValueToAlias, self).__init__(*args, **kw_args)

    def getValueAliasSet(self):
        """The ValueAliasSet having the ValueToAlias mappings
        """
        return self._ValueAliasSet

    def setValueAliasSet(self, value):
        if self._ValueAliasSet is not None:
            filtered = [x for x in self.ValueAliasSet.Values if x != self]
            self._ValueAliasSet._Values = filtered

        self._ValueAliasSet = value
        if self._ValueAliasSet is not None:
            self._ValueAliasSet._Values.append(self)

    ValueAliasSet = property(getValueAliasSet, setValueAliasSet)

