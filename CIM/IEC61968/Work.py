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

""" This package contains the core information classes that support work management and network extension planning applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Common import Document



from enthought.traits.api import Instance, List, Property, Enum, Date, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of work.
WorkKind = Enum("service", "reconnect", "disconnect", "other", "meter", "construction", "inspection", "maintenance", desc="Kind of work.")

#------------------------------------------------------------------------------
#  "Work" class:
#------------------------------------------------------------------------------

class Work(Document):
    """ Document used to request, initiate, track and record work. This is synonymous with Work Breakdown Structure (WBS), which is traversed through the (currently informative) recursive association of Work. Note that the work name is equal to the WBS name, which is given in the inherited 'name' attribute.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkFlowSteps = List(Instance("CIM.IEC61968.Informative.InfWork.WorkFlowStep"))

    # All the customers for which this work is performed.
    Customers = List(Instance("CIM.IEC61968.Customers.Customer"),
        desc="All the customers for which this work is performed.")

    WorkTasks = List(Instance("CIM.IEC61968.Informative.InfWork.WorkTask"))

    ErpProjectAccounting = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpProjectAccounting",
        transient=True,
        opposite="Works",
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

    Project = Instance("CIM.IEC61968.Informative.InfWork.Project",
        transient=True,
        opposite="Works",
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

    Designs = List(Instance("CIM.IEC61968.Informative.InfWork.Design"))

    BusinessCase = Instance("CIM.IEC61968.Informative.InfWork.BusinessCase",
        transient=True,
        opposite="Works",
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

    WorkBillingInfo = Instance("CIM.IEC61968.Informative.InfCustomers.WorkBillingInfo",
        transient=True,
        opposite="Works",
        editor=InstanceEditor(name="_workbillinginfos"))

    def _get_workbillinginfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCustomers.WorkBillingInfo" ]
        else:
            return []

    _workbillinginfos = Property(fget=_get_workbillinginfos)

    WorkCostDetails = List(Instance("CIM.IEC61968.Informative.InfWork.WorkCostDetail"))

    Request = Instance("CIM.IEC61968.Informative.InfWork.Request",
        transient=True,
        opposite="Works",
        editor=InstanceEditor(name="_requests"))

    def _get_requests(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Request" ]
        else:
            return []

    _requests = Property(fget=_get_requests)

    # Kind of work.
    kind = WorkKind(desc="Kind of work.")

    # Date and time work was requested.
    requestDateTime = Date(desc="Date and time work was requested.")

    # Priority of work.
    priority = Str(desc="Priority of work.")

    #--------------------------------------------------------------------------
    #  Begin "Work" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind", "requestDateTime", "priority",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "WorkFlowSteps", "Customers", "WorkTasks", "ErpProjectAccounting", "Project", "Designs", "BusinessCase", "WorkBillingInfo", "WorkCostDetails", "Request",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Work.Work",
        title="Work",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Work" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
