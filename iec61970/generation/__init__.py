# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" This package contains packages that have information for Unit Commitment and Economic Dispatch of Hydro and Thermal Generating Units, Load Forecasting, Automatic Generation Control, and Unit Modeling for Dynamic Training Simulator.
"""
from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits



class GenerationVersion(HasTraits):
    version = String
    date = AbsoluteDateTime


