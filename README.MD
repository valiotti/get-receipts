# NalogRuPython

Python клиент для проверки чеков с помощью API nalog.ru

Для авторизации используется номер телефона с подтверждением по СМС.  

Чтобы получить интересующий вас чек, необходимо выполнить:
```python
import json

from nalog_python import NalogRuPython

client = NalogRuPython()
qr_code = "t=20200727T1117&s=4850.00&fn=9287440300634471&i=13571&fp=3730902192&n=1"
ticket = client.get_ticket(qr_code)
print(json.dumps(ticket, indent=4, ensure_ascii=False))
```

где `qr_code` текст, который закодирован в QR код чека

JSON чека:
```json
{
    "id": "5f35424ed38b52fdf004dbf3",
    "status": 2,
    "kind": "kkt",
    "createdAt": "2020-08-13T13:38:22+03:00",
    "statusDescription": {},
    "qr": "t=20200709T2008&s=7273.00&fn=9282440300688488&i=14186&fp=1460060363&n=1",
    "operation": {
        "date": "2020-07-09T20:08:00+03:00",
        "type": 1,
        "sum": 727300
    },
    "seller": {
        "name": "ООО \"Лента\"",
        "inn": "7814148471"
    },
    "process": [
        {
            "time": "2020-08-13T13:38:23+03:00",
            "result": 2
        }
    ],
    "query": {
        "operationType": 1,
        "sum": 727300,
        "documentId": 14186,
        "fsId": "9282440300688488",
        "fiscalSign": "1460060363",
        "date": "2020-07-09T20:08"
    },
    "ticket": {
        "document": {
            "receipt": {
                "dateTime": 1594314480,
                "cashTotalSum": 0,
                "ecashTotalSum": 727300,
                "fiscalDocumentNumber": 14186,
                "fiscalDriveNumber": "9282440300688488",
                "fiscalSign": 1460060363,
                "items": [
                    {
                        "name": "Пакет ЛЕНТА средний майка 12кг",
                        "price": 699,
                        "quantity": 3,
                        "sum": 2097
                    },
                    {
                        "name": "Уголь GIARDINO CLUB Premium берез.1,5кг",
                        "price": 12999,
                        "quantity": 1,
                        "sum": 12999
                    },
                    {
                        "name": "Арбуз ВЕС.",
                        "price": 3999,
                        "quantity": 7.925,
                        "sum": 31692
                    },
                    {
                        "name": "Соус DOLMIO острый 500г",
                        "price": 12989,
                        "quantity": 1,
                        "sum": 12989
                    },
                    {
                        "name": "Нап пивн SCHOFFERHOFER Grapef2,5%ж/б0.5L",
                        "price": 13999,
                        "quantity": 1,
                        "sum": 13999
                    },
                    {
                        "name": "Пиво KILKENNY DRAUGHT темн 4,3%ж/б 0.44L",
                        "price": 12999,
                        "quantity": 1,
                        "sum": 12999
                    },
                    {
                        "name": "Соус DOLMIO с ароматными травами 500г",
                        "price": 12989,
                        "quantity": 1,
                        "sum": 12989
                    },
                    {
                        "name": "Биойогурт BIOБАЛАНС Злаки 1% 270г",
                        "price": 4069,
                        "quantity": 1,
                        "sum": 4069
                    },
                    {
                        "name": "Икра ЛЕНТА кабачковая 520г",
                        "price": 5999,
                        "quantity": 1,
                        "sum": 5999
                    },
                    {
                        "name": "Вишня СВОЙ УРОЖАЙ б/к зам 600г",
                        "price": 26779,
                        "quantity": 1,
                        "sum": 26779
                    },
                    {
                        "name": "Форель СВОЯ РЫБКА фил-кус с/с в/у 200г",
                        "price": 29003,
                        "quantity": 1,
                        "sum": 29003
                    },
                    {
                        "name": "Соус PALADIN Майонезный Перечный 275г",
                        "price": 3999,
                        "quantity": 1,
                        "sum": 3999
                    },
                    {
                        "name": "Биойогурт BIOБАЛАНС Вишн-черешня 1% 270г",
                        "price": 4069,
                        "quantity": 2,
                        "sum": 8138
                    },
                    {
                        "name": "Сыр CASTELLO Matured Havarti выдер45%250",
                        "price": 29999,
                        "quantity": 1,
                        "sum": 29999
                    },
                    {
                        "name": "Паштет POLCA Нежный по-домашнему 175г",
                        "price": 14999,
                        "quantity": 1,
                        "sum": 14999
                    },
                    {
                        "name": "Фарш МИРАТОРГ мрамр говяд Блэк Ангус 400",
                        "price": 17689,
                        "quantity": 1,
                        "sum": 17689
                    },
                    {
                        "name": "Сыр VIOLA плавленый Сливочный 50% 200г",
                        "price": 14699,
                        "quantity": 1,
                        "sum": 14699
                    },
                    {
                        "name": "Филе грудки индейки ИНДИЛАЙТ ГВУ 500г",
                        "price": 18900,
                        "quantity": 1,
                        "sum": 18900
                    },
                    {
                        "name": "Вино игр MEZZA Виньети бел cух Ит 0.75L",
                        "price": 64958,
                        "quantity": 1,
                        "sum": 64958
                    },
                    {
                        "name": "Икра YAN баклажанная пикантная 470г",
                        "price": 9989,
                        "quantity": 1,
                        "sum": 9989
                    },
                    {
                        "name": "Ликер LIMONCELLO десертный 25% Ит 0.5L",
                        "price": 59999,
                        "quantity": 1,
                        "sum": 59999
                    },
                    {
                        "name": "Напиток б/а ЗАНДУКЕЛИ тархун 0.5L",
                        "price": 6989,
                        "quantity": 1,
                        "sum": 6989
                    },
                    {
                        "name": "Напит б/а НАТАХТАРИ Тархун ср/г ст 0.5L",
                        "price": 6989,
                        "quantity": 1,
                        "sum": 6989
                    },
                    {
                        "name": "Напит б/а SCHWEPPES Indian Тоник газ0.9L",
                        "price": 8579,
                        "quantity": 1,
                        "sum": 8579
                    },
                    {
                        "name": "Сок ЛЕНТА Гранатовый прям отж ст 0.31L",
                        "price": 4499,
                        "quantity": 3,
                        "sum": 13497
                    },
                    {
                        "name": "Нап раст ГРЕЕН МИЛК рис осн миндаль750мл",
                        "price": 13479,
                        "quantity": 2,
                        "sum": 26958
                    },
                    {
                        "name": "Хлопья ГЕРКУЛЕС овсяные Монастырск 500г",
                        "price": 5539,
                        "quantity": 2,
                        "sum": 11078
                    },
                    {
                        "name": "Кешью 365 ДНЕЙ жареный 200г",
                        "price": 19999,
                        "quantity": 1,
                        "sum": 19999
                    },
                    {
                        "name": "Курага ЗВЕЗДОЧКИ отборная 300г",
                        "price": 15969,
                        "quantity": 1,
                        "sum": 15969
                    },
                    {
                        "name": "Нап б/а SANPELLEGRINO Лимон газ.0.33L",
                        "price": 6989,
                        "quantity": 1,
                        "sum": 6989
                    },
                    {
                        "name": "Сосиски МЯСН ИСТОР Фермерские 310г",
                        "price": 15669,
                        "quantity": 1,
                        "sum": 15669
                    },
                    {
                        "name": "Томаты черри розовые 500 г",
                        "price": 19999,
                        "quantity": 1,
                        "sum": 19999
                    },
                    {
                        "name": "Черешня вес 1кг",
                        "price": 17999,
                        "quantity": 0.458,
                        "sum": 8244
                    },
                    {
                        "name": "Чай TWININGS Эрл Грей /ар берг 25пак 50г",
                        "price": 21399,
                        "quantity": 1,
                        "sum": 21399
                    },
                    {
                        "name": "Хлебушек домашний бездрожжевой 330г",
                        "price": 3999,
                        "quantity": 1,
                        "sum": 3999
                    },
                    {
                        "name": "Хлеб КАРАВАЙ Столовый рж-пш полов 375г",
                        "price": 3079,
                        "quantity": 1,
                        "sum": 3079
                    },
                    {
                        "name": "Вишня вес 1кг",
                        "price": 22999,
                        "quantity": 0.36,
                        "sum": 8280
                    },
                    {
                        "name": "Сдоба Сладкое трио вес",
                        "price": 27499,
                        "quantity": 0.13,
                        "sum": 3575
                    },
                    {
                        "name": "Вафли ЛЕНТА Мяг с шок. начинкой 4шт 216г",
                        "price": 6999,
                        "quantity": 1,
                        "sum": 6999
                    },
                    {
                        "name": "Продукт овсян VELLE ферм черносл 180г",
                        "price": 5999,
                        "quantity": 2,
                        "sum": 11998
                    },
                    {
                        "name": "Хлеб АРНАУТ Чемпион-Лидер нарез 350г",
                        "price": 6629,
                        "quantity": 1,
                        "sum": 6629
                    },
                    {
                        "name": "Пирожное ORION Choco Pie Cherry 360г",
                        "price": 11799,
                        "quantity": 1,
                        "sum": 11799
                    },
                    {
                        "name": "Огурцы короткоплодные колючие 450г",
                        "price": 4999,
                        "quantity": 1,
                        "sum": 4999
                    },
                    {
                        "name": "Круассан миндальный 120г",
                        "price": 4999,
                        "quantity": 1,
                        "sum": 4999
                    },
                    {
                        "name": "Бананы вес 1кг",
                        "price": 5399,
                        "quantity": 0.69,
                        "sum": 3725
                    },
                    {
                        "name": "Томат розовый Томимаро Мучо 700г",
                        "price": 17999,
                        "quantity": 1,
                        "sum": 17999
                    },
                    {
                        "name": "Печенье ПЕТРОХЛЕБ Овсяное 400г",
                        "price": 4509,
                        "quantity": 1,
                        "sum": 4509
                    },
                    {
                        "name": "Нектарины вес 1кг",
                        "price": 12899,
                        "quantity": 1.032,
                        "sum": 13312
                    },
                    {
                        "name": "Галеты BONDUELLE Сицилийские овощные300г",
                        "price": 23059,
                        "quantity": 1,
                        "sum": 23059
                    },
                    {
                        "name": "Яйцо курин РОСКАР стол Экстра С0 10шт",
                        "price": 6999,
                        "quantity": 1,
                        "sum": 6999
                    }
                ],
                "kktRegId": "0000092968041899    ",
                "nds10": 27094,
                "nds18": 71548,
                "operationType": 1,
                "operator": "Яблокова Надежда Николаевна",
                "receiptCode": 3,
                "requestNumber": 258,
                "retailPlaceAddress": "Россия, 188643,Ленинградская обл., Всеволожский м.р-н, г. Всеволожск, ш Дорога Жизни, д. 6,",
                "shiftNumber": 50,
                "taxationType": 1,
                "totalSum": 727300,
                "user": "ООО \"Лента\"",
                "userInn": "7814148471"
            }
        }
    },
    "organization": {
        "name": "ООО \"Лента\"",
        "inn": "7814148471"
    }
}
```
