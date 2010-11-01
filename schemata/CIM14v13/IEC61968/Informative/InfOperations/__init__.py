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
