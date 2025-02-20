from i18n import current_lang, trans

name = input(f"{trans[current_lang]['name']}? ")
if name:
    print(f"{trans[current_lang]['hello']}, {name}!")
else:
    print(f"{trans[current_lang]['hello']}, {trans[current_lang]['world']}!")
