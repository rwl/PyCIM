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

class MetaBlockConSignal(IdentifiedObject):

    def __init__(self, MetaBlockConInput=None, MemberOf_MetaBlockConnectivity=None, MetaBlockConOutput=None, metaBlockConnectivity0=None, *args, **kw_args):
        """Initialises a new 'MetaBlockConSignal' instance.

        @param MetaBlockConInput:
        @param MemberOf_MetaBlockConnectivity:
        @param MetaBlockConOutput:
        @param metaBlockConnectivity0:
        """
        self._MetaBlockConInput = None
        self.MetaBlockConInput = MetaBlockConInput

        self._MemberOf_MetaBlockConnectivity = None
        self.MemberOf_MetaBlockConnectivity = MemberOf_MetaBlockConnectivity

        self._MetaBlockConOutput = None
        self.MetaBlockConOutput = MetaBlockConOutput

        self._metaBlockConnectivity0 = None
        self.metaBlockConnectivity0 = metaBlockConnectivity0

        super(MetaBlockConSignal, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MetaBlockConInput", "MemberOf_MetaBlockConnectivity", "MetaBlockConOutput", "metaBlockConnectivity0"]
    _many_refs = []

    def getMetaBlockConInput(self):
        
        return self._MetaBlockConInput

    def setMetaBlockConInput(self, value):
        if self._MetaBlockConInput is not None:
            self._MetaBlockConInput._MetaBlockConSignal = None

        self._MetaBlockConInput = value
        if self._MetaBlockConInput is not None:
            self._MetaBlockConInput.MetaBlockConSignal = None
            self._MetaBlockConInput._MetaBlockConSignal = self

    MetaBlockConInput = property(getMetaBlockConInput, setMetaBlockConInput)

    def getMemberOf_MetaBlockConnectivity(self):
        
        return self._MemberOf_MetaBlockConnectivity

    def setMemberOf_MetaBlockConnectivity(self, value):
        if self._MemberOf_MetaBlockConnectivity is not None:
            filtered = [x for x in self.MemberOf_MetaBlockConnectivity.MetaBlockConSignal if x != self]
            self._MemberOf_MetaBlockConnectivity._MetaBlockConSignal = filtered

        self._MemberOf_MetaBlockConnectivity = value
        if self._MemberOf_MetaBlockConnectivity is not None:
            if self not in self._MemberOf_MetaBlockConnectivity._MetaBlockConSignal:
                self._MemberOf_MetaBlockConnectivity._MetaBlockConSignal.append(self)

    MemberOf_MetaBlockConnectivity = property(getMemberOf_MetaBlockConnectivity, setMemberOf_MetaBlockConnectivity)

    def getMetaBlockConOutput(self):
        
        return self._MetaBlockConOutput

    def setMetaBlockConOutput(self, value):
        if self._MetaBlockConOutput is not None:
            filtered = [x for x in self.MetaBlockConOutput.MetaBlockConSignal if x != self]
            self._MetaBlockConOutput._MetaBlockConSignal = filtered

        self._MetaBlockConOutput = value
        if self._MetaBlockConOutput is not None:
            if self not in self._MetaBlockConOutput._MetaBlockConSignal:
                self._MetaBlockConOutput._MetaBlockConSignal.append(self)

    MetaBlockConOutput = property(getMetaBlockConOutput, setMetaBlockConOutput)

    def getmetaBlockConnectivity0(self):
        
        return self._metaBlockConnectivity0

    def setmetaBlockConnectivity0(self, value):
        if self._metaBlockConnectivity0 is not None:
            filtered = [x for x in self.metaBlockConnectivity0.metaBlockConSignal0 if x != self]
            self._metaBlockConnectivity0._metaBlockConSignal0 = filtered

        self._metaBlockConnectivity0 = value
        if self._metaBlockConnectivity0 is not None:
            if self not in self._metaBlockConnectivity0._metaBlockConSignal0:
                self._metaBlockConnectivity0._metaBlockConSignal0.append(self)

    metaBlockConnectivity0 = property(getmetaBlockConnectivity0, setmetaBlockConnectivity0)

