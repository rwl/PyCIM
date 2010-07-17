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

""" Contains only diagrams to be discussed with WG13, for consolidating T&amp;D models.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Core import ConductingEquipment
from CIM.IEC61970.Core import Equipment
from CIM.IEC61970.Wires import ACLineSegment
from CIM.IEC61970.Wires import RatioTapChanger
from CIM import Element
from CIM.IEC61970.Domain import Reactance
from CIM.IEC61970.Domain import Resistance
from CIM.IEC61970.Domain import Susceptance
from CIM.IEC61970.Domain import Conductance
from CIM.IEC61970.Core import PhaseCode
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import CurrentFlow



from enthought.traits.api import Instance, List, Property, Int, Bool, Str, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "PerLengthPhaseImpedance" class:
#------------------------------------------------------------------------------

class PerLengthPhaseImpedance(IdentifiedObject):
    """ Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All data that belong to this conductor phase impedance.
    PhaseImpedanceData = List(Instance("CIM.IEC61968.WiresExt.PhaseImpedanceData"),
        desc="All data that belong to this conductor phase impedance.")

    # All conductor segments described by this phase impedance.
    ConductorSegments = List(Instance("CIM.IEC61968.WiresExt.DistributionLineSegment"),
        desc="All conductor segments described by this phase impedance.")

    # Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix.
    conductorCount = Int(desc="Number of phase, neutral, and other wires retained. Constrains the number of matrix elements and the phase codes that can be used with this matrix.")

    #--------------------------------------------------------------------------
    #  Begin "PerLengthPhaseImpedance" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "conductorCount",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PhaseImpedanceData", "ConductorSegments",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.PerLengthPhaseImpedance",
        title="PerLengthPhaseImpedance",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PerLengthPhaseImpedance" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DistributionTransformerWinding" class:
#------------------------------------------------------------------------------

