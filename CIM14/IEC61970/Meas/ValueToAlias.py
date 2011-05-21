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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ValueToAlias(IdentifiedObject):
    """Describes the translation of one particular value into a name, e.g. 1->'Open'
    """

    def __init__(self, value=0, ValueAliasSet=None, *args, **kw_args):
        """Initialises a new 'ValueToAlias' instance.

        @param value: The value that is mapped 
        @param ValueAliasSet: The ValueAliasSet having the ValueToAlias mappings
        """
        #: The value that is mapped
        self.value = value

        self._ValueAliasSet = None
        self.ValueAliasSet = ValueAliasSet

        super(ValueToAlias, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": int}
    _defaults = {"value": 0}
    _enums = {}
    _refs = ["ValueAliasSet"]
    _many_refs = []

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
            if self not in self._ValueAliasSet._Values:
                self._ValueAliasSet._Values.append(self)

    ValueAliasSet = property(getValueAliasSet, setValueAliasSet)

