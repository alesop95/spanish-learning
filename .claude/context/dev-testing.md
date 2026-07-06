---
generated-from-commit: 2caee17
generated-from-branch: main
generated-date: 2026-07-06
covers-paths:
  - tools/doc-ingest.py
last-verified-commit: 2caee17
---

# Test di sviluppo

> Adattata: non ci sono test automatici applicativi. La verifica end-to-end rilevante qui è che
> la pipeline di ingestione funzioni e che il loop di apprendimento (`/profile` → `/learn` →
> `/review`) sia effettivamente eseguibile.

## Verifica della pipeline di ingestione

`python tools/doc-ingest.py` deve girare senza errori sul corpus in `_notes/raw-sources/` e
produrre `_notes/.tmp-doc-cache/_INDEX.md` aggiornato. Rieseguirlo dopo ogni aggiunta di nuovi
documenti grezzi.

## Verifica del loop di apprendimento

Checklist operativa manuale in `_notes/TEST-CHECKLIST.md` (locale, non tracciata): prima
esecuzione di `/profile`, poi `/learn` (deve citare una fonte reale da `SOURCES.md` o dalla
cache), poi `/review` se Anki è collegato.

## Hook e controlli di qualità

Nessuno automatizzato per ora; nessun lint o build applicabile a un progetto senza codice
applicativo.
