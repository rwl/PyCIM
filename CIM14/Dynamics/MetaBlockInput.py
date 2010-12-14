# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.Dynamics.MetaBlockConnectable import MetaBlockConnectable

class MetaBlockInput(MetaBlockConnectable):
    """Linkage at the dynanics meta model level.    The output of a block could link to this. This is a public interface external to the block.
    """

    def __init__(self, blockInputReference0=None, MemberOf_MetaBlock=None, blockUsageInputReference0=None, blockInputType0=None, tieToMeasurement0=None, *args, **kw_args):
        """Initialises a new 'MetaBlockInput' instance.

        @param blockInputReference0: References the idenfiied input for the block reference.
        @param MemberOf_MetaBlock: Inputs belong to a block.
        @param blockUsageInputReference0:
        @param blockInputType0:
        @param tieToMeasurement0: The identified block input to which this measurement applies.   Note this applies only to the external interface of blocks.
        """
        self._blockInputReference0 = []
        self.blockInputReference0 = [] if blockInputReference0 is None else blockInputReference0

        self._MemberOf_MetaBlock = None
        self.MemberOf_MetaBlock = MemberOf_MetaBlock

        self._blockUsageInputReference0 = []
        self.blockUsageInputReference0 = [] if blockUsageInputReference0 is None else blockUsageInputReference0

        self._blockInputType0 = None
        self.blockInputType0 = blockInputType0

        self._tieToMeasurement0 = []
        self.tieToMeasurement0 = [] if tieToMeasurement0 is None else tieToMeasurement0

        super(MetaBlockInput, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["blockInputReference0", "MemberOf_MetaBlock", "blockUsageInputReference0", "blockInputType0", "tieToMeasurement0"]
    _many_refs = ["blockInputReference0", "blockUsageInputReference0", "tieToMeasurement0"]

    def getblockInputReference0(self):
        """References the idenfiied input for the block reference.
        """
        return self._blockInputReference0

    def setblockInputReference0(self, value):
        for x in self._blockInputReference0:
            x.metaBlockInput0 = None
        for y in value:
            y._metaBlockInput0 = self
        self._blockInputReference0 = value

    blockInputReference0 = property(getblockInputReference0, setblockInputReference0)

    def addblockInputReference0(self, *blockInputReference0):
        for obj in blockInputReference0:
            obj.metaBlockInput0 = self

    def removeblockInputReference0(self, *blockInputReference0):
        for obj in blockInputReference0:
            obj.metaBlockInput0 = None

    def getMemberOf_MetaBlock(self):
        """Inputs belong to a block.
        """
        return self._MemberOf_MetaBlock

    def setMemberOf_MetaBlock(self, value):
        if self._MemberOf_MetaBlock is not None:
            filtered = [x for x in self.MemberOf_MetaBlock.MetaBlockInput if x != self]
            self._MemberOf_MetaBlock._MetaBlockInput = filtered

        self._MemberOf_MetaBlock = value
        if self._MemberOf_MetaBlock is not None:
            if self not in self._MemberOf_MetaBlock._MetaBlockInput:
                self._MemberOf_MetaBlock._MetaBlockInput.append(self)

    MemberOf_MetaBlock = property(getMemberOf_MetaBlock, setMemberOf_MetaBlock)

    def getblockUsageInputReference0(self):
        
        return self._blockUsageInputReference0

    def setblockUsageInputReference0(self, value):
        for x in self._blockUsageInputReference0:
            x.metaBlockInput0 = None
        for y in value:
            y._metaBlockInput0 = self
        self._blockUsageInputReference0 = value

    blockUsageInputReference0 = property(getblockUsageInputReference0, setblockUsageInputReference0)

    def addblockUsageInputReference0(self, *blockUsageInputReference0):
        for obj in blockUsageInputReference0:
            obj.metaBlockInput0 = self

    def removeblockUsageInputReference0(self, *blockUsageInputReference0):
        for obj in blockUsageInputReference0:
            obj.metaBlockInput0 = None

    def getblockInputType0(self):
        
        return self._blockInputType0

    def setblockInputType0(self, value):
        if self._blockInputType0 is not None:
            filtered = [x for x in self.blockInputType0.metaBlockInput0 if x != self]
            self._blockInputType0._metaBlockInput0 = filtered

        self._blockInputType0 = value
        if self._blockInputType0 is not None:
            if self not in self._blockInputType0._metaBlockInput0:
                self._blockInputType0._metaBlockInput0.append(self)

    blockInputType0 = property(getblockInputType0, setblockInputType0)

    def gettieToMeasurement0(self):
        """The identified block input to which this measurement applies.   Note this applies only to the external interface of blocks.
        """
        return self._tieToMeasurement0

    def settieToMeasurement0(self, value):
        for x in self._tieToMeasurement0:
            x.metaBlockInput0 = None
        for y in value:
            y._metaBlockInput0 = self
        self._tieToMeasurement0 = value

    tieToMeasurement0 = property(gettieToMeasurement0, settieToMeasurement0)

    def addtieToMeasurement0(self, *tieToMeasurement0):
        for obj in tieToMeasurement0:
            obj.metaBlockInput0 = self

    def removetieToMeasurement0(self, *tieToMeasurement0):
        for obj in tieToMeasurement0:
            obj.metaBlockInput0 = None

