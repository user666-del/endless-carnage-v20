@namespace
class SpriteKind:
    curser = SpriteKind.create()
    Health = SpriteKind.create()
    Power_up = SpriteKind.create()
    Ammo_count = SpriteKind.create()
    Alt_count = SpriteKind.create()
    Alt_ammu = SpriteKind.create()
    Boss = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global b_count, Boss_health
    sprites.destroy(otherSprite, effects.disintegrate, 500)
    if True:
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        info.change_score_by(b_count)
        b_count = 0
    Boss_health += -5
sprites.on_overlap(SpriteKind.player, SpriteKind.Power_up, on_on_overlap)

def on_b_pressed():
    global bullet, Ammo
    if Ammo > 0:
        # Shoots upwards
        bullet = sprites.create_projectile_from_sprite(img("""
                . 2 . 
                            2 1 2 
                            2 1 2 
                            2 1 2 
                            . 2 .
            """),
            mySprite,
            0,
            0)
        spriteutils.set_velocity_at_angle(bullet, spriteutils.angle_from(mySprite, mySprite2), 100)
        bullet.set_kind(SpriteKind.projectile)
        Ammo += -1
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    global Alt
    sprites.destroy(otherSprite2, effects.disintegrate, 500)
    Alt += 3
sprites.on_overlap(SpriteKind.player, SpriteKind.Alt_ammu, on_on_overlap2)

def on_on_created(sprite3):
    global Boss_health
    Boss_health = 400
sprites.on_created(SpriteKind.Boss, on_on_created)

def on_on_overlap3(sprite5, otherSprite5):
    global b_count
    sprites.destroy(otherSprite5, effects.disintegrate, 500)
    sprites.destroy(bullet, effects.ashes, 500)
    b_count += -1
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

def on_a_pressed():
    global bullet, Alt
    if Alt > 0:
        # Shoots upwards
        bullet = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 2 2 . . . . . . . . . 
                            . . . . . . 2 1 1 1 2 . . . . . . . . 
                            . . . . . . 2 1 1 1 2 . . . . . . . . 
                            . . . . . . 2 1 1 1 2 . . . . . . . . 
                            . . . . . . . 2 2 2 . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            0)
        spriteutils.set_velocity_at_angle(bullet, spriteutils.angle_from(mySprite, mySprite2), 100)
        bullet.set_kind(SpriteKind.projectile)
        Alt += -1
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_player2_button_a_pressed():
    global Ammo
    pause(2000)
    Ammo = 10
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_on_overlap4(sprite52, otherSprite52):
    global Boss_health, zom_activation
    Boss_health += -1
    if Boss_health <= 0:
        sprites.destroy(zombie_boss, effects.disintegrate, 500)
        zom_activation += 1
    else:
        sprites.destroy(bullet, effects.disintegrate, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Boss, on_on_overlap4)

def on_on_overlap5(sprite6, otherSprite6):
    sprites.destroy(otherSprite6, effects.disintegrate, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap5)

