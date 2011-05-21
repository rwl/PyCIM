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

from CIM14.CPSM.Equipment.Element import Element

class TieFlow(Element):
    """A flow specification in terms of location and direction for a control area.
    """

    def __init__(self, positiveFlowIn=False, ControlArea=None, Terminal=None, *args, **kw_args):
        """Initialises a new 'TieFlow' instance.

        @param positiveFlowIn: The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
        @param ControlArea: The control area of the tie flows.
        @param Terminal: The terminal to which this tie flow belongs.
        """
        #: The flow is positive into the terminal.  A flow is positive if it is an import into the control area.
        self.positiveFlowIn = positiveFlowIn

        self._ControlArea = None
        self.ControlArea = ControlArea

        self._Terminal = None
        self.Terminal = Terminal

        super(TieFlow, self).__init__(*args, **kw_args)

    _attrs = ["positiveFlowIn"]
    _attr_types = {"positiveFlowIn": bool}
    _defaults = {"positiveFlowIn": False}
    _enums = {}
    _refs = ["ControlArea", "Terminal"]
    _many_refs = []

    def getControlArea(self):
        """The control area of the tie flows.
        """
        return self._ControlArea

    def setControlArea(self, value):
        if self._ControlArea is not None:
            filtered = [x for x in self.ControlArea.TieFlow if x != self]
            self._ControlArea._TieFlow = filtered

        self._ControlArea = value
        if self._ControlArea is not None:
            if self not in self._ControlArea._TieFlow:
                self._ControlArea._TieFlow.append(self)

    ControlArea = property(getControlArea, setControlArea)

    def getTerminal(self):
        """The terminal to which this tie flow belongs.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.TieFlow if x != self]
            self._Terminal._TieFlow = filtered

        self._Terminal = value
        if self._Terminal is not None:
            if self not in self._Terminal._TieFlow:
                self._Terminal._TieFlow.append(self)

    Terminal = property(getTerminal, setTerminal)

