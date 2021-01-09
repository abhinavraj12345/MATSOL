import pandas as pd
import networkx as nx
from networkx.algorithms import bipartite
from numpy import nan
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import random


class ExamTimeTable:
        
        
    def __call__(self,data,plottitle):
        self.create_graph(data,plottitle)
        coloring = self.graph_coloring(plottitle)
        return coloring
        
        
    def create_graph(self,data,plottitle):
        self.n_graph = nx.Graph()
        self.students_set = set()
        self.subject_set = set()
        col_to_handle = data.shape[1]
        for row in data.iterrows():
            a, b = row[1][0].split(':')
            student_name = a.strip()
            subject_1 = b.strip()
            self.students_set.add(student_name)
            self.subject_set.add(subject_1)

            if student_name and subject_1 is not nan:
                self.n_graph.add_node(student_name,bipartite=0)
                self.n_graph.add_node(subject_1,bipartite=1,color='red')
                self.n_graph.add_edge(student_name,subject_1)


            try:
                for i in range(1,col_to_handle):
                    var_subject = row[1][i].strip()
                    if var_subject is not nan:
                        if var_subject not in self.subject_set:
                            self.n_graph.add_node(var_subject,bipartite=1,color='red')
                        self.n_graph.add_edge(student_name,var_subject)
                        self.subject_set.add(var_subject)
            except:
                pass
        colored_dict = nx.get_node_attributes(self.n_graph, 'color')
        default_color = '#5FBB6B'
        color_seq = [colored_dict.get(node, default_color) for node in self.n_graph.nodes()]
        #simple network graph
        legend_elements = [Line2D([0], [0],marker='o', color='w', label='Subjects',markerfacecolor='r', markersize=15 ),
                   Line2D([0], [0], marker='o', color='w', label='Students',
                          markerfacecolor='#5FBB6B', markersize=15)]
        fig = plt.figure(figsize=(12,8))
        plt.title(plottitle)
        plt.legend(handles=legend_elements, loc='lower right' )
        nx.draw(self.n_graph, with_labels=True, node_color=color_seq)
        #filename_1 = tempfile.NamedTemporaryFile().name + ".jpg"
        fig.savefig('./static/image_1.png',dpi=300, bbox_inches='tight')

        #bipartite graph
        l, r = nx.bipartite.sets(self.n_graph)
        pos = {}
        pos.update((node, (1, index)) for index, node in enumerate(l))
        pos.update((node, (2, index)) for index, node in enumerate(r))
        fig = plt.figure(figsize=(10,7))
        plt.title(plottitle)
        plt.legend(handles=legend_elements, loc='upper right' )
        nx.draw(self.n_graph, pos=pos,with_labels=True,node_color=color_seq)
        #filename_2 = tempfile.NamedTemporaryFile().name + ".jpg"
        fig.savefig('./static/image_2.png',dpi=300, bbox_inches='tight')

        
    def graph_coloring(self,plottitle):
        number_of_colors = len(self.subject_set)
        colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
        print(colors)
        subject_labels = {i:i for i in self.subject_set}
        G=nx.projected_graph(self.n_graph,self.subject_set)
        coloring = nx.coloring.greedy_color(G)
        print(coloring)
        fig = plt.figure(figsize=(7,7))
        plt.axis('off')
        plt.title(plottitle)
        n_colors = len(colors)
        pos = nx.spring_layout(G)
        for i in range(n_colors):
            nx.draw_networkx_nodes(G,pos,[x for x in G.nodes() if coloring[x]==i],width=8,node_color=colors[i])
        nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
        nx.draw_networkx_labels(G,pos,labels=subject_labels,font_size=20)
        #filename_3 = tempfile.NamedTemporaryFile().name + ".jpg"
        fig.savefig('./static/image_3.png',dpi=300, bbox_inches='tight')
        return coloring
        
        
        
        
