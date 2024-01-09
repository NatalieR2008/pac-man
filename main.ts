namespace SpriteKind {
    export const Prey = SpriteKind.create()
    export const Boost = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    tiles.setTileAt(location, assets.tile`myTile0`)
    info.changeScoreBy(1)
    pellets += 1
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    pacman,
    assets.animation`Pacman up`,
    100,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Prey, function (sprite2, otherSprite2) {
    info.changeScoreBy(5)
    tiles.placeOnRandomTile(otherSprite2, assets.tile`myTile3`)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    pacman,
    assets.animation`PacMan Right`,
    100,
    true
    )
})
info.onCountdownEnd(function () {
    game.gameOver(true)
    game.splash(info.score())
    game.splash(info.highScore())
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    pacman,
    assets.animation`Pacman Left`,
    100,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, otherSprite) {
    info.changeScoreBy(3)
    sprites.destroy(otherSprite)
    red_ghost.setKind(SpriteKind.Prey)
    pink_ghost.setKind(SpriteKind.Prey)
    orange_ghost.setKind(SpriteKind.Prey)
    cyan_ghost.setKind(SpriteKind.Prey)
    red_ghost.setImage(assets.image`Prey`)
    pink_ghost.setImage(assets.image`Prey`)
    orange_ghost.setImage(assets.image`Prey`)
    cyan_ghost.setImage(assets.image`Prey`)
    pause(3000)
    red_ghost.setKind(SpriteKind.Enemy)
    pink_ghost.setKind(SpriteKind.Enemy)
    orange_ghost.setKind(SpriteKind.Enemy)
    cyan_ghost.setKind(SpriteKind.Enemy)
    red_ghost.setImage(assets.image`Red ghost`)
    pink_ghost.setImage(assets.image`Pink Ghost`)
    orange_ghost.setImage(assets.image`Orange ghost`)
    cyan_ghost.setImage(assets.image`Cyan ghost`)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    pacman,
    assets.animation`PacMan Down`,
    100,
    true
    )
})
info.onLifeZero(function () {
    game.gameOver(false)
    game.splash(info.score())
    game.splash(info.highScore())
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite22, otherSprite22) {
    for (let index = 0; index < 1; index++) {
        info.changeScoreBy(-3)
        info.changeLifeBy(-1)
        tiles.placeOnTile(pacman, tiles.getTileLocation(15, 30))
        pause(100)
    }
})
let orange_ghost: Sprite = null
let cyan_ghost: Sprite = null
let pink_ghost: Sprite = null
let red_ghost: Sprite = null
let pacman: Sprite = null
pacman = sprites.create(assets.image`Pac-Man Right`, SpriteKind.Player)
tiles.setCurrentTilemap(tilemap`level1`)
tiles.placeOnTile(pacman, tiles.getTileLocation(15, 30))
let pellets = 0
red_ghost = sprites.create(assets.image`Red ghost`, SpriteKind.Enemy)
pink_ghost = sprites.create(assets.image`Pink Ghost`, SpriteKind.Enemy)
cyan_ghost = sprites.create(assets.image`Cyan ghost`, SpriteKind.Enemy)
orange_ghost = sprites.create(assets.image`Orange ghost`, SpriteKind.Enemy)
let PowerPellets = [
sprites.create(assets.image`PowerPellet`, SpriteKind.Projectile),
sprites.create(assets.image`PowerPellet`, SpriteKind.Projectile),
sprites.create(assets.image`PowerPellet`, SpriteKind.Projectile),
sprites.create(assets.image`PowerPellet`, SpriteKind.Projectile),
sprites.create(assets.image`PowerPellet`, SpriteKind.Projectile),
sprites.create(assets.image`PowerPellet`, SpriteKind.Projectile)
]
for (let value of PowerPellets) {
    for (let index = 0; index < 6; index++) {
        tiles.placeOnRandomTile(value, assets.tile`myTile2`)
    }
}
let Difficulty = game.askForString("Difficulty (E, M, H)", 1)
red_ghost.setPosition(randint(50, 2000), randint(50, 2000))
red_ghost.setBounceOnWall(true)
pink_ghost.setPosition(randint(50, 200), randint(50, 200))
pink_ghost.setBounceOnWall(true)
orange_ghost.setPosition(randint(50, 2000), randint(50, 200))
orange_ghost.setBounceOnWall(true)
cyan_ghost.setPosition(randint(50, 2000), randint(50, 200))
cyan_ghost.setBounceOnWall(true)
red_ghost.follow(pacman)
pink_ghost.follow(pacman)
orange_ghost.follow(pacman)
cyan_ghost.follow(pacman)
info.startCountdown(180)
game.setGameOverScoringType(game.ScoringType.HighScore)
if (Difficulty == "e") {
    info.setScore(0)
    info.setLife(4)
    pacman.setVelocity(75, 75)
    red_ghost.setVelocity(50, 50)
    pink_ghost.setVelocity(50, 50)
    orange_ghost.setVelocity(50, 50)
    cyan_ghost.setVelocity(50, 50)
} else if (Difficulty == "m") {
    info.setScore(0)
    info.setLife(2)
    pacman.setVelocity(50, 50)
    red_ghost.setVelocity(50, 50)
    pink_ghost.setVelocity(50, 50)
    orange_ghost.setVelocity(50, 50)
    cyan_ghost.setVelocity(50, 50)
} else if (Difficulty == "h") {
    info.setScore(0)
    info.setLife(1)
    pacman.setVelocity(50, 50)
    red_ghost.setVelocity(75, 75)
    pink_ghost.setVelocity(50, 50)
    orange_ghost.setVelocity(50, 50)
    cyan_ghost.setVelocity(50, 50)
}
forever(function () {
    scene.cameraFollowSprite(pacman)
    controller.moveSprite(pacman)
    game.setGameOverEffect(false, effects.melt)
    game.setGameOverEffect(true, effects.starField)
    game.setGameOverMessage(false, "YOU DIED")
    game.setGameOverMessage(true, "YOU SURVIVED!")
    if (pellets == 532) {
        game.gameOver(true)
        game.splash(info.score())
        game.splash(info.highScore())
    }
})
