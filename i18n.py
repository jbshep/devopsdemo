supported_langs = ["en_US", "es_MX"]

from pathlib import Path
if not Path('.lang').exists():
    open('.lang').write('en_US')

current_lang = open('.lang').read().strip()
if not current_lang:
    current_lang = "en_US"

trans = {
    "en_US" : {
        "hello" : "hello",
        "world" : "world",
        "name" : "name",
    },
    "es_MX" : {
        "hello" : "hola",
        "world" : "mundo",
        "name" : "nombre",
    },
}

T = trans[current_lang]
