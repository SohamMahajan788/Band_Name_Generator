import pyfiglet

print("🎵 Welcome to Band Name Generator! 🎸")
city_name = input("🏙️ What is the name of the city you grew up in? 🌆\n")
pet_name = input("🐾 What's your pet's name?\n")
band_name = city_name + " " + pet_name
ascii_art = pyfiglet.figlet_format(band_name)
print("🎤 Your Band name could be:\n")
print(ascii_art)