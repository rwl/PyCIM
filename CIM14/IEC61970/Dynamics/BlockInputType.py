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

class BlockInputType(IdentifiedObject):

    def __init__(self, slotInput0=None, metaBlockInput0=None, *args, **kw_args):
        """Initialises a new 'BlockInputType' instance.

        @param slotInput0:
        @param metaBlockInput0:
        """
        self._slotInput0 = []
        self.slotInput0 = [] if slotInput0 is None else slotInput0

        self._metaBlockInput0 = []
        self.metaBlockInput0 = [] if metaBlockInput0 is None else metaBlockInput0

        super(BlockInputType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["slotInput0", "metaBlockInput0"]
    _many_refs = ["slotInput0", "metaBlockInput0"]

    def getslotInput0(self):
        
        return self._slotInput0

    def setslotInput0(self, value):
        for x in self._slotInput0:
            x.blockInputType0 = None
        for y in value:
            y._blockInputType0 = self
        self._slotInput0 = value

    slotInput0 = property(getslotInput0, setslotInput0)

    def addslotInput0(self, *slotInput0):
        for obj in slotInput0:
            obj.blockInputType0 = self

    def removeslotInput0(self, *slotInput0):
        for obj in slotInput0:
            obj.blockInputType0 = None

    def getmetaBlockInput0(self):
        
        return self._metaBlockInput0

    def setmetaBlockInput0(self, value):
        for x in self._metaBlockInput0:
            x.blockInputType0 = None
        for y in value:
            y._blockInputType0 = self
        self._metaBlockInput0 = value

    metaBlockInput0 = property(getmetaBlockInput0, setmetaBlockInput0)

    def addmetaBlockInput0(self, *metaBlockInput0):
        for obj in metaBlockInput0:
            obj.blockInputType0 = self

    def removemetaBlockInput0(self, *metaBlockInput0):
        for obj in metaBlockInput0:
            obj.blockInputType0 = None

