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

from CIM15.IEC61970.OperationalLimits.OperationalLimitSet import OperationalLimitSet

class CurrentLimitSet(OperationalLimitSet):

    def __init__(self, CurrentLimits=None, *args, **kw_args):
        """Initialises a new 'CurrentLimitSet' instance.

        @param CurrentLimits:
        """
        self._CurrentLimits = []
        self.CurrentLimits = [] if CurrentLimits is None else CurrentLimits

        super(CurrentLimitSet, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["CurrentLimits"]
    _many_refs = ["CurrentLimits"]

    def getCurrentLimits(self):
        
        return self._CurrentLimits

    def setCurrentLimits(self, value):
        for x in self._CurrentLimits:
            x.CurrentLimitSet = None
        for y in value:
            y._CurrentLimitSet = self
        self._CurrentLimits = value

    CurrentLimits = property(getCurrentLimits, setCurrentLimits)

    def addCurrentLimits(self, *CurrentLimits):
        for obj in CurrentLimits:
            obj.CurrentLimitSet = self

    def removeCurrentLimits(self, *CurrentLimits):
        for obj in CurrentLimits:
            obj.CurrentLimitSet = None

