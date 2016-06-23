#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint, sample, choice
from pydot.pydot import *
from math import ceil
from itertools import chain

def settings_ger():
    dungeon={"name": ["Kerker", "Festung", "Verlies", "Bastille", "Turm", "Zwingburg"],
             "suffix": ["des Schreckens", "der Verdammnis", "der Dunkelheit",  "der Schatten", "des Wahnsinns", "der Verzweiflung", "des Todes"],
             "cellcolor":"lightgrey",
             "cellshape": "box",
             "rooms": ["Waffenkammer", "Wachraum", "Zelle", "Kreuzung", "Leerer Raum", "Baracke", "Trainingsraum", "Schrein", "Lagerraum", "Bibliothek", "Folterkammer", "Arena", "Gallerie", "Wohnraum", "Schlafzimmer", "Schmiede"],
             "paths": ["Korridor","Tür", "Eisenbeschlagene Tür", "Aufzug", "Treppe", "Leiter","Geheimgang"]
             }
    
    wilderness={"name": ["Wald", "Hain", "Wildnis"],
             "suffix": ["des Schreckens", "der Verdammnis", "der Dunkelheit",  "der Schatten", "der Einsamkeit", "der Verzweiflung", "der Riesen", "der Trolle"],
             "cellcolor":"green",
             "cellshape": "ellipse",
             "rooms": ["Menhir", "Lichtung", "Dickicht", "Bach", "Fluss", "Furt", "Hügelgrab", "Niederung", "Sumpf", "Irrgarten", "Schlucht", "Teich", "See", "Staudamm", "Alte Ruinen", "Monument"],
             "paths": ["Pfad","Hohlweg", "Treppe", "Feldweg", "Brücke", "Verborgener Pfad"]
             }
    
    cavern={"name": ["Höhle", "Kaverne", "Labyrinth"],
             "suffix": ["des Schreckens", "der Verdammnis", "der Dunkelheit",  "der Schatten", "der Einsamkeit", "der Verzweiflung", "der Riesen", "der Trolle", "der Untoten"],
             "cellcolor":"burlywood",
             "cellshape": "trapezium",
             "rooms": ["Pilzwald", "Einsturz", "Klamm", "Tropfsteinhöhle", "Mine", "Unterirdischer Fluss", "Unterirdischer See", "Lavastrom", "Säulengarten", "Abgrund"],
             "paths": ["Pfad","Tunnel", "Durchgang", "Brücke", "Schacht", "Höhle", "Kamin"]
             }
    catacomb={"name": ["Katakomben", "Grab", "Ruhestätte"],
             "suffix": ["des Schreckens", "der Verdammnis", "der Dunkelheit",  "der Schatten", "der Einsamkeit", "der Verzweiflung", "der Riesen", "der Trolle", "der Untoten"],
             "cellcolor":"gray",
             "cellshape": "octagon",
             "rooms": ["Krypta", "Schrein", "Grabmal", "Statue", "Sarkophag", "Arkanes Portal", "Falsches Grab" ],
             "paths": ["Korridor","Gang", "Tunnel", "Durchgang", "Brücke", "Torbogen", "Geheimgang"]
             }      
             
    settings=[dungeon, wilderness, cavern,catacomb]
    return settings
    
