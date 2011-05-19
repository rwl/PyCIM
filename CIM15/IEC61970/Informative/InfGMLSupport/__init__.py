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

"""The package contains portions of the model defined by graphic standards such as those proposed by OpenGIS Consortium referred to as the Geography Markup Language (GML). It facilitates integration among electric utility applications (CIM) and Geographical Information Systems (GIS) and other applications. Rather than inventing new CIM classes that accomplish similar functionality as in existing GML, the preferred approach is to use and extend 'Gml' classes as appropriate. Note that care has been taken to separate the geometry of features from how features can be graphically represented. GML supports the concept of a geographic feature, which is 'an abstraction of a real world phenomenon; it is a geographic feature if it is associated with a location relative to the Earth'. So a digital representation of the real world can be thought of as a set of features. The state of a feature is defined by a set of properties, where each property can be thought of as a {name, type, value} triple. The number of properties a feature may have, together with their names and types, are determined by its type definition. Geographic features with geometry are those with properties that may be geometry-valued.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'A Geographic Feature is 'an abstraction of a real world phenomenon; it is a geographic feature if it can is asociated with a location relative to the Earth. A digital representation of the real world can be thought of as a set of features. He state of a feature is defined by a set of properties, whre each property can be thought of as a (name, type, value) triple. The number of propoerties a feature may have, together with their names and types, are determined by its type definition. Geographic features with geometry are those with properties tht may be geometry-valued. Geographic features in GML include coverages and observations as subtypes. A coverage is a type of feature that has a coverage function with a spatial domain and a value  set range of homogeneous 2 to n dimensional tuples. A coverage can represent one feature or a collection of features 'to model and make visible spatial relationships between, and the spatial distribution of, earth phenomena.' A reference system provides a scale of measurement for assigning values to a location, time or other descriptive quantity or quality. A coordinate reference system consists of set of coordinate system axes that are related to the earth through a datum that defines the size and shape of the earth. Geometries in GML indicate the coordinate reference system in which the measurements have ben made. The 'parent' geometry element of a geometric complex or geometric aggregate makes this indication for its constituent geometries.'
"""

from CIM15.IEC61970.Informative.InfGMLSupport.GmlFeatureType import GmlFeatureType
from CIM15.IEC61970.Informative.InfGMLSupport.Map import Map
from CIM15.IEC61970.Informative.InfGMLSupport.GmlPointGeometry import GmlPointGeometry
from CIM15.IEC61970.Informative.InfGMLSupport.GmlHalo import GmlHalo
from CIM15.IEC61970.Informative.InfGMLSupport.GmlColour import GmlColour
from CIM15.IEC61970.Informative.InfGMLSupport.GmlFont import GmlFont
from CIM15.IEC61970.Informative.InfGMLSupport.GmlPolygonSymbol import GmlPolygonSymbol
from CIM15.IEC61970.Informative.InfGMLSupport.GmlStroke import GmlStroke
from CIM15.IEC61970.Informative.InfGMLSupport.GmlBaseSymbol import GmlBaseSymbol
from CIM15.IEC61970.Informative.InfGMLSupport.GmlPosition import GmlPosition
from CIM15.IEC61970.Informative.InfGMLSupport.GmlTextSymbol import GmlTextSymbol
from CIM15.IEC61970.Informative.InfGMLSupport.GmlPolygonGeometry import GmlPolygonGeometry
from CIM15.IEC61970.Informative.InfGMLSupport.GmlObservation import GmlObservation
from CIM15.IEC61970.Informative.InfGMLSupport.GmlMark import GmlMark
from CIM15.IEC61970.Informative.InfGMLSupport.GmlGraphic import GmlGraphic
from CIM15.IEC61970.Informative.InfGMLSupport.GmlLabelPlacement import GmlLabelPlacement
from CIM15.IEC61970.Informative.InfGMLSupport.GmlGeometryStyle import GmlGeometryStyle
from CIM15.IEC61970.Informative.InfGMLSupport.GmlLineGeometry import GmlLineGeometry
from CIM15.IEC61970.Informative.InfGMLSupport.GmlValue import GmlValue
from CIM15.IEC61970.Informative.InfGMLSupport.GmlLineSymbol import GmlLineSymbol
from CIM15.IEC61970.Informative.InfGMLSupport.GmlDiagramObject import GmlDiagramObject
from CIM15.IEC61970.Informative.InfGMLSupport.GmlPointSymbol import GmlPointSymbol
from CIM15.IEC61970.Informative.InfGMLSupport.GmlTopologyStyle import GmlTopologyStyle
from CIM15.IEC61970.Informative.InfGMLSupport.GmlSelector import GmlSelector
from CIM15.IEC61970.Informative.InfGMLSupport.GmlSvgParameter import GmlSvgParameter
from CIM15.IEC61970.Informative.InfGMLSupport.GmlLabelStyle import GmlLabelStyle
from CIM15.IEC61970.Informative.InfGMLSupport.GmlFill import GmlFill
from CIM15.IEC61970.Informative.InfGMLSupport.Diagram import Diagram
from CIM15.IEC61970.Informative.InfGMLSupport.GmlSymbol import GmlSymbol
from CIM15.IEC61970.Informative.InfGMLSupport.GmlFeatureStyle import GmlFeatureStyle
from CIM15.IEC61970.Informative.InfGMLSupport.GmlRasterSymbol import GmlRasterSymbol

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#InfGMLSupport"
nsPrefix = "cimInfGMLSupport"


class QueryGrammarKind(str):
    """Values are: other, xpath, xquery
    """
    pass

class DiagramKind(str):
    """Values are: other, geographic, internalView, designSketch, schematic
    """
    pass
