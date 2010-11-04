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

"""The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis.
"""

ns_prefix = "cimControlArea"
ns_uri = "http://iec.ch/TC57/CIM-generic#ControlArea"

from CIM14v13.IEC61970.ControlArea.TieFlow import TieFlow
from CIM14v13.IEC61970.ControlArea.ControlArea import ControlArea
from CIM14v13.IEC61970.ControlArea.ControlAreaGeneratingUnit import ControlAreaGeneratingUnit
from CIM14v13.IEC61970.ControlArea.AltGeneratingUnitMeas import AltGeneratingUnitMeas
from CIM14v13.IEC61970.ControlArea.AltTieMeas import AltTieMeas
