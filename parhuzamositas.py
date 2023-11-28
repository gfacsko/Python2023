#
# Párhuzamos programozás Pythonban példaprogramok
# Developed by Gabor FACSKO (facsko.gabor@uni-milton.hu)
# Milton Friedman University, Budapest, 2023
# -----------------------------------------------------------------
#
# http://faragocsaba.hu/parhuzamositas

'''
# Generátorok

def generator(n):
    print(f'generátor {n} eleje')
    yield 10 * n + 1
    print(f'generátor {n} közepe')
    yield 10 * n + 2
    print(f'generátor {n} vége')
    yield 10 * n + 3

generatorok = [generator(1), generator(2), generator(3)]
while True:
    vege = 0
    for generator in generatorok:
        try:
            reszeredmény = next(generator)
            print(reszeredmény)
        except StopIteration:
            vege += 1
    if vege == len(generatorok):
        break
'''

'''
# Coroutine létrehozása
import time

def lassu_fuggveny(n):
    print(f'Lassú függvény {n} eleje')
    time.sleep(1)
    print(f'Lassú függvény {n} vége')


for i in range(3):
    lassu_fuggveny(i)
    time.sleep(0.1)
'''

'''
import asyncio

async def lassu_fuggveny(n):
    print(f'Lassú függvény {n} eleje')
    await asyncio.sleep(1)
    print(f'Lassú függvény {n} vége')


async def main():
    feladatok = []
    for i in range(3):
        feladatok.append(asyncio.create_task(lassu_fuggveny(i)))
    for feladat in feladatok:
        await feladat


asyncio.run(main())
'''


'''
# Visszatérési érték

import asyncio


async def lassu_osszead(n, a, b):
    print(f'lassú összead {n} eleje')
    await asyncio.sleep(1)
    print(f'lassú összead {n} vége')
    return a + b


async def main():
    osszeadasok = [
        (3, 2),
        (1, 5),
        (2, 6),
    ]
    feladatok = []
    for i, osszeadas in enumerate(osszeadasok):
        feladatok.append(lassu_osszead(i, *osszeadas))

        # feladatok.append(asyncio.create_task(lassú_összead(i, *összeadás)))
    # eredmények = []
    # for feladat in feladatok:
    #    eredmények.append(await feladat)
    eredmenyek = await asyncio.gather(*feladatok)
    print(eredmenyek)

asyncio.run(main())
'''

'''
# Fájlok generálása

import random

random.seed(12345)
for i in range(5):
    fajlnev = f'szamok{i}.txt'
    print(fajlnev)
    with open(fajlnev, 'w') as fajl:
        for _ in range(10_000_000):
            print(random.randint(1, 100), file=fajl)

'''

'''
# Aszinkron fájlbeolvasás

import asyncio
import aiofiles


async def aszinkron_fajlolvasas(faljnev):
    print(f'Aszinkron fájlolvasás eleje: {faljnev}')
    async with aiofiles.open(faljnev) as f:
        tartalom = await f.read()
    print(f'Aszinkron fájlolvasás vége: {faljnev}')
    osszeg = ([int(sor) for sor in tartalom.split()])
    print(f'Összeg kiszámolva: {faljnev}')
    return sum(osszeg)


async def main():
    feladatok = []
    for i in range(5):
        feladatok.append(asyncio.create_task(aszinkron_fajlolvasas(f'szamok{i}.txt')))
    eredmeny = await asyncio.gather(*feladatok)
    print(eredmeny)


asyncio.run(main())
'''

# Aszinkron netes letöltés

import asyncio
import aiohttp

# Weboldalakat tölt le
async def weboldal_meret(url):
    print(f'Letolt: {url}')
    # Letölti a weboldalt
    async with aiohttp.ClientSession() as session:
        # Kiszámítja a méretét
        async with session.get(url) as valasz:
            tartalom = await valasz.text()
            print(f'{url} letöltése kész')
            return len(tartalom)


async def main():
    weboldalak = [
        'http://faragocsaba.hu/python',
        'https://www.python.org/',
        'https://www.w3schools.com/python/',
        'https://www.tutorialspoint.com/python/',
        'https://www.pythontutorial.net/',
    ]
    # A weboldalakat letöltő és méretét kiszámító aszinkron taszkokat indít el
    feladatok = []
    for weboldal in weboldalak:
        feladatok.append(asyncio.create_task(weboldal_meret(weboldal)))
    # Begyűjti az eredményeket
    eredmenyek = []
    for feladat in feladatok:
        eredmenyek.append(await feladat)
    # Kiírja az eredményeket
    print(eredmenyek)

# Lehetővé teszi a webws kommunikációt
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# Elindítja az aszinkron taszkokat
asyncio.run(main())