Usage
-----

To use PyCIM with the Python interpreter, IPython is recommended.  For example,
to instantiate a ConnecticityNode:

.. sourcecode:: ipython

  In [1]: from CIM14.IEC61970.Core import ConnectivityNode

  In [2]: node = ConnectivityNode(name='Node 1')

To associate the node with a Terminal:

.. sourcecode:: ipython

  In [3]: from CIM14.IEC61970.Core import Terminal

  In [4]: t = Terminal(name='T1', ConnectivityNode=node)

  In [5]: node.Terminals[0].name
  Out[5]: 'T1'

To add a Terminal to a ConnectivityNode:

.. sourcecode:: ipython

  In [6]: t2 = Terminal()

  In [7]: node.addTerminals(t2)

  In [8]: t2.ConnectivityNode.name
  Out[8]: 'Node 1'

To view the docstring for an attribute:

.. sourcecode:: ipython

  In [9]: t.connected?
  Type:     bool
  Base Class: <type 'bool'>
  String Form:    False
  Namespace:  Interactive
  Docstring:
      bool(x) -> bool

      Returns True when the argument x is true, False otherwise.
      The builtins True and False are the only two instances of the class bool.
      The class bool is a subclass of the class int, and cannot be subclassed.