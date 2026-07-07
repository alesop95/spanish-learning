---
generated-from-commit: 2caee17
generated-from-branch: main
generated-date: 2026-07-06
covers-paths: []
last-verified-commit: PENDING-NEXT-COMMIT
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
2. ~~Verificare il comando esatto di `ankimcp/anki-mcp-server`~~ — fatto 2026-07-06, `.mcp.json`
   aggiornato col comando reale (`@ankimcp/anki-mcp-server --stdio`). Resta da fare, a carico
   dell'utente: installare Anki desktop + add-on AnkiConnect e verificare la connessione dal vivo.
3. Aprire il vault Obsidian `vault-spagnolo/` e verificare che gli account Claude Code lo vedano
   tramite il server `obsidian-vaults` aggiornato.
4. Rivalutare l'upgrade da `doc-ingest` a `knowledge-mcp` quando il corpus indicizzato cresce oltre
   i pochi libri già presenti, o quando serve un retrieval semantico più preciso della sola cache
   Markdown.
5. ~~Costruire il mazzo Anki dedicato ai falsi amici italiano→spagnolo~~ — fatto 2026-07-06,
   `tools/generate-falsos-amigos-deck.py` (18 falsi amici + 4 interferenze grammaticali). Da
   importare in Anki una volta installato.
7. Procurarsi "Spanish Pronouns and Prepositions" (unico libro digitale catalogato ma assente
   dall'archivio, vedi `SOURCES.md` sezione 2) se serve materiale per `spa-02`/`spa-09`.
6. (Bassa priorità, da valutare in parallelo) Un deploy pubblico e leggibile ovunque di
   `LEARNER_PROFILE.md` / `SOURCES.md` / `SESSION-LOG.md`, per consultare roadmap e fonti anche
   fuori da Claude Code (es. da telefono). Il repository è già pubblico su GitHub, quindi i file
   Markdown sono già leggibili via `github.com/alesop95/spanish-learning` senza deploy aggiuntivo;
   un passo oltre sarebbe GitHub Pages con un rendering più leggibile (indice, roadmap con stato
   dei moduli, log sessioni), da valutare senza urgenza e senza esporre nulla oltre a ciò che è già
   tracciato (nessun binario, coerente con ADR-005).

## Idee e ipotesi da verificare

~~Se il titolo "Pronouns and Prepositions" ... o incluso in uno dei volumi "all-in-one"~~ —
risolto 2026-07-06: è un libro reale, genuinamente assente dall'archivio (vedi `SOURCES.md`,
sezione 2). Da recuperare se serve per `spa-02` o `spa-09`.
~~Se le due copie di "Spanish Verb Tenses" ... siano edizioni diverse~~ — risolto 2026-07-06:
stesso contenuto, duplicato rimosso su conferma dell'utente.

Nuovo, emerso dalla verifica del catalogo: **"Contacto — Curso de español para italianos"**
(cartaceo, Zanichelli, con attività DELE Nivel Intermedio) è una fonte molto pertinente non
ancora usata in nessuna unità della roadmap pedagogica — valutare se e quando introdurla in
`LEARNER_PROFILE.md` una volta che il learner arriva al livello intermedio.
