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

class SlotReference(IdentifiedObject):
    """The specific role the block usage is playing in a connection frame. This allows connections to be established at the meta dynamics level and not at the instance level.
    """

    def __init__(self, slot0=None, block0=None, compositeModel0=None, *args, **kw_args):
        """Initialises a new 'SlotReference' instance.

        @param slot0:
        @param block0:
        @param compositeModel0:
        """
        self._slot0 = None
        self.slot0 = slot0

        self._block0 = []
        self.block0 = [] if block0 is None else block0

        self._compositeModel0 = []
        self.compositeModel0 = [] if compositeModel0 is None else compositeModel0

        super(SlotReference, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["slot0", "block0", "compositeModel0"]
    _many_refs = ["block0", "compositeModel0"]

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        if self._slot0 is not None:
            filtered = [x for x in self.slot0.slotReference0 if x != self]
            self._slot0._slotReference0 = filtered

        self._slot0 = value
        if self._slot0 is not None:
            if self not in self._slot0._slotReference0:
                self._slot0._slotReference0.append(self)

    slot0 = property(getslot0, setslot0)

    def getblock0(self):
        
        return self._block0

    def setblock0(self, value):
        for x in self._block0:
            x.slotReference0 = None
        for y in value:
            y._slotReference0 = self
        self._block0 = value

    block0 = property(getblock0, setblock0)

    def addblock0(self, *block0):
        for obj in block0:
            obj.slotReference0 = self

    def removeblock0(self, *block0):
        for obj in block0:
            obj.slotReference0 = None

    def getcompositeModel0(self):
        
        return self._compositeModel0

    def setcompositeModel0(self, value):
        for p in self._compositeModel0:
            filtered = [q for q in p.slotReference0 if q != self]
            self._compositeModel0._slotReference0 = filtered
        for r in value:
            if self not in r._slotReference0:
                r._slotReference0.append(self)
        self._compositeModel0 = value

    compositeModel0 = property(getcompositeModel0, setcompositeModel0)

    def addcompositeModel0(self, *compositeModel0):
        for obj in compositeModel0:
            if self not in obj._slotReference0:
                obj._slotReference0.append(self)
            self._compositeModel0.append(obj)

    def removecompositeModel0(self, *compositeModel0):
        for obj in compositeModel0:
            if self in obj._slotReference0:
                obj._slotReference0.remove(self)
            self._compositeModel0.remove(obj)

