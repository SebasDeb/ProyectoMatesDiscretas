import networkx as nx
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import os

# Crear el grafo
udlap = nx.Graph()

# Nodos y descripciones 
nodes = ["GC", "A", "GA", "BQ", "GB", "CT", "CFR", "CL", "ATL", "TD", "CIR", 
         "C1", "C2", "C3", "C4", "C5", "C6", "C7", "CC", "CRL", "CB", "CG",
         "J1", "J2", "J3", "J4", "J5", "J6", "AG", "HU", "LB", "LA", "CI", 
         "IA", "CN", "TI", "HA", "AU", "BI", "CS", "NE", "CE", "iOS", "SL", 
         "1", "RH", "PU", "PF", "AP", "A14", "A14CT", "AR"]

node_descriptions = {
    "GC": "Gimnasio Luison", "A": "Alberca", "GA": "Gimnasio Moe",
    "BQ": "Canchas de Basquetbol", "GB": "Gimnasio Pesas", "CT": "Canchas de Tenis",
    "CFR": "Canchas de Futbol Rápido", "CL": "Campo de Lanzamiento", "ATL": "Pista de Atletismo",
    "TD": "Templo del Dolor", "CIR": "Centro de Rehabilitación", "BI": "Biblioteca",
    "CC": "Colegio Cain-Murray", "CRL": "Colegio Ray Lindley", "CB": "Colegio Bernal",
    "CG": "Colegio Gaos", "J1": "Plaza de las Banderas", "J2": "Jardín de la Fogata",
    "J3": "Jardín de la Meditación", "J4": "Jardín de la Pareja", "J5": "Lago",
    "J6": "Jardín Central", "AG": "Ágora", "HU": "Humanidades", "LB": "Laboratorios B",
    "LA": "Laboratorios A", "CI": "Ciencias", "IA": "Ingenierías", "CN": "Ciencias Naturales",
    "TI": "Tecnologías de la Información", "HA": "Rectoría", "AU": "Auditorio",
    "CS": "Ciencias Sociales", "NE": "Negocios", "CE": "Centro Estudiantil", "iOS": "Laboratorio iOS",
    "SL": "Ciencias de la Salud", "1": "Crédito y Cobranza", "RH": "Recursos Humanos",
    "PU": "Comunicación", "PF": "Planta Física", "AP": "Acceso Periférico",
    "A14": "Acceso 14", "A14CT": "Acceso 14 Canchas Tenis", "AR": "Acceso Recta"
}

# Conexiones y distancias 
distances = {
    ("AP", "CB"): 193, ("AP", "HU"): 260, ("CB", "HU"): 150, ("HU", "AG"): 70,
    ("AG", "LA"): 110, ("AG", "HA"): 135, ("LA", "HA"): 110, ("LA", "CN"): 90,
    ("LA", "IA"): 60, ("LA", "CI"): 55, ("CI", "LB"): 70, ("CI", "IA"): 70,
    ("IA", "TI"): 70, ("IA", "CN"): 55, ("CN", "TI"): 60, ("CN", "HA"): 95,
    ("CN", "AU"): 70, ("CN", "J1"): 75, ("CN", "BI"): 125, ("TI", "1"): 65,
    ("TI", "J1"): 50, ("1", "J1"): 70, ("1", "BI"): 130, ("1", "RH"): 170,
    ("1", "C4"): 195, ("RH", "PF"): 60, ("RH", "PU"): 60, ("RH", "C4"): 145,
    ("RH", "J4"): 240, ("PU", "C4"): 90, ("PU", "PF"): 100, ("C4", "CFR"): 185,
    ("PF", "AR"): 75, ("AR", "CL"): 170, ("AR", "C1"): 285, ("AR", "C6"): 300,
    ("AR", "CC"): 265, ("BI", "J1"): 55, ("BI", "AU"): 88, ("BI", "J6"): 75,
    ("BI", "J4"): 55, ("BI", "iOS"): 60, ("J4", "iOS"): 45, ("J4", "CC"): 30,
    ("J6", "AU"): 55, ("J6", "iOS"): 100, ("J6", "CE"): 65, ("J6", "CS"): 55,
    ("CS", "NE"): 50, ("NE", "J2"): 115, ("J2", "HA"): 120, ("J2", "J3"): 60,
    ("NE", "J3"): 105, ("NE", "CG"): 190, ("CE", "CS"): 90, ("CE", "iOS"): 50,
    ("CE", "CG"): 265, ("CE", "CRL"): 100, ("CE", "J5"): 95, ("CC", "iOS"): 50,
    ("CC", "J5"): 95, ("CRL", "CG"): 220, ("CRL", "SL"): 100, ("CRL", "J5"): 50,
    ("J5", "TD"): 80, ("J5", "CL"): 230, ("J5", "SL"): 100, ("CL", "TD"): 170,
    ("SL", "C3"): 105, ("SL", "C2"): 80, ("SL", "TD"): 90, ("SL", "GA"): 140,
    ("TD", "C1"): 195, ("C1", "GA"): 160, ("C1", "ATL"): 100, ("C1", "C6"): 200,
    ("C6", "C5"): 250, ("C5", "ATL"): 10, ("C5", "C7"): 190, ("C7", "GC"): 60,
    ("GC", "GB"): 60, ("GC", "CT"): 75, ("GC", "CIR"): 90, ("CIR", "ATL"): 60,
    ("GA", "CIR"): 65, ("GA", "A"): 50, ("GA", "C2"): 85, ("A", "C2"): 100,
    ("A", "GC"): 65, ("A", "BQ"): 50, ("A", "GB"): 55, ("BQ", "C2"): 90,
    ("BQ", "GB"): 25, ("BQ", "A14CT"): 100, ("BQ", "CT"): 40, ("CT", "GB"): 25,
    ("CT", "BQ"): 35, ("CT", "A14CT"): 90
}