class DistributionTransformerWinding(ConductingEquipment):
    """ Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. - 'windingType' attribute is replaced by 'sequenceNumber' attribute on WindingInfo class. - all the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    FromWindingInsulations = List(Instance("CIM.IEC61968.Informative.InfAssets.WindingInsulation"))

    # (accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.
    PiImpedance = Instance("CIM.IEC61968.WiresExt.WindingPiImpedance",
        desc="(accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.",
        transient=True,
        opposite="Windings",
        editor=InstanceEditor(name="_windingpiimpedances"))

    def _get_windingpiimpedances(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.WindingPiImpedance" ]
        else:
            return []

    _windingpiimpedances = Property(fget=_get_windingpiimpedances)

    # Phase tap changer associated with this winding.
    PhaseTapChanger = Instance("CIM.IEC61970.Wires.PhaseTapChanger",
        desc="Phase tap changer associated with this winding.",
        transient=True,
        opposite="Winding",
        editor=InstanceEditor(name="_phasetapchangers"))

    def _get_phasetapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.PhaseTapChanger" ]
        else:
            return []

    _phasetapchangers = Property(fget=_get_phasetapchangers)

    # Ratio tap changer associated with this winding.
    RatioTapChanger = Instance("CIM.IEC61970.Wires.RatioTapChanger",
        desc="Ratio tap changer associated with this winding.",
        transient=True,
        opposite="Winding",
        editor=InstanceEditor(name="_ratiotapchangers"))

    def _get_ratiotapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.RatioTapChanger" ]
        else:
            return []

    _ratiotapchangers = Property(fget=_get_ratiotapchangers)

    # Data for this winding.
    WindingInfo = Instance("CIM.IEC61968.AssetModels.WindingInfo",
        desc="Data for this winding.",
        transient=True,
        opposite="Windings",
        editor=InstanceEditor(name="_windinginfos"))

    def _get_windinginfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.WindingInfo" ]
        else:
            return []

    _windinginfos = Property(fget=_get_windinginfos)

    # Transformer this winding belongs to.
    Transformer = Instance("CIM.IEC61968.WiresExt.DistributionTransformer",
        desc="Transformer this winding belongs to.",
        transient=True,
        opposite="Windings",
        editor=InstanceEditor(name="_distributiontransformers"))

    def _get_distributiontransformers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.DistributionTransformer" ]
        else:
            return []

    _distributiontransformers = Property(fget=_get_distributiontransformers)

    ToWindingInsulations = List(Instance("CIM.IEC61968.Informative.InfAssets.WindingInsulation"))

    # (for Yn and Zn connections) True if the neutral is solidly grounded.
    grounded = Bool(desc="(for Yn and Zn connections) True if the neutral is solidly grounded.")

    # (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true.
    xground = Reactance(desc="(for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true.")

    # (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true.
    rground = Resistance(desc="(for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true.")

    #--------------------------------------------------------------------------
    #  Begin "DistributionTransformerWinding" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "grounded", "xground", "rground",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "FromWindingInsulations", "PiImpedance", "PhaseTapChanger", "RatioTapChanger", "WindingInfo", "Transformer", "ToWindingInsulations",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.DistributionTransformerWinding",
        title="DistributionTransformerWinding",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DistributionTransformerWinding" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WindingPiImpedance" class:
#------------------------------------------------------------------------------

class WindingPiImpedance(IdentifiedObject):
    """ Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All windings having this Pi impedance.
    Windings = List(Instance("CIM.IEC61968.WiresExt.DistributionTransformerWinding"),
        desc="All windings having this Pi impedance.")

    # Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.
    x = Reactance(desc="Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.")

    # Zero sequence series resistance of the winding.
    r0 = Resistance(desc="Zero sequence series resistance of the winding.")

    # Zero sequence magnetizing branch susceptance.
    b0 = Susceptance(desc="Zero sequence magnetizing branch susceptance.")

    # Magnetizing branch conductance (G mag).
    g = Conductance(desc="Magnetizing branch conductance (G mag).")

    # Zero sequence magnetizing branch conductance.
    g0 = Conductance(desc="Zero sequence magnetizing branch conductance.")

    # Zero sequence series reactance of the winding.
    x0 = Reactance(desc="Zero sequence series reactance of the winding.")

    # Magnetizing branch susceptance (B mag).  The value can be positive or negative.
    b = Susceptance(desc="Magnetizing branch susceptance (B mag).  The value can be positive or negative.")

    # DC resistance of the winding.
    r = Resistance(desc="DC resistance of the winding.")

    #--------------------------------------------------------------------------
    #  Begin "WindingPiImpedance" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "x", "r0", "b0", "g", "g0", "x0", "b", "r",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Windings",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.WindingPiImpedance",
        title="WindingPiImpedance",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindingPiImpedance" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DistributionTransformer" class:
#------------------------------------------------------------------------------

