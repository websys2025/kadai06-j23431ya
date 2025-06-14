import requests

id = 1000
API_URL = "https://pokeapi.co/api/v2/pokemon/"+str(id)

R = requests.get(API_URL)
data = R.json()
print("名前: " + data["name"])

#ポケモンの図鑑番号からポケモンの名前を習得するプログラム。
#エンドポイントはhttps://pokeapi.co/api/v2/pokemon/()。()に図鑑番号をいれる
#今回はサーフゴー