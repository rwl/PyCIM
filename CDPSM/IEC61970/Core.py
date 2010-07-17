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

from CDPSM import Element
from CDPSM.IEC61970.Domain import Voltage



from enthought.traits.api import Instance, List, Property, Enum, Bool, Str, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


PhaseCode = Enum("ABC", "splitSecondary2N", "ABN", "CN", "ACN", "BC", "AN", "BN", "AB", "splitSecondary1N", "N", "C", "AC", "ABCN", "splitSecondary12N", "A", "B", "BCN")

#------------------------------------------------------------------------------
#  "IdentifiedObject" class:
#------------------------------------------------------------------------------

class IdentifiedObject(Element):
    """ This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.This attribute is only used when generating XSD Profiles.  For RDF Profiles, the RDF ID is used.A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.This attribute is only used when generating XSD Profiles.  For RDF Profiles, the RDF ID is used.
    mRID = Str(desc="A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.This attribute is only used when generating XSD Profiles.  For RDF Profiles, the RDF ID is used.A Model Authority issues mRIDs. Given that each Model Authority has a unique id and this id is part of the mRID, then the mRID is globally unique.This attribute is only used when generating XSD Profiles.  For RDF Profiles, the RDF ID is used.")

    # The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.
    description = Str(desc="The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.The description is a free human readable text describing or naming the object. It may be non unique and may not correlate to a naming hierarchy.")

    # The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.
    name = Str(desc="The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.The name is a free text human readable name of the object. It may be non unique and may not correlate to a naming hierarchy.")

    # The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.
    localName = Str(desc="The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.The localName is a human readable name of the object. It is only used with objects organized in a naming hierarchy. The simplest naming hierarchy has just one parent (the root) giving a flat naming hierarchy. However, the naming hierarchy usually has several levels, e.g. Substation, VoltageLevel, Equipment etc. Children of the same parent have names that are unique among them. If the uniqueness requirement cannot be met IdentifiedObject.localName shall not be used, use IdentifiedObject.name  instead.")

    # The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.
    aliasName = Str(desc="The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.The aliasName is free text human readable name of the object alternative to IdentifiedObject.name. It may be non unique and may not correlate to a naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.IdentifiedObject",
        title="IdentifiedObject",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IdentifiedObject" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BaseVoltage" class:
#------------------------------------------------------------------------------

class BaseVoltage(IdentifiedObject):
    """ Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
    ConductingEquipment = List(Instance("CDPSM.IEC61970.Core.ConductingEquipment"),
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.")

    # The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.
    VoltageLevel = List(Instance("CDPSM.IEC61970.Core.VoltageLevel"),
        desc="The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.")

    # The PowerSystemResource's base voltage.The PowerSystemResource's base voltage.
    nominalVoltage = Voltage(desc="The PowerSystemResource's base voltage.The PowerSystemResource's base voltage.")

    #--------------------------------------------------------------------------
    #  Begin "BaseVoltage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName", "nominalVoltage",
                label="Attributes"),
            VGroup("Model", "ConductingEquipment", "VoltageLevel",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.BaseVoltage",
        title="BaseVoltage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BaseVoltage" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PSRType" class:
#------------------------------------------------------------------------------

class PSRType(IdentifiedObject):
    """ Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Power system resources classified with this PSRType.Power system resources classified with this PSRType.
    PowerSystemResources = List(Instance("CDPSM.IEC61970.Core.PowerSystemResource"),
        desc="Power system resources classified with this PSRType.Power system resources classified with this PSRType.")

    #--------------------------------------------------------------------------
    #  Begin "PSRType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "PowerSystemResources",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.PSRType",
        title="PSRType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PSRType" user definitions:
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
    Region = Instance("CDPSM.IEC61970.Core.GeographicalRegion", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Regions",
        editor=InstanceEditor(name="_geographicalregions"))

    def _get_geographicalregions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.GeographicalRegion" ]
        else:
            return []

    _geographicalregions = Property(fget=_get_geographicalregions)

    # A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.
    Lines = List(Instance("CDPSM.IEC61970.Wires.Line"),
        desc="A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.")

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Substations = List(Instance("CDPSM.IEC61970.Core.Substation"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "SubGeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "Region", "Lines", "Substations",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.SubGeographicalRegion",
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
    """ An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    ConductingEquipment = Instance("CDPSM.IEC61970.Core.ConductingEquipment", allow_none=False,
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes",
        transient=True,
        opposite="Terminals",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    ConnectivityNode = Instance("CDPSM.IEC61970.Topology.ConnectivityNode", allow_none=False,
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.",
        transient=True,
        opposite="Terminals",
        editor=InstanceEditor(name="_connectivitynodes"))

    def _get_connectivitynodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Topology.ConnectivityNode" ]
        else:
            return []

    _connectivitynodes = Property(fget=_get_connectivitynodes)

    # The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.
    sequenceNumber = Int(desc="The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.")

    # The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithmThe terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm
    connected = Bool(desc="The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithmThe terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm")

    #--------------------------------------------------------------------------
    #  Begin "Terminal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName", "sequenceNumber", "connected",
                label="Attributes"),
            VGroup("Model", "ConductingEquipment", "ConnectivityNode",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.Terminal",
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
    Regions = List(Instance("CDPSM.IEC61970.Core.SubGeographicalRegion"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "GeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "Regions",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.GeographicalRegion",
        title="GeographicalRegion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeographicalRegion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerSystemResource" class:
#------------------------------------------------------------------------------

class PowerSystemResource(IdentifiedObject):
    """ A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Geographical location of this power system resource.Geographical location of this power system resource.
    GeoLocation = Instance("CDPSM.IEC61968.Common.GeoLocation",
        desc="Geographical location of this power system resource.Geographical location of this power system resource.",
        transient=True,
        opposite="PowerSystemResources",
        editor=InstanceEditor(name="_geolocations"))

    def _get_geolocations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.Common.GeoLocation" ]
        else:
            return []

    _geolocations = Property(fget=_get_geolocations)

    # PSRType (custom classification) for this PowerSystemResource.PSRType (custom classification) for this PowerSystemResource.
    PSRType = Instance("CDPSM.IEC61970.Core.PSRType",
        desc="PSRType (custom classification) for this PowerSystemResource.PSRType (custom classification) for this PowerSystemResource.",
        transient=True,
        opposite="PowerSystemResources",
        editor=InstanceEditor(name="_psrtypes"))

    def _get_psrtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.PSRType" ]
        else:
            return []

    _psrtypes = Property(fget=_get_psrtypes)

    #--------------------------------------------------------------------------
    #  Begin "PowerSystemResource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.PowerSystemResource",
        title="PowerSystemResource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerSystemResource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConnectivityNodeContainer" class:
#------------------------------------------------------------------------------

class ConnectivityNodeContainer(PowerSystemResource):
    """ A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Connectivity nodes contained by this container.Connectivity nodes contained by this container.
    ConnectivityNodes = List(Instance("CDPSM.IEC61970.Topology.ConnectivityNode"),
        desc="Connectivity nodes contained by this container.Connectivity nodes contained by this container.")

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNodeContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "ConnectivityNodes",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.ConnectivityNodeContainer",
        title="ConnectivityNodeContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectivityNodeContainer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Equipment" class:
#------------------------------------------------------------------------------

class Equipment(PowerSystemResource):
    """ The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    EquipmentContainer = Instance("CDPSM.IEC61970.Core.EquipmentContainer",
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Equipments",
        editor=InstanceEditor(name="_equipmentcontainers"))

    def _get_equipmentcontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.EquipmentContainer" ]
        else:
            return []

    _equipmentcontainers = Property(fget=_get_equipmentcontainers)

    # The equipment is normally in service.The equipment is normally in service.
    normaIlyInService = Bool(desc="The equipment is normally in service.The equipment is normally in service.")

    #--------------------------------------------------------------------------
    #  Begin "Equipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.Equipment",
        title="Equipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Equipment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquipmentContainer" class:
#------------------------------------------------------------------------------

class EquipmentContainer(ConnectivityNodeContainer):
    """ A modeling construct to provide a root class for all Equipment classesA modeling construct to provide a root class for all Equipment classes
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Equipments = List(Instance("CDPSM.IEC61970.Core.Equipment"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "EquipmentContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "ConnectivityNodes", "Equipments",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.EquipmentContainer",
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
    Region = Instance("CDPSM.IEC61970.Core.SubGeographicalRegion", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Substations",
        editor=InstanceEditor(name="_subgeographicalregions"))

    def _get_subgeographicalregions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    VoltageLevels = List(Instance("CDPSM.IEC61970.Core.VoltageLevel"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    #--------------------------------------------------------------------------
    #  Begin "Substation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "ConnectivityNodes", "Equipments", "Region", "VoltageLevels",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.Substation",
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

    # ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
    Terminals = List(Instance("CDPSM.IEC61970.Core.Terminal"),
        desc="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes")

    # Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.
    BaseVoltage = Instance("CDPSM.IEC61970.Core.BaseVoltage",
        desc="Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.",
        transient=True,
        opposite="ConductingEquipment",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # Describes the phases carried by a conducting equipment.Describes the phases carried by a conducting equipment.
    phases = PhaseCode(desc="Describes the phases carried by a conducting equipment.Describes the phases carried by a conducting equipment.")

    #--------------------------------------------------------------------------
    #  Begin "ConductingEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.ConductingEquipment",
        title="ConductingEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductingEquipment" user definitions:
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
    BaseVoltage = Instance("CDPSM.IEC61970.Core.BaseVoltage", allow_none=False,
        desc="The base voltage used for all equipment within the VoltageLevel.The base voltage used for all equipment within the VoltageLevel.",
        transient=True,
        opposite="VoltageLevel",
        editor=InstanceEditor(name="_basevoltages"))

    def _get_basevoltages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.BaseVoltage" ]
        else:
            return []

    _basevoltages = Property(fget=_get_basevoltages)

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Bays = List(Instance("CDPSM.IEC61970.Core.Bay"),
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    Substation = Instance("CDPSM.IEC61970.Core.Substation",
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="VoltageLevels",
        editor=InstanceEditor(name="_substations"))

    def _get_substations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.Substation" ]
        else:
            return []

    _substations = Property(fget=_get_substations)

    # The bus bar's low voltage limitThe bus bar's low voltage limit
    lowVoltageLimit = Voltage(desc="The bus bar's low voltage limitThe bus bar's low voltage limit")

    # The bus bar's high voltage limitThe bus bar's high voltage limit
    highVoltageLimit = Voltage(desc="The bus bar's high voltage limitThe bus bar's high voltage limit")

    #--------------------------------------------------------------------------
    #  Begin "VoltageLevel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName", "lowVoltageLimit", "highVoltageLimit",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "ConnectivityNodes", "Equipments", "BaseVoltage", "Bays", "Substation",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.VoltageLevel",
        title="VoltageLevel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLevel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Bay" class:
#------------------------------------------------------------------------------

class Bay(EquipmentContainer):
    """ A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The association is used in the naming hierarchy.The association is used in the naming hierarchy.
    VoltageLevel = Instance("CDPSM.IEC61970.Core.VoltageLevel", allow_none=False,
        desc="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
        transient=True,
        opposite="Bays",
        editor=InstanceEditor(name="_voltagelevels"))

    def _get_voltagelevels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.VoltageLevel" ]
        else:
            return []

    _voltagelevels = Property(fget=_get_voltagelevels)

    #--------------------------------------------------------------------------
    #  Begin "Bay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "ConnectivityNodes", "Equipments", "VoltageLevel",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Core.Bay",
        title="Bay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Bay" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
