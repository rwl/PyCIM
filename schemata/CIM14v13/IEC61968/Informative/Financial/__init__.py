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

"""This package is responsible for Settlement and Billing. These classes represent the legal entities who participate in formal or informal agreements.
"""

ns_prefix = "cimFinancial"
ns_uri = "http://iec.ch/TC57/CIM-generic#Financial"

from CIM14v13.IEC61968.Informative.Financial.Marketer import Marketer
from CIM14v13.IEC61968.Informative.Financial.FinancialVersion import FinancialVersion
from CIM14v13.IEC61968.Informative.Financial.CustomerConsumer import CustomerConsumer
from CIM14v13.IEC61968.Informative.Financial.TransmissionProvider import TransmissionProvider
from CIM14v13.IEC61968.Informative.Financial.TransmissionProduct import TransmissionProduct
from CIM14v13.IEC61968.Informative.Financial.GenerationProvider import GenerationProvider
from CIM14v13.IEC61968.Informative.Financial.OpenAccessProduct import OpenAccessProduct
from CIM14v13.IEC61968.Informative.Financial.IntSchedAgreement import IntSchedAgreement
from CIM14v13.IEC61968.Informative.Financial.ControlAreaOperator import ControlAreaOperator