# Configuración de posiciones 
img_width, img_height = 1200, 857
node_positions = {
    "GC": (815, img_height - 467), "A": (760, img_height - 462), 
    "GA": (719, img_height - 468), "BQ": (771, img_height - 428),
    "GB": (806, img_height - 438), "CT": (841, img_height - 417),
    "CFR": (103, img_height - 479), "CL": (500, img_height - 511),
    "ATL": (736, img_height - 555), "TD": (580, img_height - 480),
    "CIR": (773, img_height - 500), "CC": (452, img_height - 457),
    "CRL": (574, img_height - 384), "CB": (228, img_height - 215),
    "CG": (678, img_height - 281), "J1": (338, img_height - 403),
    "J2": (424, img_height - 287), "J3": (463, img_height - 277),
    "J4": (409, img_height - 437), "J5": (520, img_height - 428),
    "J6": (426, img_height - 373), "AG": (234, img_height - 313),
    "HU": (221, img_height - 275), "LB": (202, img_height - 375),
    "LA": (273, img_height - 338), "CI": (236, img_height - 371),
    "IA": (272, img_height - 368), "CN": (318, img_height - 364),
    "TI": (290, img_height - 389), "HA": (336, img_height - 327),
    "AU": (367, img_height - 358), "BI": (373, img_height - 413),
    "CS": (446, img_height - 333), "NE": (486, img_height - 318),
    "CE": (459, img_height - 368), "iOS": (442, img_height - 402),
    "SL": (617, img_height - 420), "1": (310, img_height - 431),
    "RH": (263, img_height - 535), "PU": (239, img_height - 550),
    "PF": (318, img_height - 559), "AP": (162, img_height - 188),
    "A14": (449, img_height - 237), "A14CT": (818, img_height - 403),
    "AR": (353, img_height - 610), "C1": (663, img_height - 551),
    "C2": (701, img_height - 433), "C3": (684, img_height - 393),
    "C4": (178, img_height - 541), "C5": (759, img_height - 579),
    "C6": (628, img_height - 647), "C7": (858, img_height - 502)
}

# Agregar nodos y conexiones al grafo
udlap.add_nodes_from(nodes)
for edge, weight in distances.items():
    udlap.add_edge(*edge, weight=weight)

# Función para encontrar la ruta más corta
def shortest_path(graph, start, end):
    try:
        path = nx.dijkstra_path(graph, start, end, weight='weight')
        distance = nx.dijkstra_path_length(graph, start, end, weight='weight')
        return path, distance
    except nx.NetworkXNoPath:
        return None, float('inf')

# Función para dibujar el grafo con el mapa de fondo
def draw_graph(path=None):
    plt.clf()
    ax = plt.gca()
    
    # Cargar y mostrar el mapa de fondo
    if os.path.exists('mapa_udlap.jpg'):
        map_img = plt.imread('mapa_udlap.jpg')
        ax.imshow(map_img, extent=[0, img_width, 0, img_height], alpha=0.8)  
    
    # Configuración de estilos 
    node_size = 180 
    font_size = 9
    edge_width = 2
    
    # Dibujar todas las aristas
    nx.draw_networkx_edges(udlap, pos=node_positions, width=edge_width, 
                         edge_color='darkgray', ax=ax, alpha=0.8)
    
    # NODOS EN NEGRO
    nx.draw_networkx_nodes(udlap, pos=node_positions, node_size=node_size, 
                         node_color='black', ax=ax, alpha=0.9)
    
    # Etiquetas de nodos en blanco sobre negro
    nx.draw_networkx_labels(udlap, pos=node_positions, font_size=font_size, 
                          font_weight='bold', font_color='white',
                          bbox=dict(facecolor='black', edgecolor='white', alpha=0.9, boxstyle='round,pad=0.3'),
                          ax=ax)
    
   
    # Resaltar la ruta 
    if path:
        path_edges = list(zip(path, path[1:]))
        
        # Nodos de la ruta 
        nx.draw_networkx_nodes(udlap, pos=node_positions, nodelist=path, 
                             node_color='black', node_size=node_size*1.3,
                             edgecolors='red', linewidths=2.5, ax=ax)
        
        # Aristas de la ruta
        nx.draw_networkx_edges(udlap, pos=node_positions, edgelist=path_edges, 
                             edge_color='red', width=edge_width*2.5, ax=ax)
        
        # Etiquetas de la ruta
        path_labels = {node: node for node in path}
        nx.draw_networkx_labels(udlap, pos=node_positions, labels=path_labels,
                              font_size=font_size+1, font_weight='bold', 
                              font_color='white',
                              bbox=dict(facecolor='red', edgecolor='black', alpha=0.9),
                              ax=ax)
    
    plt.title("Mapa UDLAP - Ruta más corta", fontsize=14, pad=20)
    plt.tight_layout()
    canvas.draw()


