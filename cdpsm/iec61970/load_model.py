# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.This package is responsible for modeling the energy consumers and the system load as curves and associated curve data. Special circumstances that may affect the load, such as seasons and daytypes, are also included here.  This information is used by Load Forecasting and Load Management.
"""

from cdpsm.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_LoadModel"

class LoadResponseCharacteristic(IdentifiedObject):
    """ Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.
    """
    # <<< load_response_characteristic
    # @generated
    def __init__(self, p_voltage_exponent=0.0, q_constant_current=0.0, p_frequency_exponent=0.0, exponent_model=False, q_constant_impedance=0.0, p_constant_current=0.0, q_frequency_exponent=0.0, p_constant_power=0.0, q_voltage_exponent=0.0, q_constant_power=0.0, p_constant_impedance=0.0, energy_consumer=None, **kw_args):
        """ Initialises a new 'LoadResponseCharacteristic' instance.
        """
        # Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true.Exponent of per unit voltage effecting real power.   This model used only when 'useExponentModel' is true. 
        self.p_voltage_exponent = p_voltage_exponent

        # Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.Portion of reactive power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        self.q_constant_current = q_constant_current

        # Exponent of per unit frequency effecting active powerExponent of per unit frequency effecting active power 
        self.p_frequency_exponent = p_frequency_exponent

        # Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used.Indicates the exponential voltage dependency model (pVoltateExponent and qVoltageExponent) is to be used.   If false, the coeficient model (consisting of pConstantImpedance, pConstantCurrent, pConstantPower, qConstantImpedance, qConstantCurrent, and qConstantPower) is to be used. 
        self.exponent_model = exponent_model

        # Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.Portion of reactive power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        self.q_constant_impedance = q_constant_impedance

        # Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.Portion of active power load modeled as constant current. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        self.p_constant_current = p_constant_current

        # Exponent of per unit frequency effecting reactive powerExponent of per unit frequency effecting reactive power 
        self.q_frequency_exponent = q_frequency_exponent

        # Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.Portion of active power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        self.p_constant_power = p_constant_power

        # Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true.Exponent of per unit voltage effecting reactive power.   This model used only when 'useExponentModel' is true. 
        self.q_voltage_exponent = q_voltage_exponent

        # Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP.Portion of reactive power load modeled as constant power. Used only if the useExponentModel is false.    This value is noralized against the sum of qZ, qI, and qP. 
        self.q_constant_power = q_constant_power

        # Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP.Portion of active power load modeled as constant impedance.  Used only if the useExponentModel is false.    This value is noralized against the sum of pZ, pI, and pP. 
        self.p_constant_impedance = p_constant_impedance


        self._energy_consumer = []
        if energy_consumer is not None:
            self.energy_consumer = energy_consumer
        else:
            self.energy_consumer = []


        super(LoadResponseCharacteristic, self).__init__(**kw_args)
    # >>> load_response_characteristic

    # <<< energy_consumer
    # @generated
    def get_energy_consumer(self):
        """ The set of loads that have the response characteristics.The set of loads that have the response characteristics.
        """
        return self._energy_consumer

    def set_energy_consumer(self, value):
        for x in self._energy_consumer:
            x._load_response = None
        for y in value:
            y._load_response = self
        self._energy_consumer = value

    energy_consumer = property(get_energy_consumer, set_energy_consumer)

    def add_energy_consumer(self, *energy_consumer):
        for obj in energy_consumer:
            obj._load_response = self
            self._energy_consumer.append(obj)

    def remove_energy_consumer(self, *energy_consumer):
        for obj in energy_consumer:
            obj._load_response = None
            self._energy_consumer.remove(obj)
    # >>> energy_consumer


    def __str__(self):
        """ Returns a string representation of the LoadResponseCharacteristic.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_response_characteristic.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadResponseCharacteristic.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadResponseCharacteristic", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.energy_consumer:
            s += '%s<%s:LoadResponseCharacteristic.energy_consumer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:LoadResponseCharacteristic.p_voltage_exponent>%s</%s:LoadResponseCharacteristic.p_voltage_exponent>' % \
            (indent, ns_prefix, self.p_voltage_exponent, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_constant_current>%s</%s:LoadResponseCharacteristic.q_constant_current>' % \
            (indent, ns_prefix, self.q_constant_current, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.p_frequency_exponent>%s</%s:LoadResponseCharacteristic.p_frequency_exponent>' % \
            (indent, ns_prefix, self.p_frequency_exponent, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.exponent_model>%s</%s:LoadResponseCharacteristic.exponent_model>' % \
            (indent, ns_prefix, self.exponent_model, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_constant_impedance>%s</%s:LoadResponseCharacteristic.q_constant_impedance>' % \
            (indent, ns_prefix, self.q_constant_impedance, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.p_constant_current>%s</%s:LoadResponseCharacteristic.p_constant_current>' % \
            (indent, ns_prefix, self.p_constant_current, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_frequency_exponent>%s</%s:LoadResponseCharacteristic.q_frequency_exponent>' % \
            (indent, ns_prefix, self.q_frequency_exponent, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.p_constant_power>%s</%s:LoadResponseCharacteristic.p_constant_power>' % \
            (indent, ns_prefix, self.p_constant_power, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_voltage_exponent>%s</%s:LoadResponseCharacteristic.q_voltage_exponent>' % \
            (indent, ns_prefix, self.q_voltage_exponent, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.q_constant_power>%s</%s:LoadResponseCharacteristic.q_constant_power>' % \
            (indent, ns_prefix, self.q_constant_power, ns_prefix)
        s += '%s<%s:LoadResponseCharacteristic.p_constant_impedance>%s</%s:LoadResponseCharacteristic.p_constant_impedance>' % \
            (indent, ns_prefix, self.p_constant_impedance, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadResponseCharacteristic")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_response_characteristic.serialize


# <<< load_model
# @generated
# >>> load_model
