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

from CIM14.IEC61970.Meas.MeasurementValue import MeasurementValue

class DiscreteValue(MeasurementValue):
    """DiscreteValue represents a discrete MeasurementValue.
    """

    def __init__(self, value=0, Discrete=None, *args, **kw_args):
        """Initialises a new 'DiscreteValue' instance.

        @param value: The value to supervise. 
        @param Discrete: Measurement to which this value is connected.
        """
        #: The value to supervise.
        self.value = value

        self._Discrete = None
        self.Discrete = Discrete

        super(DiscreteValue, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": int}
    _defaults = {"value": 0}
    _enums = {}
    _refs = ["Discrete"]
    _many_refs = []

    def getDiscrete(self):
        """Measurement to which this value is connected.
        """
        return self._Discrete

    def setDiscrete(self, value):
        if self._Discrete is not None:
            filtered = [x for x in self.Discrete.DiscreteValues if x != self]
            self._Discrete._DiscreteValues = filtered

        self._Discrete = value
        if self._Discrete is not None:
            if self not in self._Discrete._DiscreteValues:
                self._Discrete._DiscreteValues.append(self)

    Discrete = property(getDiscrete, setDiscrete)

