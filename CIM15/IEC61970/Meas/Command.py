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

from CIM15.IEC61970.Meas.Control import Control

class Command(Control):
    """A Command is a discrete control used for supervisory control.A Command is a discrete control used for supervisory control.
    """

    def __init__(self, value=0, normalValue=0, Discrete=None, ValueAliasSet=None, *args, **kw_args):
        """Initialises a new 'Command' instance.

        @param value: The value representing the actuator output 
        @param normalValue: Normal value for Control.value e.g. used for percentage scaling 
        @param Discrete: The Measurement variable used for control.
        @param ValueAliasSet: The Commands using the set for translation.
        """
        #: The value representing the actuator output
        self.value = value

        #: Normal value for Control.value e.g. used for percentage scaling
        self.normalValue = normalValue

        self._Discrete = None
        self.Discrete = Discrete

        self._ValueAliasSet = None
        self.ValueAliasSet = ValueAliasSet

        super(Command, self).__init__(*args, **kw_args)

    _attrs = ["value", "normalValue"]
    _attr_types = {"value": int, "normalValue": int}
    _defaults = {"value": 0, "normalValue": 0}
    _enums = {}
    _refs = ["Discrete", "ValueAliasSet"]
    _many_refs = []

    def getDiscrete(self):
        """The Measurement variable used for control.
        """
        return self._Discrete

    def setDiscrete(self, value):
        if self._Discrete is not None:
            self._Discrete._Command = None

        self._Discrete = value
        if self._Discrete is not None:
            self._Discrete.Command = None
            self._Discrete._Command = self

    Discrete = property(getDiscrete, setDiscrete)

    def getValueAliasSet(self):
        """The Commands using the set for translation.
        """
        return self._ValueAliasSet

    def setValueAliasSet(self, value):
        if self._ValueAliasSet is not None:
            filtered = [x for x in self.ValueAliasSet.Commands if x != self]
            self._ValueAliasSet._Commands = filtered

        self._ValueAliasSet = value
        if self._ValueAliasSet is not None:
            if self not in self._ValueAliasSet._Commands:
                self._ValueAliasSet._Commands.append(self)

    ValueAliasSet = property(getValueAliasSet, setValueAliasSet)

