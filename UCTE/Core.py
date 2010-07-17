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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from UCTE import Element
from UCTE.Domain import Voltage



from enthought.traits.api import Instance, List, Property, Bool, Str, Int, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "IdentifiedObject" class:
#------------------------------------------------------------------------------

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = Str(desc="The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.")

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit.
    name = Str(desc="The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.This attribute is required on all instances in this Profile that inherit from IdentifiedObject except for the following Classes: 1) BaseVoltage; 2) Terminal; 3) TransformerWinding; 4) RatioTapChanger; 5) PhaseTapChanger; 6) OperationalLImitSet; 7) CurrentLimit; and, 8) VoltageLimit.")

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.   The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.   
    aliasName = Str(desc="The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.   The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.In the UCTE profile the aliasName is used to hold the EIC code.    The code length is 16 characters.    Not all CIM classes have an EIC code so the attribute is optional.   ")

    #--------------------------------------------------------------------------
    #  Begin "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="UCTE.Core.IdentifiedObject",
        title="IdentifiedObject",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurveData" class:
#------------------------------------------------------------------------------

class CurveData(Element):
    """ Data point values for defining a curve or scheduleData point values for defining a curve or schedule
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Curve defined by this CurveData.The Curve defined by this CurveData.
    CurveSchedule = Instance("UCTE.Core.Curve", allow_none=False,
        desc="The Curve defined by this CurveData.The Curve defined by this CurveData.",
        transient=True,
        opposite="CurveScheduleDatas",
        editor=InstanceEditor(name="_curves"))

    def _get_curves(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.Curve" ]
        else:
            return []

    _curves = Property(fget=_get_curves)

    # The data value of the  first Y-axis variable, depending on the Y-axis unitsThe data value of the  first Y-axis variable, depending on the Y-axis units
    y1value = Float(desc="The data value of the  first Y-axis variable, depending on the Y-axis unitsThe data value of the  first Y-axis variable, depending on the Y-axis units")

    # The data value of the X-axis variable,  depending on the X-axis unitsThe data value of the X-axis variable,  depending on the X-axis units
    xvalue = Float(desc="The data value of the X-axis variable,  depending on the X-axis unitsThe data value of the X-axis variable,  depending on the X-axis units")

    # The data value of the second Y-axis variable (if present), depending on the Y-axis unitsThe data value of the second Y-axis variable (if present), depending on the Y-axis units
    y2value = Float(desc="The data value of the second Y-axis variable (if present), depending on the Y-axis unitsThe data value of the second Y-axis variable (if present), depending on the Y-axis units")

    #--------------------------------------------------------------------------
    #  Begin "CurveData" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "y1value", "xvalue", "y2value",
                label="Attributes"),
            VGroup("Model", "CurveSchedule",
                label="References"),
            dock="tab"),
        id="UCTE.Core.CurveData",
        title="CurveData",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurveData" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Curve" class:
#------------------------------------------------------------------------------

class Curve(IdentifiedObject):
    """ Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The point data values that define a curveThe point data values that define a curve
    CurveScheduleDatas = List(Instance("UCTE.Core.CurveData"),
        desc="The point data values that define a curveThe point data values that define a curve")

    #--------------------------------------------------------------------------
    #  Begin "Curve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "CurveScheduleDatas",
                label="References"),
            dock="tab"),
        id="UCTE.Core.Curve",
        title="Curve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Curve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConnectivityNodeContainer" class:
#------------------------------------------------------------------------------

class ConnectivityNodeContainer(IdentifiedObject):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile. The TopologicalNode will normally belong only to a VoltageLevel within a Substation. In the case of X-nodes, the TopologicalNode is not contained.    A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile. The TopologicalNode will normally belong only to a VoltageLevel within a Substation. In the case of X-nodes, the TopologicalNode is not contained.    
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The topological nodes which belong to this connectivity node container.The topological nodes which belong to this connectivity node container.
    TopologicalNode = List(Instance("UCTE.Topology.TopologicalNode"),
        desc="The topological nodes which belong to this connectivity node container.The topological nodes which belong to this connectivity node container.")

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNodeContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="UCTE.Core.ConnectivityNodeContainer",
        title="ConnectivityNodeContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectivityNodeContainer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Equipment" class:
#------------------------------------------------------------------------------

