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

from CIM14v13.IEC61970.Wires.RegulatingCondEq import RegulatingCondEq

class FrequencyConverter(RegulatingCondEq):
    """A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.
    """

    def __init__(self, maxU=0.0, minU=0.0, minP=0.0, frequency=0.0, maxP=0.0, operatingMode='', **kw_args):
        """Initializes a new 'FrequencyConverter' instance.

        @param maxU: The maximum voltage on the DC side at which the frequency converter should operate. 
        @param minU: The minimum voltage on the DC side at which the frequency converter should operate. 
        @param minP: The minimum active power on the DC side at which the frequence converter should operate. 
        @param frequency: Frequency on the AC side. 
        @param maxP: The maximum active power on the DC side at which the frequence converter should operate. 
        @param operatingMode: Operating mode for the frequency converter 
        """
        #: The maximum voltage on the DC side at which the frequency converter should operate.
        self.maxU = maxU

        #: The minimum voltage on the DC side at which the frequency converter should operate.
        self.minU = minU

        #: The minimum active power on the DC side at which the frequence converter should operate.
        self.minP = minP

        #: Frequency on the AC side.
        self.frequency = frequency

        #: The maximum active power on the DC side at which the frequence converter should operate.
        self.maxP = maxP

        #: Operating mode for the frequency converter
        self.operatingMode = operatingMode

        super(FrequencyConverter, self).__init__(**kw_args)

