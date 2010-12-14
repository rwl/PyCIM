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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class LoadResponseCharacteristic(IdentifiedObject):
    """Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.
    """

    def __init__(self, pFrequencyExponent=0.0, qFrequencyExponent=0.0, pConstantPower=0.0, pConstantCurrent=0.0, pVoltageExponent=0.0, pConstantImpedance=0.0, qConstantImpedance=0.0, qConstantPower=0.0, qVoltageExponent=0.0, exponentModel=False, qConstantCurrent=0.0, EnergyConsumer=None, *args, **kw_args):
        """Initialises a new 'LoadResponseCharacteristic' instance.

        @param pFrequencyExponent: Exponent of per unit frequency effecting active power 
        @param qFrequencyExponent: Exponent of per unit frequency effecting reactive power 
        @param pConstantPower: Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        @param pConstantCurrent: Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        @param pVoltageExponent: Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true. 
        @param pConstantImpedance: Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        @param qConstantImpedance: Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        @param qConstantPower: Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        @param qVoltageExponent: Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true. 
        @param exponentModel: Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used. 
        @param qConstantCurrent: Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        @param EnergyConsumer: The set of loads that have the response characteristics.
        """
        #: Exponent of per unit frequency effecting active power
        self.pFrequencyExponent = pFrequencyExponent

        #: Exponent of per unit frequency effecting reactive power
        self.qFrequencyExponent = qFrequencyExponent

        #: Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
        self.pConstantPower = pConstantPower

        #: Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
        self.pConstantCurrent = pConstantCurrent

        #: Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
        self.pVoltageExponent = pVoltageExponent

        #: Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
        self.pConstantImpedance = pConstantImpedance

        #: Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
        self.qConstantImpedance = qConstantImpedance

        #: Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
        self.qConstantPower = qConstantPower

        #: Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
        self.qVoltageExponent = qVoltageExponent

        #: Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.
        self.exponentModel = exponentModel

        #: Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
        self.qConstantCurrent = qConstantCurrent

        self._EnergyConsumer = []
        self.EnergyConsumer = [] if EnergyConsumer is None else EnergyConsumer

        super(LoadResponseCharacteristic, self).__init__(*args, **kw_args)

    _attrs = ["pFrequencyExponent", "qFrequencyExponent", "pConstantPower", "pConstantCurrent", "pVoltageExponent", "pConstantImpedance", "qConstantImpedance", "qConstantPower", "qVoltageExponent", "exponentModel", "qConstantCurrent"]
    _attr_types = {"pFrequencyExponent": float, "qFrequencyExponent": float, "pConstantPower": float, "pConstantCurrent": float, "pVoltageExponent": float, "pConstantImpedance": float, "qConstantImpedance": float, "qConstantPower": float, "qVoltageExponent": float, "exponentModel": bool, "qConstantCurrent": float}
    _defaults = {"pFrequencyExponent": 0.0, "qFrequencyExponent": 0.0, "pConstantPower": 0.0, "pConstantCurrent": 0.0, "pVoltageExponent": 0.0, "pConstantImpedance": 0.0, "qConstantImpedance": 0.0, "qConstantPower": 0.0, "qVoltageExponent": 0.0, "exponentModel": False, "qConstantCurrent": 0.0}
    _enums = {}
    _refs = ["EnergyConsumer"]
    _many_refs = ["EnergyConsumer"]

    def getEnergyConsumer(self):
        """The set of loads that have the response characteristics.
        """
        return self._EnergyConsumer

    def setEnergyConsumer(self, value):
        for x in self._EnergyConsumer:
            x.LoadResponse = None
        for y in value:
            y._LoadResponse = self
        self._EnergyConsumer = value

    EnergyConsumer = property(getEnergyConsumer, setEnergyConsumer)

    def addEnergyConsumer(self, *EnergyConsumer):
        for obj in EnergyConsumer:
            obj.LoadResponse = self

    def removeEnergyConsumer(self, *EnergyConsumer):
        for obj in EnergyConsumer:
            obj.LoadResponse = None

