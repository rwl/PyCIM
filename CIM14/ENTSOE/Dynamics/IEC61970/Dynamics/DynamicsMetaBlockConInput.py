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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreIdentifiedObject import CoreIdentifiedObject

class DynamicsMetaBlockConInput(CoreIdentifiedObject):

    def __init__(self, MetaBlockConSignal=None, MemberOf_MetaBlockConnection=None, *args, **kw_args):
        """Initialises a new 'DynamicsMetaBlockConInput' instance.

        @param MetaBlockConSignal: 
        @param MemberOf_MetaBlockConnection:
        """
        self._MetaBlockConSignal = None
        self.MetaBlockConSignal = MetaBlockConSignal

        self._MemberOf_MetaBlockConnection = None
        self.MemberOf_MetaBlockConnection = MemberOf_MetaBlockConnection

        super(DynamicsMetaBlockConInput, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MetaBlockConSignal", "MemberOf_MetaBlockConnection"]
    _many_refs = []

    def getMetaBlockConSignal(self):
        """
        """
        return self._MetaBlockConSignal

    def setMetaBlockConSignal(self, value):
        if self._MetaBlockConSignal is not None:
            self._MetaBlockConSignal._MetaBlockConInput = None

        self._MetaBlockConSignal = value
        if self._MetaBlockConSignal is not None:
            self._MetaBlockConSignal.MetaBlockConInput = None
            self._MetaBlockConSignal._MetaBlockConInput = self

    MetaBlockConSignal = property(getMetaBlockConSignal, setMetaBlockConSignal)

    def getMemberOf_MetaBlockConnection(self):
        
        return self._MemberOf_MetaBlockConnection

    def setMemberOf_MetaBlockConnection(self, value):
        if self._MemberOf_MetaBlockConnection is not None:
            filtered = [x for x in self.MemberOf_MetaBlockConnection.MetaBlockConInput if x != self]
            self._MemberOf_MetaBlockConnection._MetaBlockConInput = filtered

        self._MemberOf_MetaBlockConnection = value
        if self._MemberOf_MetaBlockConnection is not None:
            if self not in self._MemberOf_MetaBlockConnection._MetaBlockConInput:
                self._MemberOf_MetaBlockConnection._MetaBlockConInput.append(self)

    MemberOf_MetaBlockConnection = property(getMemberOf_MetaBlockConnection, setMemberOf_MetaBlockConnection)

