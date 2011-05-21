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

from CIM14.Element import Element

class CompositeModel(Element):

    def __init__(self, slotReference0=None, *args, **kw_args):
        """Initialises a new 'CompositeModel' instance.

        @param slotReference0:
        """
        self._slotReference0 = []
        self.slotReference0 = [] if slotReference0 is None else slotReference0

        super(CompositeModel, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["slotReference0"]
    _many_refs = ["slotReference0"]

    def getslotReference0(self):
        
        return self._slotReference0

    def setslotReference0(self, value):
        for p in self._slotReference0:
            filtered = [q for q in p.compositeModel0 if q != self]
            self._slotReference0._compositeModel0 = filtered
        for r in value:
            if self not in r._compositeModel0:
                r._compositeModel0.append(self)
        self._slotReference0 = value

    slotReference0 = property(getslotReference0, setslotReference0)

    def addslotReference0(self, *slotReference0):
        for obj in slotReference0:
            if self not in obj._compositeModel0:
                obj._compositeModel0.append(self)
            self._slotReference0.append(obj)

    def removeslotReference0(self, *slotReference0):
        for obj in slotReference0:
            if self in obj._compositeModel0:
                obj._compositeModel0.remove(self)
            self._slotReference0.remove(obj)

