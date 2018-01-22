#include <cgraph.h>
#include <cstdio>

extern "C" {

  void node_set_label (Agnode_t * node, const char * label) {
    agset (node, "label", const_cast<char*> (label)) ;
  }

  const char * node_get_label (Agnode_t * node) {
    return agget (node, const_cast<char*> ("label")) ;
  }

  Agraph_t * make_graph (const char * name) {
    auto g = agopen (const_cast<char*> (name), Agdirected, nullptr) ;
    agattr (g, AGNODE, "label", "<unlabelled>") ;
    return g ;
  }

  void graph_close (Agraph_t * g) {
    agclose (g) ;
  }

  void graph_save (Agraph_t * g, const char * fname) {
    auto handle = std::fopen (fname, "w") ;
    agwrite (g, handle) ;
    std::fclose (handle) ;
  }

  Agnode_t * graph_node (Agraph_t * g, const char * label) {
    auto n = agnode (g, nullptr, TRUE) ;
    node_set_label (n, label) ;
    return n ;
  }

  Agedge_t * graph_edge (Agraph_t * g, Agnode_t * head, Agnode_t * tail) {
    return agedge (g, head, tail, nullptr, TRUE) ;
  }

  Agraph_t * graph_subgraph (Agraph_t * g, const char * name) {
    return agsubg (g, const_cast<char*> (name), TRUE) ;
  }
}

