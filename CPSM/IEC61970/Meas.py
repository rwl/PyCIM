#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------

""" Contains entities that describe dynamic measurement data exchanged between applications.Contains entities that describe dynamic measurement data exchanged between applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CPSM.IEC61970.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "Measurement" class:
#------------------------------------------------------------------------------

class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of  power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of  power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The PowerSystemResource that contains the Measurement in the naming hierarchyThe PowerSystemResource that contains the Measurement in the naming hierarchy
    MemberOf_PSR = Instance("CPSM.IEC61970.Core.PowerSystemResource", allow_none=False,
        desc="The PowerSystemResource that contains the Measurement in the naming hierarchyThe PowerSystemResource that contains the Measurement in the naming hierarchy",
        transient=True,
        opposite="Contains_Measurements",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    # The type for the MeasurementThe type for the Measurement
    MeasurementType = Instance("CPSM.IEC61970.Meas.MeasurementType", allow_none=False,
        desc="The type for the MeasurementThe type for the Measurement",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_measurementtypes"))

    def _get_measurementtypes(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Meas.MeasurementType" ]
        else:
            return []

    _measurementtypes = Property(fget=_get_measurementtypes)

    # One or more measurements may be associated with a terminal in the networkOne or more measurements may be associated with a terminal in the network
    Terminal = Instance("CPSM.IEC61970.Core.Terminal", allow_none=False,
        desc="One or more measurements may be associated with a terminal in the networkOne or more measurements may be associated with a terminal in the network",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # The Unit for the MeasurementThe Unit for the Measurement
    Unit = Instance("CPSM.IEC61970.Core.Unit", allow_none=False,
        desc="The Unit for the MeasurementThe Unit for the Measurement",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    #--------------------------------------------------------------------------
    #  Begin "Measurement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "MemberOf_PSR", "MeasurementType", "Terminal", "Unit",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.Measurement",
        title="Measurement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Measurement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementValue" class:
#------------------------------------------------------------------------------

class MeasurementValue(IdentifiedObject):
    """ The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
    MeasurementValueSource = Instance("CPSM.IEC61970.Meas.MeasurementValueSource", allow_none=False,
        desc="A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.",
        transient=True,
        opposite="MeasurementValues",
        editor=InstanceEditor(name="_measurementvaluesources"))

    def _get_measurementvaluesources(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Meas.MeasurementValueSource" ]
        else:
            return []

    _measurementvaluesources = Property(fget=_get_measurementvaluesources)

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "MeasurementValueSource",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.MeasurementValue",
        title="MeasurementValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementValueSource" class:
#------------------------------------------------------------------------------

class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The MeasurementValues updated by the sourceThe MeasurementValues updated by the source
    MeasurementValues = List(Instance("CPSM.IEC61970.Meas.MeasurementValue"),
        desc="The MeasurementValues updated by the sourceThe MeasurementValues updated by the source")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueSource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "MeasurementValues",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.MeasurementValueSource",
        title="MeasurementValueSource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValueSource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementType" class:
#------------------------------------------------------------------------------

class MeasurementType(IdentifiedObject):
    """ Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The measurements associated with the TypeThe measurements associated with the Type
    Measurements = List(Instance("CPSM.IEC61970.Meas.Measurement"),
        desc="The measurements associated with the TypeThe measurements associated with the Type")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Measurements",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.MeasurementType",
        title="MeasurementType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LimitSet" class:
#------------------------------------------------------------------------------

class LimitSet(IdentifiedObject):
    """ Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.
    isPercentageLimits = Bool(desc="Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.")

    #--------------------------------------------------------------------------
    #  Begin "LimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "isPercentageLimits",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.LimitSet",
        title="LimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DiscreteValue" class:
#------------------------------------------------------------------------------

class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue.DiscreteValue represents a discrete MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Measurement to which this value is connected.Measurement to which this value is connected.
    MemberOf_Measurement = Instance("CPSM.IEC61970.Meas.Discrete", allow_none=False,
        desc="Measurement to which this value is connected.Measurement to which this value is connected.",
        transient=True,
        opposite="Contain_MeasurementValues",
        editor=InstanceEditor(name="_discretes"))

    def _get_discretes(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Meas.Discrete" ]
        else:
            return []

    _discretes = Property(fget=_get_discretes)

    #--------------------------------------------------------------------------
    #  Begin "DiscreteValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "MeasurementValueSource", "MemberOf_Measurement",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.DiscreteValue",
        title="DiscreteValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DiscreteValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Analog" class:
#------------------------------------------------------------------------------

class Analog(Measurement):
    """ Analog represents an analog Measurement.Analog represents an analog Measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The values connected to this measurement.The values connected to this measurement.
    Contain_MeasurementValues = List(Instance("CPSM.IEC61970.Meas.AnalogValue"),
        desc="The values connected to this measurement.The values connected to this measurement.")

    # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
    positiveFlowIn = Bool(desc="If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.")

    #--------------------------------------------------------------------------
    #  Begin "Analog" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "positiveFlowIn",
                label="Attributes"),
            VGroup("Model", "MemberOf_PSR", "MeasurementType", "Terminal", "Unit", "Contain_MeasurementValues",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.Analog",
        title="Analog",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Analog" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AnalogValue" class:
#------------------------------------------------------------------------------

class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue.AnalogValue represents an analog MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Measurement to which this value is connected.Measurement to which this value is connected.
    MemberOf_Measurement = Instance("CPSM.IEC61970.Meas.Analog", allow_none=False,
        desc="Measurement to which this value is connected.Measurement to which this value is connected.",
        transient=True,
        opposite="Contain_MeasurementValues",
        editor=InstanceEditor(name="_analogs"))

    def _get_analogs(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Meas.Analog" ]
        else:
            return []

    _analogs = Property(fget=_get_analogs)

    #--------------------------------------------------------------------------
    #  Begin "AnalogValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "MeasurementValueSource", "MemberOf_Measurement",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.AnalogValue",
        title="AnalogValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Discrete" class:
#------------------------------------------------------------------------------

class Discrete(Measurement):
    """ Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The values connected to this measurement.The values connected to this measurement.
    Contain_MeasurementValues = List(Instance("CPSM.IEC61970.Meas.DiscreteValue"),
        desc="The values connected to this measurement.The values connected to this measurement.")

    #--------------------------------------------------------------------------
    #  Begin "Discrete" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "MemberOf_PSR", "MeasurementType", "Terminal", "Unit", "Contain_MeasurementValues",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Meas.Discrete",
        title="Discrete",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Discrete" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
