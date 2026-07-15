from chars import *
import random
import time
import sys

def creation():
    name = input("Adın ne kahraman?: ")
    if not isinstance(name, str) or not name.strip():
        print("Geçerli bir isim girilmedi, default isim: Yabancı")
        name = "Yabancı"
    
    time.sleep(1)
    print("\n"+ "Class Listesi, birini seç:"+ "\n" + "1)Knight"+ "\n" "2)Dwarf" + "\n" + "3)Elf" + "\n" "4)Dark Elf")
    secim = str(input("Seçimin: "))
    if secim.lower() == "1" or secim.lower() == "knight":
        print("Knight")
        player = Knight(name)
    elif secim.lower() == "2" or secim.lower() == "dwarf":
        print("Dwarf")
        player = Dwarf(name)
    elif secim.lower() == "3" or secim.lower() == "elf":
        print("Elf")
        player = Elf(name)
    elif secim.lower() == "4" or secim.lower() == "dark elf":
        print("Dark Elf")
        player = DarkElf(name)
    else:
        print("Geçersiz seçim, otomatik olarak Knight sınıfı atandı")
        player = Knight(name)
    return player

def battle(player,enemy):
    player.special_used = False
    enemy.special_used = False
    print("Savaş başlıyor")
    while player.base_hp > 0 and enemy.base_hp > 0:
        
        time.sleep(1)
        print("Oyuncu Turu:")
        print(f"Statlar: HP:{player.base_hp}, ATK:{player.base_attack}, MANA:{player.base_mana}")
        print("Seçenekler: 1)Normal Saldırı, 2)Özel Saldırı")
        time.sleep(1)
        choice = input("Seçimin?")
        if choice == "1":
            enemy.base_hp -= player.base_attack
            print(f"Normal saldırı kullanıldı,{player.base_attack} kadar hasar verildi")
            time.sleep(2)
            print(f"Düşman sağlığı: {enemy.base_hp}")
        elif choice == "2":
            if isinstance(player,Dwarf):
                player.special_skill()
            else:
                player.special_skill(enemy)
        else:
            print("Geçersiz girdi, normal saldırı yapılıyor")
            enemy.base_hp -= player.base_attack
        if enemy.base_hp <= 0:
            print(f"{player.isim} kazandı!")
            break
        
        time.sleep(2)
        
        print("Düşman Turu:")
        time.sleep(1)
        if enemy.base_mana >= 75 and random.random()< enemy.skill_chance:
            print("Düşman özel yeteneğini kullandı!")
            time.sleep(1)
            enemy.special_skill(player)
        else:
            print("Düşman normal saldırısını kullandı!")
            player.base_hp -= enemy.base_attack
            time.sleep(2)
            print(f"Düşman {enemy.base_attack} kadar hasar verdi")
        
        if player.base_hp <= 0:
            print("Düşman kazandı")
            break
        player.passive_skill()
        enemy.passive_skill()
            
    
