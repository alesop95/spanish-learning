---
generated-from-commit: 2caee17
generated-from-branch: main
generated-date: 2026-07-06
covers-paths: []
last-verified-commit: PENDING-NEXT-COMMIT
stato: in verifica
---

# Lavoro in corso

> La fonte di verità su cosa è fatto resta `memory/index.md` e il work-log, non le spunte di questo file.

## Feature: onboarding iniziale del learner

Cosa fa: prima esecuzione di `/profile` per raccogliere topic/obiettivo (spagnolo), livello di partenza, tempo disponibile e cadenza, profilo cognitivo opt-in, preferenze di stile, e costruire la prima roadmap pedagogica in `LEARNER_PROFILE.md`.

File da creare: nessuno (la skill `build-roadmap` scrive in `LEARNER_PROFILE.md`, già presente come scaffold vuoto).

File da modificare:

```
LEARNER_PROFILE.md   popolato con le risposte reali del learner e la roadmap costruita
README.md            guida pubblica e operativa d'uso del sistema, creata da zero
```

Definition of done:

- [x] `/profile` eseguito con risposte reali, non placeholder
- [x] Roadmap pedagogica presente in `LEARNER_PROFILE.md` (unità spa-01…spa-11)
- [x] Comando `anki-mcp-server` verificato, OCR funzionante, mazzo falsi amici generato, catalogo libri corretto (giro di sviluppo chiuso 2026-07-07)
- [x] Documentazione operativa scritta in `README.md` (onboarding, ciclo di studio, doc-ingest, Anki, mazzo falsi amici, vault, stato e riferimenti)
- [x] Prima unità erogata con `/learn` (spa-01), con citazione di fonti reali della libreria catalogata in `SOURCES.md` (Spanish Conversation, Basic Spanish, Complete Spanish All-in-One)

Domande aperte: nessuna bloccante. La feature di onboarding iniziale è chiusa; il lavoro prosegue come normale ciclo pedagogico (`/learn`/`/review`) guidato dalla roadmap in `LEARNER_PROFILE.md`, non più tracciato qui finché non emerge una feature strutturale nuova (es. collegamento reale di Anki, o un cambio di stack).

## Riconciliazione

Ultima verifica: 2026-07-07, al commit `2caee17` (modifiche successive non ancora committate).
