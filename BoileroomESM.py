from boileroom.esmfold import ESMFold
from boileroom import app
import os
import numpy as np

@app.local_entrypoint()
def main():
    # Initialize the model
    model = ESMFold()

    # Predict structure for a protein sequence
    sequence = "MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKRHDFFKSAMPEGYVQERTIFFKDDGNYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNYNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSALSKDPNEKRDHMVLLEFVTAAGITHGMDELYK"
    
    result = model.fold.remote([sequence])

    # Access prediction results
    coordinates = result.positions
    

    print(coordinates)
    
    def save_to_pdb(sequence, coordinates, file_path):
        """ Save the coordinates of one chain (first model, first chain) to a PDB file."""

        # Convert to numpy array in case it's not already
        coordinates = np.array(coordinates)


        with open(file_path, 'w') as f:
            for i, (res, (x, y, z)) in enumerate(zip(sequence, coords), start=1):
                # Skip zero coordinates (likely padding)
                if np.allclose([x, y, z], 0.0):
                    continue
                f.write(
                    f"ATOM  {i:5d}  CA  {res} A{i:4d}    "
                    f"{x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00           C\n"
                )
            f.write("END\n")

    file_path = os.path.expanduser("~/Desktop/folded_structure_complex2.pdb")
    save_to_pdb(sequence, coordinates, file_path)
    print(f"PDB file saved to: {file_path}")




