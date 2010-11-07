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

class MetaBlockParameter(MetaBlockConnectable):
    """An identified parameter of a block.   This is meta dynamics model and does not contain specific parameter values. When using a block one would need to supply specific parameter values. These are typically time constants, but are not restricted to this.  Sometimes, for standard blocks, the block paramter may come directly from the attributes of an associated PowerSystemResource object, but such parameters may be specified to enable user defined models to alter the behavior of a standard block.
    """

    def __init__(self, BlockParameter=None, MemberOf_MetaBlock=None, **kw_args):
        """Initializes a new 'MetaBlockParameter' instance.

        @param BlockParameter:
        @param MemberOf_MetaBlock: Paramters belong to a block.
        """
        self._BlockParameter = []
        self.BlockParameter = [] if BlockParameter is None else BlockParameter

        self._MemberOf_MetaBlock = None
        self.MemberOf_MetaBlock = MemberOf_MetaBlock

        super(MetaBlockParameter, self).__init__(**kw_args)

    def getBlockParameter(self):
        
        return self._BlockParameter

    def setBlockParameter(self, value):
        for x in self._BlockParameter:
            x._MetaBlockParameter = None
        for y in value:
            y._MetaBlockParameter = self
        self._BlockParameter = value

    BlockParameter = property(getBlockParameter, setBlockParameter)

    def addBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj._MetaBlockParameter = self
            self._BlockParameter.append(obj)

    def removeBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj._MetaBlockParameter = None
            self._BlockParameter.remove(obj)

    def getMemberOf_MetaBlock(self):
        """Paramters belong to a block.
        """
        return self._MemberOf_MetaBlock

    def setMemberOf_MetaBlock(self, value):
        if self._MemberOf_MetaBlock is not None:
            filtered = [x for x in self.MemberOf_MetaBlock.MetaBlockParameter if x != self]
            self._MemberOf_MetaBlock._MetaBlockParameter = filtered

        self._MemberOf_MetaBlock = value
        if self._MemberOf_MetaBlock is not None:
            self._MemberOf_MetaBlock._MetaBlockParameter.append(self)

    MemberOf_MetaBlock = property(getMemberOf_MetaBlock, setMemberOf_MetaBlock)

