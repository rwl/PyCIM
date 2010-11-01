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

"""The package contains portions of the model defined by graphic standards such as those proposed by OpenGIS Consortium referred to as the Geography Markup Language (GML). It facilitates integration among electric utility applications (CIM) and Geographical Information Systems (GIS) and other applications. Rather than inventing new CIM classes that accomplish similar functionality as in existing GML, the preferred approach is to use and extend 'Gml' classes as appropriate. Note that care has been taken to separate the geometry of features from how features can be graphically represented. GML supports the concept of a geographic feature, which is 'an abstraction of a real world phenomenon; it is a geographic feature if it is associated with a location relative to the Earth'. So a digital representation of the real world can be thought of as a set of features. The state of a feature is defined by a set of properties, where each property can be thought of as a {name, type, value} triple. The number of properties a feature may have, together with their names and types, are determined by its type definition. Geographic features with geometry are those with properties that may be geometry-valued.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'A Geographic Feature is 'an abstraction of a real world phenomenon; it is a geographic feature if it can is asociated with a location relative to the Earth. A digital representation of the real world can be thought of as a set of features. He state of a feature is defined by a set of properties, whre each property can be thought of as a (name, type, value) triple. The number of propoerties a feature may have, together with their names and types, are determined by its type definition. Geographic features with geometry are those with properties tht may be geometry-valued. Geographic features in GML include coverages and observations as subtypes. A coverage is a type of feature that has a coverage function with a spatial domain and a value  set range of homogeneous 2 to n dimensional tuples. A coverage can represent one feature or a collection of features 'to model and make visible spatial relationships between, and the spatial distribution of, earth phenomena.' A reference system provides a scale of measurement for assigning values to a location, time or other descriptive quantity or quality. A coordinate reference system consists of set of coordinate system axes that are related to the earth through a datum that defines the size and shape of the earth. Geometries in GML indicate the coordinate reference system in which the measurements have ben made. The 'parent' geometry element of a geometric complex or geometric aggregate makes this indication for its constituent geometries.'
"""

ns_prefix = "cimInfGMLSupport"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfGMLSupport"
