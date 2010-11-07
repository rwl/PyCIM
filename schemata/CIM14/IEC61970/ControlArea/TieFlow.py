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

class TieFlow(Element):
    """A flow specification in terms of location and direction for a control area.
    """

    def __init__(self, positiveFlowIn=False, ControlArea=None, AltTieMeas=None, Terminal=None, **kw_args):
        """Initializes a new 'TieFlow' instance.

        @param positiveFlowIn: The flow is positive into the terminal.  A flow is positive if it is an import into the control area. 
        @param ControlArea: The control area of the tie flows.
        @param AltTieMeas: The primary and alternate tie flow measurements associated with the tie flow.
        @param Terminal: The terminal to which this tie flow belongs.
        """
        #: The flow is positive into the terminal.  A flow is positive if it is an import into the control area.
        self.positiveFlowIn = positiveFlowIn

        self._ControlArea = None
        self.ControlArea = ControlArea

        self._AltTieMeas = []
        self.AltTieMeas = [] if AltTieMeas is None else AltTieMeas

        self._Terminal = None
        self.Terminal = Terminal

        super(TieFlow, self).__init__(**kw_args)

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
            self._ControlArea._TieFlow.append(self)

    ControlArea = property(getControlArea, setControlArea)

    def getAltTieMeas(self):
        """The primary and alternate tie flow measurements associated with the tie flow.
        """
        return self._AltTieMeas

    def setAltTieMeas(self, value):
        for x in self._AltTieMeas:
            x._TieFlow = None
        for y in value:
            y._TieFlow = self
        self._AltTieMeas = value

    AltTieMeas = property(getAltTieMeas, setAltTieMeas)

    def addAltTieMeas(self, *AltTieMeas):
        for obj in AltTieMeas:
            obj._TieFlow = self
            self._AltTieMeas.append(obj)

    def removeAltTieMeas(self, *AltTieMeas):
        for obj in AltTieMeas:
            obj._TieFlow = None
            self._AltTieMeas.remove(obj)

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
            self._Terminal._TieFlow.append(self)

    Terminal = property(getTerminal, setTerminal)

