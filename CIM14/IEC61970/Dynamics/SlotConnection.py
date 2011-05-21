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

class SlotConnection(IdentifiedObject):
    """Standard connectivity if not specified at the instance level..
    """

    def __init__(self, connectionFrame0=None, slotInput0=None, slotOutput0=None, *args, **kw_args):
        """Initialises a new 'SlotConnection' instance.

        @param connectionFrame0:
        @param slotInput0:
        @param slotOutput0:
        """
        self._connectionFrame0 = None
        self.connectionFrame0 = connectionFrame0

        self._slotInput0 = None
        self.slotInput0 = slotInput0

        self._slotOutput0 = None
        self.slotOutput0 = slotOutput0

        super(SlotConnection, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["connectionFrame0", "slotInput0", "slotOutput0"]
    _many_refs = []

    def getconnectionFrame0(self):
        
        return self._connectionFrame0

    def setconnectionFrame0(self, value):
        if self._connectionFrame0 is not None:
            filtered = [x for x in self.connectionFrame0.slotConnection0 if x != self]
            self._connectionFrame0._slotConnection0 = filtered

        self._connectionFrame0 = value
        if self._connectionFrame0 is not None:
            if self not in self._connectionFrame0._slotConnection0:
                self._connectionFrame0._slotConnection0.append(self)

    connectionFrame0 = property(getconnectionFrame0, setconnectionFrame0)

    def getslotInput0(self):
        
        return self._slotInput0

    def setslotInput0(self, value):
        if self._slotInput0 is not None:
            self._slotInput0._slotConnection0 = None

        self._slotInput0 = value
        if self._slotInput0 is not None:
            self._slotInput0.slotConnection0 = None
            self._slotInput0._slotConnection0 = self

    slotInput0 = property(getslotInput0, setslotInput0)

    def getslotOutput0(self):
        
        return self._slotOutput0

    def setslotOutput0(self, value):
        if self._slotOutput0 is not None:
            filtered = [x for x in self.slotOutput0.slotConnection0 if x != self]
            self._slotOutput0._slotConnection0 = filtered

        self._slotOutput0 = value
        if self._slotOutput0 is not None:
            if self not in self._slotOutput0._slotConnection0:
                self._slotOutput0._slotConnection0.append(self)

    slotOutput0 = property(getslotOutput0, setslotOutput0)