def start_game():
    player = creation()
    time.sleep(1)
    print("Uzun zaman önce Avalon adlı bir krallıkta bir maceracı yaşardı, söylentiye göre bu maceracı iblis kral ile olan savaşında mağlup olmuş ve bir zindana hapsedilmiş: Termina Zindanına")
    time.sleep(2)
    print("Yüce Maceracı, senin gibi onlarca insan bu zindana keşfe çıktı, lakin biri bile geri dönmedi")
    time.sleep(2)
    print("Bakalım senin kaderin ne olacak? Termina zindanından sağ çıkıp kadim maceracının yüzüğünü ona getirirsen sana prensesin sözünü verdi.")
    time.sleep(2)
    print("Sakın korkma, ve sakın rehavete kapılma. Bu zindanda en güçlü diye birşey yoktur, her balıktan daha büyüğü elbette vardır...")
    time.sleep(2)
    print("Zindanın kapısından girdin ve karşına kapıcı niteliğinde bir iblis çıktı. Çok güçlü değil, senin için çocuk oyuncağı olmalı")
    first_enemy = Demon("Kapıcı iblis")
    battle(player,first_enemy)
    if player.base_hp <= 0:
        time.sleep(1)
        print("Karanlık seni yuttu. Buraya kadarmış")
        sys.exit()
    time.sleep(1)
    print("İblisi yendin, biraz ilerleyince ileride bir yol ayrımı buldun? Hem sağında hem de solunda bir kapı duruyor. Karar senin...")
    secim1 = input("Seçimin?: ")
    
    if secim1.lower() == "sağ":
        print("Sağ kapıdan girdin, ve 100 metre ilerledikten sonra dibi karanlık bir delik gördün. Atlayacak mısın?")
        secim2 = input("Atla/Atlama: ")
        if secim2.lower() == "atla":
            time.sleep(1)
            print("Dibi görünmeyen deliklere atlamak pek mantıklı bir fikir değildi. Öldün, bir maceracı için saçma bir ölüm olsa gerek, buraya kadarmış... ")
            sys.exit()
        elif secim2.lower() == "atlama":
            time.sleep(1)
            print("Doğru seçim, kapıların olduğu koridora geri dönüyorsun... ")
            secim1 = "sol"
        else:
            time.sleep(1)
            print("Kararsız kaldın ve işini şansa bırakmamaya karar verdin. Kapıların olduğu koridora geri dönüyorsun")
            secim1 = "sol"
    if secim1.lower() == "sol":
        print("Karşına ikinci bir iblis çıktı, savaş vakti")
        time.sleep(1)
        second_enemy = Demon("İblis")
        battle(player,second_enemy)
        if player.base_hp <= 0:
            time.sleep(1)
            print("Karanlık seni yuttu. Buraya kadarmış")
            sys.exit()
        time.sleep(1)
        print("Yoluna devam ettin ve bir kamp ateşi keşfettin, şimdilik dinlensen iyi olacak")
        time.sleep(1)
        print("Dinleniyorsun...")
        player.base_hp = min(player.max_hp, player.base_hp + 50)
        time.sleep(2)
        print(f"Dinlenme tamamlandı, 50 hp yeniledin. Güncel durum: {player}")
        time.sleep(3)
        print("\nYola devam etme vakti")
    else:
        time.sleep(1)
        print("Seçim yapmamayı tercih ettin, ve en sonunda iblisler seni uykunda öldürdü. Buraya kadarmış...")
        sys.exit()
        
    print("Fakat o da ne? Arkanda bir tüccar belirdi, ve sana şunları söylüyor:")
    time.sleep(2)
    print("Bu noktadan sonra iblisler altın düşürebilir, bu altınlarla benden eşyalar satın alabilirsin...")
    time.sleep(3)
    print("Kafa salladın, ve tam yola devam edecekken aklına bir fikir geldi: Bu tüccarı neden öldürmeyeyim ki? Eşyaların hepsi benim olur para da harcamam.")
    time.sleep(2)
    print("İç sesini dinleyecek misin?")
    time.sleep(2)
    secim3 = input("Evet/Hayır")
    if secim3.lower() == "evet":
        time.sleep(2)
        print("Masumlara saldıranlardan kahraman olmaz. Zindan kapalı da olsa kafana yıldırım düştü ve öldün, buraya kadarmış...")
        sys.exit()
    print("Kafandaki bu saçma düşünceyi başından savdın ve devam ettin.")
    time.sleep(2)
    print("Yolda devam ederken bir iblis karşına çıktı, savaş vakti")
    third_enemy = Demon("İblis")
    battle(player,third_enemy)
    if player.base_hp <= 0:
            time.sleep(1)
            print("Karanlık seni yuttu. Buraya kadarmış")
            sys.exit()
    time.sleep(1)
    player.gold += random.randint(10, 30)
    print(f" İblis bir avuç altın düşürdü, güncel altın miktarın: {player.gold}")
    time.sleep(2)
    print("Yola devam ediyorsun...")
    time.sleep(3)
    print("Türlü tünellerden geçip saatlerce bataklıkları ve yokuşları aştıktan sonra bir sonraki kamp ateşine varıyorsun, fakat önünde seni bir iblis bekliyor")
    time.sleep(1)
    stitch = Demon("Stitch")
    battle(player,stitch)
    if player.base_hp <= 0:
            time.sleep(1)
            print("Karanlık seni yuttu. Buraya kadarmış")
            sys.exit()
    print("İblise tam son vuruşu yapmadan önce konuşmaya başlıyor ve senden af diliyor.")
    time.sleep(2)
    print("Anlattığına göre adı Stitch imiş ve sana cebindeki tüm altınları fırlatıyor")
    player.gold += 50
    time.sleep(1)
    print(f"Güncel altın miktarı: {player.gold}")
    time.sleep(2)
    print("Onu bağışlayacak mısın?")
    secim4 = input("Evet/Hayır")
    time.sleep(1)
    if secim4.lower() == "hayır":
        print("Onu öldürdün, sonra da bir süre kamp ateşinde dinlendin. Sonra bir kapı gördün, lakin bir kilit ile kilitlenmiş. Kapı açılmadı ve başka bir yola saptın.")
        time.sleep(3)
        print("Labirent yollarında kayboldun ve açlıktan öldün. BUraya kadarmış...")
        sys.exit()
    elif secim4.lower() == "evet":
        print("İçinden bir ses bunun doğru karar olduğunu söylüyor. Stitch sana bir anahtar verdi ve teşekkür ederek ayrıldı.")
    else:
        print("Emin olamadın, stitch de ikna olman için sana bir anahtar verdi ve kaçtı.")
    time.sleep(2)
    print("Kamp ateşinde dinlendin")
    time.sleep(1)
    print("Dinleniyorsun...")
    player.base_hp = min(player.max_hp, player.base_hp + 50)
    time.sleep(2)
    print(f"Dinlenme tamamlandı, 50 hp yeniledin. Güncel durum: {player}")
    time.sleep(3)
    print("\nYola devam etme vakti")
    time.sleep(2)
    print("Tüccarı gördün. 50 altına sana güzel bir kılıç satabilir.")
    time.sleep(1)
    secim5 = input("Satın alıyor musun?(Evet/Hayır)")
    if secim5.lower() == "evet" and player.gold >= 50:
        time.sleep(1)
        print("Kılıcı satın aldın")
        player.gold -= 50
        time.sleep(1)
        print("Güçlendiğini hissediyorsun...")
        player.base_attack += 35
        time.sleep(1)
        print(f"Yeni saldırı gücü: {player.base_attack}")
    elif secim5.lower() == "evet":
        print("Maalesef paran yetmedi")
    elif secim5.lower() == "hayır":
        print("Kabul etmedin ve yola devam ettin.")
    else:
        print("Emin olamadın ve satın almamaya karar verdin.")
    
    time.sleep(2)
    print("Yola devam ettin ve kapıyı gördün. Stitchin anahtarını soktun ve kapıdan içeri girince gözlerine inanamadın. Bu o yüzük")
    time.sleep(2)
    print("Lakin tam yüzüğü alacakken seni arkadan dev bir iblis yakaladı ve duvara fırlattı")
    time.sleep(1)
    print("Görünüşüne göre bu zindanın en güçlüsü, ve yüzüğün koruyucusu. Etraftaki kemikler, insanların neden evine dönmediklerini açıklar nitelikte.")
    time.sleep(2)
    print("Fakat düşünecek vakit yok, savaş başlasın, son bir kez.")
    time.sleep(1)
    boss = Boss("Dev iblis")
    battle(player,boss)
    if player.base_hp <= 0:
            time.sleep(1)
            print("Karanlık seni yuttu. Buraya kadarmış...")
            sys.exit()
    time.sleep(2)
    print("Savaş bitti, yüzük artık senindir. Yüzüğü aldın ve krallığına döndün")
    time.sleep(2)
    print("Yüzüğü krala takdim ettin, karşılığında prenses ile evlendin ve ülkede kahraman da ilan edildikten sonra huzur dolu bir hayat yaşadın.")
    time.sleep(2)
    print("Oynadığın için teşekkürler <3...")
    sys.exit()
        
        