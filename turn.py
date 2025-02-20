import json 
import re


with open('row.txt', "r", encoding="utf-8") as file:
    txt = file.read()

data = {
    "branch": re.search(r"Филиал ТОО(.+)", txt).group(1).strip(),
    "bin": re.search(r"БИН (\d+)", txt).group(1),
    "nds_series": re.search(r"НДС Серия (\d+)", txt).group(1),
    "kassa_number": re.search(r"Касса (\d+-\d+)", txt).group(1),
    "smena": re.search(r"Смена (\d+)", txt).group(1),
    "sequence_number": re.search(r"Порядковый номер чека №(\d+)", txt).group(1),
    "check_number": re.search(r"Чек №(\d+)", txt).group(1),
    "cashier": re.search(r"Кассир (.+)", txt).group(1).strip(),
}

items = []
for idx, match in enumerate(re.findall(r"\d+\.\s+(.+?)\s+([\d,]+)\s+x\s+([\d,]+)\s+([\d,]+)", txt), start=1):
    items.append({
        "id": idx,
        "name": match[0],
        "price": match[1],
        "quantity": match[2],
        "sum": match[3] 
    })
data["items"] = items

data["nds_percentage"] = "12%"
data["nds_total"] = re.search(r"в т.ч. НДС 12%:\s*([\d,]+)", txt).group(1)
data["fiscal_sign"] = re.search(r"Фискальный признак:\s*(\d+)", txt).group(1)
data["place"] = re.search(r"г. Нур-султан,.+", txt).group(0)
data["time"] = re.search(r"Время:\s*([\d:. ]+)", txt).group(1)
data["operator"] = re.search(r"Оператор фискальных данных:\s*([^Ф]+)", txt).group(1).strip()
data["verification_site"] = re.search(r"Для проверки чека зайдите на сайт:([^\n]+)", txt).group(1).strip()
data["fiscal_receipt"] = "ФИСКАЛЬНЫЙ ЧЕК"
data["fp"] = "ФП"
data["ink_ofd"] = re.search(r"ИНК ОФД:\s*(\d+)", txt).group(1)
data["kkm_code"] = re.search(r"Код ККМ КГД \(РНМ\):\s*(\d+)", txt).group(1)
data["znm"] = re.search(r"ЗНМ:\s*(\w+)", txt).group(1)
data["webkassa"] = "WEBKASSA.KZ"

json_file = "row.json"
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent = 4)