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

"""This package contains functions common for distribution management.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Locations are logical entities which are related to a geographical position. Locations can be defined as points, lines or polygons. Location serves as a parent class for e.g. Zone, WorkLocation or ServiceLocation. Both Assets and PowerSystemResources are typically associated to a location. Aside from coordinates, useful properties of Locations can include Directions (i.e. driving instructions) and relationships to Organizations. ActivityRecord is a generalized class used to track the history of an object (e.g. Asset, PowerSystemResource, Customer, Location, Organisation or ErpContact). An ActivityRecord is a type of Document. Key properties of an ActivityRecord include statusDate, status, statusReason and remarks. TODO: Update attribute names. The graphical and geographical aspects of Assets, Locations and PowerSystemResources are managed using Graphical Markup Language (GML), which was defined by the Open GIS Consortium.  Using GML, a diagram is a collection of presentation objects. This package defines the classes Diagram and Presentation. TODO: These are now under Common package.'
"""

ns_prefix = "cimInfCommon"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfCommon"
