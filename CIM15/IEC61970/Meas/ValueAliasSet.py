# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ValueAliasSet(IdentifiedObject):
    """Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.
    """

    def __init__(self, Discretes=None, Commands=None, Values=None, *args, **kw_args):
        """Initialises a new 'ValueAliasSet' instance.

        @param Discretes: The Measurements using the set for translation
        @param Commands: The ValueAliasSet used for translation of a Control value to a name.
        @param Values: The ValueToAlias mappings included in the set
        """
        self._Discretes = []
        self.Discretes = [] if Discretes is None else Discretes

        self._Commands = []
        self.Commands = [] if Commands is None else Commands

        self._Values = []
        self.Values = [] if Values is None else Values

        super(ValueAliasSet, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Discretes", "Commands", "Values"]
    _many_refs = ["Discretes", "Commands", "Values"]

    def getDiscretes(self):
        """The Measurements using the set for translation
        """
        return self._Discretes

    def setDiscretes(self, value):
        for x in self._Discretes:
            x.ValueAliasSet = None
        for y in value:
            y._ValueAliasSet = self
        self._Discretes = value

    Discretes = property(getDiscretes, setDiscretes)

    def addDiscretes(self, *Discretes):
        for obj in Discretes:
            obj.ValueAliasSet = self

    def removeDiscretes(self, *Discretes):
        for obj in Discretes:
            obj.ValueAliasSet = None

    def getCommands(self):
        """The ValueAliasSet used for translation of a Control value to a name.
        """
        return self._Commands

    def setCommands(self, value):
        for x in self._Commands:
            x.ValueAliasSet = None
        for y in value:
            y._ValueAliasSet = self
        self._Commands = value

    Commands = property(getCommands, setCommands)

    def addCommands(self, *Commands):
        for obj in Commands:
            obj.ValueAliasSet = self

    def removeCommands(self, *Commands):
        for obj in Commands:
            obj.ValueAliasSet = None

    def getValues(self):
        """The ValueToAlias mappings included in the set
        """
        return self._Values

    def setValues(self, value):
        for x in self._Values:
            x.ValueAliasSet = None
        for y in value:
            y._ValueAliasSet = self
        self._Values = value

    Values = property(getValues, setValues)

    def addValues(self, *Values):
        for obj in Values:
            obj.ValueAliasSet = self

    def removeValues(self, *Values):
        for obj in Values:
            obj.ValueAliasSet = None

