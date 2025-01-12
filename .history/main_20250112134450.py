from graphviz import Digraph

# Create UML Activity Diagram for Spotify Recommendation Feature
uml_diagram = Digraph(format="png", name="Spotify_Recommendation_Process")

# Nodes
uml_diagram.attr(rankdir="TB", size="8,10")
uml_diagram.node("Start", "Start", shape="ellipse")
uml_diagram.node("UserInitiates", "User initiates recommendations", shape="rectangle")
uml_diagram.node("CollectData", "Collect user data\n(history, saved tracks)", shape="rectangle")
uml_diagram.node("APIGateway", "API Gateway forwards request", shape="rectangle")
uml_diagram.node("AnalyzeData", "Recommendation Engine analyzes data", shape="rectangle")
uml_diagram.node("QueryDB", "Query Music Catalog\nfor relevant tracks", shape="rectangle")
uml_diagram.node("GeneratePlaylist", "Generate playlist", shape="rectangle")
uml_diagram.node("ReturnToUser", "Return playlist to user", shape="rectangle")
uml_diagram.node("End", "End", shape="ellipse")

# Connections
uml_diagram.edge("Start", "UserInitiates")
uml_diagram.edge("UserInitiates", "CollectData")
uml_diagram.edge("CollectData", "APIGateway")
uml_diagram.edge("APIGateway", "AnalyzeData")
uml_diagram.edge("AnalyzeData", "QueryDB")
uml_diagram.edge("QueryDB", "GeneratePlaylist")
uml_diagram.edge("GeneratePlaylist", "ReturnToUser")
uml_diagram.edge("ReturnToUser", "End")

# Render UML Diagram
uml_path = "/mnt/data/Spotify_Recommendation_Process_UML"
uml_diagram.render(uml_path, format="png", cleanup=True)

uml_path + ".png"
