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




from enthought.traits.api import Enum
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


UnitSymbol = Enum("V_VAr", "VArh", "none", "V", "J", "ohm", "H", "rad", "Pa", "s", "g", "W", "VAh", "F", "h", "W_Hz", "Hz", "N", "VAr", "W_s", "S", "J_s", "m2", "m", "m3", "min", "s-1", "deg", "Wh", "VA", "A", "_C", "kg_J", "Hz-1")

UnitMultiplier = Enum("c", "k", "G", "M", "T", "micro", "n", "none", "d", "m", "p")

Currency = Enum("GBP", "SEK", "INR", "NOK", "EUR", "DKK", "CNY", "RUR", "CAD", "other", "AUD", "USD", "CHF", "JPY")

MonetaryAmountPerEnergyUnit = Enum("USD_per_Wh", "EUR_per_Wh")

MonetaryAmountRate = Enum("USD_per_s", "EUR_per_s")

MonetaryAmountPerHeatUnit = Enum("EUR_per_J", "USD_per_J")



# EOF -------------------------------------------------------------------------
