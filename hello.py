from i18n import T 

name = input(f"{T['name']}? ")
if name:
    print(f"{T['hello']}, {name}!")
else:
    print(f"{T['hello']}, {T['world']}!")
