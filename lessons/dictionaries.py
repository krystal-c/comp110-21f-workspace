"""Demonstrations of dictionary capabilities."""


# Declaring the type of dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary 
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students") 

# Remove a key value pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for the existance of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

print(schools)

# Update/reassign key-value pair
schools["UNC"] = 20_000
schools["NCSU"] += 200

# Demonstration of dictionary literals

# Empty dictionary literals
schools = {}  # Same as dict()
print(schools)

# Alternatively, initialize the key-value pairs
schools = {"UNC": 19_400, "Dukie": 6_717, "NCSU": 26_150}
print(schools)

# What happens when a key does not exist? 
print(schools["UNCC"])