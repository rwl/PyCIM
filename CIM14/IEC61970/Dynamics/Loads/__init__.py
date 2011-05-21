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


from CIM14.IEC61970.Dynamics.Loads.AggregateLoad import AggregateLoad
from CIM14.IEC61970.Dynamics.Loads.LoadStatic import LoadStatic
from CIM14.IEC61970.Dynamics.Loads.LoadStaticSystem import LoadStaticSystem
from CIM14.IEC61970.Dynamics.Loads.LoadStaticOwner import LoadStaticOwner
from CIM14.IEC61970.Dynamics.Loads.LoadStaticZone import LoadStaticZone
from CIM14.IEC61970.Dynamics.Loads.LoadStaticBus import LoadStaticBus
from CIM14.IEC61970.Dynamics.Loads.LoadStaticArea import LoadStaticArea
from CIM14.IEC61970.Dynamics.Loads.LoadMotor import LoadMotor

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Loads"
nsPrefix = "cimLoads"


class StaticLoadType(str):
    """Type of static load
    Values are: ZIP1, exponential, ZIP2
    """
    pass
