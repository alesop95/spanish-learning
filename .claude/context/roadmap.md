---
generated-from-commit: PENDING-FIRST-COMMIT
generated-from-branch: main
generated-date: 2026-07-06
covers-paths: []
last-verified-commit: PENDING-FIRST-COMMIT
---

# Roadmap

> Direzione e priorità del *progetto* (strumenti, integrazioni). Distinta dalla roadmap
> *pedagogica* dello spagnolo, che vive dentro `LEARNER_PROFILE.md` ed è costruita da
> `build-roadmap` in base a categoria, livello e cadenza del learner.

## Direzione

Portare il tutor da un setup minimo (solo file locali + doc-ingest) a un ambiente con spaced
repetition attiva e, se il corpus lo giustifica, retrieval semantico vero.

## Priorità

1. Eseguire `/profile` e ottenere la prima roadmap pedagogica reale.
2. Installare Anki desktop + AnkiConnect e verificare il comando esatto di `ankimcp/anki-mcp-server`
   dal suo README, poi collegarlo in `.mcp.json`.
3. Aprire il vault Obsidian `vault-spagnolo/` e verificare che gli account Claude Code lo vedano
   tramite il server `obsidian-vaults` aggiornato.
4. Rivalutare l'upgrade da `doc-ingest` a `knowledge-mcp` quando il corpus indicizzato cresce oltre
   i pochi libri già presenti, o quando serve un retrieval semantico più preciso della sola cache
   Markdown.
5. Costruire il mazzo Anki dedicato ai falsi amici italiano→spagnolo (sezione 7 di `SOURCES.md`),
   dato che nessun mazzo pubblico esistente lo copre.

## Idee e ipotesi da verificare

Se il titolo "Pronouns and Prepositions" catalogato in `elenco_libri_spagnolo_0220.xlsx` sia
davvero mancante dall'archivio estratto o incluso in uno dei volumi "all-in-one" (vedi `SOURCES.md`,
sezione 2). Se le due copie di "Spanish Verb Tenses" (hash diversi) siano edizioni diverse o una
scansione di qualità inferiore da scartare.
