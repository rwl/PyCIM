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

from CIM15.IEC61970.Wires.RegulatingCondEq import RegulatingCondEq

class FrequencyConverter(RegulatingCondEq):
    """A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.
    """

    def __init__(self, maxU=0.0, maxP=0.0, frequency=0.0, minP=0.0, minU=0.0, operatingMode='', *args, **kw_args):
        """Initialises a new 'FrequencyConverter' instance.

        @param maxU: The maximum voltage on the DC side at which the frequency converter should operate. 
        @param maxP: The maximum active power on the DC side at which the frequence converter should operate. 
        @param frequency: Frequency on the AC side. 
        @param minP: The minimum active power on the DC side at which the frequence converter should operate. 
        @param minU: The minimum voltage on the DC side at which the frequency converter should operate. 
        @param operatingMode: Operating mode for the frequency converter 
        """
        #: The maximum voltage on the DC side at which the frequency converter should operate.
        self.maxU = maxU

        #: The maximum active power on the DC side at which the frequence converter should operate.
        self.maxP = maxP

        #: Frequency on the AC side.
        self.frequency = frequency

        #: The minimum active power on the DC side at which the frequence converter should operate.
        self.minP = minP

        #: The minimum voltage on the DC side at which the frequency converter should operate.
        self.minU = minU

        #: Operating mode for the frequency converter
        self.operatingMode = operatingMode

        super(FrequencyConverter, self).__init__(*args, **kw_args)

    _attrs = ["maxU", "maxP", "frequency", "minP", "minU", "operatingMode"]
    _attr_types = {"maxU": float, "maxP": float, "frequency": float, "minP": float, "minU": float, "operatingMode": str}
    _defaults = {"maxU": 0.0, "maxP": 0.0, "frequency": 0.0, "minP": 0.0, "minU": 0.0, "operatingMode": ''}
    _enums = {}
    _refs = []
    _many_refs = []