def on_on_score():
    global zombie_boss
    zombie_boss = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 2 2 7 7 7 2 2 2 . . . . 
                    . . . . 2 2 7 7 7 2 2 2 . . . . 
                    f f f f 7 7 7 7 7 7 7 2 f f f f 
                    f f f f 7 7 7 7 7 7 7 2 f f f f 
                    f f f f 7 7 7 2 2 2 7 2 f f f f 
                    f f f f 7 7 7 2 2 7 7 2 f f f f 
                    f f f f 2 7 7 7 7 7 2 2 f f f f 
                    f f f f . . . . . . . . f f f f 
                    7 7 7 7 . . . . . . . . 7 7 7 7 
                    7 7 7 7 . . . . . . . . 7 7 7 7 
                    7 7 7 7 . . . . . . . . 7 7 7 7 
                    7 7 7 7 . . . . . . . . 7 7 7 7 
                    7 7 7 7 . . . . . . . . 7 7 7 7
        """),
        SpriteKind.Boss)
    zombie_boss.set_position(randint(0, 160), randint(0, 120))
    # Adjust speed of zombie
    zombie_boss.follow(mySprite, 20)
info.on_score(100, on_on_score)

def on_on_overlap6(sprite32, otherSprite3):
    sprites.destroy(otherSprite3, effects.disintegrate, 500)
    info.change_life_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Health, on_on_overlap6)

def on_life_zero():
    game.game_over(False)
    game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
info.on_life_zero(on_life_zero)

def on_on_overlap7(sprite62, otherSprite62):
    
    def on_throttle():
        info.change_life_by(-2)
    timer.throttle("attack", 500, on_throttle)
    
sprites.on_overlap(SpriteKind.player, SpriteKind.Boss, on_on_overlap7)

mySprite3: Sprite = None
alt_powerup: Sprite = None
my_sprite4: Sprite = None
Alt_ammo: Sprite = None
round2: Sprite = None
zombie2: Sprite = None
zombie: Sprite = None
zombie_boss: Sprite = None
bullet: Sprite = None
Boss_health = 0
b_count = 0
Alt = 0
Ammo = 0
mySprite2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 7 7 7 7 7 7 . . . . . 
            . . . . . 7 7 f f 7 7 . . . . . 
            . . . . . 7 f f f f 7 . . . . . 
            . . . . . 7 7 7 7 7 7 . . . . . 
            . . . e e f f f f f f e e . . . 
            . . . e e f f f f f f e e . . . 
            . . . e e f f f f f f e e . . . 
            . . . e e f f f f f f e e . . . 
            . . . e e f f f f f f e e . . . 
            . . . . . 8 8 8 8 8 8 . . . . . 
            . . . . . 8 8 8 8 8 8 . . . . . 
            . . . . . 8 8 . . 8 8 . . . . . 
            . . . . . 8 8 . . 8 8 . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
mySprite2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 1 1 . . . . . . . 
            . . . . . . . 1 1 . . . . . . . 
            . . . . . . . 1 1 . . . . . . . 
            . . . . 1 1 1 . . 1 1 1 . . . . 
            . . . . 1 1 1 . . 1 1 1 . . . . 
            . . . . . . . 1 1 . . . . . . . 
            . . . . . . . 1 1 . . . . . . . 
            . . . . . . . 1 1 . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.curser)
controller.move_sprite(mySprite)
controller.player2.move_sprite(mySprite2)
scene.set_background_image(img("""
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccccbcccbbccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbcccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccccccccccccccccccccbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbccccccccccccccccccbbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccbbbbbbbbbbbcccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbccccccccbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccbbbccccccccbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbccccccccbbbbbcccccccccccbbbbbbbbbbbbbbccccccccccccccccccccccccccbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbcccccbbbbbbbbbbbbb8888888bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbcccccbbbbbbbbbbbb885555588bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbb
        bbbbbbbbbbccccbbbbbbbbbbbbb858555858bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777888888888888888bbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbb
        bbbbbbbbbbccccbbbbbbbbbbbbb858858858bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777888855558888888bbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbb
        bbbbbbbbbbcccbbbbbbbbbbbbbb858858858bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb7777777888588855588888bbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbb
        bbbbbbbbbbcccbbbbbbbbbbbbbb855585558bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777888558855888888bbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbb
        bbbbbbbbbbcccbbbbbbbbbbbbbbee5555588bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777888555585588888bbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbb
        bbbbbbbbbbcccbbbbbbbbbbbbbbee5858578bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77777777888558855888888bbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbb
        bbbbbbbbbbcccbbbbbbbbbbbbbbbe8888877bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777b888588855588888bbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbb
        bbbbbbbbbbcccbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb777777b888855558888888bbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbb
        bbbbbbbbbbccccbbbbbbbbbbbbbbbbb7777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb77bb888888888888888bbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbb
        bbbbbbbbbbccccbbbbbbbbbbbbbbbbbb777777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbb
        bbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbb77777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbb
        bbbbbbbbbbbccccbbbbbbbbbbbbbbbbbb777bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbb
        bbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbb
        bbbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbb
        bbbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbb
        bbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccbbbbbbbbbbbbbbbbbcccbbbbbbbb
        bbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc222222222222cccbbbbbbbbbbbbbbbccccbbbbbbb
        bbbbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc222222222422222ccccbbbbbbbbbbbbccccbbbbbbb
        bbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc2222222224242222222cccbbbbbbbbbbbcccbbbbbbb
        bbbbbbbbbbbbbccccdddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc2222224442242222222222ccbbbbbbbbbbcccbbbbbbb
        bbbbbbbbbbbbbbcccdddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc222222422242224222222222ccbbbbbbbbccccbbbbbbb
        bbbbbbbbbbbbbbcccddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc2222224222422222222222422cbbbbbbbbccccbbbbbbb
        bbbbbbbbbbbbbbccccdddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc22224224222422222244224242cbbbbbbbbcccbbbbbbbb
        bbbbbbbbbbbbbbccccdddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc22222222444222422422422422cbbbbbbbbcccbbbbbbbb
        bbbbbbbbbbbbbbbcccdddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc22222222222222222422422222cbbbbbbbbcccbbbbbbbb
        bbbbbbbbbbbbbbbcccdddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc22222422222222222244222222cbbbbbbbccccbbbbbbbb
        bbbbbbbbbbbbbbbcccddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc22224242222224442222222222cbbbbbbbccccbbbbbbbb
        bbbbbbbbbbbbbbbcccdddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc22222422224242224224224222cbbbbbbbcccbbbbbbbbb
        bbbbbbbbbbbbbbbcccdddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc2222224422242224242422222cbbbbbbbcccbbbbbbbbb
        bbbbbbbbbbbbbbbcccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc22224224224222422422222ccbbbbbbbccccbbbbbbbb
        bbbbbbbbbbbbbbbcccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc222422422244422222222ccbbbbbbbbccccbbbbbbbb
        bbbbbbbbbbbbbbbcccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc222442222222222222cccbbbbbbbbbbcccbbbbbbbb
        bbbbbbbbbbbbbbbcccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc22222222222222ccccbbbbbbbbbbbbcccbbbbbbbb
        bbbbbbbbbbbbbbbcccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc222222222cccccbbbbbbbbbbbbbbbcccbbbbbbbb
        bbbbbbbbbbbbbbbcccdddddccccccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbccc2222cccccbbbbbbbbbbbbbbbbbbcccbbbbbbbb
        bbbbbbbbbbbbbbbcccdddcc22222cccddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbb
        bbbbbbbbbbbbbbbcccddcc22422222ccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc2242422222cccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc222422224222cddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc244224242422cbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc422422224222ccbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc4224222222222ccbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc244222222222222cbbbbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc222222242244422ccbbbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc2222222224222422cccccbbbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc22224222242224222222ccbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc222222222422242224222ccbbbbbbbbbbbbbddddddddddddddddddddddddddd777ddddddd33dddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccbbc2222222222444222424222cbbbbbbbbbbbbbbbbddddddddddddddddddddddd7777ddddd3333ddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbccccbbcc222222222222222242222cbbbbbbbbbbbbbbbbbbbbbddddddddddddddddd7777dddddd3223dddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbccccbbbc22422444222242222222cbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddd7777ddddddd3dddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbccccbbbbc2222422242222222222ccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddd77ddddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbcccccbbbbbc22242224222222222ccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddd77dddd7f1732dddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbcccccbbbbbc22242224222cccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdd77d2277777332d3ddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbcccccbbbbbcc22244422cccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66dd27777773d32dddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccbbbbbbbcc2222222ccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66bd77777777dddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666677777777ddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66666667777777dddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb66666666667777777ddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb666666666666677777ddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8866666666666666b777dddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb888866666666666666bbbbbdddddddddddddddddddddddddddddddddbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88888886666666666666bbbbbbbdddddddddddddddddddddddddddddddbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb888888888666666666bb66bbbbbbbbbddddddddddddddddddddddddddddddbbbbbbbbbbbbbccccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8888888888886666666bbb66bbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbbbcccbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88888888888888666bbbbbb77bbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbbcccbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8888888888888866bbbbbbb77bbbbbbbbbbbbdddddddddddddddddddddddddddddbbbbbbbbbbbcccbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbcccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb88888b8888888bbbbbbbbb77bbbbbbbbbbbbbbdddddddddddddddddddddddddddbbbbbbbbbbbcccbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb8888888bbbbbbbbbb77bbbbbbbbbbbbbbbdddddddddddddddddddddddddddbbbbbbbbbbcccbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbb8888888bbbbbbbbbbb77bbbbbbbbbbbbbbbbdddddddddddddddddddddddddddbbbbbbbbbcccbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbb888888bbbbbbbbbbbbb77bbbbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbcccbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbccccccccccccbbbbbbbbbbbbbbbbbbbbb88888bbbbbbbbbbbbbb77bbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddbbbbbbbbccccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccbbbbbbbbbbbbbbbbbbbbb88bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddbbbbbbbbccccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddbbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddbbbbbbbcccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddbbbbcccccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddcccccccbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddddddddddddddcccccbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbcccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccddddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbcccccdddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbcccccccbddddddddddddddddddddddddbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbccccccccbbbbddddddddddddddddddddddddbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbbbbbbbccccccccccccccccbccccccccccccbbbbbdddddddddddddddddddddddddbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbdddddddddddddddddddddddddbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccbbbbbbbbbbbdddddddddddddddddddddddddbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbbbbbbbbbbbbdddddddddddddddddddddddddbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddddddddddddddddddddddddbbbbbbbbbbbbbbb
