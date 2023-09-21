# https://stackoverflow.com/questions/14172028/html-parse-tree-using-python-2-7
import streamlit as st
import networkx as nx
from lxml import html
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

# Text/Title
st.title("Visualización de html a árbol")
st.write("Prueba con streamlit de código sacado de https://stackoverflow.com/questions/14172028/html-parse-tree-using-python-2-7")

def traverse(parent, graph, labels):
    labels[parent] = parent.tag
    for node in parent.getchildren():
        graph.add_edge(parent, node)
        traverse(node, graph, labels)

def dibuja(raw):
    G = nx.DiGraph()
    labels = {}     # needed to map from node to tag
    html_tag = html.document_fromstring(raw)
    traverse(html_tag, G, labels)

    pos = graphviz_layout(G, prog='dot')

    label_props = {'size': 16,
                'color': 'black',
                'weight': 'bold',
                'horizontalalignment': 'center',
                'verticalalignment': 'center',
                'clip_on': True}
    bbox_props = {'boxstyle': "round, pad=0.2",
                'fc': "grey",
                'ec': "b",
                'lw': 1.5}

    nx.draw_networkx_edges(G, pos, arrows=True)
    ax = plt.gca()

    for node, label in labels.items():
            x, y = pos[node]
            ax.text(x, y, label,
                    bbox=bbox_props,
                    **label_props)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()



raw = st.text_area("Introduce el código html: ")
if st.button("Submit"):
   dibuja(raw)


