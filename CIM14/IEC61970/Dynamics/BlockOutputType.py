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

class BlockOutputType(IdentifiedObject):

    def __init__(self, metaBlockOutput0=None, slotOutput0=None, *args, **kw_args):
        """Initialises a new 'BlockOutputType' instance.

        @param metaBlockOutput0:
        @param slotOutput0:
        """
        self._metaBlockOutput0 = []
        self.metaBlockOutput0 = [] if metaBlockOutput0 is None else metaBlockOutput0

        self._slotOutput0 = []
        self.slotOutput0 = [] if slotOutput0 is None else slotOutput0

        super(BlockOutputType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["metaBlockOutput0", "slotOutput0"]
    _many_refs = ["metaBlockOutput0", "slotOutput0"]

    def getmetaBlockOutput0(self):
        
        return self._metaBlockOutput0

    def setmetaBlockOutput0(self, value):
        for x in self._metaBlockOutput0:
            x.blockOutputType0 = None
        for y in value:
            y._blockOutputType0 = self
        self._metaBlockOutput0 = value

    metaBlockOutput0 = property(getmetaBlockOutput0, setmetaBlockOutput0)

    def addmetaBlockOutput0(self, *metaBlockOutput0):
        for obj in metaBlockOutput0:
            obj.blockOutputType0 = self

    def removemetaBlockOutput0(self, *metaBlockOutput0):
        for obj in metaBlockOutput0:
            obj.blockOutputType0 = None

    def getslotOutput0(self):
        
        return self._slotOutput0

    def setslotOutput0(self, value):
        for x in self._slotOutput0:
            x.blockOutputType0 = None
        for y in value:
            y._blockOutputType0 = self
        self._slotOutput0 = value

    slotOutput0 = property(getslotOutput0, setslotOutput0)

    def addslotOutput0(self, *slotOutput0):
        for obj in slotOutput0:
            obj.blockOutputType0 = self

    def removeslotOutput0(self, *slotOutput0):
        for obj in slotOutput0:
            obj.blockOutputType0 = None

