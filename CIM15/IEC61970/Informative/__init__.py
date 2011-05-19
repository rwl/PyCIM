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

"""This package contains functions common for distribution management.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Locations are logical entities which are related to a geographical position. Locations can be defined as points, lines or polygons. Location serves as a parent class for e.g. Zone, WorkLocation or ServiceLocation. Both Assets and PowerSystemResources are typically associated to a location. Aside from coordinates, useful properties of Locations can include Directions (i.e. driving instructions) and relationships to Organizations. ActivityRecord is a generalized class used to track the history of an object (e.g. Asset, PowerSystemResource, Customer, Location, Organisation or ErpContact). An ActivityRecord is a type of Document. Key properties of an ActivityRecord include statusDate, status, statusReason and remarks. TODO: Update attribute names. The graphical and geographical aspects of Assets, Locations and PowerSystemResources are managed using Graphical Markup Language (GML), which was defined by the Open GIS Consortium.  Using GML, a diagram is a collection of presentation objects. This package defines the classes Diagram and Presentation. TODO: These are now under Common package.'
"""


nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#Informative"
nsPrefix = "cimInformative"

