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

""" This package shows all the root level subpackage dependencies of the combined CIM model.
"""

from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.packagedependencies"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#PackageDependencies"

class PackageDependenciesCIMVeresion(Element):
    """ The version of dependencies description among top level subpackages of the combined CIM model.  This is not the same as the combined packages version.
    """
    # <<< package_dependencies_cimveresion
    # @generated
    def __init__(self, date='', vesion='', **kw_args):
        """ Initialises a new 'PackageDependenciesCIMVeresion' instance.
        """
        # Date of last change to the main package dependencies in format YYYY-MM-DD.   This is updated when the version attribute is updated. 
        self.date = date

        # The version of the main subpackages of the combined CIM model.  The format is simply an integer.  The version (and date) initial values should be updated any time the dependencies in the model change and require an actual change to the diagrams within this package. 
        self.vesion = vesion



        super(PackageDependenciesCIMVeresion, self).__init__(**kw_args)
    # >>> package_dependencies_cimveresion


    def __str__(self):
        """ Returns a string representation of the PackageDependenciesCIMVeresion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< package_dependencies_cimveresion.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PackageDependenciesCIMVeresion.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PackageDependenciesCIMVeresion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:PackageDependenciesCIMVeresion.date>%s</%s:PackageDependenciesCIMVeresion.date>' % \
            (indent, ns_prefix, self.date, ns_prefix)
        s += '%s<%s:PackageDependenciesCIMVeresion.vesion>%s</%s:PackageDependenciesCIMVeresion.vesion>' % \
            (indent, ns_prefix, self.vesion, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PackageDependenciesCIMVeresion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> package_dependencies_cimveresion.serialize


# <<< package_dependencies
# @generated
# >>> package_dependencies