"""))
info.set_life(10)
game.splash("ENDLESS CARNAGE")
game.splash("READ THIS!!!!")
game.splash("\"wasd\" to move")
game.splash("\"ijkl\" to move courser")
game.splash("\"qe\" to shoot", "press \"u\" to reload")
game.splash("Shoot as many zombies as", "Posible")
Ammo = 10
Alt = 3
b_count = 0
zom_activation = 0
mySprite.set_stay_in_screen(True)
mySprite2.set_stay_in_screen(True)

def on_update_interval():
    global zombie, b_count
    if info.score() < 100:
        zombie = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 7 3 7 . . . . . . . 
                            . . . . . 7 3 2 3 3 . . . . . . 
                            . . . . 8 7 2 3 2 7 8 . . . . . 
                            . . . . 7 8 2 7 7 8 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        zombie.set_position(randint(0, 160), randint(0, 120))
        # Makes the zombie follow the player
        zombie.follow(mySprite, 30)
        b_count += 1
    if zom_activation == 1:
        zombie = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 7 3 7 . . . . . . . 
                            . . . . . 7 3 2 3 3 . . . . . . 
                            . . . . 8 7 2 3 2 7 8 . . . . . 
                            . . . . 7 8 2 7 7 8 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        zombie.set_position(randint(0, 160), randint(0, 120))
        # Makes the zombie follow the player
        zombie.follow(mySprite, 30)
        b_count += 1
    else:
        b_count += 0
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global zombie2, b_count
    if info.score() < 100:
        zombie2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . b b 7 . . . . . . . 
                            . . . . . b b b b 7 . . . . . . 
                            . . . . 8 7 2 b 7 7 8 . . . . . 
                            . . . . 7 8 2 7 7 8 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        zombie2.set_position(randint(0, 160), randint(0, 120))
        # Adjust speed of zombie
        zombie2.follow(mySprite, 40)
        b_count += 1
    if zom_activation == 1:
        zombie2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . b b 7 . . . . . . . 
                            . . . . . b b b b 7 . . . . . . 
                            . . . . 8 7 2 b 7 7 8 . . . . . 
                            . . . . 7 8 2 7 7 8 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.enemy)
        zombie2.set_position(randint(0, 160), randint(0, 120))
        # Adjust speed of zombie
        zombie2.follow(mySprite, 40)
        b_count += 1
    else:
        b_count += 0
game.on_update_interval(5000, on_update_interval2)

def on_forever():
    global round2
    if Ammo == 10:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . 1 . . . . 1 1 1 1 . . . 
                            . . . 1 1 . . . 1 1 . . 1 1 . . 
                            . . 1 . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 . . . . 1 . . 
                            . . . . 1 . . . 1 1 . . 1 1 . . 
                            . . 1 1 1 1 1 . . 1 1 1 1 . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 9:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . 7 7 7 7 7 7 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 7 7 7 7 7 7 . . . . . 
                            . . . . . . . . . . 7 . . . . . 
                            . . . . . . . . . . 7 . . . . . 
                            . . . . . . . . . . 7 . . . . . 
                            . . . . . . . . . . 7 . . . . . 
                            . . . . . . . . . . 7 . . . . . 
                            . . . . . . . . . . 7 . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 8:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . 7 7 7 7 7 . . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . . 7 7 7 7 7 . . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . . 7 7 7 7 7 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 7:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . 7 7 7 7 7 7 7 7 7 . . . 
                            . . . . . . . . . . . . 7 . . . 
                            . . . . . . . . . . . . 7 . . . 
                            . . . . . . . . . . . 7 7 . . . 
                            . . . . . . . . . . 7 7 . . . . 
                            . . . . . . . . . 7 7 . . . . . 
                            . . . . . . . . 7 7 . . . . . . 
                            . . . . . . . 7 7 . . . . . . . 
                            . . . . . . . 7 . . . . . . . . 
                            . . . . . . 7 7 . . . . . . . . 
                            . . . . . . 7 . . . . . . . . . 
                            . . . . . . 7 . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 6:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . 4 4 . . . . . . 
                            . . . . . . . 4 4 . . . . . . . 
                            . . . . . . 4 4 . . . . . . . . 
                            . . . . . 4 4 . . . . . . . . . 
                            . . . . 4 4 4 4 4 4 . . . . . . 
                            . . . . 4 . . . . . 4 . . . . . 
                            . . . . 4 . . . . . 4 . . . . . 
                            . . . . 4 . . . . . 4 . . . . . 
                            . . . . 4 . . . . . 4 . . . . . 
                            . . . . 4 . . . . . 4 . . . . . 
                            . . . . . 4 4 4 4 4 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 5:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 4 4 4 4 4 4 4 . . . . 
                            . . . . . 4 . . . . . . . . . . 
                            . . . . . 4 . . . . . . . . . . 
                            . . . . . 4 . . . . . . . . . . 
                            . . . . . 4 . . . . . . . . . . 
                            . . . . . 4 4 4 4 4 . . . . . . 
                            . . . . . . . . . 4 4 . . . . . 
                            . . . . . . . . . . 4 4 . . . . 
                            . . . . . . . . . . . 4 . . . . 
                            . . . . . . . . . . . 4 . . . . 
                            . . . . . . . . . . 4 4 . . . . 
                            . . . . . . . . . 4 4 . . . . . 
                            . . . . . 4 4 4 4 4 . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 4:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . 4 4 . . . . . . 
                            . . . . . . . 4 . 4 . . . . . . 
                            . . . . . . 4 . . 4 . . . . . . 
                            . . . . . 4 . . . 4 . . . . . . 
                            . . . . 4 . . . . 4 . . . . . . 
                            . . . . 4 4 4 4 4 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 3:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . 1 1 1 1 1 . . . . . . 
                            . . . . 1 1 2 2 2 1 1 . . . . . 
                            . . . . 1 2 1 1 1 2 1 1 . . . . 
                            . . . . 1 2 1 . 1 1 2 1 . . . . 
                            . . . . 1 1 1 . . 1 2 1 . . . . 
                            . . . . . . . . 1 1 2 1 . . . . 
                            . . . . . 1 1 1 1 2 2 1 . . . . 
                            . . . . . 1 2 2 2 2 1 1 . . . . 
                            . . . . . 1 1 1 1 2 1 1 . . . . 
                            . . . . . . . . 1 1 2 1 . . . . 
                            . . . . . . . . . 1 2 1 . . . . 
                            . . . . 1 1 1 . . 1 2 1 . . . . 
                            . . . . 1 2 1 . . 1 2 1 . . . . 
                            . . . . 1 2 1 1 1 1 2 1 . . . . 
                            . . . . 1 1 2 2 2 2 1 1 . . . . 
                            . . . . . 1 1 1 1 1 1 . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 2:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . 1 1 1 1 1 1 1 1 . . . . 
                            . . . 1 1 2 2 2 2 2 2 1 1 . . . 
                            . . . 1 2 2 1 1 1 1 2 2 1 1 . . 
                            . . . 1 2 1 1 . . 1 1 2 2 1 . . 
                            . . . 1 1 1 . . . . 1 1 2 1 . . 
                            . . . . . . . . . . 1 1 2 1 . . 
                            . . . . . . . . . 1 1 2 2 1 . . 
                            . . . . . . . . 1 1 2 2 1 1 . . 
                            . . . . . . 1 1 1 2 2 1 1 . . . 
                            . . . . 1 1 1 2 2 2 1 1 . . . . 
                            . . . 1 1 2 2 2 1 1 1 . . . . . 
                            . . . 1 2 1 1 1 1 1 1 1 1 1 . . 
                            . . . 1 2 2 2 2 2 2 2 2 2 1 . . 
                            . . . 1 1 1 1 1 1 1 1 1 1 1 . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    elif Ammo == 1:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . 1 1 1 1 . . . . . . 
                            . . . . . 1 1 2 2 1 . . . . . . 
                            . . . . 1 1 2 1 2 1 . . . . . . 
                            . . . . 1 2 1 1 2 1 . . . . . . 
                            . . . . 1 1 1 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . 1 1 1 1 2 1 1 1 1 . . . 
                            . . . . 1 2 2 2 2 2 2 2 1 . . . 
                            . . . . 1 1 1 1 1 1 1 1 1 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    else:
        sprites.destroy(round2)
        round2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 1 1 1 1 1 . . . . . 
                            . . . . . 1 1 . . . 1 1 . . . . 
                            . . . . . 1 . . . . . 1 . . . . 
                            . . . . . 1 . . . . . . . . . . 
                            . . . . . 1 . . . 1 1 1 . . . . 
                            . . . . . 1 . . . . 1 1 . . . . 
                            . . . . . . 1 1 1 1 . 1 . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Ammo_count)
    round2.set_position(10, 100)
forever(on_forever)

def on_forever2():
    global Alt_ammo
    if Alt == 6:
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . 7 . . . . . . 
                            . . . . . . . . 7 7 . . . . . . 
                            . . . . . . . 7 7 . . . . . . . 
                            . . . . . . 7 7 . . . . . . . . 
                            . . . . . 7 7 . . . . . . . . . 
                            . . . . 7 7 7 7 7 7 . . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . 7 . . . . . 7 . . . . . 
                            . . . . . 7 7 7 7 7 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Alt_count)
    elif Alt == 5:
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 7 7 7 7 7 7 7 . . . . 
                            . . . . . 7 . . . . . . . . . . 
                            . . . . . 7 . . . . . . . . . . 
                            . . . . . 7 . . . . . . . . . . 
                            . . . . . 7 . . . . . . . . . . 
                            . . . . . 7 7 7 7 7 . . . . . . 
                            . . . . . . . . . 7 7 . . . . . 
                            . . . . . . . . . . 7 7 . . . . 
                            . . . . . . . . . . . 7 . . . . 
                            . . . . . . . . . . . 7 . . . . 
                            . . . . . . . . . . 7 7 . . . . 
                            . . . . . . . . . 7 7 . . . . . 
                            . . . . . 7 7 7 7 7 . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Alt_count)
    elif Alt == 4:
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . 4 4 . . . . . . 
                            . . . . . . . 4 . 4 . . . . . . 
                            . . . . . . 4 . . 4 . . . . . . 
                            . . . . . 4 . . . 4 . . . . . . 
                            . . . . 4 . . . . 4 . . . . . . 
                            . . . . 4 4 4 4 4 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Alt_count)
    elif Alt == 3:
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . 4 4 4 . . . . . . . 
                            . . . . . 4 . . . 4 . . . . . . 
                            . . . . . 4 . . . . 4 . . . . . 
                            . . . . . . . . . . 4 . . . . . 
                            . . . . . . . . . . 4 . . . . . 
                            . . . . . . . . . 4 4 . . . . . 
                            . . . . . . 4 4 4 4 . . . . . . 
                            . . . . . . . . . 4 . . . . . . 
                            . . . . . . . . . 4 4 . . . . . 
                            . . . . . . . . . . 4 . . . . . 
                            . . . . . . . . . . 4 . . . . . 
                            . . . . . 4 . . . . 4 . . . . . 
                            . . . . . 4 4 . . 4 4 . . . . . 
                            . . . . . . 4 4 4 4 . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Alt_count)
    elif Alt == 2:
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . 1 1 1 1 1 1 1 1 . . . . 
                            . . . 1 1 2 2 2 2 2 2 1 1 . . . 
                            . . . 1 2 2 1 1 1 1 2 2 1 1 . . 
                            . . . 1 2 1 1 . . 1 1 2 2 1 . . 
                            . . . 1 1 1 . . . . 1 1 2 1 . . 
                            . . . . . . . . . . 1 1 2 1 . . 
                            . . . . . . . . . 1 1 2 2 1 . . 
                            . . . . . . . . 1 1 2 2 1 1 . . 
                            . . . . . . 1 1 1 2 2 1 1 . . . 
                            . . . . 1 1 1 2 2 2 1 1 . . . . 
                            . . 1 1 1 2 2 2 1 1 1 . . . . . 
                            . . 1 2 2 2 1 1 1 1 1 1 1 1 . . 
                            . . 1 2 2 2 2 2 2 2 2 2 2 1 . . 
                            . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Alt_count)
    elif Alt == 1:
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img("""
                . . . . . . 1 1 1 1 . . . . . . 
                            . . . . . 1 1 2 2 1 . . . . . . 
                            . . . . 1 1 2 1 2 1 . . . . . . 
                            . . . . 1 2 1 1 2 1 . . . . . . 
                            . . . . 1 1 1 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . . . . 1 2 1 . . . . . . 
                            . . . . 1 1 1 1 2 1 1 1 1 . . . 
                            . . . . 1 2 2 2 2 2 2 2 1 . . . 
                            . . . . 1 1 1 1 1 1 1 1 1 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Alt_count)
    else:
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 1 1 1 1 1 . . . . . 
                            . . . . . 1 1 . . . 1 1 . . . . 
                            . . . . . 1 . . . . . 1 . . . . 
                            . . . . . 1 . . . . . . . . . . 
                            . . . . . 1 . . . 1 1 1 . . . . 
                            . . . . . 1 . . . . 1 1 . . . . 
                            . . . . . . 1 1 1 1 . 1 . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Alt_count)
    Alt_ammo.set_position(140, 100)