class DistributionTransformer(Equipment):
    """ An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Transformer data.
    TransformerInfo = Instance("CIM.IEC61968.AssetModels.TransformerInfo",
        desc="Transformer data.",
        transient=True,
        opposite="Transformers",
        editor=InstanceEditor(name="_transformerinfos"))

    def _get_transformerinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.TransformerInfo" ]
        else:
            return []

    _transformerinfos = Property(fget=_get_transformerinfos)

    TransformerObservations = List(Instance("CIM.IEC61968.Informative.InfAssets.TransformerObservation"))

    # All windings of this transformer.
    Windings = List(Instance("CIM.IEC61968.WiresExt.DistributionTransformerWinding"),
        desc="All windings of this transformer.")

    # Bank this transformer belongs to.
    TransformerBank = Instance("CIM.IEC61968.WiresExt.TransformerBank",
        desc="Bank this transformer belongs to.",
        transient=True,
        opposite="Transformers",
        editor=InstanceEditor(name="_transformerbanks"))

    def _get_transformerbanks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.TransformerBank" ]
        else:
            return []

    _transformerbanks = Property(fget=_get_transformerbanks)

    #--------------------------------------------------------------------------
    #  Begin "DistributionTransformer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "TransformerInfo", "TransformerObservations", "Windings", "TransformerBank",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.DistributionTransformer",
        title="DistributionTransformer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DistributionTransformer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DistributionLineSegment" class:
#------------------------------------------------------------------------------

class DistributionLineSegment(ACLineSegment):
    """ Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Conductor data of this conductor segment.
    ConductorInfo = Instance("CIM.IEC61968.AssetModels.ConductorInfo",
        desc="Conductor data of this conductor segment.",
        transient=True,
        opposite="ConductorSegments",
        editor=InstanceEditor(name="_conductorinfos"))

    def _get_conductorinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.ConductorInfo" ]
        else:
            return []

    _conductorinfos = Property(fget=_get_conductorinfos)

    # Sequence impedance of this conductor segment; used for balanced model.
    SequenceImpedance = Instance("CIM.IEC61968.WiresExt.PerLengthSequenceImpedance",
        desc="Sequence impedance of this conductor segment; used for balanced model.",
        transient=True,
        opposite="ConductorSegments",
        editor=InstanceEditor(name="_perlengthsequenceimpedances"))

    def _get_perlengthsequenceimpedances(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.PerLengthSequenceImpedance" ]
        else:
            return []

    _perlengthsequenceimpedances = Property(fget=_get_perlengthsequenceimpedances)

    # Phase impedance of this conductor segment; used for unbalanced model.
    PhaseImpedance = Instance("CIM.IEC61968.WiresExt.PerLengthPhaseImpedance",
        desc="Phase impedance of this conductor segment; used for unbalanced model.",
        transient=True,
        opposite="ConductorSegments",
        editor=InstanceEditor(name="_perlengthphaseimpedances"))

    def _get_perlengthphaseimpedances(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.PerLengthPhaseImpedance" ]
        else:
            return []

    _perlengthphaseimpedances = Property(fget=_get_perlengthphaseimpedances)

    ConductorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ConductorAsset"))

    #--------------------------------------------------------------------------
    #  Begin "DistributionLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "length", "bch", "r", "gch", "r0", "b0ch", "x0", "x", "g0ch",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "ConductorInfo", "SequenceImpedance", "PhaseImpedance", "ConductorAssets",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.DistributionLineSegment",
        title="DistributionLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DistributionLineSegment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PerLengthSequenceImpedance" class:
#------------------------------------------------------------------------------

class PerLengthSequenceImpedance(IdentifiedObject):
    """ Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All conductor segments described by this sequence impedance.
    ConductorSegments = List(Instance("CIM.IEC61968.WiresExt.DistributionLineSegment"),
        desc="All conductor segments described by this sequence impedance.")

    # Zero sequence series resistance, per unit of length.
    r0 = Resistance(desc="Zero sequence series resistance, per unit of length.")

    # Positive sequence shunt (charging) susceptance, per unit of length.
    bch = Susceptance(desc="Positive sequence shunt (charging) susceptance, per unit of length.")

    # Positive sequence series reactance, per unit of length.
    x = Reactance(desc="Positive sequence series reactance, per unit of length.")

    # Positive sequence series resistance, per unit of length.
    r = Resistance(desc="Positive sequence series resistance, per unit of length.")

    # Positive sequence shunt (charging) conductance, per unit of length.
    gch = Conductance(desc="Positive sequence shunt (charging) conductance, per unit of length.")

    # Zero sequence series reactance, per unit of length.
    x0 = Reactance(desc="Zero sequence series reactance, per unit of length.")

    # Zero sequence shunt (charging) susceptance, per unit of length.
    b0ch = Susceptance(desc="Zero sequence shunt (charging) susceptance, per unit of length.")

    # Zero sequence shunt (charging) conductance, per unit of length.
    g0ch = Conductance(desc="Zero sequence shunt (charging) conductance, per unit of length.")

    #--------------------------------------------------------------------------
    #  Begin "PerLengthSequenceImpedance" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "r0", "bch", "x", "r", "gch", "x0", "b0ch", "g0ch",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ConductorSegments",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.PerLengthSequenceImpedance",
        title="PerLengthSequenceImpedance",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PerLengthSequenceImpedance" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerBank" class:
#------------------------------------------------------------------------------

class TransformerBank(Equipment):
    """ An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All transformers that belong to this bank.
    Transformers = List(Instance("CIM.IEC61968.WiresExt.DistributionTransformer"),
        desc="All transformers that belong to this bank.")

    # Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections.
    vectorGroup = Str(desc="Vector group of the bank for protective relaying, e.g., Dyn1. For unbalanced transformers, this may not be simply determined from the constituent winding connections.")

    #--------------------------------------------------------------------------
    #  Begin "TransformerBank" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "vectorGroup",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Transformers",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.TransformerBank",
        title="TransformerBank",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerBank" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DistributionTapChanger" class:
#------------------------------------------------------------------------------

class DistributionTapChanger(RatioTapChanger):
    """ Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Phase voltage controlling this regulator, measured at regulator location.
    monitoredPhase = PhaseCode(desc="Phase voltage controlling this regulator, measured at regulator location.")

    # Target voltage on the PT secondary base.
    targetVoltage = Voltage(desc="Target voltage on the PT secondary base.")

    # Line drop compensator resistance setting for reverse power flow.
    reverseLineDropR = Resistance(desc="Line drop compensator resistance setting for reverse power flow.")

    # Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection.
    limitVoltage = Voltage(desc="Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection.")

    # Line drop compensator reactance setting for reverse power flow.
    reverseLineDropX = Reactance(desc="Line drop compensator reactance setting for reverse power flow.")

    # Line drop compensator resistance setting for normal (forward) power flow.
    lineDropR = Resistance(desc="Line drop compensator resistance setting for normal (forward) power flow.")

    # If true, the line drop compensation is to be applied.
    lineDropCompensation = Bool(desc="If true, the line drop compensation is to be applied.")

    # Line drop compensator reactance setting for normal (forward) power flow.
    lineDropX = Reactance(desc="Line drop compensator reactance setting for normal (forward) power flow.")

    # Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'.
    bandVoltage = Voltage(desc="Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'.")

    # Built-in current transformer primary rating.
    ctRating = CurrentFlow(desc="Built-in current transformer primary rating.")

    # Built-in voltage transducer ratio.
    ptRatio = Float(desc="Built-in voltage transducer ratio.")

    # Built-in current transducer ratio.
    ctRatio = Float(desc="Built-in current transducer ratio.")

    #--------------------------------------------------------------------------
    #  Begin "DistributionTapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "neutralStep", "subsequentDelay", "neutralU", "stepVoltageIncrement", "lowStep", "normalStep", "regulationStatus", "highStep", "initialDelay", "ltcFlag", "tculControlMode", "monitoredPhase", "targetVoltage", "reverseLineDropR", "limitVoltage", "reverseLineDropX", "lineDropR", "lineDropCompensation", "lineDropX", "bandVoltage", "ctRating", "ptRatio", "ctRatio",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "RegulatingControl", "ImpedanceVariationCurve", "SvTapStep", "TapSchedules", "Winding", "RatioVariationCurve", "TransformerWinding",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.DistributionTapChanger",
        title="DistributionTapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DistributionTapChanger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PhaseImpedanceData" class:
#------------------------------------------------------------------------------

class PhaseImpedanceData(Element):
    """ Triplet of resistance, reactance, and susceptance matrix element values.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Conductor phase impedance to which this data belongs.
    PhaseImpedance = Instance("CIM.IEC61968.WiresExt.PerLengthPhaseImpedance",
        desc="Conductor phase impedance to which this data belongs.",
        transient=True,
        opposite="PhaseImpedanceData",
        editor=InstanceEditor(name="_perlengthphaseimpedances"))

    def _get_perlengthphaseimpedances(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.PerLengthPhaseImpedance" ]
        else:
            return []

    _perlengthphaseimpedances = Property(fget=_get_perlengthphaseimpedances)

    # Reactance matrix element value, per length of unit.
    x = Reactance(desc="Reactance matrix element value, per length of unit.")

    # Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2.
    sequenceNumber = Int(desc="Column-wise element index, assuming a symmetrical matrix. Ranges from 1 to N + N*(N-1)/2.")

    # Susceptance matrix element value, per length of unit.
    b = Susceptance(desc="Susceptance matrix element value, per length of unit.")

    # Resistance matrix element value, per length of unit.
    r = Resistance(desc="Resistance matrix element value, per length of unit.")

    #--------------------------------------------------------------------------
    #  Begin "PhaseImpedanceData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "x", "sequenceNumber", "b", "r",
                label="Attributes"),
            VGroup("Parent", "PhaseImpedance",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.WiresExt.PhaseImpedanceData",
        title="PhaseImpedanceData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PhaseImpedanceData" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
