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

from CIM14.IEC61970.Meas.Control import Control

class SetPoint(Control):
    """A SetPoint is an analog control used for supervisory control.
    """

    def __init__(self, minValue=0.0, value=0.0, maxValue=0.0, normalValue=0.0, Analog=None, **kw_args):
        """Initializes a new 'SetPoint' instance.

        @param minValue: Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs. 
        @param value: The value representing the actuator output 
        @param maxValue: Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs. 
        @param normalValue: Normal value for Control.value e.g. used for percentage scaling 
        @param Analog: The Measurement variable used for control
        """
        #: Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
        self.minValue = minValue

        #: The value representing the actuator output
        self.value = value

        #: Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
        self.maxValue = maxValue

        #: Normal value for Control.value e.g. used for percentage scaling
        self.normalValue = normalValue

        self._Analog = None
        self.Analog = Analog

        super(SetPoint, self).__init__(**kw_args)

    def getAnalog(self):
        """The Measurement variable used for control
        """
        return self._Analog

    def setAnalog(self, value):
        if self._Analog is not None:
            self._Analog._SetPoint = None

        self._Analog = value
        if self._Analog is not None:
            self._Analog._SetPoint = self

    Analog = property(getAnalog, setAnalog)

