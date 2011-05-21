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

from CIM14.Element import Element

class BranchGroupTerminal(Element):
    """A specific directed terminal flow for a branch group.
    """

    def __init__(self, positiveFlowIn=False, BranchGroup=None, Terminal=None, *args, **kw_args):
        """Initialises a new 'BranchGroupTerminal' instance.

        @param positiveFlowIn: The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false. 
        @param BranchGroup: The branch group to which the directed branch group terminals belong.
        @param Terminal: The terminal to be summed.
        """
        #: The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.
        self.positiveFlowIn = positiveFlowIn

        self._BranchGroup = None
        self.BranchGroup = BranchGroup

        self._Terminal = None
        self.Terminal = Terminal

        super(BranchGroupTerminal, self).__init__(*args, **kw_args)

    _attrs = ["positiveFlowIn"]
    _attr_types = {"positiveFlowIn": bool}
    _defaults = {"positiveFlowIn": False}
    _enums = {}
    _refs = ["BranchGroup", "Terminal"]
    _many_refs = []

    def getBranchGroup(self):
        """The branch group to which the directed branch group terminals belong.
        """
        return self._BranchGroup

    def setBranchGroup(self, value):
        if self._BranchGroup is not None:
            filtered = [x for x in self.BranchGroup.BranchGroupTerminal if x != self]
            self._BranchGroup._BranchGroupTerminal = filtered

        self._BranchGroup = value
        if self._BranchGroup is not None:
            if self not in self._BranchGroup._BranchGroupTerminal:
                self._BranchGroup._BranchGroupTerminal.append(self)

    BranchGroup = property(getBranchGroup, setBranchGroup)

    def getTerminal(self):
        """The terminal to be summed.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.BranchGroupTerminal if x != self]
            self._Terminal._BranchGroupTerminal = filtered

        self._Terminal = value
        if self._Terminal is not None:
            if self not in self._Terminal._BranchGroupTerminal:
                self._Terminal._BranchGroupTerminal.append(self)

    Terminal = property(getTerminal, setTerminal)

