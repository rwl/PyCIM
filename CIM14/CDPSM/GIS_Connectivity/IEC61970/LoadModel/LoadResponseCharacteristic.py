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

from CIM14.CDPSM.GIS_Connectivity.IEC61970.Core.IdentifiedObject import IdentifiedObject

class LoadResponseCharacteristic(IdentifiedObject):
    """Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.
    """

    def __init__(self, pVoltageExponent=0.0, qConstantCurrent=0.0, pFrequencyExponent=0.0, exponentModel=False, qConstantImpedance=0.0, pConstantCurrent=0.0, qFrequencyExponent=0.0, pConstantPower=0.0, qVoltageExponent=0.0, qConstantPower=0.0, pConstantImpedance=0.0, *args, **kw_args):
        """Initialises a new 'LoadResponseCharacteristic' instance.

        @param pVoltageExponent: Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true. 
        @param qConstantCurrent: Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        @param pFrequencyExponent: Exponent of per unit frequency effecting active power 
        @param exponentModel: Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used. 
        @param qConstantImpedance: Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        @param pConstantCurrent: Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        @param qFrequencyExponent: Exponent of per unit frequency effecting reactive power 
        @param pConstantPower: Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        @param qVoltageExponent: Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true. 
        @param qConstantPower: Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        @param pConstantImpedance: Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        """
        #: Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.
        self.pVoltageExponent = pVoltageExponent

        #: Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
        self.qConstantCurrent = qConstantCurrent

        #: Exponent of per unit frequency effecting active power
        self.pFrequencyExponent = pFrequencyExponent

        #: Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.
        self.exponentModel = exponentModel

        #: Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
        self.qConstantImpedance = qConstantImpedance

        #: Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
        self.pConstantCurrent = pConstantCurrent

        #: Exponent of per unit frequency effecting reactive power
        self.qFrequencyExponent = qFrequencyExponent

        #: Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
        self.pConstantPower = pConstantPower

        #: Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.
        self.qVoltageExponent = qVoltageExponent

        #: Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.
        self.qConstantPower = qConstantPower

        #: Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.
        self.pConstantImpedance = pConstantImpedance

        super(LoadResponseCharacteristic, self).__init__(*args, **kw_args)

    _attrs = ["pVoltageExponent", "qConstantCurrent", "pFrequencyExponent", "exponentModel", "qConstantImpedance", "pConstantCurrent", "qFrequencyExponent", "pConstantPower", "qVoltageExponent", "qConstantPower", "pConstantImpedance"]
    _attr_types = {"pVoltageExponent": float, "qConstantCurrent": float, "pFrequencyExponent": float, "exponentModel": bool, "qConstantImpedance": float, "pConstantCurrent": float, "qFrequencyExponent": float, "pConstantPower": float, "qVoltageExponent": float, "qConstantPower": float, "pConstantImpedance": float}
    _defaults = {"pVoltageExponent": 0.0, "qConstantCurrent": 0.0, "pFrequencyExponent": 0.0, "exponentModel": False, "qConstantImpedance": 0.0, "pConstantCurrent": 0.0, "qFrequencyExponent": 0.0, "pConstantPower": 0.0, "qVoltageExponent": 0.0, "qConstantPower": 0.0, "pConstantImpedance": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

