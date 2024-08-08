from itertools import combinations

# Read the list of teams from the file 'teams.txt'
with open('teams.txt', 'r') as file:
    teams = [line.strip() for line in file if line.strip()]

# Check if we have exactly 10 teams
if len(teams) != 10:
    print(f"Error: The file 'teams.txt' must contain exactly 10 teams. Found {len(teams)} teams.")
else:
    # Generate all possible pairs without duplicates
    pairings = list(combinations(teams, 2))

    # Generate all possible rounds (each round is a combination of 5 pairs)
    # Each team must appear exactly once in a round
    all_rounds = []

    for round_comb in combinations(pairings, 5):
        # Flatten the list of pairs in the round to check if all teams are used exactly once
        teams_used = [team for pair in round_comb for team in pair]
        
        # If all 10 teams are used exactly once, it's a valid round
        if len(set(teams_used)) == 10:
            all_rounds.append(round_comb)

    # Write all possible valid rounds to 'pairings.txt'
    with open('pairings.txt', 'w') as output_file:
        for i, rnd in enumerate(all_rounds, 1):
            output_file.write(f"Round {i}:\n")
            for pair in rnd:
                output_file.write(f"{pair[0]} vs {pair[1]}\n")
            output_file.write("\n")  # Add an empty line between rounds

    print(f"Total number of valid rounds: {len(all_rounds)}")
    print("All rounds have been written to 'pairings.txt'.")
