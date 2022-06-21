# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:43:34 2022

@author: Nick
"""

   
from words import wp,new_words4,words4
import networkx as nx
G = nx.Graph()

#print("removed words are:", [w for w in words4 if w not in new_words4])
new_dict = True

if new_dict:
    #test with modified words list
    new_words4.append("taco") #hotfix for issue in nathans dict
    new_words4.append("slaw") #hotfix for issue in nathans dict
    new_words4.append("noir") #hotfix for issue in nathans dict
    new_words4.append("quag") #hotfix for issue in nathans dict
    words4 = new_words4
else:
    from words import words4

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

#solve test problem        
print([p for p in nx.all_shortest_paths(G,"solo","duet")])

#determine the connected subgraphs - 
subgraphs = list(nx.connected_components(G))

sorted_subgraphs = sorted(subgraphs,key=len,reverse=True)
print(len(sorted_subgraphs[0]), " out of ", len(words4), " words are connected to the main dictionary")
print("the following sets of words are unreachable from the main dictionary:")
print(sorted_subgraphs[1:])
#flatten the array
unreachable_words = [w for a in sorted_subgraphs[1:] for w in a]

for pair in wp:
    #check they're in the dictionary at all
    if pair[0] not in words4:
        print("error: ", pair[0], " is not in the dictionary")
        continue
    if pair[1] not in words4:
        print("error: ", pair[1], " is not in the dictionary")
        continue
    
    #print(pair)
    if pair[0] in unreachable_words:
        print("error: ", pair[0], " is an unreachable word for this dictionary")
        continue
    if pair[1] in unreachable_words:
        print("error: ", pair[1], " is an unreachable word for this dictionary")
        continue
    try:
        sols = [p for p in nx.all_shortest_paths(G,pair[0],pair[1])]
        print(sols)
    except:
        print("Yikes - problem for ", pair)
        raise
    
    
    
    