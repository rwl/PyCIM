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

""" Contains entities that describe dynamic measurement data exchanged between applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Core import Equipment
from CIM import Element
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.SCADA import Source



from enthought.traits.api import Instance, List, Property, Enum, Bool, Date, Int, Str, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Validity for MeasurementValue.
Validity = Enum("GOOD", "INVALID", "QUESTIONABLE", desc="Validity for MeasurementValue.")

#------------------------------------------------------------------------------
#  "LimitSet" class:
#------------------------------------------------------------------------------

class LimitSet(IdentifiedObject):
    """ Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.
    isPercentageLimits = Bool(desc="Tells if the limit values are in percentage of normalValue or the specified Unit for Measurements and Controls.")

    #--------------------------------------------------------------------------
    #  Begin "LimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "isPercentageLimits",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.LimitSet",
        title="LimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementValue" class:
#------------------------------------------------------------------------------

class MeasurementValue(IdentifiedObject):
    """ The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlValues = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlValue"))

    # A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
    MeasurementValueSource = Instance("CIM.IEC61970.Meas.MeasurementValueSource",
        desc="A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.",
        transient=True,
        opposite="MeasurementValues",
        editor=InstanceEditor(name="_measurementvaluesources"))

    def _get_measurementvaluesources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.MeasurementValueSource" ]
        else:
            return []

    _measurementvaluesources = Property(fget=_get_measurementvaluesources)

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="MeasurementValues",
        editor=InstanceEditor(name="_erppersons"))

    def _get_erppersons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPerson" ]
        else:
            return []

    _erppersons = Property(fget=_get_erppersons)

    ProcedureDataSets = List(Instance("CIM.IEC61968.Informative.InfAssets.ProcedureDataSet"))

    # Link to the physical telemetered point associated with this measurement.
    RemoteSource = Instance("CIM.IEC61970.SCADA.RemoteSource",
        desc="Link to the physical telemetered point associated with this measurement.",
        transient=True,
        opposite="MeasurementValue",
        editor=InstanceEditor(name="_remotesources"))

    def _get_remotesources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.SCADA.RemoteSource" ]
        else:
            return []

    _remotesources = Property(fget=_get_remotesources)

    # A MeasurementValue has a MeasurementValueQuality associated with it.
    MeasurementValueQuality = Instance("CIM.IEC61970.Meas.MeasurementValueQuality",
        desc="A MeasurementValue has a MeasurementValueQuality associated with it.",
        transient=True,
        opposite="MeasurementValue",
        editor=InstanceEditor(name="_measurementvaluequalitys"))

    def _get_measurementvaluequalitys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.MeasurementValueQuality" ]
        else:
            return []

    _measurementvaluequalitys = Property(fget=_get_measurementvaluequalitys)

    # The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.
    sensorAccuracy = PerCent(desc="The limit, expressed as a percentage of the sensor maximum, that errors will not exceed when the sensor is used under  reference conditions.")

    # The time when the value was last updated
    timeStamp = Date(desc="The time when the value was last updated")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sensorAccuracy", "timeStamp",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlValues", "MeasurementValueSource", "ErpPerson", "ProcedureDataSets", "RemoteSource", "MeasurementValueQuality",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.MeasurementValue",
        title="MeasurementValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ValueAliasSet" class:
#------------------------------------------------------------------------------

class ValueAliasSet(IdentifiedObject):
    """ Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Measurements using the set for translation
    Discretes = List(Instance("CIM.IEC61970.Meas.Discrete"),
        desc="The Measurements using the set for translation")

    # The ValueAliasSet used for translation of a Control value to a name.
    Commands = List(Instance("CIM.IEC61970.Meas.Command"),
        desc="The ValueAliasSet used for translation of a Control value to a name.")

    # The ValueToAlias mappings included in the set
    Values = List(Instance("CIM.IEC61970.Meas.ValueToAlias"),
        desc="The ValueToAlias mappings included in the set")

    #--------------------------------------------------------------------------
    #  Begin "ValueAliasSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Discretes", "Commands", "Values",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.ValueAliasSet",
        title="ValueAliasSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ValueAliasSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PotentialTransformer" class:
