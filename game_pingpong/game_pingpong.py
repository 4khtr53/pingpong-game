#step 1: import modules
from pygame import * #game 2d

font.init() #bikin font

init() #install package yang penting2 (ex: core2 pygame)

#step 2: taruh variable penampung nama image
img_back = r"C:\Users\Ben Isa\Desktop\Algorithmic\game_pingpong\meja_pingpong.png"
img_kanan = r"C:\Users\Ben Isa\Desktop\Algorithmic\game_pingpong\bet#1.png"
img_kiri = r"C:\Users\Ben Isa\Desktop\Algorithmic\game_pingpong\bet#2.png"
img_bola = r"C:\Users\Ben Isa\Desktop\Algorithmic\game_pingpong\bola.png"


#step 3: buat screen
width = 887
height = 500

screen = display.set_mode((width, height))
background = transform.scale(image.load(img_back), (width, height))

#step 4: buat kelas untuk bikin karakter
class karakter():
    def __init__(self, img, x, y, width, height): #karakteristik dari karakter
        self.image = transform.scale(image.load(img), (width, height))

        self.rect = self.image.get_rect()
        #pindah posisi ke x dan y yg udah ditentukan
        self.rect.x = x
        self.rect.y = y
    
    def draw(self): #tampilin karakter ke dalam screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

    #method untuk pergerakan
    def tombol_panah(self, kec):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: #batasan klo pencet atas
            self.rect.y -= kec
        if keys[K_DOWN] and self.rect.y < (width-5):
            self.rect.y += kec

    #jawab sendiri -> buat fungsi untuk tombol W, S
    def tombol_WS(self, kec):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: #batasan klo pencet atas
            self.rect.y -= kec
        if keys[K_s] and self.rect.y < (width-5):
            self.rect.y += kec
    
    def tabrakan(self, rect):
        return self.rect.colliderect(rect)


#step 5:
#pergerakan bola
dx = 3
dy = 3

#OPTIONAL -> KALO GAK DIPAKE, MAKA HAPUS AJA
#score pemain
font_16 = font.Font(None, 36) #16->ukuran font
warna_text = (0,0,0) #black

font1 = font.Font(None, 80)

#kalimatnya diganti aja
win_kanan = font1.render("Yeay kanan menang", True, warna_text)
win_kiri = font1.render("Yeay kiri menang", True, warna_text)


#variable score pemain
score_kanan = 0
score_kiri = 0

#step 6: upload karakter
bola_w, bola_h = 50, 50
bola = karakter(img_bola, 250,250, bola_w, bola_h)

kanan_w, kanan_h = 25, 50
kanan = karakter(img_kanan, width-50,250, kanan_w, kanan_h)

kiri_w, kiri_h = 25,50
kiri = karakter(img_kiri, 50,250,kiri_w,kiri_h)

kec_kanan = 5
kec_kiri = 5

#step 7: jalannya permainan
permainan_dimulai = True

fps = time.Clock() #frame per second

while permainan_dimulai:
    screen.blit(background, (0,0))
    bola.draw()
    kanan.draw()
    kiri.draw()
    
    #pergerakan
    kanan.tombol_panah(kec_kanan)
    kiri.tombol_WS(kec_kiri)

    #peraturan
    for e in event.get():
        #jika kita pencet tombol silang x
        if e.type == QUIT:
            quit()
    
    #pergerakan bola otomatis
    bola.rect.x += dx
    bola.rect.y += dy

    #cek jika bola kena karakter kiri
    if bola.tabrakan(kiri.rect):
        dx *= -1 #mantul

    #cek score kanan
    if bola.rect.x < 50: #kena gawang kiri
        score_kanan += 1
        bola.rect.x, bola.rect.y = 250,250 
    
    #cek jika bola kena karakter kanan
    if bola.tabrakan(kanan.rect):
        dx *= -1 #mantul

    #cek score kiri
    if bola.rect.x > (width-50): #kena gawang kanan
        score_kiri += 1
        bola.rect.x, bola.rect.y = 250,250 
        

    #cek jika bola ada di bawah bgt
    if bola.rect.y > (height-25):
        dy *= -1

    if bola.rect.y < 25:
        dy *= -1

    if score_kiri >= 2:
        screen.blit(win_kiri, (320, 250))
        dx, dy, kec_kanan, kec_kiri = 0, 0, 0, 0

    
    if score_kanan >= 2:
        screen.blit(win_kanan, (320, 250))
        dx, dy, kec_kanan, kec_kiri = 0, 0, 0, 0


    text_score_kiri = font_16.render("score:"+str(score_kiri), True, warna_text)
    text_score_kanan = font_16.render("score:"+str(score_kanan), True, warna_text)

    screen.blit(text_score_kiri, (10,10)) #posisi  kiri atas
    screen.blit(text_score_kanan, (width-110,10)) #posisi kanan atas

    display.update()
    fps.tick(60)
    





