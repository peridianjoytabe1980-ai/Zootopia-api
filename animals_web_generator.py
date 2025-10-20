import data_fetcher

# Serialize a single animal into HTML
def serialize_animal(animal):
    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")
    locations = ", ".join(animal.get("locations", []))
    animal_type = animal.get("characteristics", {}).get("type")

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    output += f'      <strong>Location:</strong> {locations}<br/>\n'
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n'
    return output

# Read HTML template
with open("animals_template.html", "r") as file:
    template_content = file.read()

# Fetch animals from API
animal_name = input("Enter a name of an animal: ")
animals = data_fetcher.fetch_data(animal_name)

# Generate full HTML content
if animals:
    output = ''.join(map(serialize_animal, animals))
else:
    output = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"

# Replace placeholder in template
new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# Write the final HTML file
with open("animals.html", "w") as file:
    file.write(new_html)

print("animals.html has been generated successfully!")
