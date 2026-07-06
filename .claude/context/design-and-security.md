---
generated-from-commit: 2caee17
generated-from-branch: main
generated-date: 2026-07-06
covers-paths: []
last-verified-commit: 2caee17
---

# Design e sicurezza applicativa

> Non applicabile nella forma prevista dal template: questo è un progetto di apprendimento
> personale, non un'applicazione con superfici esposte o autenticazione. Scheda mantenuta come
> scaffold minimo per coerenza con l'anatomia canonica, non riempita di contenuto inventato.

## Paradigmi di software design

Non applicabile: nessun codice applicativo, solo orchestrazione di agenti/skill e uno script di
ingestione documentale (`tools/doc-ingest.py`), la cui logica vive nel template di origine e non
si duplica qui.

## Sicurezza applicativa

L'unica superficie rilevante è la privacy dei dati personali del learner: `LEARNER_PROFILE.md` è
tracciato e pubblico (il repository GitHub è pubblico), quindi non deve mai contenere dati
sensibili oltre a preferenze di apprendimento. I libri protetti da copyright restano
deliberatamente fuori da git (`_notes/raw-sources/`, vedi `.gitignore`); solo i metadati
bibliografici in `SOURCES.md` sono tracciati. Nessun segreto o credenziale è previsto in questo
progetto.

## Diagrammi

Nessun diagramma applicabile per ora.
