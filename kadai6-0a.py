import requests

APP_ID = "d15e525d8c71e64fa929f1fd01a199e552060f13"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0003109761",
    "lang": "J",                  #  日本語
    "cdTime": "2024100000", #2024年度のデータを習得
    #"cdCat01": "11"　いらない？
}

#2024年度の雇用者報酬のデータを習得するプログラム。
#エンドポイントはhttps://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
#'VALUE'の'10億円', '$': '316386.1'のデータが金額(10億円)、'％', '$': '4.6'のデータが前年度比(％)

#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)