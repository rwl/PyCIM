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

from CIM15.CDPSM.Connectivity.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerEnd(IdentifiedObject):
    """TransformerEnd is a conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose. This successor TransformerEnd class is more flexible and has important differences with TransformerWinding.
    """

    def __init__(self, Terminal=None, *args, **kw_args):
        """Initialises a new 'TransformerEnd' instance.

        @param Terminal: External terminal of the power transformer to which this end belongs.
        """
        self._Terminal = None
        self.Terminal = Terminal

        super(TransformerEnd, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Terminal"]
    _many_refs = []

    def getTerminal(self):
        """External terminal of the power transformer to which this end belongs.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.TransformerEnd if x != self]
            self._Terminal._TransformerEnd = filtered

        self._Terminal = value
        if self._Terminal is not None:
            if self not in self._Terminal._TransformerEnd:
                self._Terminal._TransformerEnd.append(self)

    Terminal = property(getTerminal, setTerminal)

