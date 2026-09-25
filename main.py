import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600 #buat ngatur ukuran layar game
CELL_SIZE = 20  #ukuran tiap blok buat nanti dijadikan ukuran makanan & ukuran ular
GRID_WIDTH = WIDTH // CELL_SIZE 
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ULAR SAKTI by PADPAD")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (220, 20, 60)
BLACK = (0, 0, 0)

font_score = pygame.font.SysFont("arial", 20, bold=True)

#pertama tentuka posisi ularnya dulu, kita buat ukuran 3 kotak
start_x = (GRID_WIDTH // 2) * CELL_SIZE
start_y = (GRID_HEIGHT // 2) * CELL_SIZE
#untuk menentukan posisi ularnya
snake_body = [
    (start_x, start_y),
    (start_x - CELL_SIZE, start_y),
    (start_x - 2 * CELL_SIZE, start_y),
]
direction = "RIGHT"  # arah gerak sekarang (bisa ke arah mana aja untuk memulainya)

#buat makanannya
food_pos = (
    random.randint(0, GRID_WIDTH - 1) * CELL_SIZE,
    random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE,
)

score = 0

clock = pygame.time.Clock()
FPS = 5

running = True

while running:

    for event in pygame.event.get(): #simpan apa aja yg udah dilalui game nya mulai dari awal sampai game nya berhenti
        if event.type == pygame.QUIT: 
            running = False #kalo diteken tombol X maka game nya bakal berhenti
        elif event.type == pygame.KEYDOWN:
            #arah gerak
            if event.key == pygame.K_a:
                direction = "LEFT"
            elif event.key == pygame.K_d:
                direction = "RIGHT"
            elif event.key == pygame.K_w:
                direction = "UP"
            elif event.key == pygame.K_s:
                direction = "DOWN"

#untuk menentuka posisi kepala sama pergerakan kepala saat kita gerakkan pakai tombol
    head_x, head_y = snake_body[0]
    if direction == "LEFT":
        head_x -= CELL_SIZE
    elif direction == "RIGHT":
        head_x += CELL_SIZE
    elif direction == "UP":
        head_y -= CELL_SIZE
    elif direction == "DOWN":
        head_y += CELL_SIZE

    new_head = (head_x, head_y)

    hit_wall = not (0 <= head_x < WIDTH and 0 <= head_y < HEIGHT) #biar klo udah lewat area bakal mati & berhenti game nya
    hit_self = new_head in snake_body #ular akan mati saat menggigit tubuhnya sendiri
    if hit_wall or hit_self:
        running = False #nah ini biar gamenya berhenti saat ular mati

#tambahin kepala
    snake_body.insert(0, new_head)

#buat kode agar ukuran ular bertambah saat memakan makanannya
    if new_head == food_pos:
        score += 1
        food_pos = (
            random.randint(0, GRID_WIDTH - 1) * CELL_SIZE,
            random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE,
        )
    else:
#putuskan ekor
        snake_body.pop()
#jadi pergerakannya itu ular akan selalu menambahkan kepalanya, dan akar selalu memutus ekornya, namun jika ia makan maka tidak akan memutus ekornya

    screen.fill(WHITE)

#buat bentuk makanannya
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

#buat bentuk ularnya
    for segment in snake_body:
        pygame.draw.rect(screen, BLUE, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

#untuk menunjukkan skor 
    score_text = font_score.render(f"Skor gw nih bos: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

#untuk menampilkan semua perubahan yg terjadi dari awal sampai saat ini
    pygame.display.update()

#batasi kecepatan FPS nya
    clock.tick(FPS)

#berhentikan game
pygame.quit()