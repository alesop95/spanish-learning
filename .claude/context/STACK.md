---
generated-from-commit: 2caee17
generated-from-branch: main
generated-date: 2026-07-06
covers-paths:
  - .mcp.json
  - tools/doc-ingest.py
  - _notes/.tmp-doc-cache/**
  - vault-spagnolo/**
last-verified-commit: 2caee17
---

# Stack di apprendimento

> Non è un progetto software: questa scheda descrive lo stack di strumenti che sostiene il tutor
> (`.claude/agents/tutor.md`), non un'applicazione. Popolata dalle decisioni prese in sessione di
> allineamento, non inventata.

## Stack e strumenti

Orchestrazione: Claude Code, pacchetto `learning-agent` (tre subagent, tre skill, tre comandi,
vedi `context/learning-agent-reference.md`). Knowledge base: `doc-ingest` (script Python,
`tools/doc-ingest.py`, dipendenza `markitdown`), che indicizza il corpus di `_notes/raw-sources/`
in una cache Markdown a costo zero sotto `_notes/.tmp-doc-cache/`, senza retrieval semantico.
Spaced repetition: `ankimcp/anki-mcp-server` via `.mcp.json`, proxy locale verso Anki
desktop + add-on AnkiConnect (installazione degli applicativi desktop a carico dell'utente).
Superficie di note personali: vault Obsidian dedicato in `vault-spagnolo/` (locale, non tracciato),
raggiungibile dagli account Claude Code di questa macchina tramite il server MCP `obsidian-vaults`
configurato a livello di account.

## Alternative deliberatamente escluse (per ora)

`knowledge-mcp` (RAG ibrido vettoriale+grafo su LightRAG) è stato valutato e scartato **solo per
l'avvio**, a favore di `doc-ingest` che ha setup più leggero; resta il upgrade path naturale
quando il corpus cresce o servono query semantiche vere (richiede Python 3.12 + `uv`, non ancora
verificati su questa macchina). `mcp-ankiconnect` (alternativa minimale ad `anki-mcp-server`) è
stato scartato a favore del server più maturo e mantenuto (vedi `SOURCES.md`, sezione 10).

## Flussi

Il learner esegue `/profile` (build-roadmap) per l'onboarding e la roadmap pedagogica, poi
`/learn` per erogare unità (tutor → kb-retriever legge `_notes/.tmp-doc-cache/` → examiner
verifica con active recall) e `/review` per il ripasso spaziato via Anki. Ogni unità cita sempre
`SOURCES.md` oltre alla knowledge base locale.

## Riferimenti a snippet

`.claude/agents/tutor.md`, `.claude/agents/kb-retriever.md` (nota di progetto in coda al file),
`tools/doc-ingest.py`, `SOURCES.md`.
