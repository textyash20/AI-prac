import tsp
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
def draw_graph(oldedges,olddistance,newedges,newdistance,optimal_distance):
    fig,ax=plt.subplots(1,2,num=1)
    pos={0:(2,5),1:(0,0),2:(5,0),3:(2,1)}
    g1=nx.Graph()
    g1.add_edges_from(oldedges)
    labels={oldedges[i]:str(olddistance[i]) for i in range(len(oldedges))}
    nx.draw_networkx(g1,pos,ax=ax[0])
    nx.draw_networkx_edge_labels(g1,pos,edge_labels=labels,ax=ax[0])
    ax[0].set_title("Without optimal path")
    g2=nx.Graph()
    g2.add_edges_from(newedges)
    labels={newedges[i]:str(newdistance[i]) for i in range(len(newedges))}
    nx.draw_networkx(g2,pos,ax=ax[2])
    nx.draw_networkx_edge_labels(g2,pos,edge_labels=labels,ax=ax[1])
    title="with optimal path\nthe best optimal distance is "+str(optimal_distance)
    ax[1].set_title(title)
    plt.show()
def maketuple(data):
    pre=data[0]
    path=[]
    for i in range(1,len(data)):
        path.append((pre,data[i]))
        pre=data[i]
    path.append((pre,data[0]))
    print(path)
    return path
def main():
    oldedges=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    olddistance=[10,15,20,35,25,30]
    graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    r=len(graph)
    dist={(i,j):graph[i][j] for i in range(r) for j in range(r)}
    optimal_distance,best_path=tsp.tsp(range(r),dist)
    newedges=maketuple(best_path)
    newdistance=[dist[newedges[i]] for i in range(len(newedges))]
#draw_graph(oldedges,olddistance,newedges,newdistance,optimaldistance)
draw_graph((0,4),(25,30),(9,15),(35,40),(5,6))
main()    
