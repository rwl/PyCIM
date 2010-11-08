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
            self._Terminal._BranchGroupTerminal.append(self)

    Terminal = property(getTerminal, setTerminal)

