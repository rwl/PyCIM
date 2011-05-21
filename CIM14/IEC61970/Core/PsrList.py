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

class PsrList(IdentifiedObject):
    """Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.
    """

    def __init__(self, typePSRList='', PowerSystemResources=None, *args, **kw_args):
        """Initialises a new 'PsrList' instance.

        @param typePSRList: Type of power system resources in this list. 
        @param PowerSystemResources:
        """
        #: Type of power system resources in this list.
        self.typePSRList = typePSRList

        self._PowerSystemResources = []
        self.PowerSystemResources = [] if PowerSystemResources is None else PowerSystemResources

        super(PsrList, self).__init__(*args, **kw_args)

    _attrs = ["typePSRList"]
    _attr_types = {"typePSRList": str}
    _defaults = {"typePSRList": ''}
    _enums = {}
    _refs = ["PowerSystemResources"]
    _many_refs = ["PowerSystemResources"]

    def getPowerSystemResources(self):
        
        return self._PowerSystemResources

    def setPowerSystemResources(self, value):
        for p in self._PowerSystemResources:
            filtered = [q for q in p.PsrLists if q != self]
            self._PowerSystemResources._PsrLists = filtered
        for r in value:
            if self not in r._PsrLists:
                r._PsrLists.append(self)
        self._PowerSystemResources = value

    PowerSystemResources = property(getPowerSystemResources, setPowerSystemResources)

    def addPowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self not in obj._PsrLists:
                obj._PsrLists.append(self)
            self._PowerSystemResources.append(obj)

    def removePowerSystemResources(self, *PowerSystemResources):
        for obj in PowerSystemResources:
            if self in obj._PsrLists:
                obj._PsrLists.remove(self)
            self._PowerSystemResources.remove(obj)

