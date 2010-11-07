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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class RectifierInverter(ConductingEquipment):
    """Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.
    """

    def __init__(self, ratedU=0.0, compoundResistance=0.0, frequency=0.0, minCompoundVoltage=0.0, minP=0.0, maxP=0.0, operatingMode='', commutatingResistance=0.0, bridges=0, maxU=0.0, commutatingReactance=0.0, minU=0.0, **kw_args):
        """Initializes a new 'RectifierInverter' instance.

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

        super(RectifierInverter, self).__init__(**kw_args)

