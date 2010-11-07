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

class BlockConstant(MetaBlockConnectable):
    """Used as a constant in the internal definition of a block.   This is meta dynamics model, so you need not specify this paramter in each usage of the block as a normal instance parameter.
    """

    def __init__(self, value=0.0, metaBlock0=None, **kw_args):
        """Initializes a new 'BlockConstant' instance.

        @param value: The constant value of used for the internal defintion of a block. 
        @param metaBlock0:
        """
        #: The constant value of used for the internal defintion of a block.
        self.value = value

        self._metaBlock0 = None
        self.metaBlock0 = metaBlock0

        super(BlockConstant, self).__init__(**kw_args)

    def getmetaBlock0(self):
        
        return self._metaBlock0

    def setmetaBlock0(self, value):
        if self._metaBlock0 is not None:
            filtered = [x for x in self.metaBlock0.blockConstant0 if x != self]
            self._metaBlock0._blockConstant0 = filtered

        self._metaBlock0 = value
        if self._metaBlock0 is not None:
            self._metaBlock0._blockConstant0.append(self)

    metaBlock0 = property(getmetaBlock0, setmetaBlock0)

