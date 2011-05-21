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

class MetaBlockConOutput(IdentifiedObject):
    """If model uses MeasurementType association, it means the output is pushed back to the steady state model (if reasonable).
    """

    def __init__(self, MetaBlockConSignal=None, MemberOf_MetaBlockConnection=None, Unit=None, *args, **kw_args):
        """Initialises a new 'MetaBlockConOutput' instance.

        @param MetaBlockConSignal:
        @param MemberOf_MetaBlockConnection:
        @param Unit:
        """
        self._MetaBlockConSignal = []
        self.MetaBlockConSignal = [] if MetaBlockConSignal is None else MetaBlockConSignal

        self._MemberOf_MetaBlockConnection = None
        self.MemberOf_MetaBlockConnection = MemberOf_MetaBlockConnection

        self._Unit = None
        self.Unit = Unit

        super(MetaBlockConOutput, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MetaBlockConSignal", "MemberOf_MetaBlockConnection", "Unit"]
    _many_refs = ["MetaBlockConSignal"]

    def getMetaBlockConSignal(self):
        
        return self._MetaBlockConSignal

    def setMetaBlockConSignal(self, value):
        for x in self._MetaBlockConSignal:
            x.MetaBlockConOutput = None
        for y in value:
            y._MetaBlockConOutput = self
        self._MetaBlockConSignal = value

    MetaBlockConSignal = property(getMetaBlockConSignal, setMetaBlockConSignal)

    def addMetaBlockConSignal(self, *MetaBlockConSignal):
        for obj in MetaBlockConSignal:
            obj.MetaBlockConOutput = self

    def removeMetaBlockConSignal(self, *MetaBlockConSignal):
        for obj in MetaBlockConSignal:
            obj.MetaBlockConOutput = None

    def getMemberOf_MetaBlockConnection(self):
        
        return self._MemberOf_MetaBlockConnection

    def setMemberOf_MetaBlockConnection(self, value):
        if self._MemberOf_MetaBlockConnection is not None:
            filtered = [x for x in self.MemberOf_MetaBlockConnection.MetaBlockConOutput if x != self]
            self._MemberOf_MetaBlockConnection._MetaBlockConOutput = filtered

        self._MemberOf_MetaBlockConnection = value
        if self._MemberOf_MetaBlockConnection is not None:
            if self not in self._MemberOf_MetaBlockConnection._MetaBlockConOutput:
                self._MemberOf_MetaBlockConnection._MetaBlockConOutput.append(self)

    MemberOf_MetaBlockConnection = property(getMemberOf_MetaBlockConnection, setMemberOf_MetaBlockConnection)

    def getUnit(self):
        
        return self._Unit

    def setUnit(self, value):
        if self._Unit is not None:
            filtered = [x for x in self.Unit.MetaBlockConOutput if x != self]
            self._Unit._MetaBlockConOutput = filtered

        self._Unit = value
        if self._Unit is not None:
            if self not in self._Unit._MetaBlockConOutput:
                self._Unit._MetaBlockConOutput.append(self)

    Unit = property(getUnit, setUnit)

