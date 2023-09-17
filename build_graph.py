from pyvis.network import Network
from parse_files import build_files_dependency_nodes_and_edges
from parse_functions import build_funcs_dependency_nodes_and_edges

def process_summary(summary):
    char_count = 0
    result = ""
    words = summary.split()
    for word in words:
        if char_count > 0:
            result += " "
            char_count += 1
        result += word
        char_count += len(word)
        if char_count >= 20:
            result += "\n"
            char_count = 0
    return result

def build_dependency_graph(nodes, edges):
    net = Network(height="1250px", width="100%", bgcolor="#03001C", font_color="black", directed=True, layout={"circle": True}, select_menu=True, filter_menu=False
)

    for node in nodes:
        title_summary = process_summary(node[1])
        print(node[0], title_summary)
        if "." in node[0]:
            net.add_node(n_id=node[0], title=title_summary, color="#A5D7E8", size=25, label=node[0], shape="circle")
        else:
            net.add_node(n_id=node[0], title=title_summary, color="#FFDEB4", size=40, label=node[0], shape="circle")
    for edge in edges:
        source, target = edge
        if "." in source:
            net.add_edge(source, target, color="#57C5B6", width=3, arrowStrikethrough=False)
        else:
            net.add_edge(source, target, color="#FFDEB4", width=3, arrowStrikethrough=False)
    return net

def build_graph(file_to_code_summary_map):
    nodes, edges = build_files_dependency_nodes_and_edges(file_to_code_summary_map)
    dependency_graph = build_dependency_graph(nodes, edges)
    dependency_graph.show("file_graph.html", notebook=False)
    nodes, edges = build_funcs_dependency_nodes_and_edges(file_to_code_summary_map)
    dependency_graph = build_dependency_graph(nodes, edges)
    dependency_graph.show("func_graph.html", notebook=False)

file_to_code_summary_map = {
    "main": ("", "FOLDER SUMMARY"),
    "module1": ("", "FOLDER SUMMARY"),
    "module2": ("", "FOLDER SUMMARY"),
    "main/main.py": ("# main.py\nfrom module1.module1 import foo\ndef bar():\n\tbaz()\n\tfoo()\ndef baz():\n\tpass\nbar()", "SUMMARY 11"),
    "module1/module1.py": ("# module1.py\nfrom module2.module2 import foo\ndef bar():\n\tfoo()\ndef baz():\n\tpass", "SUMMARY 22fvabdfk vbajdf bvladf vlkabf lkv baklbfvl abdfv kjbafl vbadbvj kladb vjabv"),
    "module2/module2.py": ("# module2.py\ndef foo():\n\tpass", "SUMMARY 33"),
}
build_graph(file_to_code_summary_map)