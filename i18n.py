supported_langs = ["en_US", "es_MX"]

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

