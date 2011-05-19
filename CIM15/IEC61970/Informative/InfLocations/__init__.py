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


from CIM15.IEC61970.Informative.InfLocations.LocationGrant import LocationGrant
from CIM15.IEC61970.Informative.InfLocations.RightOfWay import RightOfWay
from CIM15.IEC61970.Informative.InfLocations.PersonPropertyRole import PersonPropertyRole
from CIM15.IEC61970.Informative.InfLocations.Zone import Zone
from CIM15.IEC61970.Informative.InfLocations.RedLine import RedLine
from CIM15.IEC61970.Informative.InfLocations.Route import Route
from CIM15.IEC61970.Informative.InfLocations.OrgPropertyRole import OrgPropertyRole
from CIM15.IEC61970.Informative.InfLocations.Direction import Direction
from CIM15.IEC61970.Informative.InfLocations.LandProperty import LandProperty
from CIM15.IEC61970.Informative.InfLocations.Hazard import Hazard

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#InfLocations"
nsPrefix = "cimInfLocations"


class LandPropertyKind(str):
    """Values are: store, customerPremise, building, external, gridSupplyPoint, substation, depot
    """
    pass

class DemographicKind(str):
    """Values are: other, urban, rural
    """
    pass

class ZoneKind(str):
    """Values are: weatherZone, other, specialRestrictionLand, electricalNetwork
    """
    pass
