from random import randrange, seed

def generate_tone_list():
    tones = list(
        map(chr, range(ord('A'), ord('S')))
    )

    tones.remove('I')
    tones.remove('O')

    return tones


def generate_tone():
    tones = generate_tone_list()

    f1 = tones[randrange(0, len(tones))]
    tones.remove(f1)
    f2 = tones[randrange(0, len(tones))]

    return tuple(sorted([f1, f2]))


def generate_tone_pair():
    tone1 = tone2 = generate_tone()

    while tone1 == tone2:
        tone2 = generate_tone()

    return (tone1, tone2)


def generate_selcal():
    tones = generate_tone_pair()

    return '-'.join(map(''.join, tones))


seed()
print(generate_selcal())