def settings_eng():
    dungeon={"name": ["Dungeon", "Fortress", "Prison", "Bastille", "Tower", "Keep"],
             "suffix": ["of Fear", "of Doom", "of Darkness",  "of Shadows", "of Madness", "of Despair", "of Death"],
             "cellcolor":"lightgrey",
             "cellshape": "box",
             "rooms": ["Armoury", "Watchroom", "Cell", "Crossing", "Empty Room", "Baracks", "Training Room", "Shrine", "Storage", "Library", "Torture Room", "Arena", "Gallery", "Living Room", "Bedchamber", "Smithy"],
             "paths": ["Corridor","Door", "Iron-wrought Door", "Elevator", "Stairs", "Ladder","Secret Passage"]
             }
    
    wilderness={"name": ["Forest", "Copse", "Wilderness"],
            "suffix": ["of Fear", "of Doom", "of Darkness",  "of Shadows", "of Madness", "of Despair", "of Death", "of Solitude", "of the Giants", "of the Trolls"],                        
             "cellcolor":"green",
             "cellshape": "ellipse",
             "rooms": ["Menhir", "Glade", "Thicket", "Brook", "River", "Ford", "Cairn", "Hollow", "Swamp", "Labyrinth", "Ravine", "Pond", "Lake", "Dam", "Old Ruins", "Monument"],
             "paths": ["Path","Gully", "Stairs", "Track", "Bridge", "Hidden Path"]
             }
    
    cavern={"name": ["Cave", "Cavern", "Labyrinth"],
             "suffix": ["of Fear", "of Doom", "of Darkness",  "of Shadows", "of Madness", "of Despair", "of Death", "of Solitude", "of the Giants", "of the Trolls"],                        
             "cellcolor":"burlywood",
             "cellshape": "trapezium",
             "rooms": ["Fungal forest", "Cave-In", "Gorge", "Flowstone Cave", "Mine", "Underground River", "Underground Lake", "Lava flow", "Pillars", "Chasm"],
             "paths": ["Path","Tunnel", "Passage", "Bridge", "Chute", "Cave", "Chimney"]
             }
    catacomb={"name": ["Catacombs", "Grave", "Sepulcher"],
             "suffix": ["of Fear", "of Doom", "of Darkness",  "of Shadows", "of Madness", "of Despair", "of Death", "of Solitude", "of the Giants", "of the Trolls", "of the Undead", "of Ghosts"],                        
             "cellcolor":"gray",
             "cellshape": "octagon",
             "rooms": ["Crypt", "Shrine", "Tomb", "Statue", "Sarcophagus", "Arcane Portal", "False Grave" ],
             "paths": ["Corridor","Hallway", "Tunnel", "Passage", "Bridge", "Portcullis", "Secret Passage"]
             }      
             
    settings=[dungeon, wilderness, cavern,catacomb]
    return settings    
        
def generatePathsForLevel(rooms):
    paths = []
    for origin in rooms:
        otherRooms = list(rooms)
        otherRooms.remove(origin)
        destination = choice(otherRooms)
        paths.append({"origin": origin, "destination": destination})
    return paths

def generateDot(nexus, levels, maxRooms, additionalPathProbability, metaPathProbability):
    settings=settings_eng()
    allPaths = []
    allRooms = []
    roomCount = 0

    graph = Graph(graph_type = "graph")
    graph.add_node(Node(nexus, shape = "tripleoctagon"))

    for level in range(0, levels):
        currentSetting = choice(settings)

        cluster = Cluster(str(level))
        graph.add_subgraph(cluster)
        cluster.set_label("%s %s" % (choice(currentSetting["name"]), choice(currentSetting["suffix"])))
        cluster.set_color(currentSetting["cellcolor"])
        cluster.set_node_defaults(style = "filled", color = currentSetting["cellcolor"], shape = currentSetting["cellshape"])

        numRooms = randint(4, min(len(currentSetting["rooms"]), maxRooms))
        rooms = ["[%i] %s" % (level, room) for room in sample(currentSetting["rooms"], numRooms)]
        allRooms.append(rooms)
        roomCount = roomCount + len(rooms)
        
        # Connect each room to exactly one other random room
        for path in [Edge(path["origin"], path["destination"], label = choice(currentSetting["paths"])) for path in generatePathsForLevel(rooms)]:
            cluster.add_edge(path)

        # Add a few other connections
        for extraPath in range(0, randint(0, ceil(numRooms ** 2 * additionalPathProbability))):
            cluster.add_edge(Edge(*sample(rooms, 2), label = choice(currentSetting["paths"])))

        allPaths.extend(cluster.get_edges())

        # Select a random entry point
        graph.add_edge(Edge(nexus, choice(rooms)))
   
    # Create paths between levels
    for metaPath in range(0, randint(0, ceil(roomCount ** 2 * metaPathProbability))):
        connectedLevels = sample(range(0, levels), 2)
        path = Edge(choice(allRooms[connectedLevels[0]]), choice(allRooms[connectedLevels[1]]), style = "dotted")
        graph.add_edge(path)
 
    return graph.to_string()
        
if __name__ == '__main__':
    print(generateDot("Nexus", 4, 10, 0.03, 0.01))
