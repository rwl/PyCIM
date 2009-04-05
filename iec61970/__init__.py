# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits



class IEC61970CIMVersion(HasTraits):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.  cim61970_v002 was created from cim10_v000_WG13cimIssues_61968_Rev6_22Feb2005 that is the merged wg13 and wg14 models. The content has a number of wg13 issue resolutions.
    """
    version = String
    date = AbsoluteDateTime