#------------------------------------------------------------------------------

class PotentialTransformer(Equipment):
    """ Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PotentialTransformerAsset = Instance("CIM.IEC61968.Informative.InfAssets.PotentialTransformerAsset",
        transient=True,
        opposite="PotentialTransformer",
        editor=InstanceEditor(name="_potentialtransformerassets"))

    def _get_potentialtransformerassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.PotentialTransformerAsset" ]
        else:
            return []

    _potentialtransformerassets = Property(fget=_get_potentialtransformerassets)

    PotentialTransformerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.PotentialTransformerTypeAsset",
        transient=True,
        opposite="PotentialTransformers",
        editor=InstanceEditor(name="_potentialtransformertypeassets"))

    def _get_potentialtransformertypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.PotentialTransformerTypeAsset" ]
        else:
            return []

    _potentialtransformertypeassets = Property(fget=_get_potentialtransformertypeassets)

    # PT accuracy classification.
    accuracyClass = Str(desc="PT accuracy classification.")

    # PT classification.
    ptClass = Str(desc="PT classification.")

    # Nominal ratio between the primary and secondary voltage.
    nominalRatio = Float(desc="Nominal ratio between the primary and secondary voltage.")

    #--------------------------------------------------------------------------
    #  Begin "PotentialTransformer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "accuracyClass", "ptClass", "nominalRatio",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "PotentialTransformerAsset", "PotentialTransformerTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Meas.PotentialTransformer",
        title="PotentialTransformer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PotentialTransformer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Limit" class:
#------------------------------------------------------------------------------

class Limit(IdentifiedObject):
    """ Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Procedures = List(Instance("CIM.IEC61968.Informative.InfAssets.Procedure"))

    #--------------------------------------------------------------------------
    #  Begin "Limit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Procedures",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.Limit",
        title="Limit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Limit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Measurement" class:
#------------------------------------------------------------------------------

