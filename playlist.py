# Playlist with duplicate songs
songs = [
    "Blinding Lights",
    "Levitating",
    "Blinding Lights",
    "Stay",
    "Peaches",
    "Levitating",
    "Good 4 U",
    "Montero",
    "Stay",
    "Industry Baby",
    "Happier Than Ever",
    "Blinding Lights",
    "Bad Habits",
    "Good 4 U",
    "Montero",
    "Leave The Door Open",
    "Drivers License",
    "Happier Than Ever",
    "Kiss Me More"
]

# Create playlist.txt
with open("playlist.txt", "w") as file:
    for song in songs:
        file.write(song + "\n")

# Read file
with open("playlist.txt", "r") as file:
    lines = file.readlines()

# Remove spaces
lines = [line.strip() for line in lines]

# Remove duplicates
unique_songs = sorted(set(lines))

# Write cleaned playlist
with open("playlist_clean.txt", "w") as file:
    for song in unique_songs:
        file.write(song + "\n")

# Output
print("Total Songs :", len(lines))
print("Unique Songs:", len(unique_songs))
print("Duplicates Removed:", len(lines)-len(unique_songs))
print("playlist_clean.txt created successfully.")