# Función para manejar el cálculo de ruta
def calculate_route():
    start = start_node.get()
    end = end_node.get()
    if start and end:
        path, distance = shortest_path(udlap, start, end)
        if path:
            start_desc = node_descriptions.get(start, start)
            end_desc = node_descriptions.get(end, end)
            route_nom = " → ".join(path)
            result.set(f"Desde {start_desc} hasta {end_desc}, el camino es de {distance} metros.")
            route_result.set(f"Ruta: {route_nom}")
            draw_graph(path)
        else:
            result.set("No hay ruta disponible.")
            route_result.set("")
            draw_graph()
    else:
        result.set("Por favor, selecciona los nodos.")
        route_result.set("")
        draw_graph()

# Crear la interfaz gráfica
# Configuración de la interfaz gráfica
window = tk.Tk()
window.title("Mapa Interactivo UDLAP")
window.geometry("1100x850")
window.configure(bg="#f0f0f0")  # Fondo gris claro


style = ttk.Style()
style.configure('TCombobox', padding=5, font=('Arial', 11))
style.configure('TButton', font=('Arial', 11, 'bold'), padding=5)

# Marco principal
main_frame = tk.Frame(window, bg="#f0f0f0", padx=20, pady=15)
main_frame.pack(fill="both", expand=True)

# Header 
header_frame = tk.Frame(main_frame, bg="#2E7D32")
header_frame.pack(fill="x", pady=(0, 15))

# Logo
logo_label = tk.Label(header_frame, text="UDLAP", font=("Arial", 24, "bold"), 
                     bg="#2E7D32", fg="white", padx=10)
logo_label.pack(side="left")

title_label = tk.Label(header_frame, text="Sistema de Navegación Campus", 
                      font=("Arial", 16, "bold"), bg="#2E7D32", fg="white")
title_label.pack(side="left", padx=10)

# Panel de control
control_frame = tk.Frame(main_frame, bg="#f0f0f0", pady=10)
control_frame.pack(fill="x")

# Controles de selección
tk.Label(control_frame, text="Punto de inicio:", bg="#f0f0f0", 
        font=("Arial", 11)).grid(row=0, column=0, padx=5, sticky="e")

start_node = ttk.Combobox(control_frame, values=nodes, width=15, 
                         font=("Arial", 11), state="readonly")
start_node.grid(row=0, column=1, padx=5)
start_node.set("Seleccione")

tk.Label(control_frame, text="Destino:", bg="#f0f0f0", 
        font=("Arial", 11)).grid(row=0, column=2, padx=5, sticky="e")

end_node = ttk.Combobox(control_frame, values=nodes, width=15, 
                       font=("Arial", 11), state="readonly")
end_node.grid(row=0, column=3, padx=5)
end_node.set("Seleccione")

# Botón con estilo moderno
calculate_btn = tk.Button(control_frame, text="Calcular Ruta", 
                         command=calculate_route, bg="#FFA726", 
                         fg="black", font=("Arial", 11, "bold"),
                         padx=15, pady=5, bd=0, relief="flat",
                         activebackground="#FB8C00", activeforeground="white")
calculate_btn.grid(row=0, column=4, padx=15)

# Panel de resultados
result_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid", 
                       borderwidth=1, padx=10, pady=10)
result_frame.pack(fill="x", pady=(0, 15))

result = tk.StringVar()
result.set("Seleccione puntos de inicio y destino")
result_label = tk.Label(result_frame, textvariable=result, wraplength=1000,
                      justify="left", bg="#ffffff", fg="#333333", 
                      font=("Arial", 11))
result_label.pack(anchor="w")

route_result = tk.StringVar()
route_label = tk.Label(result_frame, textvariable=route_result, wraplength=1000,
                      justify="left", bg="#ffffff", fg="#1E88E5", 
                      font=("Arial", 11, "bold"))
route_label.pack(anchor="w", pady=(5, 0))

# Área del mapa
map_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid", borderwidth=1)
map_frame.pack(fill="both", expand=True)

# Configuración del gráfico
fig = plt.figure(figsize=(10, 7), dpi=100)
fig.patch.set_facecolor('#ffffff')  # Fondo blanco para el área del gráfico
canvas = FigureCanvasTkAgg(fig, master=map_frame)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

# Barra de estado
status_frame = tk.Frame(window, bg="#2E7D32", height=25)
status_frame.pack(fill="x", side="bottom")
status_label = tk.Label(status_frame, text="Sistema de Navegación UDLAP © 2025", 
                       bg="#2E7D32", fg="white", font=("Arial", 9))
status_label.pack(side="right", padx=10)

# Dibujar el grafo inicial
draw_graph()

# Iniciar la aplicación
window.mainloop()
