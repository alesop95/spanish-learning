---
generated-from-commit: PENDING-FIRST-COMMIT
generated-from-branch: main
generated-date: 2026-07-06
covers-paths: []
last-verified-commit: PENDING-FIRST-COMMIT
stato: in corso
---

# Lavoro in corso

> La fonte di verità su cosa è fatto resta `memory/index.md` e il work-log, non le spunte di
> questo file.

## Feature: onboarding iniziale del learner

Cosa fa: prima esecuzione di `/profile` per raccogliere topic/obiettivo (spagnolo), livello di
partenza, tempo disponibile e cadenza, profilo cognitivo opt-in, preferenze di stile, e costruire
la prima roadmap pedagogica in `LEARNER_PROFILE.md`.

File da creare: nessuno (la skill `build-roadmap` scrive in `LEARNER_PROFILE.md`, già presente
come scaffold vuoto).

File da modificare:

```
LEARNER_PROFILE.md   popolato con le risposte reali del learner e la roadmap costruita
```

Definition of done:

- [ ] `/profile` eseguito con risposte reali, non placeholder
- [ ] Roadmap pedagogica presente in `LEARNER_PROFILE.md`
- [ ] Prima unità erogata con `/learn`, con citazione di una fonte reale da `SOURCES.md`

Domande aperte:

Se collegare Anki (`ankimcp/anki-mcp-server`) prima o dopo la prima lezione: non bloccante, il
tutor traccia comunque i progressi in `LEARNER_PROFILE.md` in assenza di Anki.

## Riconciliazione

Ultima verifica: 2026-07-06, al commit `PENDING-FIRST-COMMIT`.
