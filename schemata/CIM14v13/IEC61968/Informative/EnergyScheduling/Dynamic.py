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

from CIM14v13.IEC61968.Informative.EnergyScheduling.EnergyTransaction import EnergyTransaction

class Dynamic(EnergyTransaction):
    """A dynamic energy transaction has more complex relationships than a simple block type. It behaves like a pseudo tie line.
    """

    def __init__(self, TieLines=None, **kw_args):
        """Initializes a new 'Dynamic' instance.

        @param TieLines: A dynamic energy transaction can act as a pseudo tie line.
        """
        self._TieLines = []
        self.TieLines = [] if TieLines is None else TieLines

        super(Dynamic, self).__init__(**kw_args)

    def getTieLines(self):
        """A dynamic energy transaction can act as a pseudo tie line.
        """
        return self._TieLines

    def setTieLines(self, value):
        for x in self._TieLines:
            x._DynamicEnergyTransaction = None
        for y in value:
            y._DynamicEnergyTransaction = self
        self._TieLines = value

    TieLines = property(getTieLines, setTieLines)

    def addTieLines(self, *TieLines):
        for obj in TieLines:
            obj._DynamicEnergyTransaction = self
            self._TieLines.append(obj)

    def removeTieLines(self, *TieLines):
        for obj in TieLines:
            obj._DynamicEnergyTransaction = None
            self._TieLines.remove(obj)

