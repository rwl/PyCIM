#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------

""" This package contains the information classes that support distribution management in general.This package contains the information classes that support distribution management in general.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CDPSM.IEC61970.Core import IdentifiedObject
from CDPSM import Element



from enthought.traits.api import Instance, List, Property, Int, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "Location" class:
#------------------------------------------------------------------------------

class Location(IdentifiedObject):
    """ The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Sequence of position points describing this location.Sequence of position points describing this location.
    PositionPoints = List(Instance("CDPSM.IEC61968.Common.PositionPoint"),
        desc="Sequence of position points describing this location.Sequence of position points describing this location.")

    #--------------------------------------------------------------------------
    #  Begin "Location" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "PositionPoints",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.Common.Location",
        title="Location",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Location" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PositionPoint" class:
#------------------------------------------------------------------------------

class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Location that this position point describes.Location that this position point describes.
    Location = Instance("CDPSM.IEC61968.Common.Location", allow_none=False,
        desc="Location that this position point describes.Location that this position point describes.",
        transient=True,
        opposite="PositionPoints",
        editor=InstanceEditor(name="_locations"))

    def _get_locations(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.Common.Location" ]
        else:
            return []

    _locations = Property(fget=_get_locations)

    # Zero-relative sequence number of this point within a series of points.Zero-relative sequence number of this point within a series of points.
    sequenceNumber = Int(desc="Zero-relative sequence number of this point within a series of points.Zero-relative sequence number of this point within a series of points.")

    # X axis position.X axis position.
    xPosition = Str(desc="X axis position.X axis position.")

    # Y axis position.Y axis position.
    yPosition = Str(desc="Y axis position.Y axis position.")

    #--------------------------------------------------------------------------
    #  Begin "PositionPoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "sequenceNumber", "xPosition", "yPosition",
                label="Attributes"),
            VGroup("Model", "Location",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.Common.PositionPoint",
        title="PositionPoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PositionPoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeoLocation" class:
#------------------------------------------------------------------------------

class GeoLocation(Location):
    """ Geographical location.Geographical location.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All power system resources at this geographical location.All power system resources at this geographical location.
    PowerSystemResources = List(Instance("CDPSM.IEC61970.Core.PowerSystemResource"),
        desc="All power system resources at this geographical location.All power system resources at this geographical location.")

    #--------------------------------------------------------------------------
    #  Begin "GeoLocation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "PositionPoints", "PowerSystemResources",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.Common.GeoLocation",
        title="GeoLocation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeoLocation" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
