#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------




from enthought.traits.api import Float, Enum
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------
CurrentFlow = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatElectrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)")
ActivePower = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the in-phase component of the currentProduct of RMS value of the voltage and the RMS value of the in-phase component of the current")
Seconds = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatTime, in secondsTime, in seconds")
Susceptance = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatImaginary part of admittance.Imaginary part of admittance.")
Conductance = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatFactor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.")
Resistance = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatResistance (real part of impedance).Resistance (real part of impedance).")
PerCent = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatNormally 0 - 100 on a defined baseNormally 0 - 100 on a defined base")
ReactivePower = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the quadrature component of the current.Product of RMS value of the voltage and the RMS value of the quadrature component of the current.")
AngleDegrees = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatMeasurement of angle in degreesMeasurement of angle in degrees")
Voltage = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatElectrical voltage.Electrical voltage.")
ApparentPower = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of the RMS value of the voltage and the RMS value of the currentProduct of the RMS value of the voltage and the RMS value of the current")
Reactance = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatReactance (imaginary part of impedance), at rated frequency.Reactance (imaginary part of impedance), at rated frequency.")
VoltagePerReactivePower = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatVoltage variation with reactive powerVoltage variation with reactive power")


UnitSymbol = Enum("W/s", "none", "s", "h", "J/s", "VA", "Wh", "ohm", "m3", "Hz-1", "W", "min", "rad", "g", "J", "H", "F", "kg/J", "VAh", "s-1", "degC", "deg", "Pa", "VAr", "S", "W/Hz", "m", "m2", "Hz", "A", "N", "V/VAr", "VArh", "V")



# EOF -------------------------------------------------------------------------
