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

from CIM14.CPSM.Equipment.LoadModel.LoadGroup import LoadGroup

class ConformLoadGroup(LoadGroup):
    """A group of loads conforming to an allocation pattern.
    """

    def __init__(self, EnergyConsumers=None, ConformLoadSchedules=None, *args, **kw_args):
        """Initialises a new 'ConformLoadGroup' instance.

        @param EnergyConsumers: Conform loads assigned to this ConformLoadGroup.
        @param ConformLoadSchedules: The ConformLoadSchedules in the ConformLoadGroup.
        """
        self._EnergyConsumers = []
        self.EnergyConsumers = [] if EnergyConsumers is None else EnergyConsumers

        self._ConformLoadSchedules = []
        self.ConformLoadSchedules = [] if ConformLoadSchedules is None else ConformLoadSchedules

        super(ConformLoadGroup, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["EnergyConsumers", "ConformLoadSchedules"]
    _many_refs = ["EnergyConsumers", "ConformLoadSchedules"]

    def getEnergyConsumers(self):
        """Conform loads assigned to this ConformLoadGroup.
        """
        return self._EnergyConsumers

    def setEnergyConsumers(self, value):
        for x in self._EnergyConsumers:
            x.LoadGroup = None
        for y in value:
            y._LoadGroup = self
        self._EnergyConsumers = value

    EnergyConsumers = property(getEnergyConsumers, setEnergyConsumers)

    def addEnergyConsumers(self, *EnergyConsumers):
        for obj in EnergyConsumers:
            obj.LoadGroup = self

    def removeEnergyConsumers(self, *EnergyConsumers):
        for obj in EnergyConsumers:
            obj.LoadGroup = None

    def getConformLoadSchedules(self):
        """The ConformLoadSchedules in the ConformLoadGroup.
        """
        return self._ConformLoadSchedules

    def setConformLoadSchedules(self, value):
        for x in self._ConformLoadSchedules:
            x.ConformLoadGroup = None
        for y in value:
            y._ConformLoadGroup = self
        self._ConformLoadSchedules = value

    ConformLoadSchedules = property(getConformLoadSchedules, setConformLoadSchedules)

    def addConformLoadSchedules(self, *ConformLoadSchedules):
        for obj in ConformLoadSchedules:
            obj.ConformLoadGroup = self

    def removeConformLoadSchedules(self, *ConformLoadSchedules):
        for obj in ConformLoadSchedules:
            obj.ConformLoadGroup = None

