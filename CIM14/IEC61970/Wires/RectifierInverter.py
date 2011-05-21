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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class RectifierInverter(ConductingEquipment):
    """Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.
    """

    def __init__(self, ratedU=0.0, compoundResistance=0.0, frequency=0.0, minCompoundVoltage=0.0, minP=0.0, maxP=0.0, operatingMode='', commutatingResistance=0.0, bridges=0, maxU=0.0, commutatingReactance=0.0, minU=0.0, *args, **kw_args):
        """Initialises a new 'RectifierInverter' instance.

        @param ratedU: Rectifier/inverter primary base voltage 
        @param compoundResistance: Compounding resistance. 
        @param frequency: Frequency on the AC side. 
        @param minCompoundVoltage: Minimum compounded DC voltage 
        @param minP: The minimum active power on the DC side at which the converter should operate. 
        @param maxP: The maximum active power on the DC side at which the fconverter should operate. 
        @param operatingMode: Operating mode for the converter. 
        @param commutatingResistance: Commutating resistance. 
        @param bridges: Number of bridges 
        @param maxU: The maximum voltage on the DC side at which the converter should operate. 
        @param commutatingReactance: Commutating reactance at AC bus frequency. 
        @param minU: The minimum voltage on the DC side at which the converter should operate. 
        """
        #: Rectifier/inverter primary base voltage
        self.ratedU = ratedU

        #: Compounding resistance.
        self.compoundResistance = compoundResistance

        #: Frequency on the AC side.
        self.frequency = frequency

        #: Minimum compounded DC voltage
        self.minCompoundVoltage = minCompoundVoltage

        #: The minimum active power on the DC side at which the converter should operate.
        self.minP = minP

        #: The maximum active power on the DC side at which the fconverter should operate.
        self.maxP = maxP

        #: Operating mode for the converter.
        self.operatingMode = operatingMode

        #: Commutating resistance.
        self.commutatingResistance = commutatingResistance

        #: Number of bridges
        self.bridges = bridges

        #: The maximum voltage on the DC side at which the converter should operate.
        self.maxU = maxU

        #: Commutating reactance at AC bus frequency.
        self.commutatingReactance = commutatingReactance

        #: The minimum voltage on the DC side at which the converter should operate.
        self.minU = minU

        super(RectifierInverter, self).__init__(*args, **kw_args)

    _attrs = ["ratedU", "compoundResistance", "frequency", "minCompoundVoltage", "minP", "maxP", "operatingMode", "commutatingResistance", "bridges", "maxU", "commutatingReactance", "minU"]
    _attr_types = {"ratedU": float, "compoundResistance": float, "frequency": float, "minCompoundVoltage": float, "minP": float, "maxP": float, "operatingMode": str, "commutatingResistance": float, "bridges": int, "maxU": float, "commutatingReactance": float, "minU": float}
    _defaults = {"ratedU": 0.0, "compoundResistance": 0.0, "frequency": 0.0, "minCompoundVoltage": 0.0, "minP": 0.0, "maxP": 0.0, "operatingMode": '', "commutatingResistance": 0.0, "bridges": 0, "maxU": 0.0, "commutatingReactance": 0.0, "minU": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

