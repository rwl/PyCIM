# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA


from dynamics.iec61970.dynamics import RotatingMachine
from dynamics import Element
from dynamics.iec61970.dynamics import AsynchronousMachine

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Generators"

class GenSync(RotatingMachine):
    """ Synchronous generator model. A single standard synchronous model is defined for the CIM, with several variations indicated by the 'model type' attribute.  This model can be used for all types of synchronous machines (salient pole, solid iron rotor, etc.).
    """
    pass
    # <<< gen_sync
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GenSync' instance.

        """


        super(GenSync, self).__init__(*args, **kw_args)
    # >>> gen_sync



class GenLoad(Element):
    """ Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record.
    """
    pass
    # <<< gen_load
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GenLoad' instance.

        """


        super(GenLoad, self).__init__(*args, **kw_args)
    # >>> gen_load



class GenAsync(AsynchronousMachine):
    """ An asynchronous (induction) generator with no external connection to the rotor windings, e.g., squirrel-cage induction machine.
    """
    pass
    # <<< gen_async
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GenAsync' instance.

        """


        super(GenAsync, self).__init__(*args, **kw_args)
    # >>> gen_async



class GenEquiv(RotatingMachine):
    """ An equivalent representation of a synchronous generator as a constant internal voltage behind an impedance Ra plus Xp.
    """
    # <<< gen_equiv
    # @generated
    def __init__(self, xp=0.0, *args, **kw_args):
        """ Initialises a new 'GenEquiv' instance.

        @param xp: Equivalent reactance, also known as Xp. 
        """
        # Equivalent reactance, also known as Xp. 
        self.xp = xp



        super(GenEquiv, self).__init__(*args, **kw_args)
    # >>> gen_equiv



# <<< generators
# @generated
# >>> generators