class Equipment(IdentifiedObject):
    """ The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. The association is used in the naming hierarchy.For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. 
    MemberOf_EquipmentContainer = Instance("UCTE.Core.EquipmentContainer",
        desc="The association is used in the naming hierarchy.For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. The association is used in the naming hierarchy.For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. ",
        transient=True,
        opposite="Contains_Equipments",
        editor=InstanceEditor(name="_equipmentcontainers"))

    def _get_equipmentcontainers(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.EquipmentContainer" ]
        else:
            return []

    _equipmentcontainers = Property(fget=_get_equipmentcontainers)

    # Indicates if the equipment is real equipment (false) or an equivalent.If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute.Indicates if the equipment is real equipment (false) or an equivalent.If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute.
    equivalent = Bool(desc="Indicates if the equipment is real equipment (false) or an equivalent.If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute.Indicates if the equipment is real equipment (false) or an equivalent.If this is missing, it is assumed to be False.  It is required for Equipment connected to the X-Node. All classes derived from Equipment are to include this attribute except for the TransformerWinding class.     For transformers the PowerTransformer class will be used to specify the real or equivalent status and the contained TransformerWinding class instances need not and should not specify this attribute.")

    #--------------------------------------------------------------------------
    #  Begin "Equipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer",
                label="References"),
            dock="tab"),
        id="UCTE.Core.Equipment",
        title="Equipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Equipment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BaseVoltage" class:
#------------------------------------------------------------------------------

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
    ConductingEquipment = List(Instance("UCTE.Core.ConductingEquipment"),
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.")

    # The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.
    VoltageLevel = List(Instance("UCTE.Core.VoltageLevel"),
        desc="The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.")

    # The topological nodes at the base voltage.The topological nodes at the base voltage.
    TopologicalNode = List(Instance("UCTE.Topology.TopologicalNode"),
        desc="The topological nodes at the base voltage.The topological nodes at the base voltage.")

    # The PowerSystemResource's base voltage.The PowerSystemResource's base voltage.
    nominalVoltage = Voltage(desc="The PowerSystemResource's base voltage.The PowerSystemResource's base voltage.")

    # If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.
    isDC = Bool(desc="If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.If true, this is a direct current base voltage and items assigned to this base voltage are also associated with a direct current capabilities.   False indicates alternating current.")

    #--------------------------------------------------------------------------
    #  Begin "BaseVoltage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "nominalVoltage", "isDC",
                label="Attributes"),
            VGroup("Model", "ConductingEquipment", "VoltageLevel", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="UCTE.Core.BaseVoltage",
        title="BaseVoltage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BaseVoltage" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquipmentContainer" class:
#------------------------------------------------------------------------------

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classesFor a TransformerWinding the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer Association. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. A modeling construct to provide a root class for all Equipment classesFor a TransformerWinding the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer Association. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. 
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Contains_Equipments = List(Instance("UCTE.Core.Equipment"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "EquipmentContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "TopologicalNode", "Contains_Equipments",
                label="References"),
            dock="tab"),
        id="UCTE.Core.EquipmentContainer",
        title="EquipmentContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquipmentContainer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Substation" class:
#------------------------------------------------------------------------------

class Substation(EquipmentContainer):
    """ A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Contains_VoltageLevels = List(Instance("UCTE.Core.VoltageLevel"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Region = Instance("UCTE.Core.SubGeographicalRegion", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Substations",
        editor=InstanceEditor(name="_subgeographicalregions"))

    def _get_subgeographicalregions(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    #--------------------------------------------------------------------------
    #  Begin "Substation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "TopologicalNode", "Contains_Equipments", "Contains_VoltageLevels", "Region",
                label="References"),
            dock="tab"),
        id="UCTE.Core.Substation",
        title="Substation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Substation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductingEquipment" class:
#------------------------------------------------------------------------------

class ConductingEquipment(Equipment):
    """ The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes.Use association to ConductingEquipment only when there is no VoltageLevel container used.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes.
    BaseVoltage = Instance("UCTE.Core.BaseVoltage",
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes.Use association to ConductingEquipment only when there is no VoltageLevel container used.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes.",
        transient=True,
        opposite="ConductingEquipment",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    Terminals = List(Instance("UCTE.Core.Terminal"),
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes")

    #--------------------------------------------------------------------------
    #  Begin "ConductingEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="UCTE.Core.ConductingEquipment",
        title="ConductingEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductingEquipment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubGeographicalRegion" class:
#------------------------------------------------------------------------------

class SubGeographicalRegion(IdentifiedObject):
    """ A subset of a geographical region of a power system network model.A subset of a geographical region of a power system network model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Substations = List(Instance("UCTE.Core.Substation"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Region = Instance("UCTE.Core.GeographicalRegion", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Regions",
        editor=InstanceEditor(name="_geographicalregions"))

    def _get_geographicalregions(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.GeographicalRegion" ]
        else:
            return []

    _geographicalregions = Property(fget=_get_geographicalregions)

    #--------------------------------------------------------------------------
    #  Begin "SubGeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "Substations", "Region",
                label="References"),
            dock="tab"),
        id="UCTE.Core.SubGeographicalRegion",
        title="SubGeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubGeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Terminal" class:
#------------------------------------------------------------------------------

class Terminal(IdentifiedObject):
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes such as EnergyConsumer and SynchronousMachine.   The flows at any ShuntCompensator can always be computed from connected voltage magnitude, number of sections and local attributes.  Branch flows are not exchanged since they can be readily be computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes such as EnergyConsumer and SynchronousMachine.   The flows at any ShuntCompensator can always be computed from connected voltage magnitude, number of sections and local attributes.  Branch flows are not exchanged since they can be readily be computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. 
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Mutual couplings associated with the branch as the first branch.Mutual couplings associated with the branch as the first branch.
    HasFirst_MutualCoupling = List(Instance("UCTE.Wires.MutualCoupling"),
        desc="Mutual couplings associated with the branch as the first branch.Mutual couplings associated with the branch as the first branch.")

    # The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
    OperationalLimitSet = List(Instance("UCTE.OperationalLimits.OperationalLimitSet"),
        desc="The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.")

    # The power flow state associated with the terminal.The power flow state associated with the terminal.
    SvPowerFlow = Instance("UCTE.StateVariables.SvPowerFlow",
        desc="The power flow state associated with the terminal.The power flow state associated with the terminal.",
        transient=True,
        opposite="Terminal",
        editor=InstanceEditor(name="_svpowerflows"))

    def _get_svpowerflows(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.StateVariables.SvPowerFlow" ]
        else:
            return []

    _svpowerflows = Property(fget=_get_svpowerflows)

    # The terminal is regulated by a control.The terminal is regulated by a control.
    RegulatingControl = List(Instance("UCTE.Wires.RegulatingControl"),
        desc="The terminal is regulated by a control.The terminal is regulated by a control.")

    # The control area tie flows to which this terminal associates.The control area tie flows to which this terminal associates.
    TieFlow = List(Instance("UCTE.ControlArea.TieFlow"),
        desc="The control area tie flows to which this terminal associates.The control area tie flows to which this terminal associates.")

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    ConductingEquipment = Instance("UCTE.Core.ConductingEquipment", allow_none=False,
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes",
        transient=True,
        opposite="Terminals",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    # The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
    TopologicalNode = Instance("UCTE.Topology.TopologicalNode", allow_none=False,
        desc="The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.",
        transient=True,
        opposite="Terminal",
        editor=InstanceEditor(name="_topologicalnodes"))

    def _get_topologicalnodes(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Topology.TopologicalNode" ]
        else:
            return []

    _topologicalnodes = Property(fget=_get_topologicalnodes)

    # Mutual couplings with the branch associated as the first branch.Mutual couplings with the branch associated as the first branch.
    HasSecond_MutualCoupling = List(Instance("UCTE.Wires.MutualCoupling"),
        desc="Mutual couplings with the branch associated as the first branch.Mutual couplings with the branch associated as the first branch.")

    # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.
    sequenceNumber = Int(desc="The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.For UCTE profile, the terminal sequence number is not required.   And, when used, follows the UML description. The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.")

    # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied.The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied.
    connected = Bool(desc="The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied.The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm for topological analysis is implied.")

    #--------------------------------------------------------------------------
    #  Begin "Terminal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "sequenceNumber", "connected",
                label="Attributes"),
            VGroup("Model", "HasFirst_MutualCoupling", "OperationalLimitSet", "SvPowerFlow", "RegulatingControl", "TieFlow", "ConductingEquipment", "TopologicalNode", "HasSecond_MutualCoupling",
                label="References"),
            dock="tab"),
        id="UCTE.Core.Terminal",
        title="Terminal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Terminal" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeographicalRegion" class:
#------------------------------------------------------------------------------

class GeographicalRegion(IdentifiedObject):
    """ A geographical region of a power system network model.A geographical region of a power system network model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Regions = List(Instance("UCTE.Core.SubGeographicalRegion"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "GeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "Regions",
                label="References"),
            dock="tab"),
        id="UCTE.Core.GeographicalRegion",
        title="GeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VoltageLevel" class:
#------------------------------------------------------------------------------

class VoltageLevel(EquipmentContainer):
    """ A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The base voltage used for all equipment within the VoltageLevel.The base voltage used for all equipment within the VoltageLevel.
    BaseVoltage = Instance("UCTE.Core.BaseVoltage", allow_none=False,
        desc="The base voltage used for all equipment within the VoltageLevel.The base voltage used for all equipment within the VoltageLevel.",
        transient=True,
        opposite="VoltageLevel",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    MemberOf_Substation = Instance("UCTE.Core.Substation", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Contains_VoltageLevels",
        editor=InstanceEditor(name="_substations"))

    def _get_substations(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.Substation" ]
        else:
            return []

    _substations = Property(fget=_get_substations)

    #--------------------------------------------------------------------------
    #  Begin "VoltageLevel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "TopologicalNode", "Contains_Equipments", "BaseVoltage", "MemberOf_Substation",
                label="References"),
            dock="tab"),
        id="UCTE.Core.VoltageLevel",
        title="VoltageLevel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLevel" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
