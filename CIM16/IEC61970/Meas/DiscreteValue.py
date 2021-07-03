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

from CIM16.IEC61970.Meas.MeasurementValue import MeasurementValue

class DiscreteValue(MeasurementValue):
    """DiscreteValue represents a discrete MeasurementValue.DiscreteValue represents a discrete MeasurementValue.
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

