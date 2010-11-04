# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

"""TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Documentation package is used for the modeling of business documents. Some of these may be electronic realizations of legacy paper document, and some may be electronic information exchanges or collections. Documents will typically reference or describe one or more CIM objects. The DataSets package is used to describe documents tyically used for exchange of collections of object descriptions (e.g., NetworkDataSet). The operational package is used to define documents related to distribution operations business processes (e.g., OperationalRestriction, SwitchingSchedule). TroubleTickets are used by Customers to report problems related to the elctrical distribution network. TroubleTickets may be grouped and be related to a PlannedOutage, OutageNotification and/or PowerSystemResource. The Outage package defines classes related to outage management (OutageStep, OutageRecord, OutageReport).'
"""

ns_prefix = "cimInfOperations"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfOperations"

from CIM14v13.IEC61968.Informative.InfOperations.SwitchingStep import SwitchingStep
from CIM14v13.IEC61968.Informative.InfOperations.ErpPersonScheduleStepRole import ErpPersonScheduleStepRole
from CIM14v13.IEC61968.Informative.InfOperations.OperationalRestriction import OperationalRestriction
from CIM14v13.IEC61968.Informative.InfOperations.SafetyDocument import SafetyDocument
from CIM14v13.IEC61968.Informative.InfOperations.OutageStep import OutageStep
from CIM14v13.IEC61968.Informative.InfOperations.ComplianceEvent import ComplianceEvent
from CIM14v13.IEC61968.Informative.InfOperations.PSREvent import PSREvent
from CIM14v13.IEC61968.Informative.InfOperations.OutageCode import OutageCode
from CIM14v13.IEC61968.Informative.InfOperations.OutageStepPsrRole import OutageStepPsrRole
from CIM14v13.IEC61968.Informative.InfOperations.NetworkDataSet import NetworkDataSet
from CIM14v13.IEC61968.Informative.InfOperations.CircuitSection import CircuitSection
from CIM14v13.IEC61968.Informative.InfOperations.OutageRecord import OutageRecord
from CIM14v13.IEC61968.Informative.InfOperations.CallBack import CallBack
from CIM14v13.IEC61968.Informative.InfOperations.ChangeItem import ChangeItem
from CIM14v13.IEC61968.Informative.InfOperations.OrgPsrRole import OrgPsrRole
from CIM14v13.IEC61968.Informative.InfOperations.OutageNotification import OutageNotification
from CIM14v13.IEC61968.Informative.InfOperations.SwitchingSchedule import SwitchingSchedule
from CIM14v13.IEC61968.Informative.InfOperations.IncidentCode import IncidentCode
from CIM14v13.IEC61968.Informative.InfOperations.PlannedOutage import PlannedOutage
from CIM14v13.IEC61968.Informative.InfOperations.TroubleTicket import TroubleTicket
from CIM14v13.IEC61968.Informative.InfOperations.IncidentRecord import IncidentRecord
from CIM14v13.IEC61968.Informative.InfOperations.ChangeSet import ChangeSet
from CIM14v13.IEC61968.Informative.InfOperations.OutageReport import OutageReport
from CIM14v13.IEC61968.Informative.InfOperations.LandBase import LandBase
from CIM14v13.IEC61968.Informative.InfOperations.Circuit import Circuit
