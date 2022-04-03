import requests
import fastapi
from fastapi import Form
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.post("/templates/rick", tags=["templates", "rick"])
@template(template_file='rick.pt')
async def read_data_form_rick(id: str = Form(...)):

    r = requests.get(f'https://rickandmortyapi.com/api/character/?name={id}')
    print(dir(r))
    hero = r.json()
    h = hero['results']
    print(f"Name: {h[0]['name']}")
    print(f"Status: {h[0]['status']}")
    print(f"Species: {h[0]['species']}")
    print(f"Image: {h[0]['image']}")
    postac = requests.get(h[0]['url'])
    dane_postaci = postac.json()
    for element in dane_postaci:
        print(element)

    return {
        "name": h[0]['name'],
        "status": h[0]['status'],
        "species": h[0]['species'],
        "image": h[0]['image'],
    }
    
    # print(type(dane_json))
    # for element in dane_json:
    #     print(element)

    # dane = dane_json["results"]

    # print(dane[0].keys())
    # for hero in dane:
        # print(f"Nazwa: {hero['name']}")
        # print(f"loc: {hero['location']}")
        # print(f"url: {hero['url']}")
        # postac = requests.get(hero['url'])
        # dane_postaci = postac.json()
        # for element in dane_postaci:
        #     print(element)

        