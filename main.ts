namespace SpriteKind {
    export const curser = SpriteKind.create()
    export const Health = SpriteKind.create()
    export const Power_up = SpriteKind.create()
    export const Ammo_count = SpriteKind.create()
    export const Alt_count = SpriteKind.create()
    export const Alt_ammu = SpriteKind.create()
    export const Boss = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Power_up, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.disintegrate, 500)
    if (true) {
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
        info.changeScoreBy(b_count)
        b_count = 0
    }
    Boss_health += -5
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Ammo > 0) {
        // Shoots upwards
        bullet = sprites.createProjectileFromSprite(img`
            . 2 . 
            2 1 2 
            2 1 2 
            2 1 2 
            . 2 . 
            `, mySprite, 0, 0)
        spriteutils.setVelocityAtAngle(bullet, spriteutils.angleFrom(mySprite, mySprite2), 100)
        bullet.setKind(SpriteKind.Projectile)
        Ammo += -1
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Alt_ammu, function (sprite2, otherSprite2) {
    sprites.destroy(otherSprite2, effects.disintegrate, 500)
    Alt += 3
})
sprites.onCreated(SpriteKind.Boss, function (sprite) {
    Boss_health = 400
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite5, otherSprite5) {
    sprites.destroy(otherSprite5, effects.disintegrate, 500)
    sprites.destroy(bullet, effects.ashes, 500)
    b_count += -1
    info.changeScoreBy(1)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Alt > 0) {
        // Shoots upwards
        bullet = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 0, 0)
        spriteutils.setVelocityAtAngle(bullet, spriteutils.angleFrom(mySprite, mySprite2), 100)
        bullet.setKind(SpriteKind.Projectile)
        Alt += -1
    }
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    pause(2000)
    Ammo = 10
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Boss, function (sprite5, otherSprite5) {
    Boss_health += -1
    if (Boss_health <= 0) {
        sprites.destroy(zombie_boss, effects.disintegrate, 500)
        zom_activation += 1
    } else {
        sprites.destroy(bullet, effects.disintegrate, 500)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite6, otherSprite6) {
    sprites.destroy(otherSprite6, effects.disintegrate, 500)
    info.changeLifeBy(-1)
})
info.onScore(100, function () {
    zombie_boss = sprites.create(img`
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
        `, SpriteKind.Boss)
    zombie_boss.setPosition(randint(0, 160), randint(0, 120))
    // Adjust speed of zombie
    zombie_boss.follow(mySprite, 20)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Health, function (sprite3, otherSprite3) {
    sprites.destroy(otherSprite3, effects.disintegrate, 500)
    info.changeLifeBy(1)
})
info.onLifeZero(function () {
    game.gameOver(false)
    game.setGameOverScoringType(game.ScoringType.HighScore)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Boss, function (sprite6, otherSprite6) {
    timer.throttle("attack", 500, function () {
        info.changeLifeBy(-2)
    })
})
let mySprite3: Sprite = null
let alt_powerup: Sprite = null
let my_sprite4: Sprite = null
let Alt_ammo: Sprite = null
let round2: Sprite = null
let zombie2: Sprite = null
let zombie: Sprite = null
let zombie_boss: Sprite = null
let bullet: Sprite = null
let Boss_health = 0
let b_count = 0
let Alt = 0
let Ammo = 0
let mySprite2: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite2 = sprites.create(img`
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
    `, SpriteKind.curser)
controller.moveSprite(mySprite)
controller.player2.moveSprite(mySprite2)
scene.setBackgroundImage(img`
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
    `)
info.setLife(10)
game.splash("ENDLESS CARNAGE")
game.splash("READ THIS!!!!")
game.splash("\"wasd\" to move")
game.splash("\"ijkl\" to move courser")
game.splash("\"qe\" to shoot", "press \"u\" to reload")
game.splash("Shoot as many zombies as", "Posible")
Ammo = 10
Alt = 3
b_count = 0
let zom_activation = 0
mySprite.setStayInScreen(true)
mySprite2.setStayInScreen(true)
game.onUpdateInterval(5000, function () {
    if (info.score() < 100) {
        zombie = sprites.create(img`
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
            `, SpriteKind.Enemy)
        zombie.setPosition(randint(0, 160), randint(0, 120))
        // Makes the zombie follow the player
        zombie.follow(mySprite, 30)
        b_count += 1
    }
    if (zom_activation == 1) {
        zombie = sprites.create(img`
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
            `, SpriteKind.Enemy)
        zombie.setPosition(randint(0, 160), randint(0, 120))
        // Makes the zombie follow the player
        zombie.follow(mySprite, 30)
    }
})
game.onUpdateInterval(5000, function () {
    if (info.score() < 100) {
        zombie2 = sprites.create(img`
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
            `, SpriteKind.Enemy)
        zombie2.setPosition(randint(0, 160), randint(0, 120))
        // Adjust speed of zombie
        zombie2.follow(mySprite, 40)
        b_count += 1
    }
    if (zom_activation == 1) {
        zombie2 = sprites.create(img`
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
            `, SpriteKind.Enemy)
        zombie2.setPosition(randint(0, 160), randint(0, 120))
        // Adjust speed of zombie
        zombie2.follow(mySprite, 40)
    }
})
forever(function () {
    if (Ammo == 10) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 9) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 8) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 7) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 6) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 5) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 4) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 3) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 2) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else if (Ammo == 1) {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    } else {
        sprites.destroy(round2)
        round2 = sprites.create(img`
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
            `, SpriteKind.Ammo_count)
    }
    round2.setPosition(10, 100)
})
forever(function () {
    if (Alt == 6) {
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img`
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
            `, SpriteKind.Alt_count)
    } else if (Alt == 5) {
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img`
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
            `, SpriteKind.Alt_count)
    } else if (Alt == 4) {
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img`
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
            `, SpriteKind.Alt_count)
    } else if (Alt == 3) {
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img`
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
            `, SpriteKind.Alt_count)
    } else if (Alt == 2) {
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img`
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
            `, SpriteKind.Alt_count)
    } else if (Alt == 1) {
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img`
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
            `, SpriteKind.Alt_count)
    } else {
        sprites.destroy(Alt_ammo)
        Alt_ammo = sprites.create(img`
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
            `, SpriteKind.Alt_count)
    }
    Alt_ammo.setPosition(140, 100)
})
game.onUpdateInterval(100, function () {
    timer.throttle("power up", 50000, function () {
        my_sprite4 = sprites.create(img`
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
            `, SpriteKind.Power_up)
        my_sprite4.setPosition(randint(0, 160), randint(0, 120))
    })
    timer.throttle("alt Reload", 150000, function () {
        alt_powerup = sprites.create(img`
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
            `, SpriteKind.Alt_ammu)
        alt_powerup.setPosition(randint(0, 160), randint(0, 120))
    })
    if (info.life() < 15) {
        timer.throttle("heal", 15000, function () {
            mySprite3 = sprites.create(img`
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
                `, SpriteKind.Health)
            mySprite3.setPosition(randint(0, 160), randint(0, 120))
        })
    } else {
        timer.throttle("heal", 100000000000000000, function () {
            mySprite3 = sprites.create(img`
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
                `, SpriteKind.Health)
            mySprite3.setPosition(randint(0, 160), randint(0, 120))
        })
    }
})
