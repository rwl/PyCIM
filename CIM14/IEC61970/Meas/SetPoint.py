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

from CIM14.IEC61970.Meas.Control import Control

class SetPoint(Control):
    """A SetPoint is an analog control used for supervisory control.
    """

    def __init__(self, minValue=0.0, value=0.0, maxValue=0.0, normalValue=0.0, Analog=None, *args, **kw_args):
        """Initialises a new 'SetPoint' instance.

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

        super(SetPoint, self).__init__(*args, **kw_args)

    _attrs = ["minValue", "value", "maxValue", "normalValue"]
    _attr_types = {"minValue": float, "value": float, "maxValue": float, "normalValue": float}
    _defaults = {"minValue": 0.0, "value": 0.0, "maxValue": 0.0, "normalValue": 0.0}
    _enums = {}
    _refs = ["Analog"]
    _many_refs = []

    def getAnalog(self):
        """The Measurement variable used for control
        """
        return self._Analog

    def setAnalog(self, value):
        if self._Analog is not None:
            self._Analog._SetPoint = None

        self._Analog = value
        if self._Analog is not None:
            self._Analog.SetPoint = None
            self._Analog._SetPoint = self

    Analog = property(getAnalog, setAnalog)

