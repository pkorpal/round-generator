import random

def parse_rounds(file_path):
    """Parse the rounds from a pairings file."""
    with open(file_path, 'r') as file:
        rounds = []
        current_round = []
        
        for line in file:
            line = line.strip()
            if line.startswith("Round"):
                if current_round:
                    rounds.append(current_round)
                    current_round = []
            elif "vs" in line:
                pair = tuple(line.split(" vs "))
                current_round.append(pair)
        
        # Add the last round
        if current_round:
            rounds.append(current_round)
    
    return rounds

def write_round_to_file(round, output_file):
    """Write the selected round to an output file."""
    with open(output_file, 'w') as file:
        file.write(f"Random Round:\n")
        for pair in round:
            file.write(f"{pair[0]} vs {pair[1]}\n")

def main():
    # File paths
    filtered_pairings_file = 'filtered_pairings.txt'
    output_file = 'random_round.txt'
    
    # Parse the filtered rounds from 'filtered_pairings.txt'
    rounds = parse_rounds(filtered_pairings_file)
    
    if not rounds:
        print("No rounds found in the filtered pairings file.")
        return
    
    # Select one random round
    selected_round = random.choice(rounds)
    
    # Write the selected round to 'random_round.txt'
    write_round_to_file(selected_round, output_file)
    
    print(f"A random round has been written to '{output_file}'.")

if __name__ == "__main__":
    main()
