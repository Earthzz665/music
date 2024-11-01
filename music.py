import pygame
import random
import time
import webbrowser  # ใช้เพื่อเปิดเว็บไซต์

pygame.mixer.init()

sounds = {
    "1": "piano.wav",
    "2": "guitar.mp3",
    "3": "rain.wav",
    "4": "opera.wav",
    "5": "wave.wav",
    "6": "bird.wav",
    "7": "checkwater.wav",
    "8": "sharpmelody.wav",
    "9": "fire.wav",
    "10": "river.mp3",
    "11": "mind.mp3",
    "12": "sound nature.mp3",
    "13": "sleep.mp3",
    "14": "space.mp3",
    "15": "bamboo.mp3",
    "16": "alien.mp3",
    "17": "amgry tiger.mp3",
    "18": "baby deer.mp3",
    "19": "beat.mp3",
    "20": "bee.mp3",
    "21": "campfire.mp3",
    "22": "crow.mp3",
    "23": "cry.mp3",
    "24": "frag.mp3",
    "25": "frogs.mp3",
    "26": "green.mp3",
    "27": "hiphop.mp3",
    "28": "leaf.mp3",
    "29": "luxury.mp3",
    "30": "meows.mp3",
    "31": "monster.mp3",
    "32": "ood.mp3",
    "33": "pokpok.mp3",
    "34": "parrots.mp3",
    "35": "tractor.mp3",
    "36": "rockdump.mp3",
    "37": "space.mp3",
   "38": "ghost.mp3",
    "39": "ghost scary.mp3",
  "40": "scary.mp3",
   
    

}

favorites = []
url = "https://www.suandoksoundtherapy.com/"  # URL ที่จะเปิด

def display_menu():
    print("เลือกประเภทเสียงที่คุณต้องการบำบัด:")
    print("0: เล่นเสียงสุ่ม")
    for key, value in sounds.items():
        print(f"{key}: {value.split('.')[0]}")
    print("f: ดูเสียงโปรด")
    print("p: หยุดชั่วคราว / เล่นต่อ")
    print("s: หยุดเสียง")
    print("w: เปิดเว็บไซต์ดนตรีบำบัด")
    print("q: ออกจากโปรแกรม")

def add_to_favorites(choice):
    if choice not in favorites:
        favorites.append(choice)
        print(f"เพิ่ม {sounds[choice].split('.')[0]} ลงในเสียงโปรดเรียบร้อย")

def open_website():
    print("กำลังเปิดเว็บไซต์ดนตรีบำบัดจิใจ")
    webbrowser.open(url)

while True:
    display_menu()
    choice = input("กรุณาเลือกตัวเลข (1-40), 'f' เพื่อดูเสียงโปรด, 'w' เพื่อเปิดเว็บไซต์, หรือ 'q' เพื่อออก: ")

    if choice == "q":
        print("ขอบคุณที่ใช้โปรแกรม!")
        break
    elif choice == "0":
        choice = random.choice(list(sounds.keys()))
    elif choice == "f":
        if favorites:
            print("เสียงโปรดของคุณ:")
            for f in favorites:
                print(f"{f}: {sounds[f].split('.')[0]}")
        else:
            print("ยังไม่มีเสียงโปรดในรายการ")
        continue
    elif choice == "w":
        open_website()
        continue
    elif choice == "p":
        if pygame.mixer.music.get_busy():
            if pygame.mixer.music.get_pos() > 0:
                pygame.mixer.music.pause()
                print("หยุดชั่วคราว...")
            else:
                pygame.mixer.music.unpause()
                print("เล่นต่อ...")
        else:
            print("ไม่มีเสียงกำลังเล่นอยู่")
        continue
    elif choice == "s":
        pygame.mixer.music.stop()
        print("หยุดเสียง")
        continue

    if choice in sounds:
        pygame.mixer.music.load(sounds[choice])
        pygame.mixer.music.play(-1)
        print(f"กำลังเล่นเสียง {sounds[choice].split('.')[0]} ... กด 's' เพื่อหยุดหรือ 'p' เพื่อหยุดชั่วคราว")
        fav = input("คุณต้องการเพิ่มเสียงนี้ในเสียงโปรดหรือไม่? (y/n): ")
        if fav.lower() == 'y':
            add_to_favorites(choice)
    else:
        print("คุณเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")
