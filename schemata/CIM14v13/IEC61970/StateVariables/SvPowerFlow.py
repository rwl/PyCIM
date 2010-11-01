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

from CIM14v13.IEC61970.StateVariables.StateVariable import StateVariable

class SvPowerFlow(StateVariable):
    """State variable for power flow.
    """

    def __init__(self, p=0.0, q=0.0, Terminal=None, *args, **kw_args):
        """Initializes a new 'SvPowerFlow' instance.

        @param p: The active power flow into the terminal. 
        @param q: The reactive power flow into the terminal. 
        @param Terminal: The terminal associated with the power flow state.
        """
        #: The active power flow into the terminal. 
        self.p = p

        #: The reactive power flow into the terminal. 
        self.q = q

        self._Terminal = None
        self.Terminal = Terminal

        super(SvPowerFlow, self).__init__(*args, **kw_args)

    def getTerminal(self):
        """The terminal associated with the power flow state.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            self._Terminal._SvPowerFlow = None

        self._Terminal = value
        if self._Terminal is not None:
            self._Terminal._SvPowerFlow = self

    Terminal = property(getTerminal, setTerminal)

