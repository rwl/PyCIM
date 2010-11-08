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

class ValueAliasSet(IdentifiedObject):
    """Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.
    """

    def __init__(self, Commands=None, Values=None, Discretes=None, *args, **kw_args):
        """Initialises a new 'ValueAliasSet' instance.

        @param Commands: The ValueAliasSet used for translation of a Control value to a name.
        @param Values: The ValueToAlias mappings included in the set
        @param Discretes: The Measurements using the set for translation
        """
        self._Commands = []
        self.Commands = [] if Commands is None else Commands

        self._Values = []
        self.Values = [] if Values is None else Values

        self._Discretes = []
        self.Discretes = [] if Discretes is None else Discretes

        super(ValueAliasSet, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Commands", "Values", "Discretes"]
    _many_refs = ["Commands", "Values", "Discretes"]

    def getCommands(self):
        """The ValueAliasSet used for translation of a Control value to a name.
        """
        return self._Commands

    def setCommands(self, value):
        for x in self._Commands:
            x._ValueAliasSet = None
        for y in value:
            y._ValueAliasSet = self
        self._Commands = value

    Commands = property(getCommands, setCommands)

    def addCommands(self, *Commands):
        for obj in Commands:
            obj._ValueAliasSet = self
            self._Commands.append(obj)

    def removeCommands(self, *Commands):
        for obj in Commands:
            obj._ValueAliasSet = None
            self._Commands.remove(obj)

    def getValues(self):
        """The ValueToAlias mappings included in the set
        """
        return self._Values

    def setValues(self, value):
        for x in self._Values:
            x._ValueAliasSet = None
        for y in value:
            y._ValueAliasSet = self
        self._Values = value

    Values = property(getValues, setValues)

    def addValues(self, *Values):
        for obj in Values:
            obj._ValueAliasSet = self
            self._Values.append(obj)

    def removeValues(self, *Values):
        for obj in Values:
            obj._ValueAliasSet = None
            self._Values.remove(obj)

    def getDiscretes(self):
        """The Measurements using the set for translation
        """
        return self._Discretes

    def setDiscretes(self, value):
        for x in self._Discretes:
            x._ValueAliasSet = None
        for y in value:
            y._ValueAliasSet = self
        self._Discretes = value

    Discretes = property(getDiscretes, setDiscretes)

    def addDiscretes(self, *Discretes):
        for obj in Discretes:
            obj._ValueAliasSet = self
            self._Discretes.append(obj)

    def removeDiscretes(self, *Discretes):
        for obj in Discretes:
            obj._ValueAliasSet = None
            self._Discretes.remove(obj)

