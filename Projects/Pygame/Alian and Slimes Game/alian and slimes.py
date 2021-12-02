#ابتدا باید pip install pygame را در سیستم عامل اجرا کنید
import pygame

#برای شروع حتما به این خط نیاز است
pygame.init()


#جهت تنظیم مختصات صفحه نمایش
screen = pygame.display.set_mode((1000, 500))

#ساعت برای تنظیم سرعت بازی
c = pygame.time.Clock()

#جهت فول اسکرین
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#جهت یافتن رزولوشن فعلی مانیتور
#infoObject = pygame.display.Info()
#pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

#جهت ذخیره سازی یک عکس
#و تغییر مختصات عکس
image = pygame.image.load('alian.png')
image = pygame.transform.scale(image, (150, 150))

mouse = pygame.image.load('slimes.png')
mouse = pygame.transform.scale(mouse, (150, 150))
rect_mouse = mouse.get_rect()
rect_mouse.x, rect_mouse.y = 700, 700

#جهت تبدیل عکس به یک مستطیل برای کارهای آتی و حرکت
rect  = image.get_rect()
rect.x = 400
rect.y = 400


running = True

#حلقه بینهایتی که بازی در آن قرار میگیرد
while running:
#تنظیم سرعت بازی به صورت سی فریم در ثانیه    
    c.tick(30)
    #جهت رنگ یکسان برای پس زمینه    
    screen.fill((200, 100, 77))#250بیشترنمیتومه باشه

#تنظیمات برای اینکه بتوان از بازی خارج شد    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            
    #یافتن کلیدی که کاربر زده جهت تنظیم تغییرات    
    move_x, move_y = 0, 0
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        move_x -= 10
    if key[pygame.K_RIGHT]:
        move_x += 10
    if key[pygame.K_UP]:
        move_y -= 10
    if key[pygame.K_DOWN]:
        move_y += 10
    move_x1,move_y1=0,0
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        move_x1 -=10
    if key[pygame.K_d]:
        move_x1 +=10
    if key[pygame.K_w]:
        move_y1 -=10
    if key[pygame.K_s]:
        move_y1 +=10
        
#ایجاد حرکت در شکل    
    rect = rect.move((move_x, move_y))
    rect_mouse=rect_mouse.move((move_x1,move_y1))
    screen.blit(mouse, rect_mouse)
    screen.blit(image, rect)
    
    #برای بررسی برخورد    
    if rect.colliderect(rect_mouse):
        break

    
    #زوشی دیگر جهت کشیدن شکل    
    #screen.blit(image, (image_x, image_y))

    #جهت آپدیت کردن صفحه نمایش    
    pygame.display.update()
    

#بستن صفحه بازی
pygame.quit()    