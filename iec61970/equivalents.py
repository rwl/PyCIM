# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

from iec61970.core import ConnectivityNodeContainer
from iec61970.core import ConductingEquipment
from iec61970.domain import Resistance
from iec61970.domain import Reactance
from iec61970.domain import Susceptance
from iec61970.domain import Conductance



from enthought.traits.api import Instance, List



class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model.
    """
    # The associated reduced equivalents.
    EquivalentEquipment = List(Instance("iec61970.equivalents.EquivalentEquipment.EquivalentEquipment"))

class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.
    """
    # The equivalent where the reduced model belongs.
    EquivalentNetwork = Instance("iec61970.equivalents.EquivalentNetwork.EquivalentNetwork", allow_none=False)

class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.
    """
    # Positive sequence series resistance of the reduced branch.
    r = Resistance
    # Positive sequence series reactance of the reduced branch.
    x = Reactance

class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.
    """
    # Positive sequence shunt susceptance.
    b = Susceptance
    # Positive sequence shunt conductance.
    g = Conductance


