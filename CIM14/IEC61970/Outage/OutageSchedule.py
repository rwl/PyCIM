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

from CIM14.IEC61970.Core.IrregularIntervalSchedule import IrregularIntervalSchedule

class OutageSchedule(IrregularIntervalSchedule):
    """The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """

    def __init__(self, SwitchingOperations=None, PowerSystemResource=None, *args, **kw_args):
        """Initialises a new 'OutageSchedule' instance.

        @param SwitchingOperations: An OutageSchedule may operate many switches.
        @param PowerSystemResource: A power system resource may have an outage schedule
        """
        self._SwitchingOperations = []
        self.SwitchingOperations = [] if SwitchingOperations is None else SwitchingOperations

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        super(OutageSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SwitchingOperations", "PowerSystemResource"]
    _many_refs = ["SwitchingOperations"]

    def getSwitchingOperations(self):
        """An OutageSchedule may operate many switches.
        """
        return self._SwitchingOperations

    def setSwitchingOperations(self, value):
        for x in self._SwitchingOperations:
            x.OutageSchedule = None
        for y in value:
            y._OutageSchedule = self
        self._SwitchingOperations = value

    SwitchingOperations = property(getSwitchingOperations, setSwitchingOperations)

    def addSwitchingOperations(self, *SwitchingOperations):
        for obj in SwitchingOperations:
            obj.OutageSchedule = self

    def removeSwitchingOperations(self, *SwitchingOperations):
        for obj in SwitchingOperations:
            obj.OutageSchedule = None

    def getPowerSystemResource(self):
        """A power system resource may have an outage schedule
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._OutageSchedule = None

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource.OutageSchedule = None
            self._PowerSystemResource._OutageSchedule = self

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

