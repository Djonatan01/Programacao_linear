import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import base64
import io

def grafoCompeto(n):

    # Crie um grafo completo
    G = nx.complete_graph(n)

    # Defina os nomes dos aeroportos como rótulos dos nós
    aeroportos = [
        "Guarulhos",
        "Galeão",
        "Brasília",
        "Confins",
        "Salvador",
        "Recife",
        "Fortaleza",
        "Manaus",
        "Porto Alegre",
        "Curitiba"
    ]

    node_labels = {}
    for i in range(len(aeroportos)):
        node_labels[i] = aeroportos[i]

    # Desenhe o grafo
    pos = nx.spring_layout(G, seed=42)  # Layout do grafo
    nx.draw(G, pos, with_labels=False, node_size=3000, node_color='green', font_size=8, font_color='black')
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8, font_color='white')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Codifique o gráfico em base64
    buffer_base64 = base64.b64encode(buffer.read()).decode()

    return buffer_base64