# Meme Generator (Flask + Docker)

To je spletna aplikacija Meme Generator, izdelana v Pythonu z uporabo ogrodja Flask in knjižnice Pillow. Aplikacija omogoča nalaganje slike, vnos zgornjega in spodnjega besedila ter generiranje nove slike – mema.

## Uporabljene tehnologije
- Python
- Flask
- Pillow (PIL)
- Docker

## Funkcionalnosti
- Nalaganje slike prek spletnega obrazca
- Vnos zgornjega in spodnjega besedila
- Generiranje nove slike z napisom
- Prikaz generiranega mema v brskalniku

## Zagon aplikacije z Dockerjem

Najprej zgradimo Docker sliko:

```bash
docker build -t meme-generator .

