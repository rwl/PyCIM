#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Test case for the Common Information Model.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import sys
import unittest
import logging

from os.path import join, dirname

from iec61970.wires import ACLineSegment

from cim.cim_reader import read_cim

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.ERROR)

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

RDFXML_FILE = join(dirname(__file__), "data", "10bus.xml")
#RDFXML_FILE = join(dirname(__file__), "data", "abb40bus_cim13.xml")

#------------------------------------------------------------------------------
#  "CIMTestCase" class:
#------------------------------------------------------------------------------

class CIMTestCase(unittest.TestCase):
    """ Defines a test case for the Common Information Model.
    """

    def setUp(self):
        """ The test runner will execute this method prior to each test.
        """
        pass


    def test_create_cim(self):
        """ Test creation of a Common Information Model.
        """
        conductor = ACLineSegment()


    def test_load_cim(self):
        """ Test loading a Common Information Model from a RDF/XML file.
        """
        model = read_cim(RDFXML_FILE)
        print "ELEMENTS:", len(model.Contains)
#        model.Contains[0].configure_traits()

if __name__ == "__main__":
    unittest.main()

# EOF -------------------------------------------------------------------------
