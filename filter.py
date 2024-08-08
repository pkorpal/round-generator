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
                pair = tuple(sorted(line.split(" vs ")))  # Sort pair to ensure order doesn't matter
                current_round.append(pair)
        
        # Add the last round
        if current_round:
            rounds.append(current_round)
    
    return rounds

def filter_rounds(input_round, all_rounds):
    """Remove all rounds containing any of the pairings from the input round, regardless of order."""
    filtered_rounds = []
    input_set = set(input_round)
    
    for rnd in all_rounds:
        if not input_set.intersection(set(rnd)):
            filtered_rounds.append(rnd)
    
    return filtered_rounds

def write_rounds_to_file(rounds, output_file):
    """Write the filtered rounds to an output file."""
    with open(output_file, 'w') as file:
        for i, rnd in enumerate(rounds, 1):
            file.write(f"Round {i}:\n")
            for pair in rnd:
                file.write(f"{pair[0]} vs {pair[1]}\n")
            file.write("\n")  # Add an empty line between rounds

def read_input_round(file_path):
    """Read the input round from a previous pairings file."""
    input_round = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if "vs" in line:
                pair = tuple(sorted(line.split(" vs ")))  # Sort pair to ensure order doesn't matter
                input_round.append(pair)
    return input_round

def main():
    # File paths
    pairings_file = 'pairings.txt'
    previous_pairings_file = 'previous_pairings.txt'
    output_file = 'filtered_pairings.txt'
    
    # Read the input round from 'previous_pairings.txt'
    input_round = read_input_round(previous_pairings_file)
    
    # Parse all rounds from the pairings file
    all_rounds = parse_rounds(pairings_file)
    
    # Filter rounds based on the input round
    filtered_rounds = filter_rounds(input_round, all_rounds)
    
    # Write the filtered rounds to the output file
    write_rounds_to_file(filtered_rounds, output_file)
    
    print(f"Filtered rounds have been written to '{output_file}'.")
    print(f"Number of filtered rounds: {len(filtered_rounds)}")

if __name__ == "__main__":
    main()
