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

from CIM14v13.Element import Element

class AltTieMeas(Element):
    """A prioritized measurement to be used for the tie flow as part of the control area specification.
    """

    def __init__(self, priority=0, AnalogValue=None, TieFlow=None, *args, **kw_args):
        """Initializes a new 'AltTieMeas' instance.

        @param priority: Priority of a measurement usage.   Lower numbers have first priority. 
        @param AnalogValue: The specific analog value used as a source.
        @param TieFlow: The tie flow of the alternate measurements.
        """
        #: Priority of a measurement usage.   Lower numbers have first priority.
        self.priority = priority

        self._AnalogValue = None
        self.AnalogValue = AnalogValue

        self._TieFlow = None
        self.TieFlow = TieFlow

        super(AltTieMeas, self).__init__(*args, **kw_args)

    def getAnalogValue(self):
        """The specific analog value used as a source.
        """
        return self._AnalogValue

    def setAnalogValue(self, value):
        if self._AnalogValue is not None:
            filtered = [x for x in self.AnalogValue.AltTieMeas if x != self]
            self._AnalogValue._AltTieMeas = filtered

        self._AnalogValue = value
        if self._AnalogValue is not None:
            self._AnalogValue._AltTieMeas.append(self)

    AnalogValue = property(getAnalogValue, setAnalogValue)

    def getTieFlow(self):
        """The tie flow of the alternate measurements.
        """
        return self._TieFlow

    def setTieFlow(self, value):
        if self._TieFlow is not None:
            filtered = [x for x in self.TieFlow.AltTieMeas if x != self]
            self._TieFlow._AltTieMeas = filtered

        self._TieFlow = value
        if self._TieFlow is not None:
            self._TieFlow._AltTieMeas.append(self)

    TieFlow = property(getTieFlow, setTieFlow)

