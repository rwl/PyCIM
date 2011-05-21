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

from CIM14.IEC61970.Dynamics.MetaBlockConnectable import MetaBlockConnectable

class BlockOutputReference(MetaBlockConnectable):
    """References output from another block at the meta dynamics level. The other block must be a BlockReference in containing block.
    """

    def __init__(self, metaBlockOutput0=None, metaBlockReference0=None, *args, **kw_args):
        """Initialises a new 'BlockOutputReference' instance.

        @param metaBlockOutput0:
        @param metaBlockReference0:
        """
        self._metaBlockOutput0 = None
        self.metaBlockOutput0 = metaBlockOutput0

        self._metaBlockReference0 = []
        self.metaBlockReference0 = [] if metaBlockReference0 is None else metaBlockReference0

        super(BlockOutputReference, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["metaBlockOutput0", "metaBlockReference0"]
    _many_refs = ["metaBlockReference0"]

    def getmetaBlockOutput0(self):
        
        return self._metaBlockOutput0

    def setmetaBlockOutput0(self, value):
        if self._metaBlockOutput0 is not None:
            filtered = [x for x in self.metaBlockOutput0.BlockOutputReference if x != self]
            self._metaBlockOutput0._BlockOutputReference = filtered

        self._metaBlockOutput0 = value
        if self._metaBlockOutput0 is not None:
            if self not in self._metaBlockOutput0._BlockOutputReference:
                self._metaBlockOutput0._BlockOutputReference.append(self)

    metaBlockOutput0 = property(getmetaBlockOutput0, setmetaBlockOutput0)

    def getmetaBlockReference0(self):
        
        return self._metaBlockReference0

    def setmetaBlockReference0(self, value):
        for p in self._metaBlockReference0:
            filtered = [q for q in p.blockOutputReference0 if q != self]
            self._metaBlockReference0._blockOutputReference0 = filtered
        for r in value:
            if self not in r._blockOutputReference0:
                r._blockOutputReference0.append(self)
        self._metaBlockReference0 = value

    metaBlockReference0 = property(getmetaBlockReference0, setmetaBlockReference0)

    def addmetaBlockReference0(self, *metaBlockReference0):
        for obj in metaBlockReference0:
            if self not in obj._blockOutputReference0:
                obj._blockOutputReference0.append(self)
            self._metaBlockReference0.append(obj)

    def removemetaBlockReference0(self, *metaBlockReference0):
        for obj in metaBlockReference0:
            if self in obj._blockOutputReference0:
                obj._blockOutputReference0.remove(self)
            self._metaBlockReference0.remove(obj)

