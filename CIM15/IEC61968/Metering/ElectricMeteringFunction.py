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

from CIM15.IEC61968.Metering.EndDeviceFunction import EndDeviceFunction

class ElectricMeteringFunction(EndDeviceFunction):
    """Functionality performed by an electric meter.Functionality performed by an electric meter.
    """

    def __init__(self, kWMultiplier=0, kWhMultiplier=0, ctRatioMultiplier=None, billingMultiplier=None, vtRatioMultiplier=None, demandMultiplier=None, *args, **kw_args):
        """Initialises a new 'ElectricMeteringFunction' instance.

        @param kWMultiplier: Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer. 
        @param kWhMultiplier: Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer. 
        @param ctRatioMultiplier: Current transformer ratio used to convert associated quantities to real measurements.
        @param billingMultiplier: Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item.
        @param vtRatioMultiplier: Voltage transformer ratio used to convert associated quantities to real measurements.
        @param demandMultiplier: An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 min, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'.
        """
        #: Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.
        self.kWMultiplier = kWMultiplier

        #: Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.
        self.kWhMultiplier = kWhMultiplier

        self.ctRatioMultiplier = ctRatioMultiplier

        self.billingMultiplier = billingMultiplier

        self.vtRatioMultiplier = vtRatioMultiplier

        self.demandMultiplier = demandMultiplier

        super(ElectricMeteringFunction, self).__init__(*args, **kw_args)

    _attrs = ["kWMultiplier", "kWhMultiplier"]
    _attr_types = {"kWMultiplier": int, "kWhMultiplier": int}
    _defaults = {"kWMultiplier": 0, "kWhMultiplier": 0}
    _enums = {}
    _refs = ["ctRatioMultiplier", "billingMultiplier", "vtRatioMultiplier", "demandMultiplier"]
    _many_refs = []

    # Current transformer ratio used to convert associated quantities to real measurements.
    ctRatioMultiplier = None

    # Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item.
    billingMultiplier = None

    # Voltage transformer ratio used to convert associated quantities to real measurements.
    vtRatioMultiplier = None

    # An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 min, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'.
    demandMultiplier = None

