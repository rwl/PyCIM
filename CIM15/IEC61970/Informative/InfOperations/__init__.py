# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Documentation package is used for the modeling of business documents. Some of these may be electronic realizations of legacy paper document, and some may be electronic information exchanges or collections. Documents will typically reference or describe one or more CIM objects. The DataSets package is used to describe documents tyically used for exchange of collections of object descriptions (e.g., NetworkDataSet). The operational package is used to define documents related to distribution operations business processes (e.g., OperationalRestriction, SwitchingSchedule). TroubleTickets are used by Customers to report problems related to the elctrical distribution network. TroubleTickets may be grouped and be related to a PlannedOutage, OutageNotification and/or PowerSystemResource. The Outage package defines classes related to outage management (OutageStep, OutageRecord, OutageReport).'
"""

from CIM15.IEC61970.Informative.InfOperations.OutageRecord import OutageRecord
from CIM15.IEC61970.Informative.InfOperations.OutageReport import OutageReport
from CIM15.IEC61970.Informative.InfOperations.ChangeItem import ChangeItem
from CIM15.IEC61970.Informative.InfOperations.PSREvent import PSREvent
from CIM15.IEC61970.Informative.InfOperations.PlannedOutage import PlannedOutage
from CIM15.IEC61970.Informative.InfOperations.CircuitSection import CircuitSection
from CIM15.IEC61970.Informative.InfOperations.SafetyDocument import SafetyDocument
from CIM15.IEC61970.Informative.InfOperations.OperationalRestriction import OperationalRestriction
from CIM15.IEC61970.Informative.InfOperations.ChangeSet import ChangeSet
from CIM15.IEC61970.Informative.InfOperations.SwitchingSchedule import SwitchingSchedule
from CIM15.IEC61970.Informative.InfOperations.Circuit import Circuit
from CIM15.IEC61970.Informative.InfOperations.NetworkDataSet import NetworkDataSet
from CIM15.IEC61970.Informative.InfOperations.OutageStep import OutageStep
from CIM15.IEC61970.Informative.InfOperations.OrgPsrRole import OrgPsrRole
from CIM15.IEC61970.Informative.InfOperations.OutageCode import OutageCode
from CIM15.IEC61970.Informative.InfOperations.IncidentCode import IncidentCode
from CIM15.IEC61970.Informative.InfOperations.LandBase import LandBase
from CIM15.IEC61970.Informative.InfOperations.ErpPersonScheduleStepRole import ErpPersonScheduleStepRole
from CIM15.IEC61970.Informative.InfOperations.SwitchingStep import SwitchingStep
from CIM15.IEC61970.Informative.InfOperations.CallBack import CallBack
from CIM15.IEC61970.Informative.InfOperations.TroubleTicket import TroubleTicket
from CIM15.IEC61970.Informative.InfOperations.IncidentRecord import IncidentRecord
from CIM15.IEC61970.Informative.InfOperations.OutageNotification import OutageNotification
from CIM15.IEC61970.Informative.InfOperations.OutageStepPsrRole import OutageStepPsrRole

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#InfOperations"
nsPrefix = "cimInfOperations"


class SwitchingStepStatusKind(str):
    """Values are: instructed, confirmed, proposed, aborted, skipped
    """
    pass

class CircuitConnectionKind(str):
    """Values are: electricallyConnected, nominallyConnected, asBuilt, other
    """
    pass

class PSREventKind(str):
    """Values are: pendingRemove, pendingReplace, outOfService, pendingAdd, unknown, inService, other
    """
    pass

class TroubleReportingKind(str):
    """Values are: email, call, letter, other
    """
    pass

class ChangeItemKind(str):
    """Values are: add, modify, delete
    """
    pass

class OutageKind(str):
    """Values are: fixed, flexible, forced
    """
    pass
