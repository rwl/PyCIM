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

from CIM16.IEC61970.Wires.EnergyConsumer import EnergyConsumer

class NonConformLoad(EnergyConsumer):
    """NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.
    """

    def __init__(self, LoadGroup=None, *args, **kw_args):
        """Initialises a new 'NonConformLoad' instance.

        @param LoadGroup: Group of this ConformLoad.
        """
        self._LoadGroup = None
        self.LoadGroup = LoadGroup

        super(NonConformLoad, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["LoadGroup"]
    _many_refs = []

    def getLoadGroup(self):
        """Group of this ConformLoad.
        """
        return self._LoadGroup

    def setLoadGroup(self, value):
        if self._LoadGroup is not None:
            filtered = [x for x in self.LoadGroup.EnergyConsumers if x != self]
            self._LoadGroup._EnergyConsumers = filtered

        self._LoadGroup = value
        if self._LoadGroup is not None:
            if self not in self._LoadGroup._EnergyConsumers:
                self._LoadGroup._EnergyConsumers.append(self)

    LoadGroup = property(getLoadGroup, setLoadGroup)

