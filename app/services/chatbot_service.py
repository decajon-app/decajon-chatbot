from transformers import pipeline

# Modelo NER
ner_pipeline = pipeline("ner", 
                        model = "bertin-project/bertin-roberta-base-spanish", 
                        aggregation_strategy="simple")

# INTENTS
INTENTS = {
    "agregar_cancion_a_grupo": ["agregar", "añadir", "poner", "incorporar", "agregar canción"],
}

# Detecar el intent basado en palabras clave
def detect_intent(command: str):
    for keyword, intent in INTENTS.items():
        if keyword in command.lower():
            return intent
    return "unknown"

def extract_entities(command: str):
    entities = ner_pipeline(command)
    return [{"entity": e['entity_group'], "word": e['word']} for e in entities]

def process_command(command: str):
    intent = detect_intent(command)
    entities = extract_entities(command)
    return {"intent": intent, "entities": entities}