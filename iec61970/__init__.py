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

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "IEC61970CIMVersion" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersion(HasTraits):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.  cim61970_v002 was created from cim10_v000_WG13cimIssues_61968_Rev6_22Feb2005 that is the merged wg13 and wg14 models. The content has a number of wg13 issue resolutions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    version = String

    date = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin iEC61970CIMVersion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End iEC61970CIMVersion user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
