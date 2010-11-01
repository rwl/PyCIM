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

"""The package covers all types of work, including inspection, maintenance, repair, restoration, and construction. It covers the full life cycle including request, initiate, track and record work. Standardized designs (compatible units) are used where possible.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Work package is used to define classes related to work. There are several different aspects of work. The Work Initiation (Work, Project, Request). The Work Design package is used for managing designs (CompatibleUnit, Design, DesignLocation, WorkTask). The Work Schedule package is used for the scheduling and coordination of work (AccessPermit, MaterialItem, OneCallRequest, Regulation). The Work Closing package is used for tracking costs of work (CostType, LaborItem, WorkCostDetail, VehicleItem). The Work Standards package is used for the definition of compatible units (CULaborItem, CUVehicleItem, CUGroup). This package is used for inspection and maintenance (InspectionDataSet, Procedure). The WorkService package defines Appointment class.'
"""

ns_prefix = "cimInfWork"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfWork"
