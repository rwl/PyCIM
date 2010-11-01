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

import sys
import logging

from simple_xml_writer import XMLWriter

logger = logging.getLogger(__name__)

def cimwrite(d, file_or_filename):
    """CIM RDF/XML serializer.

    @type d: dict
    @param d: Map of URIs to CIM objects.
    @type file_or_filename: File-like-object or path to file.
    @param file_or_filename: CIM RDF/XML file to write.
    @rtype: bool
    @return: Write success.
    """
    w = XMLWriter(sys.stdout)

    html = w.start("html")

    w.start("head")
    w.element("title", "my document")
    w.element("meta", name="generator", value="my application 1.0")
    w.end()

    w.start("body")
    w.element("h1", "this is a heading")
    w.element("p", "this is a paragraph")

    w.start("p")
    w.data("this is ")
    w.element("b", "bold")
    w.data(" and ")
    w.element("i", "italic")
    w.data(".")
    w.end("p")

    w.close(html)