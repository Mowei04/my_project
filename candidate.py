"""
@author: Jiawei Lin
"""
import os
import csv


class Candidate:
    def __init__(self, filepath: str):
        # Check if file exists
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        self.header = []
        self.data = []
        with open(filepath, mode='r') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)

                # Check if file is empty
                if not rows:
                    raise ValueError("The file is empty.")

                # Assign header and validate it
                self.header = rows[0]
                if not self.header or any(not col.strip() for col in self.header):
                    raise ValueError("The header contains empty or invalid columns.")

                # Assign data and initialize votes to 0
                for row in rows[1:]:
                    if len(row) != len(self.header) or any(not cell.strip() for cell in row):
                        raise ValueError(f"Invalid data row: {row}")
                    # Initialise votes to 0;
                    row[-1] = 0
                    self.data.append(row)  

    def details(self) -> list:
        details = []
        for row in self.data:
            dict = {}
            for i in range(len(self.header)):
                dict[self.header[i]] = row[i]
            details.append(dict)
        return details
        

if __name__ == "__main__":
    # You can add more code or comment out the following to test your
    # implementation. If you are commenting out the code, make sure there
    # is at least one line of code left when you submit this to Gradescope
    candidate = Candidate('candidates.csv')
    print("Header:", candidate.header)
    print(candidate.details())