forever(on_forever2)

def on_update_interval3():
    
    def on_throttle2():
        global my_sprite4
        my_sprite4 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . d d d . . . . . . . . 
                            . . . . d d b d d . . . . . . . 
                            . . . . d b d b d d . . . . . . 
                            . . . . d d f f f d d . . . . . 
                            . . . . d f f f f f d . . . . . 
                            . . . . d f f f f f d . . . . . 
                            . . . . d f f f f f d . . . . . 
                            . . . . d d f f f d d . . . . . 
                            . . . . . d d d d d . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Power_up)
        my_sprite4.set_position(randint(0, 160), randint(0, 120))
    timer.throttle("power up", 50000, on_throttle2)
    
    
    def on_throttle3():
        global alt_powerup
        alt_powerup = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . 6 6 6 6 . . . . . . . . 
                            . . . . . . 6 6 6 6 6 . . . . . 
                            . . . . . . . . . . 6 6 . . . . 
                            . . . . 6 6 6 6 6 6 6 6 6 . . . 
                            . . . . 6 6 4 6 4 6 4 6 6 . . . 
                            . . . . 6 6 5 6 5 6 5 6 6 . . . 
                            . . . . 6 6 5 6 5 6 5 6 6 . . . 
                            . . . . 6 6 6 6 6 6 6 6 6 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Alt_ammu)
        alt_powerup.set_position(randint(0, 160), randint(0, 120))
    timer.throttle("alt Reload", 150000, on_throttle3)
    
    if info.life() < 15:
        
        def on_throttle4():
            global mySprite3
            mySprite3 = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . 2 3 . . . . . 
                                    . . . . . . 2 3 . 2 2 . 2 2 . . 
                                    . . . . . . . 2 2 3 2 2 . . . . 
                                    . . . . . . 2 3 3 3 2 . . . . . 
                                    . . . . . . 2 3 3 2 2 . . . . . 
                                    . . . . . 2 3 3 2 2 . . . . . . 
                                    . . . . . . 2 2 2 . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                SpriteKind.Health)
            mySprite3.set_position(randint(0, 160), randint(0, 120))
        timer.throttle("heal", 15000, on_throttle4)
        
    else:
        
        def on_throttle5():
            global mySprite3
            mySprite3 = sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . 2 3 . . . . . 
                                    . . . . . . 2 3 . 2 2 . 2 2 . . 
                                    . . . . . . . 2 2 3 2 2 . . . . 
                                    . . . . . . 2 3 3 3 2 . . . . . 
                                    . . . . . . 2 3 3 2 2 . . . . . 
                                    . . . . . 2 3 3 2 2 . . . . . . 
                                    . . . . . . 2 2 2 . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                SpriteKind.Health)
            mySprite3.set_position(randint(0, 160), randint(0, 120))
        timer.throttle("heal", 100000000000000000, on_throttle5)
        
game.on_update_interval(100, on_update_interval3)