class Measurement(IdentifiedObject):
    """ A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_assets"))

    def _get_assets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.Asset" ]
        else:
            return []

    _assets = Property(fget=_get_assets)

    # A measurement is made on the A side of a tie point
    For_TiePoint = Instance("CIM.IEC61968.Informative.Reservation.TiePoint",
        desc="A measurement is made on the A side of a tie point",
        transient=True,
        opposite="For_Measurements",
        editor=InstanceEditor(name="_tiepoints"))

    def _get_tiepoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Reservation.TiePoint" ]
        else:
            return []

    _tiepoints = Property(fget=_get_tiepoints)

    # The PowerSystemResource that contains the Measurement in the naming hierarchy
    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        desc="The PowerSystemResource that contains the Measurement in the naming hierarchy",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    # A measurement is a data source for dynamic interchange schedules
    DynamicSchedules = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.DynamicSchedule"),
        desc="A measurement is a data source for dynamic interchange schedules")

    Pnode = Instance("CIM.IEC61968.Informative.MarketOperations.Pnode",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_pnodes"))

    def _get_pnodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.MarketOperations.Pnode" ]
        else:
            return []

    _pnodes = Property(fget=_get_pnodes)

    # One or more measurements may be associated with a terminal in the network
    Terminal = Instance("CIM.IEC61970.Core.Terminal",
        desc="One or more measurements may be associated with a terminal in the network",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # Measurements are specified in types of documents, such as procedures.
    Documents = List(Instance("CIM.IEC61968.Common.Document"),
        desc="Measurements are specified in types of documents, such as procedures.")

    Locations = List(Instance("CIM.IEC61968.Common.Location"))

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    ViolationLimits = List(Instance("CIM.IEC61968.Informative.MarketOperations.ViolationLimit"))

    # A measurement is made on the B side of a tie point
    By_TiePoint = Instance("CIM.IEC61968.Informative.Reservation.TiePoint",
        desc="A measurement is made on the B side of a tie point",
        transient=True,
        opposite="By_Measurements",
        editor=InstanceEditor(name="_tiepoints"))

    def _get_tiepoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Reservation.TiePoint" ]
        else:
            return []

    _tiepoints = Property(fget=_get_tiepoints)

    # The Unit for the Measurement
    Unit = Instance("CIM.IEC61970.Core.Unit",
        desc="The Unit for the Measurement",
        transient=True,
        opposite="Measurements",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    # Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc.
    measurementType = Str(desc="Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc.")

    #--------------------------------------------------------------------------
    #  Begin "Measurement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "measurementType",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Asset", "For_TiePoint", "PowerSystemResource", "DynamicSchedules", "Pnode", "Terminal", "Documents", "Locations", "ChangeItems", "ViolationLimits", "By_TiePoint", "Unit",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Meas.Measurement",
        title="Measurement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Measurement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Control" class:
#------------------------------------------------------------------------------

class Control(IdentifiedObject):
    """ Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The remote point controlling the physical actuator.
    RemoteControl = Instance("CIM.IEC61970.SCADA.RemoteControl",
        desc="The remote point controlling the physical actuator.",
        transient=True,
        opposite="Control",
        editor=InstanceEditor(name="_remotecontrols"))

    def _get_remotecontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.SCADA.RemoteControl" ]
        else:
            return []

    _remotecontrols = Property(fget=_get_remotecontrols)

    # The Unit for the Control.
    Unit = Instance("CIM.IEC61970.Core.Unit",
        desc="The Unit for the Control.",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    # Regulating device governed by this control output.
    RegulatingCondEq = Instance("CIM.IEC61970.Wires.RegulatingCondEq",
        desc="Regulating device governed by this control output.",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_regulatingcondeqs"))

    def _get_regulatingcondeqs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.RegulatingCondEq" ]
        else:
            return []

    _regulatingcondeqs = Property(fget=_get_regulatingcondeqs)

    # The type of Control
    ControlType = Instance("CIM.IEC61970.Meas.ControlType",
        desc="The type of Control",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_controltypes"))

    def _get_controltypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.ControlType" ]
        else:
            return []

    _controltypes = Property(fget=_get_controltypes)

    # The last time a control output was sent
    timeStamp = Date(desc="The last time a control output was sent")

    # Indicates that a client is currently sending control commands that has not completed
    operationInProgress = Bool(desc="Indicates that a client is currently sending control commands that has not completed")

    #--------------------------------------------------------------------------
    #  Begin "Control" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "timeStamp", "operationInProgress",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "RemoteControl", "Unit", "RegulatingCondEq", "ControlType",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.Control",
        title="Control",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Control" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ValueToAlias" class:
#------------------------------------------------------------------------------

class ValueToAlias(IdentifiedObject):
    """ Describes the translation of one particular value into a name, e.g. 1->'Open'
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The ValueAliasSet having the ValueToAlias mappings
    ValueAliasSet = Instance("CIM.IEC61970.Meas.ValueAliasSet",
        desc="The ValueAliasSet having the ValueToAlias mappings",
        transient=True,
        opposite="Values",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.ValueAliasSet" ]
        else:
            return []

    _valuealiassets = Property(fget=_get_valuealiassets)

    # The value that is mapped
    value = Int(desc="The value that is mapped")

    #--------------------------------------------------------------------------
    #  Begin "ValueToAlias" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ValueAliasSet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.ValueToAlias",
        title="ValueToAlias",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ValueToAlias" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Quality61850" class:
#------------------------------------------------------------------------------

class Quality61850(Element):
    """ Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.
    source = Source(desc="Source gives information related to the origin of a value. The value may be acquired from the process, defaulted or substituted.")

    # Validity of the measurement value.
    validity = Validity(desc="Validity of the measurement value.")

    # Measurement value is transmitted for test purposes.
    test = Bool(desc="Measurement value is transmitted for test purposes.")

    # Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.
    overFlow = Bool(desc="Measurement value is beyond the capability of being  represented properly. For example, a counter value overflows from maximum count back to a value of zero.")

    # Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.
    estimatorReplaced = Bool(desc="Value has been replaced by State Estimator. estimatorReplaced is not an IEC61850 quality bit but has been put in this class for convenience.")

    # A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.
    suspect = Bool(desc="A correlation function has detected that the value is not consitent with other values. Typically set by a network State Estimator.")

    # Measurement value may be incorrect due to a reference being out of calibration.
    badReference = Bool(desc="Measurement value may be incorrect due to a reference being out of calibration.")

    # Measurement value is blocked and hence unavailable for transmission.
    operatorBlocked = Bool(desc="Measurement value is blocked and hence unavailable for transmission.")

    # To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).
    oscillatory = Bool(desc="To prevent some overload of the communication it is sensible to detect and suppress oscillating (fast changing) binary inputs. If a signal changes in a defined time (tosc) twice in the same direction (from 0 to 1 or from 1 to 0) then oscillation is detected and the detail quality identifier 'oscillatory' is set. If it is detected a configured numbers of transient changes could be passed by. In this time the validity status 'questionable' is set. If after this defined numbers of changes the signal is still in the oscillating state the value shall be set either to the opposite state of the previous stable value or to a defined default value. In this case the validity status 'questionable' is reset and 'invalid' is set as long as the signal is oscillating. If it is configured such that no transient changes should be passed by then the validity status 'invalid' is set immediately in addition to the detail quality identifier 'oscillatory' (used for status information only).")

    # This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.
    failure = Bool(desc="This identifier indicates that a supervision function has detected an internal or external failure, e.g. communication failure.")

    # Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.
    oldData = Bool(desc="Measurement value is old and possibly invalid, as it has not been successfully updated during a specified time interval.")

    # Measurement value is beyond a predefined range of value.
    outOfRange = Bool(desc="Measurement value is beyond a predefined range of value.")

    #--------------------------------------------------------------------------
    #  Begin "Quality61850" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "source", "validity", "test", "overFlow", "estimatorReplaced", "suspect", "badReference", "operatorBlocked", "oscillatory", "failure", "oldData", "outOfRange",
                label="Attributes", columns=1),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.Quality61850",
        title="Quality61850",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Quality61850" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementValueSource" class:
#------------------------------------------------------------------------------

class MeasurementValueSource(IdentifiedObject):
    """ MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The MeasurementValues updated by the source
    MeasurementValues = List(Instance("CIM.IEC61970.Meas.MeasurementValue"),
        desc="The MeasurementValues updated by the source")

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueSource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MeasurementValues",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.MeasurementValueSource",
        title="MeasurementValueSource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValueSource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentTransformer" class:
#------------------------------------------------------------------------------

class CurrentTransformer(Equipment):
    """ Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CurrentTransformerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.CurrentTransformerTypeAsset",
        transient=True,
        opposite="CurrentTransformers",
        editor=InstanceEditor(name="_currenttransformertypeassets"))

    def _get_currenttransformertypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.CurrentTransformerTypeAsset" ]
        else:
            return []

    _currenttransformertypeassets = Property(fget=_get_currenttransformertypeassets)

    CurrentTransformerAsset = Instance("CIM.IEC61968.Informative.InfAssets.CurrentTransformerAsset",
        transient=True,
        opposite="CurrentTransformer",
        editor=InstanceEditor(name="_currenttransformerassets"))

    def _get_currenttransformerassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.CurrentTransformerAsset" ]
        else:
            return []

    _currenttransformerassets = Property(fget=_get_currenttransformerassets)

    # CT accuracy classification.
    accuracyClass = Str(desc="CT accuracy classification.")

    # Percent of rated current for which the CT remains accurate within specified limits.
    accuracyLimit = Str(desc="Percent of rated current for which the CT remains accurate within specified limits.")

    # Intended usage of the CT; i.e. metering, protection.
    usage = Str(desc="Intended usage of the CT; i.e. metering, protection.")

    # Number of cores.
    coreCount = Int(desc="Number of cores.")

    # For multi-ratio CT's, the maximum permissable ratio attainable.
    maxRatio = Float(desc="For multi-ratio CT's, the maximum permissable ratio attainable.")

    # CT classification; i.e. class 10P.
    ctClass = Str(desc="CT classification; i.e. class 10P.")

    #--------------------------------------------------------------------------
    #  Begin "CurrentTransformer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "accuracyClass", "accuracyLimit", "usage", "coreCount", "maxRatio", "ctClass",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "CurrentTransformerTypeAsset", "CurrentTransformerAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Meas.CurrentTransformer",
        title="CurrentTransformer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentTransformer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ControlType" class:
#------------------------------------------------------------------------------

class ControlType(IdentifiedObject):
    """ Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Controls having the ControlType
    Controls = List(Instance("CIM.IEC61970.Meas.Control"),
        desc="The Controls having the ControlType")

    #--------------------------------------------------------------------------
    #  Begin "ControlType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Controls",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.ControlType",
        title="ControlType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccumulatorLimitSet" class:
#------------------------------------------------------------------------------

class AccumulatorLimitSet(LimitSet):
    """ An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Measurements using the LimitSet.
    Measurements = List(Instance("CIM.IEC61970.Meas.Accumulator"),
        desc="The Measurements using the LimitSet.")

    # The limit values used for supervision of Measurements.
    Limits = List(Instance("CIM.IEC61970.Meas.AccumulatorLimit"),
        desc="The limit values used for supervision of Measurements.")

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "isPercentageLimits",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Limits",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.AccumulatorLimitSet",
        title="AccumulatorLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorLimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AnalogLimitSet" class:
#------------------------------------------------------------------------------

class AnalogLimitSet(LimitSet):
    """ An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The limit values used for supervision of Measurements.
    Limits = List(Instance("CIM.IEC61970.Meas.AnalogLimit"),
        desc="The limit values used for supervision of Measurements.")

    # The Measurements using the LimitSet.
    Measurements = List(Instance("CIM.IEC61970.Meas.Analog"),
        desc="The Measurements using the LimitSet.")

    #--------------------------------------------------------------------------
    #  Begin "AnalogLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "isPercentageLimits",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Limits", "Measurements",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.AnalogLimitSet",
        title="AnalogLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogLimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccumulatorValue" class:
#------------------------------------------------------------------------------

class AccumulatorValue(MeasurementValue):
    """ AccumulatorValue represents a accumulated (counted) MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Measurement to which this value is connected.
    Accumulator = Instance("CIM.IEC61970.Meas.Accumulator",
        desc="Measurement to which this value is connected.",
        transient=True,
        opposite="AccumulatorValues",
        editor=InstanceEditor(name="_accumulators"))

    def _get_accumulators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Accumulator" ]
        else:
            return []

    _accumulators = Property(fget=_get_accumulators)

    # The value to supervise. The value is positive.
    value = Int(desc="The value to supervise. The value is positive.")

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlValues", "MeasurementValueSource", "ErpPerson", "ProcedureDataSets", "RemoteSource", "MeasurementValueQuality", "Accumulator",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.AccumulatorValue",
        title="AccumulatorValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccumulatorLimit" class:
#------------------------------------------------------------------------------

class AccumulatorLimit(Limit):
    """ Limit values for Accumulator measurements
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The set of limits.
    LimitSet = Instance("CIM.IEC61970.Meas.AccumulatorLimitSet",
        desc="The set of limits.",
        transient=True,
        opposite="Limits",
        editor=InstanceEditor(name="_accumulatorlimitsets"))

    def _get_accumulatorlimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.AccumulatorLimitSet" ]
        else:
            return []

    _accumulatorlimitsets = Property(fget=_get_accumulatorlimitsets)

    # The value to supervise against. The value is positive.
    value = Int(desc="The value to supervise against. The value is positive.")

    #--------------------------------------------------------------------------
    #  Begin "AccumulatorLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Procedures", "LimitSet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.AccumulatorLimit",
        title="AccumulatorLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccumulatorLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Analog" class:
#------------------------------------------------------------------------------

class Analog(Measurement):
    """ Analog represents an analog Measurement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The values connected to this measurement.
    AnalogValues = List(Instance("CIM.IEC61970.Meas.AnalogValue"),
        desc="The values connected to this measurement.")

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("CIM.IEC61970.Meas.AnalogLimitSet"),
        desc="A measurement may have zero or more limit ranges defined for it.")

    # The Control variable associated with the Measurement
    SetPoint = Instance("CIM.IEC61970.Meas.SetPoint",
        desc="The Control variable associated with the Measurement",
        transient=True,
        opposite="Analog",
        editor=InstanceEditor(name="_setpoints"))

    def _get_setpoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.SetPoint" ]
        else:
            return []

    _setpoints = Property(fget=_get_setpoints)

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Float(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    # If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.
    positiveFlowIn = Bool(desc="If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource.")

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = Float(desc="Normal measurement value, e.g., used for percentage calculations.")

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = Float(desc="Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values")

    #--------------------------------------------------------------------------
    #  Begin "Analog" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "measurementType", "maxValue", "positiveFlowIn", "normalValue", "minValue",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Asset", "For_TiePoint", "PowerSystemResource", "DynamicSchedules", "Pnode", "Terminal", "Documents", "Locations", "ChangeItems", "ViolationLimits", "By_TiePoint", "Unit", "AnalogValues", "LimitSets", "SetPoint",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Meas.Analog",
        title="Analog",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Analog" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SetPoint" class:
#------------------------------------------------------------------------------

class SetPoint(Control):
    """ A SetPoint is an analog control used for supervisory control.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Measurement variable used for control
    Analog = Instance("CIM.IEC61970.Meas.Analog",
        desc="The Measurement variable used for control",
        transient=True,
        opposite="SetPoint",
        editor=InstanceEditor(name="_analogs"))

    def _get_analogs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Analog" ]
        else:
            return []

    _analogs = Property(fget=_get_analogs)

    # Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    minValue = Float(desc="Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs.")

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = Float(desc="Normal value for Control.value e.g. used for percentage scaling")

    # The value representing the actuator output
    value = Float(desc="The value representing the actuator output")

    # Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.
    maxValue = Float(desc="Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs.")

    #--------------------------------------------------------------------------
    #  Begin "SetPoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "timeStamp", "operationInProgress", "minValue", "normalValue", "value", "maxValue",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "RemoteControl", "Unit", "RegulatingCondEq", "ControlType", "Analog",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.SetPoint",
        title="SetPoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SetPoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AnalogLimit" class:
#------------------------------------------------------------------------------

class AnalogLimit(Limit):
    """ Limit values for Analog measurements
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The set of limits.
    LimitSet = Instance("CIM.IEC61970.Meas.AnalogLimitSet",
        desc="The set of limits.",
        transient=True,
        opposite="Limits",
        editor=InstanceEditor(name="_analoglimitsets"))

    def _get_analoglimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.AnalogLimitSet" ]
        else:
            return []

    _analoglimitsets = Property(fget=_get_analoglimitsets)

    # The value to supervise against.
    value = Float(desc="The value to supervise against.")

    #--------------------------------------------------------------------------
    #  Begin "AnalogLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Procedures", "LimitSet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.AnalogLimit",
        title="AnalogLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Discrete" class:
#------------------------------------------------------------------------------

class Discrete(Measurement):
    """ Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Control variable associated with the Measurement.
    Command = Instance("CIM.IEC61970.Meas.Command",
        desc="The Control variable associated with the Measurement.",
        transient=True,
        opposite="Discrete",
        editor=InstanceEditor(name="_commands"))

    def _get_commands(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Command" ]
        else:
            return []

    _commands = Property(fget=_get_commands)

    # The ValueAliasSet used for translation of a MeasurementValue.value to a name
    ValueAliasSet = Instance("CIM.IEC61970.Meas.ValueAliasSet",
        desc="The ValueAliasSet used for translation of a MeasurementValue.value to a name",
        transient=True,
        opposite="Discretes",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.ValueAliasSet" ]
        else:
            return []

    _valuealiassets = Property(fget=_get_valuealiassets)

    # The values connected to this measurement.
    DiscreteValues = List(Instance("CIM.IEC61970.Meas.DiscreteValue"),
        desc="The values connected to this measurement.")

    # Normal measurement value, e.g., used for percentage calculations.
    normalValue = Int(desc="Normal measurement value, e.g., used for percentage calculations.")

    # Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values
    minValue = Int(desc="Normal value range minimum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values")

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Int(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    #--------------------------------------------------------------------------
    #  Begin "Discrete" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "measurementType", "normalValue", "minValue", "maxValue",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Asset", "For_TiePoint", "PowerSystemResource", "DynamicSchedules", "Pnode", "Terminal", "Documents", "Locations", "ChangeItems", "ViolationLimits", "By_TiePoint", "Unit", "Command", "ValueAliasSet", "DiscreteValues",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Meas.Discrete",
        title="Discrete",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Discrete" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Accumulator" class:
#------------------------------------------------------------------------------

class Accumulator(Measurement):
    """ Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The values connected to this measurement.
    AccumulatorValues = List(Instance("CIM.IEC61970.Meas.AccumulatorValue"),
        desc="The values connected to this measurement.")

    # A measurement may have zero or more limit ranges defined for it.
    LimitSets = List(Instance("CIM.IEC61970.Meas.AccumulatorLimitSet"),
        desc="A measurement may have zero or more limit ranges defined for it.")

    # Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.
    maxValue = Int(desc="Normal value range maximum for any of the MeasurementValue.values. Used for scaling, e.g. in bar graphs or of telemetered raw values.")

    #--------------------------------------------------------------------------
    #  Begin "Accumulator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "measurementType", "maxValue",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Asset", "For_TiePoint", "PowerSystemResource", "DynamicSchedules", "Pnode", "Terminal", "Documents", "Locations", "ChangeItems", "ViolationLimits", "By_TiePoint", "Unit", "AccumulatorValues", "LimitSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Meas.Accumulator",
        title="Accumulator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Accumulator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StringMeasurementValue" class:
#------------------------------------------------------------------------------

class StringMeasurementValue(MeasurementValue):
    """ StringMeasurementValue represents a measurement value of type string.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Measurement to which this value is connected.
    StringMeasurement = Instance("CIM.IEC61970.Meas.StringMeasurement",
        desc="Measurement to which this value is connected.",
        transient=True,
        opposite="StringMeasurementValues",
        editor=InstanceEditor(name="_stringmeasurements"))

    def _get_stringmeasurements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.StringMeasurement" ]
        else:
            return []

    _stringmeasurements = Property(fget=_get_stringmeasurements)

    # The value to supervise.
    value = Str(desc="The value to supervise.")

    #--------------------------------------------------------------------------
    #  Begin "StringMeasurementValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlValues", "MeasurementValueSource", "ErpPerson", "ProcedureDataSets", "RemoteSource", "MeasurementValueQuality", "StringMeasurement",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.StringMeasurementValue",
        title="StringMeasurementValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StringMeasurementValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Command" class:
#------------------------------------------------------------------------------

class Command(Control):
    """ A Command is a discrete control used for supervisory control.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Measurement variable used for control.
    Discrete = Instance("CIM.IEC61970.Meas.Discrete",
        desc="The Measurement variable used for control.",
        transient=True,
        opposite="Command",
        editor=InstanceEditor(name="_discretes"))

    def _get_discretes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Discrete" ]
        else:
            return []

    _discretes = Property(fget=_get_discretes)

    # The Commands using the set for translation.
    ValueAliasSet = Instance("CIM.IEC61970.Meas.ValueAliasSet",
        desc="The Commands using the set for translation.",
        transient=True,
        opposite="Commands",
        editor=InstanceEditor(name="_valuealiassets"))

    def _get_valuealiassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.ValueAliasSet" ]
        else:
            return []

    _valuealiassets = Property(fget=_get_valuealiassets)

    # Normal value for Control.value e.g. used for percentage scaling
    normalValue = Int(desc="Normal value for Control.value e.g. used for percentage scaling")

    # The value representing the actuator output
    value = Int(desc="The value representing the actuator output")

    #--------------------------------------------------------------------------
    #  Begin "Command" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "timeStamp", "operationInProgress", "normalValue", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "RemoteControl", "Unit", "RegulatingCondEq", "ControlType", "Discrete", "ValueAliasSet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.Command",
        title="Command",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Command" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DiscreteValue" class:
#------------------------------------------------------------------------------

class DiscreteValue(MeasurementValue):
    """ DiscreteValue represents a discrete MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Measurement to which this value is connected.
    Discrete = Instance("CIM.IEC61970.Meas.Discrete",
        desc="Measurement to which this value is connected.",
        transient=True,
        opposite="DiscreteValues",
        editor=InstanceEditor(name="_discretes"))

    def _get_discretes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Discrete" ]
        else:
            return []

    _discretes = Property(fget=_get_discretes)

    # The value to supervise.
    value = Int(desc="The value to supervise.")

    #--------------------------------------------------------------------------
    #  Begin "DiscreteValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlValues", "MeasurementValueSource", "ErpPerson", "ProcedureDataSets", "RemoteSource", "MeasurementValueQuality", "Discrete",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.DiscreteValue",
        title="DiscreteValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DiscreteValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeasurementValueQuality" class:
#------------------------------------------------------------------------------

class MeasurementValueQuality(Quality61850):
    """ Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A MeasurementValue has a MeasurementValueQuality associated with it.
    MeasurementValue = Instance("CIM.IEC61970.Meas.MeasurementValue",
        desc="A MeasurementValue has a MeasurementValueQuality associated with it.",
        transient=True,
        opposite="MeasurementValueQuality",
        editor=InstanceEditor(name="_measurementvalues"))

    def _get_measurementvalues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.MeasurementValue" ]
        else:
            return []

    _measurementvalues = Property(fget=_get_measurementvalues)

    #--------------------------------------------------------------------------
    #  Begin "MeasurementValueQuality" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "source", "validity", "test", "overFlow", "estimatorReplaced", "suspect", "badReference", "operatorBlocked", "oscillatory", "failure", "oldData", "outOfRange",
                label="Attributes", columns=1),
            VGroup("Parent", "MeasurementValue",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Meas.MeasurementValueQuality",
        title="MeasurementValueQuality",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeasurementValueQuality" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AnalogValue" class:
#------------------------------------------------------------------------------

class AnalogValue(MeasurementValue):
    """ AnalogValue represents an analog MeasurementValue.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The usage of the measurement within the control area specification.
    AltTieMeas = List(Instance("CIM.IEC61970.ControlArea.AltTieMeas"),
        desc="The usage of the measurement within the control area specification.")

    # Measurement to which this value is connected.
    Analog = Instance("CIM.IEC61970.Meas.Analog",
        desc="Measurement to which this value is connected.",
        transient=True,
        opposite="AnalogValues",
        editor=InstanceEditor(name="_analogs"))

    def _get_analogs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.Analog" ]
        else:
            return []

    _analogs = Property(fget=_get_analogs)

    # The alternate generating unit for which this measurement value applies.
    AltGeneratingUnit = List(Instance("CIM.IEC61970.ControlArea.AltGeneratingUnitMeas"),
        desc="The alternate generating unit for which this measurement value applies.")

    # The value to supervise.
    value = Float(desc="The value to supervise.")

    #--------------------------------------------------------------------------
    #  Begin "AnalogValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlValues", "MeasurementValueSource", "ErpPerson", "ProcedureDataSets", "RemoteSource", "MeasurementValueQuality", "AltTieMeas", "Analog", "AltGeneratingUnit",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Meas.AnalogValue",
        title="AnalogValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AnalogValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StringMeasurement" class:
#------------------------------------------------------------------------------

class StringMeasurement(Measurement):
    """ StringMeasurement represents a measurement with values of type string.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The values connected to this measurement.
    StringMeasurementValues = List(Instance("CIM.IEC61970.Meas.StringMeasurementValue"),
        desc="The values connected to this measurement.")

    #--------------------------------------------------------------------------
    #  Begin "StringMeasurement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "measurementType",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Asset", "For_TiePoint", "PowerSystemResource", "DynamicSchedules", "Pnode", "Terminal", "Documents", "Locations", "ChangeItems", "ViolationLimits", "By_TiePoint", "Unit", "StringMeasurementValues",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61970.Meas.StringMeasurement",
        title="StringMeasurement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StringMeasurement" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
