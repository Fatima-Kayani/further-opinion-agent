import requests
import pandas as pd

terms = []
page = 1

while True:
    print(f"Fetching page {page}...")
    response = requests.get("https://api.disease-ontology.org/v1/terms", params={"page": page, "page_size": 100})
    data = response.json()

    if not data["results"]:
        break

    for item in data["results"]:
        terms.append({
    "id": item.get("id"),
    "label": item.get("label"),
    "definition": item.get("definition", ""),
    "synonyms": ", ".join(
        s["label"] if isinstance(s, dict) and "label" in s else str(s)
        for s in item.get("synonyms", [])
        if s
    ),
    "xrefs": ", ".join(item.get("xrefs", []))
})


    page += 1

# Save for backup
df = pd.DataFrame(terms)
df = df[df["definition"] != ""]  # remove entries without definitions
df.to_csv("disease_ontology.csv", index=False)