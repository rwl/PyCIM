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

class ConnectionFrame(IdentifiedObject):

    def __init__(self, slotConnection0=None, slot0=None, *args, **kw_args):
        """Initialises a new 'ConnectionFrame' instance.

        @param slotConnection0:
        @param slot0:
        """
        self._slotConnection0 = []
        self.slotConnection0 = [] if slotConnection0 is None else slotConnection0

        self._slot0 = []
        self.slot0 = [] if slot0 is None else slot0

        super(ConnectionFrame, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["slotConnection0", "slot0"]
    _many_refs = ["slotConnection0", "slot0"]

    def getslotConnection0(self):
        
        return self._slotConnection0

    def setslotConnection0(self, value):
        for x in self._slotConnection0:
            x.connectionFrame0 = None
        for y in value:
            y._connectionFrame0 = self
        self._slotConnection0 = value

    slotConnection0 = property(getslotConnection0, setslotConnection0)

    def addslotConnection0(self, *slotConnection0):
        for obj in slotConnection0:
            obj.connectionFrame0 = self

    def removeslotConnection0(self, *slotConnection0):
        for obj in slotConnection0:
            obj.connectionFrame0 = None

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        for x in self._slot0:
            x.connectionFrame0 = None
        for y in value:
            y._connectionFrame0 = self
        self._slot0 = value

    slot0 = property(getslot0, setslot0)

    def addslot0(self, *slot0):
        for obj in slot0:
            obj.connectionFrame0 = self

    def removeslot0(self, *slot0):
        for obj in slot0:
            obj.connectionFrame0 = None

