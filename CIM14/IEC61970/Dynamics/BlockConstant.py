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

from CIM14.IEC61970.Dynamics.MetaBlockConnectable import MetaBlockConnectable

class BlockConstant(MetaBlockConnectable):
    """Used as a constant in the internal definition of a block.   This is meta dynamics model, so you need not specify this paramter in each usage of the block as a normal instance parameter.
    """

    def __init__(self, value=0.0, metaBlock0=None, *args, **kw_args):
        """Initialises a new 'BlockConstant' instance.

        @param value: The constant value of used for the internal defintion of a block. 
        @param metaBlock0:
        """
        #: The constant value of used for the internal defintion of a block.
        self.value = value

        self._metaBlock0 = None
        self.metaBlock0 = metaBlock0

        super(BlockConstant, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = ["metaBlock0"]
    _many_refs = []

    def getmetaBlock0(self):
        
        return self._metaBlock0

    def setmetaBlock0(self, value):
        if self._metaBlock0 is not None:
            filtered = [x for x in self.metaBlock0.blockConstant0 if x != self]
            self._metaBlock0._blockConstant0 = filtered

        self._metaBlock0 = value
        if self._metaBlock0 is not None:
            if self not in self._metaBlock0._blockConstant0:
                self._metaBlock0._blockConstant0.append(self)

    metaBlock0 = property(getmetaBlock0, setmetaBlock0)

