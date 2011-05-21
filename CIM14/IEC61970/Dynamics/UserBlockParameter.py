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

from CIM14.IEC61970.Dynamics.MetaBlockParameter import MetaBlockParameter

class UserBlockParameter(MetaBlockParameter):
    """Concrete class intended to obtain a parameter value from a user of the block  in the parameter list at the instance level.
    """

    def __init__(self, BlockUsageParameter=None, *args, **kw_args):
        """Initialises a new 'UserBlockParameter' instance.

        @param BlockUsageParameter:
        """
        self._BlockUsageParameter = []
        self.BlockUsageParameter = [] if BlockUsageParameter is None else BlockUsageParameter

        super(UserBlockParameter, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["BlockUsageParameter"]
    _many_refs = ["BlockUsageParameter"]

    def getBlockUsageParameter(self):
        
        return self._BlockUsageParameter

    def setBlockUsageParameter(self, value):
        for x in self._BlockUsageParameter:
            x.UserBlockParameter = None
        for y in value:
            y._UserBlockParameter = self
        self._BlockUsageParameter = value

    BlockUsageParameter = property(getBlockUsageParameter, setBlockUsageParameter)

    def addBlockUsageParameter(self, *BlockUsageParameter):
        for obj in BlockUsageParameter:
            obj.UserBlockParameter = self

    def removeBlockUsageParameter(self, *BlockUsageParameter):
        for obj in BlockUsageParameter:
            obj.UserBlockParameter = None

