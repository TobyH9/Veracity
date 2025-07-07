import py3Dmol

def view_pdb(pdb_path):
    with open(pdb_path, 'r') as f:
        pdb_data = f.read()

    view = py3Dmol.view(width=600, height=400)
    view.addModel(pdb_data, 'pdb')
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.zoomTo()
    return view.show()

view_pdb("/Users/tobyhallett/Desktop/folded_structure.pdb")