import json
import os
from datetime import datetime
import pytz

DATA_FILE = os.getenv("DATA_FILE", "dati.json")
# Il primo utente che esegue /start diventa proprietario del bot.
# Nessun ID Telegram deve essere configurato nel codice.
OWNER_FILE = os.getenv("OWNER_FILE", "owner.json")


def get_owner_id():
    try:
        with open(OWNER_FILE, "r", encoding="utf-8") as f:
            return int(json.load(f)["owner_id"])
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
        return None


def claim_owner(user_id):
    owner = get_owner_id()
    if owner is not None:
        return owner == user_id
    try:
        with open(OWNER_FILE, "x", encoding="utf-8") as f:
            json.dump({"owner_id": user_id}, f)
        return True
    except FileExistsError:
        return get_owner_id() == user_id


def is_owner(user_id):
    return get_owner_id() == user_id

TZ = pytz.timezone("Europe/Rome")


def now_it():
    return datetime.now(TZ)


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_user_key():
    return "owner"


def ensure_user(data):
    user = get_user_key()
    if user not in data:
        data[user] = {
            "records": [],
            "work_start": None
        }
    return user


def get_user_data():
    data = load_data()
    user = ensure_user(data)
    return data, user


def add_record(record):
    data, user = get_user_data()
    data[user]["records"].append(record)
    save_data(data)


def set_work_start(value):
    data, user = get_user_data()
    data[user]["work_start"] = value
    save_data(data)


def get_work_start():
    data = load_data()
    user = get_user_key()
    return data.get(user, {}).get("work_start")


def reset_month():
    data = load_data()
    user = ensure_user(data)
    data[user] = {
        "records": [],
        "work_start": None
    }
    save_data(data)


def get_records():
    data = load_data()
    user = get_user_key()
    return data.get(user, {}).get("records", [])


def today_records():
    today = now_it().strftime("%Y-%m-%d")
    return [r for r in get_records() if r.get("data") == today]


def current_session_seconds():
    work_start = get_work_start()
    if not work_start:
        return 0

    try:
        naive_dt = datetime.strptime(work_start, "%Y-%m-%d %H:%M:%S")
        start_dt = TZ.localize(naive_dt)
        diff = now_it() - start_dt
        return max(0, int(diff.total_seconds()))
    except Exception:
        return 0
