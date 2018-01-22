from cgraph import Graph

# A dummy webrtc app

with Graph.wrap ("app", "demo.gv") as g :
  
  class app :
    start = g.node ('start')
    stop = g.node ('end')

  class menu :
    c = g.cluster ('menu')

    root = c.node ('main menu')
    session = c.node ('session')
    quit = c.node ('quit')

    c.edges (
        (root, session),
        (root, quit))

  g.edges (
      (app.start, menu.root),
      (menu.quit, app.stop))

  class session :
    c = g.cluster ('session')

    root = c.node ('session')
    create_offer = c.node ('generate host string')
    accept_offer = c.node ('accept host string')
    accept_answer = c.node ('accept connection string')
    generate_answer = c.node ('generate connection string')

    c.edges (
        (root, create_offer),
        (root, accept_offer),
        (create_offer, accept_answer),
        (accept_offer, generate_answer))

  g.edge (menu.session, session.root)

