from contextlib import contextmanager
from ctypes import (
    cdll,
    c_void_p, c_char_p
    )

_raw = cdll.LoadLibrary ("./_cgraph.so") 

_raw.node_set_label.argtypes = [c_void_p, c_char_p]
_raw.node_set_label.restype = None

_raw.node_get_label.argtypes = [c_void_p]
_raw.node_get_label.restype = c_char_p

_raw.make_graph.argtypes = [c_char_p]
_raw.make_graph.restype = c_void_p

_raw.graph_close.argtypes = [c_void_p]
_raw.graph_close.restype = None

_raw.graph_save.argtypes = [c_void_p, c_char_p]
_raw.graph_save.restype = None

_raw.graph_node.argtypes = [c_void_p, c_char_p]
_raw.graph_node.restype = c_void_p

_raw.graph_edge.argtypes = [c_void_p, c_void_p, c_void_p]
_raw.graph_edge.restype = c_void_p

_raw.graph_subgraph.argtypes = [c_void_p, c_char_p]
_raw.graph_subgraph.restype = c_void_p

class Node :

  def __init__ (self, _handle) :
    self._handle = _handle

  def _set_label (self, label) :
    return _raw.node_set_label (self._handle, label.encode ('utf-8'))

  def _get_label (self) :
    return _raw.node_get_label (self._handle)

  label = property (_get_label, _set_label)

class Graph :

  def __init__ (self, x) :
    if isinstance (x, str) :
      self._handle = _raw.make_graph (x.encode ('utf-8'))
    else :
      self._handle = x

  def close (self) :
    _raw.graph_close (self._handle)

  def save (self, fname) :
    _raw.graph_save (self._handle, fname.encode ('utf-8'))

  def node (self, label) :
    return _raw.graph_node (self._handle, label.encode ('utf-8'))

  def edge (self, head, tail) :
    return _raw.graph_edge (self._handle, head, tail)

  def edges (self, *tups) :
    for h,t in tups :
      self.edge (h, t)

  def subgraph (self, name) :
    return Graph (_raw.graph_subgraph (self._handle, name.encode ('utf-8')))

  def cluster (self, name) :
    return self.subgraph (f'cluster:{name}')

  @staticmethod
  @contextmanager
  def wrap (gname, fname) :
    g = Graph (gname)
    yield g
    g.save (fname)
    g.close ()

