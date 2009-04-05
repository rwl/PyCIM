#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------

""" Test case for the Common Information Model.
"""

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from os.path import join, dirname
import unittest

import iec61970 as cim

from iec61970.wires import ACLineSegment

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

RDFXML_FILE = join(dirname(__file__), "data/9bus-wscc.xml")

#-------------------------------------------------------------------------------
#  "CIMTestCase" class:
#-------------------------------------------------------------------------------

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
        conductor.configure_traits()

if __name__ == "__main__":
    unittest.main()

# EOF -------------------------------------------------------------------------
