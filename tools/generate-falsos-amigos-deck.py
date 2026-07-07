#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate-falsos-amigos-deck.py - Genera un mazzo Anki (.apkg) dedicato ai falsi
amici e alle interferenze grammaticali italiano->spagnolo (unita' spa-02 della
roadmap in LEARNER_PROFILE.md).

Nessun mazzo pubblico su AnkiWeb copre questa coppia di lingue (verificato in
SOURCES.md, sezione 5), quindi il mazzo si genera da una lista curata invece di
scaricarne uno. La lista di falsi amici lessicali riprende SOURCES.md sezione 7
(a sua volta da ricerca su fonti pedagogiche italiano<->spagnolo) ed e' ampliata
con voci di uso comune, generalmente note nella didattica delle due lingue, non
bisognose di citazione puntuale come i dati di ricerca. Le interferenze
grammaticali sono un piccolo set separato, taggato a parte.

Uso:
    python generate-falsos-amigos-deck.py
    python generate-falsos-amigos-deck.py --out _notes/anki-decks/falsos-amigos-it-es.apkg

Dipendenza: genanki (pip install genanki). L'output .apkg e' un artefatto
derivato, non tracciato in git (vedi .gitignore, cartella _notes/): la fonte di
verita' e' la lista Python in questo script, tracciata.
"""

import argparse
import genanki

# ID fissi e stabili: reimportare il mazzo aggiorna le card esistenti invece di
# duplicarle, a patto di non rigenerarli.
MODEL_ID = 1607392319
DECK_ID = 1607392320

MODEL = genanki.Model(
    MODEL_ID,
    "Falso amico IT-ES",
    fields=[
        {"name": "Parola"},
        {"name": "Trappola"},
        {"name": "Significato reale"},
        {"name": "Come si dice invece"},
        {"name": "Esempio"},
    ],
    templates=[
        {
            "name": "Riconoscimento",
            "qfmt": "In spagnolo, cosa significa <b>{{Parola}}</b>?<br><i>(occhio alla somiglianza con l'italiano)</i>",
            "afmt": (
                "{{FrontSide}}<hr id='answer'>"
                "<b>Significa:</b> {{Significato reale}}<br>"
                "<b>Trappola:</b> {{Trappola}}<br>"
                "<b>Per dire {{Trappola}} in spagnolo:</b> {{Come si dice invece}}<br>"
                "<i>{{Esempio}}</i>"
            ),
        }
    ],
)

# Falsi amici lessicali: (parola spagnola, cosa un italiano assume per somiglianza,
# significato reale in spagnolo, come si dice invece in spagnolo il concetto italiano, esempio)
FALSOS_AMIGOS = [
    ("burro", "burro (alimento)", "asino (donkey)", "mantequilla", "El burro lleva la carga por el camino."),
    ("guardar", "guardare (to look at)", "custodire, conservare, tenere", "mirar", "Voy a guardar este dinero para el viaje."),
    ("salir", "salire (to go up)", "uscire (to go out)", "subir", "Salgo de casa a las ocho."),
    ("pronto", "pronto (ready)", "presto, tra poco (soon)", "listo", "Hasta pronto, nos vemos la próxima semana."),
    ("carta", "carta (paper)", "lettera (letter); anche carta da gioco/menu", "papel", "Te escribo esta carta desde Madrid."),
    ("oficina", "officina (workshop/garage)", "ufficio (office)", "taller", "Trabajo en una oficina en el centro."),
    ("loro", "loro (they/their)", "pappagallo (parrot)", "ellos / ellas / su(s)", "El loro repite todo lo que oye."),
    ("aceite", "aceto (vinegar)", "olio (oil)", "vinagre", "Cocino con aceite de oliva."),
    ("contestar", "contestare (to protest/dispute)", "rispondere (to answer)", "protestar / impugnar", "Voy a contestar tu mensaje mañana."),
    ("embarazada", "imbarazzata (embarrassed)", "incinta (pregnant)", "avergonzada", "Mi hermana está embarazada de seis meses."),
    ("largo", "largo (wide)", "lungo (long)", "ancho", "El viaje fue muy largo."),
    ("topo", "topo (mouse)", "talpa (mole)", "ratón", "El topo cava túneles bajo el jardín."),
    ("gamba", "gamba (leg)", "gambero (shrimp/prawn)", "pierna", "Pedimos gambas a la plancha."),
    ("mantel", "mantello (cloak)", "tovaglia (tablecloth)", "manto / capa", "Pon el mantel antes de cenar."),
    ("aula", "aula (classroom, in realtà uguale)", "aula, ma anche 'aura' in alcuni contesti letterari — attenzione minima, quasi vero amico", "aula", "La clase empieza en el aula 3."),
    ("subir", "subire (to suffer/undergo)", "salire (to go up)", "sufrir / padecer", "Vamos a subir la montaña este fin de semana."),
    ("presunto", "presunto (alleged); non 'prosciutto'", "presunto (alleged) — quasi vero amico, ma occhio a non pensare al salume", "jamón (per il salume)", "El presunto culpable fue detenido ayer."),
    ("squadra", "squadra (team, in italiano)", "escuadra = strumento da disegno/riga a squadra; il team si dice 'equipo'", "equipo", "Nuestro equipo ganó el partido."),
]

# Interferenze grammaticali (tag separato, non falsi amici lessicali)
GRAMMAR_MODEL = genanki.Model(
    MODEL_ID + 1,
    "Interferenza grammaticale IT-ES",
    fields=[{"name": "Domanda"}, {"name": "Risposta"}],
    templates=[
        {
            "name": "Concetto",
            "qfmt": "{{Domanda}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Risposta}}",
        }
    ],
)

GRAMMAR_POINTS = [
    (
        "Perché 'ayer he comido' suona strano a un ispanofono, anche se un italiano lo direbbe naturale ('ieri ho mangiato')?",
        "Lo spagnolo distingue più nettamente il pretérito indefinido (ayer comí, azione conclusa e datata) dal pretérito perfecto compuesto (he comido, con effetto sul presente o oggi). L'italiano usa il passato prossimo per entrambi i casi, quindi l'interferenza tipica è usare troppo 'he + participio' dove uno spagnolo userebbe l'indefinido.",
    ),
    (
        "Perché non si può sempre tradurre 'per' con una sola parola in spagnolo?",
        "Lo spagnolo distingue 'por' (causa, mezzo, tempo approssimativo, scambio: 'gracias por tu ayuda') da 'para' (scopo, destinazione, destinatario: 'esto es para ti'). L'italiano usa 'per' per entrambi i casi, quindi va imparata la distinzione caso per caso, non tradotta a orecchio.",
    ),
    (
        "Perché il congiuntivo spagnolo sembra comparire più spesso di quello italiano?",
        "Lo spagnolo usa il congiuntivo in più contesti obbligatori (dopo 'querer que', 'es posible que', 'cuando' riferito al futuro, ecc.) dove l'italiano a volte accetta l'indicativo o l'infinito. Non fidarsi dell'istinto dall'italiano: verificare caso per caso se il verbo reggente richiede il congiuntivo.",
    ),
    (
        "Qual è l'errore di pronuncia più comune di un italiano sulla 'r' e la 'j' spagnole?",
        "La 'r' vibrante spagnola (in posizione iniziale o doppia, 'rr') è più marcata di qualunque 'r' italiana: va esercitata a parte. La 'j' spagnola è un suono aspirato gutturale (come una 'h' forte), non la 'g' dolce o la 'gi' italiana: un italiano tende a addolcirla per abitudine.",
    ),
]


def build_deck():
    deck = genanki.Deck(DECK_ID, "Spagnolo::Falsi amici e interferenze IT-ES")
    for parola, trappola, significato, come_si_dice, esempio in FALSOS_AMIGOS:
        note = genanki.Note(
            model=MODEL,
            fields=[parola, trappola, significato, come_si_dice, esempio],
            tags=["falso-amico", "spa-02"],
        )
        deck.add_note(note)
    for domanda, risposta in GRAMMAR_POINTS:
        note = genanki.Note(
            model=GRAMMAR_MODEL,
            fields=[domanda, risposta],
            tags=["interferenza-grammaticale", "spa-02"],
        )
        deck.add_note(note)
    return deck


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[2])
    parser.add_argument(
        "--out",
        default="_notes/anki-decks/falsos-amigos-it-es.apkg",
        help="Percorso di output del file .apkg (default: _notes/anki-decks/falsos-amigos-it-es.apkg)",
    )
    args = parser.parse_args()

    import os
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)

    deck = build_deck()
    genanki.Package(deck).write_to_file(args.out)
    print(
        f"Mazzo generato: {args.out} "
        f"({len(FALSOS_AMIGOS)} falsi amici + {len(GRAMMAR_POINTS)} interferenze grammaticali)"
    )


if __name__ == "__main__":
    main()
