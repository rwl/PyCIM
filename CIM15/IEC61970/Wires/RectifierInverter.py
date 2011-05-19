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

from CIM15.IEC61970.Core.ConductingEquipment import ConductingEquipment

class RectifierInverter(ConductingEquipment):
    """Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.
    """

    def __init__(self, ratedU=0.0, maxU=0.0, bridges=0, compoundResistance=0.0, commutatingResistance=0.0, minP=0.0, operatingMode='', minU=0.0, commutatingReactance=0.0, maxP=0.0, frequency=0.0, minCompoundVoltage=0.0, *args, **kw_args):
        """Initialises a new 'RectifierInverter' instance.

        @param ratedU: Rectifier/inverter primary base voltage 
        @param maxU: The maximum voltage on the DC side at which the converter should operate. 
        @param bridges: Number of bridges 
        @param compoundResistance: Compounding resistance. 
        @param commutatingResistance: Commutating resistance. 
        @param minP: The minimum active power on the DC side at which the converter should operate. 
        @param operatingMode: Operating mode for the converter. 
        @param minU: The minimum voltage on the DC side at which the converter should operate. 
        @param commutatingReactance: Commutating reactance at AC bus frequency. 
        @param maxP: The maximum active power on the DC side at which the fconverter should operate. 
        @param frequency: Frequency on the AC side. 
        @param minCompoundVoltage: Minimum compounded DC voltage 
        """
        #: Rectifier/inverter primary base voltage
        self.ratedU = ratedU

        #: The maximum voltage on the DC side at which the converter should operate.
        self.maxU = maxU

        #: Number of bridges
        self.bridges = bridges

        #: Compounding resistance.
        self.compoundResistance = compoundResistance

        #: Commutating resistance.
        self.commutatingResistance = commutatingResistance

        #: The minimum active power on the DC side at which the converter should operate.
        self.minP = minP

        #: Operating mode for the converter.
        self.operatingMode = operatingMode

        #: The minimum voltage on the DC side at which the converter should operate.
        self.minU = minU

        #: Commutating reactance at AC bus frequency.
        self.commutatingReactance = commutatingReactance

        #: The maximum active power on the DC side at which the fconverter should operate.
        self.maxP = maxP

        #: Frequency on the AC side.
        self.frequency = frequency

        #: Minimum compounded DC voltage
        self.minCompoundVoltage = minCompoundVoltage

        super(RectifierInverter, self).__init__(*args, **kw_args)

    _attrs = ["ratedU", "maxU", "bridges", "compoundResistance", "commutatingResistance", "minP", "operatingMode", "minU", "commutatingReactance", "maxP", "frequency", "minCompoundVoltage"]
    _attr_types = {"ratedU": float, "maxU": float, "bridges": int, "compoundResistance": float, "commutatingResistance": float, "minP": float, "operatingMode": str, "minU": float, "commutatingReactance": float, "maxP": float, "frequency": float, "minCompoundVoltage": float}
    _defaults = {"ratedU": 0.0, "maxU": 0.0, "bridges": 0, "compoundResistance": 0.0, "commutatingResistance": 0.0, "minP": 0.0, "operatingMode": '', "minU": 0.0, "commutatingReactance": 0.0, "maxP": 0.0, "frequency": 0.0, "minCompoundVoltage": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

