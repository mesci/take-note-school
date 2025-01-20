import os

USER_CREDENTIALS = {"admin": "sifre123"}

NOTES_FILE = "notes.txt"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, "r") as file:
        lines = file.readlines()
    notes = {}
    for line in lines:
        note_id, title, content = line.strip().split("|", 2)
        notes[int(note_id)] = {"title": title, "content": content}
    return notes

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        for note_id, note in notes.items():
            file.write(f"{note_id}|{note['title']}|{note['content']}\n")

def login():
    print("Not Alma Uygulamasına Hoş Geldiniz!")
    username = input("Kullanıcı Adı: ")
    password = input("Şifre: ")

    if USER_CREDENTIALS.get(username) == password:
        print("Giriş başarılı!\n")
        return True
    else:
        print("Hatalı kullanıcı adı veya şifre.\n")
        return False

def add_note():
    title = input("Not Başlığı: ")
    content = input("Not İçeriği: ")
    note_id = max(data.keys(), default=0) + 1
    data[note_id] = {"title": title, "content": content}
    save_notes(data)
    print(f"\nNot başarıyla eklendi! (ID: {note_id})\n")

def edit_note():
    note_id = int(input("Düzenlemek istediğiniz notun ID'sini girin: "))
    if note_id in data:
        print(f"Mevcut Başlık: {data[note_id]['title']}")
        new_title = input("Yeni Başlık (boş bırakırsanız değişmez): ")
        print(f"Mevcut İçerik: {data[note_id]['content']}")
        new_content = input("Yeni İçerik (boş bırakırsanız değişmez): ")

        if new_title:
            data[note_id]['title'] = new_title
        if new_content:
            data[note_id]['content'] = new_content

        save_notes(data)
        print("\nNot başarıyla güncellendi!\n")
    else:
        print("Geçersiz not ID'si.\n")

def delete_note():
    note_id = int(input("Silmek istediğiniz notun ID'sini girin: "))
    if note_id in data:
        del data[note_id]
        save_notes(data)
        print("\nNot başarıyla silindi!\n")
    else:
        print("Geçersiz not ID'si.\n")


def list_notes():
    if not data:
        print("\nHiç not bulunmuyor.\n")
    else:
        print("\nTüm Notlar")
        for note_id, note in data.items():
            print(f"ID: {note_id}\nBaşlık: {note['title']}\nİçerik: {note['content']}\n")

def main_menu():
    while True:
        print("1. Yeni Not Ekle")
        print("2. Not Düzenle")
        print("3. Not Sil")
        print("4. Tüm Notları Listele")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            list_notes()
        elif choice == "5":
            print("Çıkış yapılıyor...\n")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.\n")

if __name__ == "__main__":
    data = load_notes()
    if login():
        main_menu()
    else:
        print("Uygulama kapatılıyor.")
