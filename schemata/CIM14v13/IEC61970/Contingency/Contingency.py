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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Contingency(IdentifiedObject):
    """An event threatening system reliability, consisting of one or more contingency elements.
    """

    def __init__(self, mustStudy=False, ContingencyConstraintLimit=None, ContingencyElement=None, *args, **kw_args):
        """Initializes a new 'Contingency' instance.

        @param mustStudy: Set true if must study this contingency. 
        @param ContingencyConstraintLimit:
        @param ContingencyElement: A contingency can have any number of contingency elements.
        """
        #: Set true if must study this contingency.
        self.mustStudy = mustStudy

        self._ContingencyConstraintLimit = []
        self.ContingencyConstraintLimit = [] if ContingencyConstraintLimit is None else ContingencyConstraintLimit

        self._ContingencyElement = []
        self.ContingencyElement = [] if ContingencyElement is None else ContingencyElement

        super(Contingency, self).__init__(*args, **kw_args)

    def getContingencyConstraintLimit(self):
        
        return self._ContingencyConstraintLimit

    def setContingencyConstraintLimit(self, value):
        for x in self._ContingencyConstraintLimit:
            x._Contingency = None
        for y in value:
            y._Contingency = self
        self._ContingencyConstraintLimit = value

    ContingencyConstraintLimit = property(getContingencyConstraintLimit, setContingencyConstraintLimit)

    def addContingencyConstraintLimit(self, *ContingencyConstraintLimit):
        for obj in ContingencyConstraintLimit:
            obj._Contingency = self
            self._ContingencyConstraintLimit.append(obj)

    def removeContingencyConstraintLimit(self, *ContingencyConstraintLimit):
        for obj in ContingencyConstraintLimit:
            obj._Contingency = None
            self._ContingencyConstraintLimit.remove(obj)

    def getContingencyElement(self):
        """A contingency can have any number of contingency elements.
        """
        return self._ContingencyElement

    def setContingencyElement(self, value):
        for x in self._ContingencyElement:
            x._Contingency = None
        for y in value:
            y._Contingency = self
        self._ContingencyElement = value

    ContingencyElement = property(getContingencyElement, setContingencyElement)

    def addContingencyElement(self, *ContingencyElement):
        for obj in ContingencyElement:
            obj._Contingency = self
            self._ContingencyElement.append(obj)

    def removeContingencyElement(self, *ContingencyElement):
        for obj in ContingencyElement:
            obj._Contingency = None
            self._ContingencyElement.remove(obj)

