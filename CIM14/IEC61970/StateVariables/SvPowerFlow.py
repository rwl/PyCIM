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

from CIM14.IEC61970.StateVariables.StateVariable import StateVariable

class SvPowerFlow(StateVariable):
    """State variable for power flow.
    """

    def __init__(self, q=0.0, p=0.0, Terminal=None, *args, **kw_args):
        """Initialises a new 'SvPowerFlow' instance.

        @param q: The reactive power flow into the terminal. 
        @param p: The active power flow into the terminal. 
        @param Terminal: The terminal associated with the power flow state.
        """
        #: The reactive power flow into the terminal.
        self.q = q

        #: The active power flow into the terminal.
        self.p = p

        self._Terminal = None
        self.Terminal = Terminal

        super(SvPowerFlow, self).__init__(*args, **kw_args)

    _attrs = ["q", "p"]
    _attr_types = {"q": float, "p": float}
    _defaults = {"q": 0.0, "p": 0.0}
    _enums = {}
    _refs = ["Terminal"]
    _many_refs = []

    def getTerminal(self):
        """The terminal associated with the power flow state.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            self._Terminal._SvPowerFlow = None

        self._Terminal = value
        if self._Terminal is not None:
            self._Terminal.SvPowerFlow = None
            self._Terminal._SvPowerFlow = self

    Terminal = property(getTerminal, setTerminal)

