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

""" The package covers all types of work, including inspection, maintenance, repair, restoration, and construction. It covers the full life cycle including request, initiate, track and record work. Standardized designs (compatible units) are used where possible.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Work package is used to define classes related to work. There are several different aspects of work. The Work Initiation (Work, Project, Request). The Work Design package is used for managing designs (CompatibleUnit, Design, DesignLocation, WorkTask). The Work Schedule package is used for the scheduling and coordination of work (AccessPermit, MaterialItem, OneCallRequest, Regulation). The Work Closing package is used for tracking costs of work (CostType, LaborItem, WorkCostDetail, VehicleItem). The Work Standards package is used for the definition of compatible units (CULaborItem, CUVehicleItem, CUGroup). This package is used for inspection and maintenance (InspectionDataSet, Procedure). The WorkService package defines Appointment class.'
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Document
from CIM.IEC61968.Informative.InfCommon import ScheduledEvent
from CIM.IEC61968.Informative.InfAssets import ProcedureDataSet
from CIM.IEC61968.Common import ActivityRecord
from CIM.IEC61968.Common import Location
from CIM.IEC61970.Domain import Length
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import CostRate
from CIM.IEC61970.Domain import Hours
from CIM.IEC61970.Domain import IntegerQuantity
from CIM.IEC61970.Domain import AbsoluteDate
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Core import PhaseCode



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool, Date, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kinds of activities to be performed on a Compatible Unit.
WorkActionKind = Enum("install", "remove", "transfer", "abandon", desc="Kinds of activities to be performed on a Compatible Unit.")
# Kind of condition factor.
ConditionFactorKind = Enum("labor", "accountAllocation", "travel", "other", "material", desc="Kind of condition factor.")
# Kind of design.
DesignKind = Enum("estimated", "asBuilt", "other", desc="Kind of design.")

#------------------------------------------------------------------------------
#  "DesignLocation" class:
#------------------------------------------------------------------------------

class DesignLocation(IdentifiedObject):
    """ A logical part of the design (e.g., pole and all equipment on a pole). This includes points and spans.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MaterialItems = List(Instance("CIM.IEC61968.Informative.InfWork.MaterialItem"))

    DesignLocationCUs = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocationCU"))

    Designs = List(Instance("CIM.IEC61968.Informative.InfWork.Design"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    MiscCostItems = List(Instance("CIM.IEC61968.Informative.InfWork.MiscCostItem"))

    ConditionFactors = List(Instance("CIM.IEC61968.Informative.InfWork.ConditionFactor"))

    Diagrams = List(Instance("CIM.IEC61968.Informative.InfCommon.Diagram"))

    ErpBomItemDatas = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpBomItemData"))

    WorkLocations = List(Instance("CIM.IEC61968.Informative.InfWork.WorkLocation"))

    # The legth of the span from the previous pole to this pole.
    spanLength = Length(desc="The legth of the span from the previous pole to this pole.")

    #--------------------------------------------------------------------------
    #  Begin "DesignLocation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "spanLength",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MaterialItems", "DesignLocationCUs", "Designs", "status", "MiscCostItems", "ConditionFactors", "Diagrams", "ErpBomItemDatas", "WorkLocations",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.DesignLocation",
        title="DesignLocation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DesignLocation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Capability" class:
#------------------------------------------------------------------------------

class Capability(IdentifiedObject):
    """ Capabilities of a crew.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Crew = Instance("CIM.IEC61968.Informative.InfWork.Crew",
        transient=True,
        opposite="Capabilities",
        editor=InstanceEditor(name="_crews"))

    def _get_crews(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Crew" ]
        else:
            return []

    _crews = Property(fget=_get_crews)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    WorkTasks = List(Instance("CIM.IEC61968.Informative.InfWork.WorkTask"))

    # Date and time interval for which this capability is valid (when it became effective and when it expires).
    validityInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Date and time interval for which this capability is valid (when it became effective and when it expires).",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    Crafts = List(Instance("CIM.IEC61968.Informative.InfCommon.Craft"))

    # Capability performance factor.
    performanceFactor = Str(desc="Capability performance factor.")

    # Category by utility's work management standards and practices.
    category = Str(desc="Category by utility's work management standards and practices.")

    #--------------------------------------------------------------------------
    #  Begin "Capability" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "performanceFactor", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Crew", "status", "WorkTasks", "validityInterval", "Crafts",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Capability",
        title="Capability",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Capability" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Design" class:
#------------------------------------------------------------------------------

class Design(Document):
    """ A design for consideration by customers, potential customers, or internal work. Note that the Version of design is the revision attribute that is inherited from Document.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    DesignLocationsCUs = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocationCU"))

    WorkCostDetails = List(Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail"))

    ErpQuoteLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem",
        transient=True,
        opposite="Design",
        editor=InstanceEditor(name="_erpquotelineitems"))

    def _get_erpquotelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem" ]
        else:
            return []

    _erpquotelineitems = Property(fget=_get_erpquotelineitems)

    DesignLocations = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocation"))

    Work = Instance("CIM.IEC61968.Work.Work",
        transient=True,
        opposite="Designs",
        editor=InstanceEditor(name="_works"))

    def _get_works(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Work.Work" ]
        else:
            return []

    _works = Property(fget=_get_works)

    ErpBOMs = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpBOM"))

    ConditionFactors = List(Instance("CIM.IEC61968.Informative.InfWork.ConditionFactor"))

    WorkTasks = List(Instance("CIM.IEC61968.Informative.InfWork.WorkTask"))

    # Kind of this design.
    kind = DesignKind(desc="Kind of this design.")

    # Price to customer for implementing design.
    price = Money(desc="Price to customer for implementing design.")

    # Estimated cost (not price) of design.
    costEstimate = Money(desc="Estimated cost (not price) of design.")

    #--------------------------------------------------------------------------
    #  Begin "Design" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind", "price", "costEstimate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "DesignLocationsCUs", "WorkCostDetails", "ErpQuoteLineItem", "DesignLocations", "Work", "ErpBOMs", "ConditionFactors", "WorkTasks",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Design",
        title="Design",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Design" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LaborItem" class:
#------------------------------------------------------------------------------

class LaborItem(IdentifiedObject):
    """ Labor used for work order.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkCostDetail = Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail",
        transient=True,
        opposite="LaborItems",
        editor=InstanceEditor(name="_workcostdetails"))

    def _get_workcostdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkCostDetail" ]
        else:
            return []

    _workcostdetails = Property(fget=_get_workcostdetails)

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="LaborItems",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    # The labor rate applied for work.
    laborRate = CostRate(desc="The labor rate applied for work.")

    # Total cost for labor. Note that this may not be able to be derived from labor rate and time charged.
    cost = Money(desc="Total cost for labor. Note that this may not be able to be derived from labor rate and time charged.")

    # Activity code identifies a specific and distinguishable unit of work.
    activityCode = Str(desc="Activity code identifies a specific and distinguishable unit of work.")

    # Time required to perform work.
    laborDuration = Hours(desc="Time required to perform work.")

    #--------------------------------------------------------------------------
    #  Begin "LaborItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "laborRate", "cost", "activityCode", "laborDuration",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "WorkCostDetail", "ErpPersons", "status", "WorkTask",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.LaborItem",
        title="LaborItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LaborItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CUMaterialItem" class:
#------------------------------------------------------------------------------

class CUMaterialItem(IdentifiedObject):
    """ Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    TypeMaterial = Instance("CIM.IEC61968.Informative.InfWork.TypeMaterial",
        transient=True,
        opposite="CUMaterialItems",
        editor=InstanceEditor(name="_typematerials"))

    def _get_typematerials(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.TypeMaterial" ]
        else:
            return []

    _typematerials = Property(fget=_get_typematerials)

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    PropertyUnits = List(Instance("CIM.IEC61968.Informative.InfWork.PropertyUnit"))

    # Code for material.
    corporateCode = Str(desc="Code for material.")

    # Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial.
    quantity = IntegerQuantity(desc="Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial.")

    #--------------------------------------------------------------------------
    #  Begin "CUMaterialItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "quantity",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "TypeMaterial", "CompatibleUnits", "PropertyUnits",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CUMaterialItem",
        title="CUMaterialItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CUMaterialItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "NonStandardItem" class:
#------------------------------------------------------------------------------

class NonStandardItem(Document):
    """ This document provides information for non-standard items like customer contributions (e.g., customer digs trench), vouchers (e.g., credit), and contractor bids.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The projected cost for this item.
    amount = Money(desc="The projected cost for this item.")

    # The category of non-standard work.
    code = Str(desc="The category of non-standard work.")

    #--------------------------------------------------------------------------
    #  Begin "NonStandardItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "amount", "code",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.NonStandardItem",
        title="NonStandardItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "NonStandardItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TypeMaterial" class:
#------------------------------------------------------------------------------

class TypeMaterial(Document):
    """ Documentation for a generic material item that may be used for design, work and other purposes. Any number of MaterialItems manufactured by various vendors may be used to perform this TypeMaterial. Note that class analagous to 'AssetModel' is not used for material items. This is because in some cases, for example, a utility sets up a Master material record for a 3 inch long half inch diameter steel bolt and they do not necessarily care what specific supplier is providing the material item. As different vendors are used to supply the part, the Stock Code of the material item can stay the same. In other cases, each time the vendor changes, a new stock code is set up so they can track material used by vendor. Therefore a Material Item 'Model' is not typically needed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpReqLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpReqLineItem"))

    ErpIssueInventories = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpIssueInventory"))

    CUMaterialItems = List(Instance("CIM.IEC61968.Informative.InfWork.CUMaterialItem"))

    MaterialItems = List(Instance("CIM.IEC61968.Informative.InfWork.MaterialItem"))

    # True if item is a stock item (default).
    stockItem = Bool(desc="True if item is a stock item (default).")

    # The value, unit of measure, and multiplier for the quantity.
    quantity = Str(desc="The value, unit of measure, and multiplier for the quantity.")

    # The category of cost to which this Material Item belongs.
    costType = Str(desc="The category of cost to which this Material Item belongs.")

    # The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.
    estUnitCost = Money(desc="The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.")

    #--------------------------------------------------------------------------
    #  Begin "TypeMaterial" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "stockItem", "quantity", "costType", "estUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpReqLineItems", "ErpIssueInventories", "CUMaterialItems", "MaterialItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.TypeMaterial",
        title="TypeMaterial",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TypeMaterial" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Appointment" class:
#------------------------------------------------------------------------------

class Appointment(ScheduledEvent):
    """ Meeting time and location.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    CallBack = Instance("CIM.IEC61968.Informative.InfOperations.CallBack",
        transient=True,
        opposite="Appointments",
        editor=InstanceEditor(name="_callbacks"))

    def _get_callbacks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.CallBack" ]
        else:
            return []

    _callbacks = Property(fget=_get_callbacks)

    # Address for appointment.
    address = Instance("CIM.IEC61968.Common.StreetAddress",
        desc="Address for appointment.",
        transient=True,
        editor=InstanceEditor(name="_streetaddresss"))

    def _get_streetaddresss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.StreetAddress" ]
        else:
            return []

    _streetaddresss = Property(fget=_get_streetaddresss)

    # Date and time reserved for appointment.
    meetingInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Date and time reserved for appointment.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    # Information about the appointment.
    remark = Str(desc="Information about the appointment.")

    # True if requested to call customer when someone is about to arrive at their premises.
    callAhead = Bool(desc="True if requested to call customer when someone is about to arrive at their premises.")

    #--------------------------------------------------------------------------
    #  Begin "Appointment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "duration", "category", "remark", "callAhead",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Document", "Assets", "ActivityRecord", "ScheduleParameterInfo", "status", "TimePoint", "ErpPersons", "CallBack", "address", "meetingInterval",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Appointment",
        title="Appointment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Appointment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MaterialItem" class:
#------------------------------------------------------------------------------

class MaterialItem(IdentifiedObject):
    """ The physical consumable supply used for work and other purposes. It includes items such as nuts, bolts, brackets, glue, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Usages = List(Instance("CIM.IEC61968.Informative.InfWork.Usage"))

    DesignLocation = Instance("CIM.IEC61968.Informative.InfWork.DesignLocation",
        transient=True,
        opposite="MaterialItems",
        editor=InstanceEditor(name="_designlocations"))

    def _get_designlocations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.DesignLocation" ]
        else:
            return []

    _designlocations = Property(fget=_get_designlocations)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="MaterialItems",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    ErpInventoryCounts = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInventoryCount"))

    ErpRecDelvLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem"))

    ErpPOLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPOLineItem"))

    WorkCostDetail = Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail",
        transient=True,
        opposite="MaterialItems",
        editor=InstanceEditor(name="_workcostdetails"))

    def _get_workcostdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkCostDetail" ]
        else:
            return []

    _workcostdetails = Property(fget=_get_workcostdetails)

    TypeMaterial = Instance("CIM.IEC61968.Informative.InfWork.TypeMaterial",
        transient=True,
        opposite="MaterialItems",
        editor=InstanceEditor(name="_typematerials"))

    def _get_typematerials(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.TypeMaterial" ]
        else:
            return []

    _typematerials = Property(fget=_get_typematerials)

    # The actual cost of this particular material in this particular quantity.
    actualCost = Money(desc="The actual cost of this particular material in this particular quantity.")

    # Code for material.
    materialCode = Str(desc="Code for material.")

    # The quantity of material used.
    quantity = IntegerQuantity(desc="The quantity of material used.")

    # The category of cost to which this Material Item belongs.
    costType = Str(desc="The category of cost to which this Material Item belongs.")

    # Description of the cost.
    costDescription = Str(desc="Description of the cost.")

    # External reference identifier for this actual material item such as a purchase order number, a serial number, etc.
    externalRefID = Str(desc="External reference identifier for this actual material item such as a purchase order number, a serial number, etc.")

    # The account to which this actual material item is charged.
    account = Str(desc="The account to which this actual material item is charged.")

    #--------------------------------------------------------------------------
    #  Begin "MaterialItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "actualCost", "materialCode", "quantity", "costType", "costDescription", "externalRefID", "account",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Usages", "DesignLocation", "status", "WorkTask", "ErpInventoryCounts", "ErpRecDelvLineItems", "ErpPOLineItems", "WorkCostDetail", "TypeMaterial",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.MaterialItem",
        title="MaterialItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MaterialItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CUContractorItem" class:
#------------------------------------------------------------------------------

class CUContractorItem(IdentifiedObject):
    """ Compatible unit contractor item.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # The amount that a given contractor will charge for performing this unit of work.
    bidAmount = Money(desc="The amount that a given contractor will charge for performing this unit of work.")

    # Activity code identifies a specific and distinguishable unit of work.
    activityCode = Str(desc="Activity code identifies a specific and distinguishable unit of work.")

    #--------------------------------------------------------------------------
    #  Begin "CUContractorItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "bidAmount", "activityCode",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "CompatibleUnits", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CUContractorItem",
        title="CUContractorItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CUContractorItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CompatibleUnit" class:
#------------------------------------------------------------------------------

class CompatibleUnit(Document):
    """ A pre-planned job model containing labor, material, and accounting requirements for standardized job planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CUWorkEquipmentItems = List(Instance("CIM.IEC61968.Informative.InfWork.CUWorkEquipmentItem"))

    CUContractorItems = List(Instance("CIM.IEC61968.Informative.InfWork.CUContractorItem"))

    Procedures = List(Instance("CIM.IEC61968.Informative.InfAssets.Procedure"))

    CUAssets = List(Instance("CIM.IEC61968.Informative.InfWork.CUAsset"))

    CUMaterialItems = List(Instance("CIM.IEC61968.Informative.InfWork.CUMaterialItem"))

    PropertyUnit = Instance("CIM.IEC61968.Informative.InfWork.PropertyUnit",
        transient=True,
        opposite="CompatibleUnits",
        editor=InstanceEditor(name="_propertyunits"))

    def _get_propertyunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.PropertyUnit" ]
        else:
            return []

    _propertyunits = Property(fget=_get_propertyunits)

    CULaborItems = List(Instance("CIM.IEC61968.Informative.InfWork.CULaborItem"))

    DesignLocationCUs = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocationCU"))

    CUAllowableAction = Instance("CIM.IEC61968.Informative.InfWork.CUAllowableAction",
        transient=True,
        opposite="CompatibleUnits",
        editor=InstanceEditor(name="_cuallowableactions"))

    def _get_cuallowableactions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.CUAllowableAction" ]
        else:
            return []

    _cuallowableactions = Property(fget=_get_cuallowableactions)

    CUGroup = Instance("CIM.IEC61968.Informative.InfWork.CUGroup",
        transient=True,
        opposite="CompatibleUnits",
        editor=InstanceEditor(name="_cugroups"))

    def _get_cugroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.CUGroup" ]
        else:
            return []

    _cugroups = Property(fget=_get_cugroups)

    CostType = Instance("CIM.IEC61968.Informative.InfWork.CostType",
        transient=True,
        opposite="CompatibleUnits",
        editor=InstanceEditor(name="_costtypes"))

    def _get_costtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.CostType" ]
        else:
            return []

    _costtypes = Property(fget=_get_costtypes)

    # Estimated total cost for perfoming CU.
    estCost = Money(desc="Estimated total cost for perfoming CU.")

    # The quantity, unit of measure, and multiplier at the CU level that applies to the materials.
    quantity = Str(desc="The quantity, unit of measure, and multiplier at the CU level that applies to the materials.")

    #--------------------------------------------------------------------------
    #  Begin "CompatibleUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "estCost", "quantity",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentItems", "CUContractorItems", "Procedures", "CUAssets", "CUMaterialItems", "PropertyUnit", "CULaborItems", "DesignLocationCUs", "CUAllowableAction", "CUGroup", "CostType",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CompatibleUnit",
        title="CompatibleUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CompatibleUnit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "InfoQuestion" class:
#------------------------------------------------------------------------------

class InfoQuestion(Document):
    """ Questions and answers associated with a type of document for purposes of clarification. Questions may be predefined or ad hoc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Remarks to qualify the question in this situation.
    questionRemark = Str(desc="Remarks to qualify the question in this situation.")

    # Answer to question.
    answer = Str(desc="Answer to question.")

    # The category of the question.
    questionCategory = Str(desc="The category of the question.")

    # The question code. If blank, refer to questionText.
    questionCode = Str(desc="The question code. If blank, refer to questionText.")

    # The date and time the quesiton was answered.
    answerDateTime = Date(desc="The date and time the quesiton was answered.")

    # For non-coded questions, the question is provided here.
    questionText = Str(desc="For non-coded questions, the question is provided here.")

    # Remarks to qualify the answer.
    answerRemark = Str(desc="Remarks to qualify the answer.")

    #--------------------------------------------------------------------------
    #  Begin "InfoQuestion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "questionRemark", "answer", "questionCategory", "questionCode", "answerDateTime", "questionText", "answerRemark",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.InfoQuestion",
        title="InfoQuestion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "InfoQuestion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MaintenanceDataSet" class:
#------------------------------------------------------------------------------

class MaintenanceDataSet(ProcedureDataSet):
    """ The result of a maintenance activity, a type of Procedure, for a given attribute of an asset is documentated in an MaintenanceDataSet.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Description of the condition of the asset just prior to maintenance being performed.
    conditionBefore = Str(desc="Description of the condition of the asset just prior to maintenance being performed.")

    # Code for the type of maintenance performed.
    maintCode = Str(desc="Code for the type of maintenance performed.")

    # Condition of asset just following maintenance procedure.
    conditionAfter = Str(desc="Condition of asset just following maintenance procedure.")

    #--------------------------------------------------------------------------
    #  Begin "MaintenanceDataSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "completedDateTime", "conditionBefore", "maintCode", "conditionAfter",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Procedure", "Properties", "MeasurementValues", "TransformerObservations",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.MaintenanceDataSet",
        title="MaintenanceDataSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MaintenanceDataSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Regulation" class:
#------------------------------------------------------------------------------

class Regulation(Document):
    """ Special requirements and/or regulations may pertain to certain types of assets or work. For example, fire protection and scaffolding.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # External reference to regulation, if applicable.
    referenceNumber = Str(desc="External reference to regulation, if applicable.")

    #--------------------------------------------------------------------------
    #  Begin "Regulation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "referenceNumber",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Regulation",
        title="Regulation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Regulation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Usage" class:
#------------------------------------------------------------------------------

class Usage(IdentifiedObject):
    """ The way material and assets are used to perform a certain type of work task. The way is described in text in the inheritied description attribute.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MaterialItem = Instance("CIM.IEC61968.Informative.InfWork.MaterialItem",
        transient=True,
        opposite="Usages",
        editor=InstanceEditor(name="_materialitems"))

    def _get_materialitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.MaterialItem" ]
        else:
            return []

    _materialitems = Property(fget=_get_materialitems)

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="Usages",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    WorkEquipmentAsset = Instance("CIM.IEC61968.Informative.InfAssets.WorkEquipmentAsset",
        transient=True,
        opposite="Usages",
        editor=InstanceEditor(name="_workequipmentassets"))

    def _get_workequipmentassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.WorkEquipmentAsset" ]
        else:
            return []

    _workequipmentassets = Property(fget=_get_workequipmentassets)

    #--------------------------------------------------------------------------
    #  Begin "Usage" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MaterialItem", "WorkTask", "status", "WorkEquipmentAsset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Usage",
        title="Usage",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Usage" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccessPermit" class:
#------------------------------------------------------------------------------

class AccessPermit(Document):
    """ A permit is sometimes needed to provide legal access to land or equipment. For example, local authority permission for road works.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Total cost of permit.
    payment = Money(desc="Total cost of permit.")

    # Permit application number that is used by municipality, state, province, etc.
    applicationNumber = Str(desc="Permit application number that is used by municipality, state, province, etc.")

    # Permit expiration date.
    expirationDate = AbsoluteDate(desc="Permit expiration date.")

    # Date that permit became official.
    effectiveDate = AbsoluteDate(desc="Date that permit became official.")

    # Permit identifier.
    permitID = Str(desc="Permit identifier.")

    #--------------------------------------------------------------------------
    #  Begin "AccessPermit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "payment", "applicationNumber", "expirationDate", "effectiveDate", "permitID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.AccessPermit",
        title="AccessPermit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccessPermit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkStatusEntry" class:
#------------------------------------------------------------------------------

class WorkStatusEntry(ActivityRecord):
    """ A type of ActivityRecord that records information about the status of an item, such as a Work or WorkTask, at a point in time.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Estimated percentage of completion of this individual work task or overall work order.
    percentComplete = PerCent(desc="Estimated percentage of completion of this individual work task or overall work order.")

    #--------------------------------------------------------------------------
    #  Begin "WorkStatusEntry" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "reason", "category", "severity", "createdDateTime", "percentComplete",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MarketFactors", "Documents", "Organisations", "ScheduledEvent", "Assets", "ErpPersons", "Locations", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.WorkStatusEntry",
        title="WorkStatusEntry",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkStatusEntry" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkTask" class:
#------------------------------------------------------------------------------

class WorkTask(Document):
    """ A set of tasks is required to implement a design.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ContractorItems = List(Instance("CIM.IEC61968.Informative.InfWork.ContractorItem"))

    # All Crews participating in this WorkTask.
    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"),
        desc="All Crews participating in this WorkTask.")

    WorkCostDetails = List(Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail"))

    Usages = List(Instance("CIM.IEC61968.Informative.InfWork.Usage"))

    QualificationRequirements = List(Instance("CIM.IEC61968.Informative.InfWork.QualificationRequirement"))

    Work = Instance("CIM.IEC61968.Work.Work",
        transient=True,
        opposite="WorkTasks",
        editor=InstanceEditor(name="_works"))

    def _get_works(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Work.Work" ]
        else:
            return []

    _works = Property(fget=_get_works)

    WorkFlowStep = Instance("CIM.IEC61968.Informative.InfWork.WorkFlowStep",
        transient=True,
        opposite="WorkTasks",
        editor=InstanceEditor(name="_workflowsteps"))

    def _get_workflowsteps(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkFlowStep" ]
        else:
            return []

    _workflowsteps = Property(fget=_get_workflowsteps)

    LaborItems = List(Instance("CIM.IEC61968.Informative.InfWork.LaborItem"))

    MaterialItems = List(Instance("CIM.IEC61968.Informative.InfWork.MaterialItem"))

    EquipmentItems = List(Instance("CIM.IEC61968.Informative.InfWork.EquipmentItem"))

    DesignLocationCUs = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocationCU"))

    OverheadCost = Instance("CIM.IEC61968.Informative.InfWork.OverheadCost",
        transient=True,
        opposite="WorkTasks",
        editor=InstanceEditor(name="_overheadcosts"))

    def _get_overheadcosts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.OverheadCost" ]
        else:
            return []

    _overheadcosts = Property(fget=_get_overheadcosts)

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    Capabilities = List(Instance("CIM.IEC61968.Informative.InfWork.Capability"))

    MiscCostItems = List(Instance("CIM.IEC61968.Informative.InfWork.MiscCostItem"))

    SwitchingSchedules = List(Instance("CIM.IEC61968.Informative.InfOperations.SwitchingSchedule"))

    Design = Instance("CIM.IEC61968.Informative.InfWork.Design",
        transient=True,
        opposite="WorkTasks",
        editor=InstanceEditor(name="_designs"))

    def _get_designs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Design" ]
        else:
            return []

    _designs = Property(fget=_get_designs)

    # If specified, override schedule and perform this task in accordance with instructions specified here.
    schedOverride = Str(desc="If specified, override schedule and perform this task in accordance with instructions specified here.")

    # The priority of this work task.
    priority = Str(desc="The priority of this work task.")

    #--------------------------------------------------------------------------
    #  Begin "WorkTask" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "schedOverride", "priority",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ContractorItems", "Crews", "WorkCostDetails", "Usages", "QualificationRequirements", "Work", "WorkFlowStep", "LaborItems", "MaterialItems", "EquipmentItems", "DesignLocationCUs", "OverheadCost", "Assets", "Capabilities", "MiscCostItems", "SwitchingSchedules", "Design",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.WorkTask",
        title="WorkTask",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkTask" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Request" class:
#------------------------------------------------------------------------------

class Request(Document):
    """ A request for work, service or project.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Organisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="Requests",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    Projects = List(Instance("CIM.IEC61968.Informative.InfWork.Project"))

    ErpQuoteLineItem = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem",
        transient=True,
        opposite="Request",
        editor=InstanceEditor(name="_erpquotelineitems"))

    def _get_erpquotelineitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem" ]
        else:
            return []

    _erpquotelineitems = Property(fget=_get_erpquotelineitems)

    Works = List(Instance("CIM.IEC61968.Work.Work"))

    # The corporate code for this request.
    corporateCode = Str(desc="The corporate code for this request.")

    # The priority of this request.
    priority = Str(desc="The priority of this request.")

    # Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created.
    actionNeeded = Str(desc="Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created.")

    #--------------------------------------------------------------------------
    #  Begin "Request" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateCode", "priority", "actionNeeded",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Organisation", "Projects", "ErpQuoteLineItem", "Works",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Request",
        title="Request",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Request" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CUAllowableAction" class:
#------------------------------------------------------------------------------

class CUAllowableAction(IdentifiedObject):
    """ Allowed actions: Install, Remove, Transfer, Abandon, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    #--------------------------------------------------------------------------
    #  Begin "CUAllowableAction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "CompatibleUnits", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CUAllowableAction",
        title="CUAllowableAction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CUAllowableAction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Project" class:
#------------------------------------------------------------------------------

class Project(Document):
    """ A collection of related work. For construction projects and maintenance projects, multiple phases may be performed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpProjectAccounting = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpProjectAccounting",
        transient=True,
        opposite="Projects",
        editor=InstanceEditor(name="_erpprojectaccountings"))

    def _get_erpprojectaccountings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpProjectAccounting" ]
        else:
            return []

    _erpprojectaccountings = Property(fget=_get_erpprojectaccountings)

    Works = List(Instance("CIM.IEC61968.Work.Work"))

    BusinessCase = Instance("CIM.IEC61968.Informative.InfWork.BusinessCase",
        transient=True,
        opposite="Projects",
        editor=InstanceEditor(name="_businesscases"))

    def _get_businesscases(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.BusinessCase" ]
        else:
            return []

    _businesscases = Property(fget=_get_businesscases)

    Requests = List(Instance("CIM.IEC61968.Informative.InfWork.Request"))

    ParentProject = Instance("CIM.IEC61968.Informative.InfWork.Project",
        transient=True,
        opposite="SubProjects",
        editor=InstanceEditor(name="_projects"))

    def _get_projects(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Project" ]
        else:
            return []

    _projects = Property(fget=_get_projects)

    SubProjects = List(Instance("CIM.IEC61968.Informative.InfWork.Project"))

    # Overall project budget.
    budget = Money(desc="Overall project budget.")

    #--------------------------------------------------------------------------
    #  Begin "Project" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "budget",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpProjectAccounting", "Works", "BusinessCase", "Requests", "ParentProject", "SubProjects",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Project",
        title="Project",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Project" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CUAsset" class:
#------------------------------------------------------------------------------

class CUAsset(IdentifiedObject):
    """ Compatible unit for various types of assets such as transformers switches, substation fences, poles, etc..
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    TypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.TypeAsset",
        transient=True,
        opposite="CUAsset",
        editor=InstanceEditor(name="_typeassets"))

    def _get_typeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.TypeAsset" ]
        else:
            return []

    _typeassets = Property(fget=_get_typeassets)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Quantity of the type asset within the CU.
    quantity = IntegerQuantity(desc="Quantity of the type asset within the CU.")

    # The code for this type of asset.
    typeAssetCode = Str(desc="The code for this type of asset.")

    #--------------------------------------------------------------------------
    #  Begin "CUAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "quantity", "typeAssetCode",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "CompatibleUnits", "TypeAsset", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CUAsset",
        title="CUAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CUAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PropertyUnit" class:
#------------------------------------------------------------------------------

class PropertyUnit(IdentifiedObject):
    """ Unit of property for reporting purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CUMaterialItems = List(Instance("CIM.IEC61968.Informative.InfWork.CUMaterialItem"))

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    WorkCostDetails = List(Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail"))

    # Activity code identifies a specific and distinguishable work action.
    activityCode = WorkActionKind(desc="Activity code identifies a specific and distinguishable work action.")

    # A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications.
    accountingUsage = Str(desc="A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications.")

    # Used for property record accounting. For example, in the USA, this would be a FERC account.
    propertyAccount = Str(desc="Used for property record accounting. For example, in the USA, this would be a FERC account.")

    #--------------------------------------------------------------------------
    #  Begin "PropertyUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "activityCode", "accountingUsage", "propertyAccount",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "CUMaterialItems", "CompatibleUnits", "status", "WorkCostDetails",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.PropertyUnit",
        title="PropertyUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PropertyUnit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "InspectionDataSet" class:
#------------------------------------------------------------------------------

class InspectionDataSet(ProcedureDataSet):
    """ Documents the result of one inspection, a type of Procedure, for a given attribute of an asset.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    AccordingToSchedules = List(Instance("CIM.IEC61968.Informative.InfCommon.ScheduleParameterInfo"))

    # Description of the conditions of the location where the asset resides.
    locationCondition = Str(desc="Description of the conditions of the location where the asset resides.")

    #--------------------------------------------------------------------------
    #  Begin "InspectionDataSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "completedDateTime", "locationCondition",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Procedure", "Properties", "MeasurementValues", "TransformerObservations", "AccordingToSchedules",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.InspectionDataSet",
        title="InspectionDataSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "InspectionDataSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CostType" class:
#------------------------------------------------------------------------------

class CostType(IdentifiedObject):
    """ A categorization for resources, often costs, in accounting transactions. Examples include: material components, building in service, coal sales, overhead, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkCostDetails = List(Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail"))

    ErpJournalEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpJournalEntry"))

    ChildCostTypes = List(Instance("CIM.IEC61968.Informative.InfWork.CostType"))

    ParentCostType = Instance("CIM.IEC61968.Informative.InfWork.CostType",
        transient=True,
        opposite="ChildCostTypes",
        editor=InstanceEditor(name="_costtypes"))

    def _get_costtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.CostType" ]
        else:
            return []

    _costtypes = Property(fget=_get_costtypes)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    # A codified representation of the resource element.
    code = Str(desc="A codified representation of the resource element.")

    # True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components).
    amountAssignmentFlag = Bool(desc="True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components).")

    # The level of the resource element in the hierarchy of resource elements (recursive relationship).
    level = Str(desc="The level of the resource element in the hierarchy of resource elements (recursive relationship).")

    # The stage for which this costType applies: estimated design, estimated actual or actual actual.
    stage = Str(desc="The stage for which this costType applies: estimated design, estimated actual or actual actual.")

    #--------------------------------------------------------------------------
    #  Begin "CostType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "amountAssignmentFlag", "level", "stage",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "WorkCostDetails", "ErpJournalEntries", "ChildCostTypes", "ParentCostType", "status", "CompatibleUnits",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CostType",
        title="CostType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CostType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkCostSummary" class:
#------------------------------------------------------------------------------

class WorkCostSummary(Document):
    """ A roll up by cost category for the entire cost of a work order. For example, total labor.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkCostDetail = Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail",
        transient=True,
        opposite="WorkCostSummary",
        editor=InstanceEditor(name="_workcostdetails"))

    def _get_workcostdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkCostDetail" ]
        else:
            return []

    _workcostdetails = Property(fget=_get_workcostdetails)

    #--------------------------------------------------------------------------
    #  Begin "WorkCostSummary" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "WorkCostDetail",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.WorkCostSummary",
        title="WorkCostSummary",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkCostSummary" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MiscCostItem" class:
#------------------------------------------------------------------------------

class MiscCostItem(IdentifiedObject):
    """ Various cost items that are not associated with compatible units. Examples include rental equipment, labor, materials, contractor costs, permits - anything not covered in a CU.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkCostDetail = Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail",
        transient=True,
        opposite="MiscCostItems",
        editor=InstanceEditor(name="_workcostdetails"))

    def _get_workcostdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkCostDetail" ]
        else:
            return []

    _workcostdetails = Property(fget=_get_workcostdetails)

    DesignLocation = Instance("CIM.IEC61968.Informative.InfWork.DesignLocation",
        transient=True,
        opposite="MiscCostItems",
        editor=InstanceEditor(name="_designlocations"))

    def _get_designlocations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.DesignLocation" ]
        else:
            return []

    _designlocations = Property(fget=_get_designlocations)

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="MiscCostItems",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # The cost per unit for this misc. item.
    costPerUnit = Money(desc="The cost per unit for this misc. item.")

    # External Reference ID (e.g. PO#, Serial #)
    externalRefID = Str(desc="External Reference ID (e.g. PO#, Serial #)")

    # The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead.
    costType = Str(desc="The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead.")

    # The quantity of the misc. item being assigned to this location.
    quantity = IntegerQuantity(desc="The quantity of the misc. item being assigned to this location.")

    # This drives the accounting treatment for this misc. item.
    account = Str(desc="This drives the accounting treatment for this misc. item.")

    #--------------------------------------------------------------------------
    #  Begin "MiscCostItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "costPerUnit", "externalRefID", "costType", "quantity", "account",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "WorkCostDetail", "DesignLocation", "WorkTask", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.MiscCostItem",
        title="MiscCostItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MiscCostItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CULaborItem" class:
#------------------------------------------------------------------------------

class CULaborItem(IdentifiedObject):
    """ Compatible unit labor item.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    QualificationRequirements = List(Instance("CIM.IEC61968.Informative.InfWork.QualificationRequirement"))

    CULaborCode = Instance("CIM.IEC61968.Informative.InfWork.CULaborCode",
        transient=True,
        opposite="CULaborItems",
        editor=InstanceEditor(name="_culaborcodes"))

    def _get_culaborcodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.CULaborCode" ]
        else:
            return []

    _culaborcodes = Property(fget=_get_culaborcodes)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    # The labor rate applied for work.
    laborRate = CostRate(desc="The labor rate applied for work.")

    # Activity code identifies a specific and distinguishable unit of work.
    activityCode = Str(desc="Activity code identifies a specific and distinguishable unit of work.")

    # Estimated time to perform work.
    laborDuration = Hours(desc="Estimated time to perform work.")

    #--------------------------------------------------------------------------
    #  Begin "CULaborItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "laborRate", "activityCode", "laborDuration",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "QualificationRequirements", "CULaborCode", "status", "CompatibleUnits",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CULaborItem",
        title="CULaborItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CULaborItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CULaborCode" class:
#------------------------------------------------------------------------------

class CULaborCode(IdentifiedObject):
    """ Labor code associated with various compatible unit labor items.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CULaborItems = List(Instance("CIM.IEC61968.Informative.InfWork.CULaborItem"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Labor code.
    code = Str(desc="Labor code.")

    #--------------------------------------------------------------------------
    #  Begin "CULaborCode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "CULaborItems", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CULaborCode",
        title="CULaborCode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CULaborCode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShiftPattern" class:
#------------------------------------------------------------------------------

class ShiftPattern(IdentifiedObject):
    """ The patterns of shifts worked by people or crews.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
    validityInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Date and time interval for which this shift pattern is valid (when it became effective and when it expires).",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Number of cycles for a temporary shift.
    cycleCount = Int(desc="Number of cycles for a temporary shift.")

    # Type of assignement intended to be worked on this shift, for example, temporary, standard, etc.
    assignmentType = Str(desc="Type of assignement intended to be worked on this shift, for example, temporary, standard, etc.")

    #--------------------------------------------------------------------------
    #  Begin "ShiftPattern" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cycleCount", "assignmentType",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "validityInterval", "Crews", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.ShiftPattern",
        title="ShiftPattern",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShiftPattern" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OverheadCost" class:
#------------------------------------------------------------------------------

class OverheadCost(IdentifiedObject):
    """ Overhead cost applied to work order.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkCostDetails = List(Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail"))

    WorkTasks = List(Instance("CIM.IEC61968.Informative.InfWork.WorkTask"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # The overhead cost to be applied.
    cost = Money(desc="The overhead cost to be applied.")

    # Overhead code.
    code = Str(desc="Overhead code.")

    #--------------------------------------------------------------------------
    #  Begin "OverheadCost" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cost", "code",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "WorkCostDetails", "WorkTasks", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.OverheadCost",
        title="OverheadCost",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OverheadCost" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DesignLocationCU" class:
#------------------------------------------------------------------------------

class DesignLocationCU(IdentifiedObject):
    """ Compatible unit at a given design location.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Designs = List(Instance("CIM.IEC61968.Informative.InfWork.Design"))

    DesignLocation = Instance("CIM.IEC61968.Informative.InfWork.DesignLocation",
        transient=True,
        opposite="DesignLocationCUs",
        editor=InstanceEditor(name="_designlocations"))

    def _get_designlocations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.DesignLocation" ]
        else:
            return []

    _designlocations = Property(fget=_get_designlocations)

    CUGroups = List(Instance("CIM.IEC61968.Informative.InfWork.CUGroup"))

    ConditionFactors = List(Instance("CIM.IEC61968.Informative.InfWork.ConditionFactor"))

    WorkTasks = List(Instance("CIM.IEC61968.Informative.InfWork.WorkTask"))

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # A code that instructs the crew what action to perform.
    cuAction = WorkActionKind(desc="A code that instructs the crew what action to perform.")

    # Year when a CU that represents an asset is removed.
    removalYear = AbsoluteDate(desc="Year when a CU that represents an asset is removed.")

    # As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation.
    cuUsage = Str(desc="As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation.")

    # A code that helps direct accounting (capital, expense, or accounting treatment).
    cuAccount = Str(desc="A code that helps direct accounting (capital, expense, or accounting treatment).")

    # The quantity of the CU being assigned to this location.
    cuQuantity = IntegerQuantity(desc="The quantity of the CU being assigned to this location.")

    # True if associated electrical equipment is intended to be energized while work is being performed.
    energizationFlag = Bool(desc="True if associated electrical equipment is intended to be energized while work is being performed.")

    #--------------------------------------------------------------------------
    #  Begin "DesignLocationCU" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cuAction", "removalYear", "cuUsage", "cuAccount", "cuQuantity", "energizationFlag",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Designs", "DesignLocation", "CUGroups", "ConditionFactors", "WorkTasks", "CompatibleUnits", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.DesignLocationCU",
        title="DesignLocationCU",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DesignLocationCU" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkFlowStep" class:
#------------------------------------------------------------------------------

class WorkFlowStep(IdentifiedObject):
    """ A pre-defined set of work steps for a given type of work.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Work = Instance("CIM.IEC61968.Work.Work",
        transient=True,
        opposite="WorkFlowSteps",
        editor=InstanceEditor(name="_works"))

    def _get_works(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Work.Work" ]
        else:
            return []

    _works = Property(fget=_get_works)

    WorkTasks = List(Instance("CIM.IEC61968.Informative.InfWork.WorkTask"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow.
    sequenceNumber = Int(desc="Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow.")

    #--------------------------------------------------------------------------
    #  Begin "WorkFlowStep" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sequenceNumber",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Work", "WorkTasks", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.WorkFlowStep",
        title="WorkFlowStep",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkFlowStep" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConditionFactor" class:
#------------------------------------------------------------------------------

class ConditionFactor(IdentifiedObject):
    """ This is to specify the various condition factors for a design that may alter the cost estimate or the allocation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    DesignLocationCUs = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocationCU"))

    DesignLocations = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocation"))

    Designs = List(Instance("CIM.IEC61968.Informative.InfWork.Design"))

    # Kind of this condition factor.
    kind = ConditionFactorKind(desc="Kind of this condition factor.")

    # The actual value of the condition factor, such as labor flat fee or percentage.
    cfValue = Str(desc="The actual value of the condition factor, such as labor flat fee or percentage.")

    #--------------------------------------------------------------------------
    #  Begin "ConditionFactor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "cfValue",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "DesignLocationCUs", "DesignLocations", "Designs",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.ConditionFactor",
        title="ConditionFactor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConditionFactor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OneCallRequest" class:
#------------------------------------------------------------------------------

class OneCallRequest(Document):
    """ A request for other utilities to mark their underground facilities prior to commencement of construction and/or maintenance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkLocations = List(Instance("CIM.IEC61968.Informative.InfWork.WorkLocation"))

    # Instructions for marking a dig area, if applicable.
    markingInstruction = Str(desc="Instructions for marking a dig area, if applicable.")

    # True if work location has been marked, for example for a dig area.
    markedIndicator = Bool(desc="True if work location has been marked, for example for a dig area.")

    # True if explosives have been or are planned to be used.
    explosivesUsed = Bool(desc="True if explosives have been or are planned to be used.")

    #--------------------------------------------------------------------------
    #  Begin "OneCallRequest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "markingInstruction", "markedIndicator", "explosivesUsed",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "WorkLocations",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.OneCallRequest",
        title="OneCallRequest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OneCallRequest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Assignment" class:
#------------------------------------------------------------------------------

class Assignment(Document):
    """ An assignment is given to an ErpPerson, Crew, Organisation, Equipment Item, Tool, etc. and may be used to perform Work, WorkTasks, Procedures, etc. TimeSchedules may be set up directly for Assignments or indirectly via the associated WorkTask. Note that these associations are all inherited through the recursive relationship on Document.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All Crews having this Assignment.
    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"),
        desc="All Crews having this Assignment.")

    # Period between the assignment becoming effective and its expiration.
    effectivePeriod = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Period between the assignment becoming effective and its expiration.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    #--------------------------------------------------------------------------
    #  Begin "Assignment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Crews", "effectivePeriod",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Assignment",
        title="Assignment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Assignment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "QualificationRequirement" class:
#------------------------------------------------------------------------------

class QualificationRequirement(IdentifiedObject):
    """ Certain skills are required and must be certified in order for a person (typically a member of a crew) to be qualified to work on types of equipment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Specifications = List(Instance("CIM.IEC61968.Informative.InfAssets.Specification"))

    WorkTasks = List(Instance("CIM.IEC61968.Informative.InfWork.WorkTask"))

    CULaborItems = List(Instance("CIM.IEC61968.Informative.InfWork.CULaborItem"))

    Skills = List(Instance("CIM.IEC61968.Informative.InfCommon.Skill"))

    # Qualification identifier.
    qualificationID = Str(desc="Qualification identifier.")

    #--------------------------------------------------------------------------
    #  Begin "QualificationRequirement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "qualificationID",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Specifications", "WorkTasks", "CULaborItems", "Skills",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.QualificationRequirement",
        title="QualificationRequirement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "QualificationRequirement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Crew" class:
#------------------------------------------------------------------------------

class Crew(IdentifiedObject):
    """ A crew is a group of people (ErpPersons) with specific skills, tools, and vehicles.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Capabilities = List(Instance("CIM.IEC61968.Informative.InfWork.Capability"))

    # All WorkTasks this Crew participates in.
    WorkTasks = List(Instance("CIM.IEC61968.Informative.InfWork.WorkTask"),
        desc="All WorkTasks this Crew participates in.")

    Vehicles = List(Instance("CIM.IEC61968.Informative.InfAssets.Vehicle"))

    # All ErpPersons that are members of this Crew.
    CrewMembers = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"),
        desc="All ErpPersons that are members of this Crew.")

    # All Assignments for this Crew.
    Assignments = List(Instance("CIM.IEC61968.Informative.InfWork.Assignment"),
        desc="All Assignments for this Crew.")

    Tools = List(Instance("CIM.IEC61968.Informative.InfAssets.Tool"))

    Route = Instance("CIM.IEC61968.Informative.InfLocations.Route",
        transient=True,
        opposite="Crews",
        editor=InstanceEditor(name="_routes"))

    def _get_routes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfLocations.Route" ]
        else:
            return []

    _routes = Property(fget=_get_routes)

    OutageSteps = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageStep"))

    WorkEquipmentAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.WorkEquipmentAsset"))

    Locations = List(Instance("CIM.IEC61968.Common.Location"))

    ShiftPatterns = List(Instance("CIM.IEC61968.Informative.InfWork.ShiftPattern"))

    # All SwitchingSchedules executed by this Crew.
    SwitchingSchedules = List(Instance("CIM.IEC61968.Informative.InfOperations.SwitchingSchedule"),
        desc="All SwitchingSchedules executed by this Crew.")

    Organisations = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation"))

    # Category by utility's work management standards and practices.
    category = Str(desc="Category by utility's work management standards and practices.")

    #--------------------------------------------------------------------------
    #  Begin "Crew" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Capabilities", "WorkTasks", "Vehicles", "CrewMembers", "Assignments", "Tools", "Route", "OutageSteps", "WorkEquipmentAssets", "Locations", "ShiftPatterns", "SwitchingSchedules", "Organisations",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.Crew",
        title="Crew",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Crew" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DiagnosisDataSet" class:
#------------------------------------------------------------------------------

class DiagnosisDataSet(ProcedureDataSet):
    """ The result of a problem (typically an asset failure) diagnosis.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Phase(s) diagnosed.
    phaseCode = PhaseCode(desc="Phase(s) diagnosed.")

    # Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other.
    failureMode = Str(desc="Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other.")

    # Remarks pertaining to root cause findings during problem diagnosis.
    rootRemark = Str(desc="Remarks pertaining to root cause findings during problem diagnosis.")

    # Root cause of problem determined during diagnosis.
    rootCause = Str(desc="Root cause of problem determined during diagnosis.")

    # Origin of problem determined during diagnosis.
    finalOrigin = Str(desc="Origin of problem determined during diagnosis.")

    # Cause of problem determined during diagnosis.
    finalCause = Str(desc="Cause of problem determined during diagnosis.")

    # Code for problem category determined during preliminary assessment.
    preliminaryCode = Str(desc="Code for problem category determined during preliminary assessment.")

    # Effect of problem.
    effect = Str(desc="Effect of problem.")

    # Remarks pertaining to preliminary assessment of problem.
    preliminaryRemark = Str(desc="Remarks pertaining to preliminary assessment of problem.")

    # Root origin of problem determined during diagnosis.
    rootOrigin = Str(desc="Root origin of problem determined during diagnosis.")

    # Code for diagnosed probem category.
    finalCode = Str(desc="Code for diagnosed probem category.")

    # Remarks pertaining to findings during problem diagnosis.
    finalRemark = Str(desc="Remarks pertaining to findings during problem diagnosis.")

    # Date and time preliminary assessment of problem was performed.
    preliminaryDateTime = Date(desc="Date and time preliminary assessment of problem was performed.")

    #--------------------------------------------------------------------------
    #  Begin "DiagnosisDataSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "completedDateTime", "phaseCode", "failureMode", "rootRemark", "rootCause", "finalOrigin", "finalCause", "preliminaryCode", "effect", "preliminaryRemark", "rootOrigin", "finalCode", "finalRemark", "preliminaryDateTime",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Procedure", "Properties", "MeasurementValues", "TransformerObservations",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.DiagnosisDataSet",
        title="DiagnosisDataSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DiagnosisDataSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ContractorItem" class:
#------------------------------------------------------------------------------

class ContractorItem(IdentifiedObject):
    """ Contractor information for work task.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="ContractorItems",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    WorkCostDetail = Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail",
        transient=True,
        opposite="ContractorItems",
        editor=InstanceEditor(name="_workcostdetails"))

    def _get_workcostdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkCostDetail" ]
        else:
            return []

    _workcostdetails = Property(fget=_get_workcostdetails)

    ErpPayables = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPayable"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # The total amount charged.
    cost = Money(desc="The total amount charged.")

    # The amount that a given contractor will charge for performing this unit of work.
    bidAmount = Money(desc="The amount that a given contractor will charge for performing this unit of work.")

    # Activity code identifies a specific and distinguishable unit of work.
    activityCode = Str(desc="Activity code identifies a specific and distinguishable unit of work.")

    #--------------------------------------------------------------------------
    #  Begin "ContractorItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cost", "bidAmount", "activityCode",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "WorkTask", "WorkCostDetail", "ErpPayables", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.ContractorItem",
        title="ContractorItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ContractorItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CUGroup" class:
#------------------------------------------------------------------------------

class CUGroup(IdentifiedObject):
    """ A Compatible Unit Group identifies a set of compatible units which may be jointly utilized for estimating and designating jobs.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ParentCUGroups = List(Instance("CIM.IEC61968.Informative.InfWork.CUGroup"))

    ChildCUGroups = List(Instance("CIM.IEC61968.Informative.InfWork.CUGroup"))

    DesignLocationCUs = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocationCU"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    #--------------------------------------------------------------------------
    #  Begin "CUGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ParentCUGroups", "ChildCUGroups", "DesignLocationCUs", "status", "CompatibleUnits",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CUGroup",
        title="CUGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CUGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CUWorkEquipmentItem" class:
#------------------------------------------------------------------------------

class CUWorkEquipmentItem(IdentifiedObject):
    """ Compatible unit for various types of WorkEquipmentAssets, including vehicles.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    TypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.TypeAsset",
        transient=True,
        opposite="CUWorkEquipmentAsset",
        editor=InstanceEditor(name="_typeassets"))

    def _get_typeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.TypeAsset" ]
        else:
            return []

    _typeassets = Property(fget=_get_typeassets)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # The equipment type code.
    equipCode = Str(desc="The equipment type code.")

    # Standard usage rate for the type of vehicle.
    rate = CostRate(desc="Standard usage rate for the type of vehicle.")

    #--------------------------------------------------------------------------
    #  Begin "CUWorkEquipmentItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "equipCode", "rate",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "CompatibleUnits", "TypeAsset", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.CUWorkEquipmentItem",
        title="CUWorkEquipmentItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CUWorkEquipmentItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkLocation" class:
#------------------------------------------------------------------------------

class WorkLocation(Location):
    """ Information about a particular location for various forms of work such as a one call request.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OneCallRequest = Instance("CIM.IEC61968.Informative.InfWork.OneCallRequest",
        transient=True,
        opposite="WorkLocations",
        editor=InstanceEditor(name="_onecallrequests"))

    def _get_onecallrequests(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.OneCallRequest" ]
        else:
            return []

    _onecallrequests = Property(fget=_get_onecallrequests)

    DesignLocations = List(Instance("CIM.IEC61968.Informative.InfWork.DesignLocation"))

    # Name, identifier, or description of the block, if applicable, in which work is to occur.
    block = Str(desc="Name, identifier, or description of the block, if applicable, in which work is to occur.")

    # The names of streets at the nearest intersection to work area.
    nearestIntersection = Str(desc="The names of streets at the nearest intersection to work area.")

    # Name, identifier, or description of the subdivision, if applicable, in which work is to occur.
    subdivision = Str(desc="Name, identifier, or description of the subdivision, if applicable, in which work is to occur.")

    # Name, identifier, or description of the lot, if applicable, in which work is to occur.
    lot = Str(desc="Name, identifier, or description of the lot, if applicable, in which work is to occur.")

    #--------------------------------------------------------------------------
    #  Begin "WorkLocation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference", "block", "nearestIntersection", "subdivision", "lot",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords", "OneCallRequest", "DesignLocations",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.WorkLocation",
        title="WorkLocation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkLocation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkCostDetail" class:
#------------------------------------------------------------------------------

class WorkCostDetail(Document):
    """ A collection of all of the individual cost items collected from multiple sources.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OverheadCost = Instance("CIM.IEC61968.Informative.InfWork.OverheadCost",
        transient=True,
        opposite="WorkCostDetails",
        editor=InstanceEditor(name="_overheadcosts"))

    def _get_overheadcosts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.OverheadCost" ]
        else:
            return []

    _overheadcosts = Property(fget=_get_overheadcosts)

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="WorkCostDetails",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    LaborItems = List(Instance("CIM.IEC61968.Informative.InfWork.LaborItem"))

    ErpProjectAccounting = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpProjectAccounting",
        transient=True,
        opposite="WorkCostDetails",
        editor=InstanceEditor(name="_erpprojectaccountings"))

    def _get_erpprojectaccountings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpProjectAccounting" ]
        else:
            return []

    _erpprojectaccountings = Property(fget=_get_erpprojectaccountings)

    EquipmentItems = List(Instance("CIM.IEC61968.Informative.InfWork.EquipmentItem"))

    WorkCostSummary = Instance("CIM.IEC61968.Informative.InfWork.WorkCostSummary",
        transient=True,
        opposite="WorkCostDetail",
        editor=InstanceEditor(name="_workcostsummarys"))

    def _get_workcostsummarys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkCostSummary" ]
        else:
            return []

    _workcostsummarys = Property(fget=_get_workcostsummarys)

    Design = Instance("CIM.IEC61968.Informative.InfWork.Design",
        transient=True,
        opposite="WorkCostDetails",
        editor=InstanceEditor(name="_designs"))

    def _get_designs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Design" ]
        else:
            return []

    _designs = Property(fget=_get_designs)

    MiscCostItems = List(Instance("CIM.IEC61968.Informative.InfWork.MiscCostItem"))

    CostType = Instance("CIM.IEC61968.Informative.InfWork.CostType",
        transient=True,
        opposite="WorkCostDetails",
        editor=InstanceEditor(name="_costtypes"))

    def _get_costtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.CostType" ]
        else:
            return []

    _costtypes = Property(fget=_get_costtypes)

    Works = List(Instance("CIM.IEC61968.Work.Work"))

    ContractorItems = List(Instance("CIM.IEC61968.Informative.InfWork.ContractorItem"))

    MaterialItems = List(Instance("CIM.IEC61968.Informative.InfWork.MaterialItem"))

    PropertyUnits = List(Instance("CIM.IEC61968.Informative.InfWork.PropertyUnit"))

    # Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other.
    amount = Money(desc="Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other.")

    # True if 'amount' is a debit, false if it is a credit.
    isDebit = Bool(desc="True if 'amount' is a debit, false if it is a credit.")

    # Date and time that 'amount' is posted to the work.
    transactionDateTime = Date(desc="Date and time that 'amount' is posted to the work.")

    # Type of work cost.
    type = Str(desc="Type of work cost.")

    #--------------------------------------------------------------------------
    #  Begin "WorkCostDetail" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "amount", "isDebit", "transactionDateTime", "type",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "OverheadCost", "WorkTask", "LaborItems", "ErpProjectAccounting", "EquipmentItems", "WorkCostSummary", "Design", "MiscCostItems", "CostType", "Works", "ContractorItems", "MaterialItems", "PropertyUnits",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.WorkCostDetail",
        title="WorkCostDetail",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkCostDetail" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquipmentItem" class:
#------------------------------------------------------------------------------

class EquipmentItem(IdentifiedObject):
    """ An equipment item, such as a vehicle, used for a work order.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkCostDetail = Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail",
        transient=True,
        opposite="EquipmentItems",
        editor=InstanceEditor(name="_workcostdetails"))

    def _get_workcostdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkCostDetail" ]
        else:
            return []

    _workcostdetails = Property(fget=_get_workcostdetails)

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="EquipmentItems",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # The cost for vehicle usage.
    cost = Money(desc="The cost for vehicle usage.")

    # Code for type of vehicle.
    code = Str(desc="Code for type of vehicle.")

    #--------------------------------------------------------------------------
    #  Begin "EquipmentItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cost", "code",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "WorkCostDetail", "WorkTask", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.EquipmentItem",
        title="EquipmentItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquipmentItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusinessCase" class:
#------------------------------------------------------------------------------

class BusinessCase(Document):
    """ Business justification for capital expenditures, usually addressing operations and maintenance costs as well.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Works = List(Instance("CIM.IEC61968.Work.Work"))

    Projects = List(Instance("CIM.IEC61968.Informative.InfWork.Project"))

    # A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.).
    corporateCode = Str(desc="A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.).")

    #--------------------------------------------------------------------------
    #  Begin "BusinessCase" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateCode",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Works", "Projects",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfWork.BusinessCase",
        title="BusinessCase",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusinessCase" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
