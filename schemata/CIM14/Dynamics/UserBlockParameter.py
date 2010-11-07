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

from CIM14.Dynamics.MetaBlockParameter import MetaBlockParameter

class UserBlockParameter(MetaBlockParameter):
    """Concrete class intended to obtain a parameter value from a user of the block  in the parameter list at the instance level.
    """

    def __init__(self, BlockUsageParameter=None, **kw_args):
        """Initializes a new 'UserBlockParameter' instance.

        @param BlockUsageParameter:
        """
        self._BlockUsageParameter = []
        self.BlockUsageParameter = [] if BlockUsageParameter is None else BlockUsageParameter

        super(UserBlockParameter, self).__init__(**kw_args)

    def getBlockUsageParameter(self):
        
        return self._BlockUsageParameter

    def setBlockUsageParameter(self, value):
        for x in self._BlockUsageParameter:
            x._UserBlockParameter = None
        for y in value:
            y._UserBlockParameter = self
        self._BlockUsageParameter = value

    BlockUsageParameter = property(getBlockUsageParameter, setBlockUsageParameter)

    def addBlockUsageParameter(self, *BlockUsageParameter):
        for obj in BlockUsageParameter:
            obj._UserBlockParameter = self
            self._BlockUsageParameter.append(obj)

    def removeBlockUsageParameter(self, *BlockUsageParameter):
        for obj in BlockUsageParameter:
            obj._UserBlockParameter = None
            self._BlockUsageParameter.remove(obj)

