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

from CIM14v13.IEC61968.Informative.MarketOperations.ConstraintTerm import ConstraintTerm

class TerminalConstraintTerm(ConstraintTerm):
    """A constraint term associated with a specific terminal on a physical piece of equipment.
    """

    def __init__(self, Terminal=None, **kw_args):
        """Initializes a new 'TerminalConstraintTerm' instance.

        @param Terminal:
        """
        self._Terminal = None
        self.Terminal = Terminal

        super(TerminalConstraintTerm, self).__init__(**kw_args)

    def getTerminal(self):
        
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.TerminalConstraints if x != self]
            self._Terminal._TerminalConstraints = filtered

        self._Terminal = value
        if self._Terminal is not None:
            self._Terminal._TerminalConstraints.append(self)

    Terminal = property(getTerminal, setTerminal)

