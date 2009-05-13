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


MonetaryAmountPerEnergyUnit = Enum("EUR_per_Wh", "USD_per_Wh")

UnitMultiplier = Enum("micro", "T", "d", "k", "G", "p", "n", "c", "none", "M", "m")

MonetaryAmountPerHeatUnit = Enum("EUR_per_J", "USD_per_J")

UnitSymbol = Enum("W_s", "VAr", "m3", "m", "F", "kg_J", "J_s", "m2", "W", "none", "g", "N", "VA", "J", "VAh", "deg", "h", "W_Hz", "V", "_C", "Pa", "A", "Hz-1", "s", "ohm", "Wh", "min", "V_VAr", "H", "S", "rad", "s-1", "VArh", "Hz")

MonetaryAmountRate = Enum("USD_per_s", "EUR_per_s")

Currency = Enum("GBP", "NOK", "AUD", "other", "JPY", "EUR", "CNY", "RUR", "CAD", "SEK", "CHF", "DKK", "INR", "USD")



# EOF -------------------------------------------------------------------------
