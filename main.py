# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:43:34 2022

@author: Nick
"""

   
from words import wp,new_words4#,words4
import networkx as nx
G = nx.Graph()

if True:
    #test with modified words list
    words4 = new_words4

G.add_nodes_from(words4)

#build the graph
for i in range(len(words4)):
    for j in range(i+1, len(words4)):
        diffs = 0
        for k in range(4):
            #see if the kth character is identical
            if words4[i][k] == words4[j][k]:
                diffs = diffs+1
        if diffs==3:
            G.add_edge(words4[i], words4[j])
        
print([p for p in nx.all_shortest_paths(G,"solo","duet")])


#for pair in wp:
#    print([p for p in nx.all_shortest_paths(G,pair[0],pair[1])])
    
    
    
    