from transformers import pipeline

# Modelo NER
ner_pipeline = pipeline("ner", 
                        model = "bertin-project/bertin-roberta-base-spanish", 
                        aggregation_strategy="simple")

# INTENTS
INTENTS = {
    "añade": "add_song",
    "agrega": "add_song",
    "canciones pendientes": "list_pending_rehearsals",
    "ensayo pendiente": "list_pending_rehearsals"
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