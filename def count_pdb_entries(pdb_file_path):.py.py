def count_pdb_entries(pdb_file_path):
    count = 0
    with open(pdb_file_path, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                count += 1
    return count

# Example usage:
print(count_pdb_entries("/Users/tobyhallett/Desktop/folded_structure_complex2.pdb"))