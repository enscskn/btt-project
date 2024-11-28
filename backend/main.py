import datetime

bus_datas = {
    "bus1": {
        "routes": "Bandırma Merkez Otobüs Durağı - Otogar",
        "times": ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00"]
    },
    "bus2": {
        "routes": "Bandırma Merkez Otobüs Durağı - Adliye",
        "times": ["08:30", "09:30", "10:30", "11:30", "12:30", "13:30", "14:30"]
    },
    "bus3": {
        "routes": "Bandırma Merkez Otobüs Durağı - Tokiler",
        "times": ["08:45", "09:45", "10:45", "11:45", "12:45", "13:45", "14:45"]
    },
    "bus4": {
        "routes": "Bandırma Merkez Otobüs Durağı - Akyıldız",
        "times": ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00"]
    },
    "bus5": {
        "routes": "Bandırma Merkez Otobüs Durağı - Levent",
        "times": ["09:30", "10:30", "11:30", "12:30", "13:30", "14:30", "15:30"]
    },
    "bus6": {
        "routes": "Bandırma Merkez Otobüs Durağı - Yeni Mahalle",
        "times": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00"]
    },
    "bus7": {
        "routes": "Bandırma Merkez Otobüs Durağı - Paşabayır",
        "times": ["10:30", "11:30", "12:30", "13:30", "14:30", "15:30", "16:30"]
    },
    "bus8": {
        "routes": "Bandırma Merkez Otobüs Durağı - 600 Evler",
        "times": ["11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    },
    "bus9": {
        "routes": "Bandırma Merkez Otobüs Durağı - Livatya",
        "times": ["11:30", "12:30", "13:30", "14:30", "15:30", "16:30", "17:30"]
    },
    "bus10": {
        "routes": "Bandırma Merkez Otobüs Durağı - Hastane",
        "times": ["12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
    },
}

def list_buses():
    print("\n --- Otobüs Hatları ---")
    for buses, data in bus_datas.items():
        print(f"{buses}: {data['routes']}")

def show_bus_times(bus):
    if bus in bus_datas:
        print(f"\n{bus} Hattı Saatleri:")
        for time in bus_datas[bus]["times"]:
            print(time)
    else:
        print("Böyle bir otobüs hattı bulunmamaktadır.")

def show_bus_routes(bus):
    if bus in bus_datas:
        print(f"\n{bus} Otobüs Güzergahları: ")
        print(bus_datas[bus]["routes"])

def until_bus_start_time(bus):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    if bus in bus_datas:
        if current_time in bus_datas[bus]["times"]:
            return "Otobüs kalkış saati geldi."
        else:
            bus_times = bus_datas[bus]["times"]
            for time in bus_times:
                if time > current_time:
                    bus_time = time
                    break
            bus_time = datetime.datetime.strptime(bus_time, "%H:%M")
            current_time = datetime.datetime.strptime(current_time, "%H:%M")
            time_difference = bus_time - current_time
            return f"Kalkış saatine {time_difference} saat kaldı."
    else:
        return "Böyle bir otobüs hattı bulunmamaktadır."


def main():
    while True:
        print("\n--- Bandırma Otobüs Hatları ve Saatleri ---")
        print("\n1. Otobüs Hatlarını Listele")
        print("\n2. Otobüs Saatlerini Göster")
        print("\n3. Otobüs Güzergah Bilgilerini Göster")
        print("\n4. Otobüs Kalkış Saatine Kalan Süreyi Göster")
        print("\n5. Çıkış")
        secim = input("Seçiminiz (1-5): ")

        if secim == "1":
            list_buses()
            wait = input("Devam etmek için bir tuşa basınız...")
        elif secim=="2":
            bus_no = input("Saatini görmek istediğiniz otobüs numarısını giriniz: ")
            show_bus_times(bus_no)
            wait = input("Devam etmek için bir tuşa basınız...")
        elif secim == "3":
            bus_no = input("Güzergahını görmek istediğiniz otobüs numarasını giriniz: ")
            show_bus_routes(bus_no)
            wait = input("Devam etmek için bir tuşa basınız...")
        elif secim == "4":
            bus_no = input("Kalan süreyi görmek istediğiniz otobüs numarasını giriniz: ")
            print(until_bus_start_time(bus_no))
            wait = input("Devam etmek için bir tuşa basınız...")
        elif secim == "5":
            print("Hoşçakalın! ")
            break
        else:
            print("Tekrar seçim yapınız!")
            wait = input("Devam etmek için bir tuşa basınız...")

main()