---
generated-from-commit: 2caee17
generated-from-branch: main
generated-date: 2026-07-06
covers-paths: []
last-verified-commit: 2caee17
---

# Roadmap

> Direzione e priorità del *progetto* (strumenti, integrazioni). Distinta dalla roadmap
> *pedagogica* dello spagnolo, che vive dentro `LEARNER_PROFILE.md` ed è costruita da
> `build-roadmap` in base a categoria, livello e cadenza del learner.

## Direzione

Portare il tutor da un setup minimo (solo file locali + doc-ingest) a un ambiente con spaced
repetition attiva e, se il corpus lo giustifica, retrieval semantico vero.

## Priorità

1. ~~Eseguire `/profile` e ottenere la prima roadmap pedagogica reale~~ — fatto 2026-07-06, vedi
   `LEARNER_PROFILE.md`.
2. Installare Anki desktop + AnkiConnect e verificare il comando esatto di `ankimcp/anki-mcp-server`
   dal suo README, poi collegarlo in `.mcp.json`.
3. Aprire il vault Obsidian `vault-spagnolo/` e verificare che gli account Claude Code lo vedano
   tramite il server `obsidian-vaults` aggiornato.
4. Rivalutare l'upgrade da `doc-ingest` a `knowledge-mcp` quando il corpus indicizzato cresce oltre
   i pochi libri già presenti, o quando serve un retrieval semantico più preciso della sola cache
   Markdown.
5. Costruire il mazzo Anki dedicato ai falsi amici italiano→spagnolo (sezione 7 di `SOURCES.md`),
   dato che nessun mazzo pubblico esistente lo copre.
6. (Bassa priorità, da valutare in parallelo) Un deploy pubblico e leggibile ovunque di
   `LEARNER_PROFILE.md` / `SOURCES.md` / `SESSION-LOG.md`, per consultare roadmap e fonti anche
   fuori da Claude Code (es. da telefono). Il repository è già pubblico su GitHub, quindi i file
   Markdown sono già leggibili via `github.com/alesop95/spanish-learning` senza deploy aggiuntivo;
   un passo oltre sarebbe GitHub Pages con un rendering più leggibile (indice, roadmap con stato
   dei moduli, log sessioni), da valutare senza urgenza e senza esporre nulla oltre a ciò che è già
   tracciato (nessun binario, coerente con ADR-005).

## Idee e ipotesi da verificare

Se il titolo "Pronouns and Prepositions" catalogato in `elenco_libri_spagnolo_0220.xlsx` sia
davvero mancante dall'archivio estratto o incluso in uno dei volumi "all-in-one" (vedi `SOURCES.md`,
sezione 2). Se le due copie di "Spanish Verb Tenses" (hash diversi) siano edizioni diverse o una
scansione di qualità inferiore da scartare.
