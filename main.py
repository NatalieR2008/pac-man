@namespace
class SpriteKind:
    Prey = SpriteKind.create()
    Boost = SpriteKind.create()

def on_overlap_tile(sprite, location):
    global pellets
    tiles.set_tile_at(location, assets.tile("""
        myTile0
    """))
    info.change_score_by(1)
    pellets += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_up_pressed():
    animation.run_image_animation(pacman, assets.animation("""
        Pacman up
    """), 100, True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite2, otherSprite2):
    info.change_score_by(5)
    tiles.place_on_random_tile(otherSprite2, assets.tile("""
        myTile3
    """))
sprites.on_overlap(SpriteKind.player, SpriteKind.Prey, on_on_overlap)

def on_left_pressed():
    animation.run_image_animation(pacman,
        assets.animation("""
            PacMan Right
        """),
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_countdown_end():
    game.game_over(True)
    game.splash(info.score())
    game.splash(info.high_score())
info.on_countdown_end(on_countdown_end)

def on_on_overlap2(sprite22, otherSprite22):
    for index in range(1):
        info.change_score_by(-3)
        info.change_life_by(-1)
        tiles.place_on_tile(pacman, tiles.get_tile_location(15, 30))
        pause(100)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

def on_right_pressed():
    animation.run_image_animation(pacman, assets.animation("""
        Pacman Left
    """), 100, True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap3(sprite3, otherSprite):
    info.change_score_by(3)
    sprites.destroy(otherSprite)
    red_ghost.set_kind(SpriteKind.Prey)
    pink_ghost.set_kind(SpriteKind.Prey)
    orange_ghost.set_kind(SpriteKind.Prey)
    cyan_ghost.set_kind(SpriteKind.Prey)
    red_ghost.set_image(assets.image("""
        Prey
    """))
    pink_ghost.set_image(assets.image("""
        Prey
    """))
    orange_ghost.set_image(assets.image("""
        Prey
    """))
    cyan_ghost.set_image(assets.image("""
        Prey
    """))
    pause(3000)
    red_ghost.set_kind(SpriteKind.enemy)
    pink_ghost.set_kind(SpriteKind.enemy)
    orange_ghost.set_kind(SpriteKind.enemy)
    cyan_ghost.set_kind(SpriteKind.enemy)
    red_ghost.set_image(assets.image("""
        Red ghost
    """))
    pink_ghost.set_image(assets.image("""
        Pink Ghost
    """))
    orange_ghost.set_image(assets.image("""
        Orange ghost
    """))
    cyan_ghost.set_image(assets.image("""
        Cyan ghost
    """))
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap3)

def on_down_pressed():
    animation.run_image_animation(pacman, assets.animation("""
        PacMan Down
    """), 100, True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    game.game_over(False)
    game.splash(info.score())
    game.splash(info.high_score())
info.on_life_zero(on_life_zero)

orange_ghost: Sprite = None
cyan_ghost: Sprite = None
pink_ghost: Sprite = None
red_ghost: Sprite = None
pacman: Sprite = None
pacman = sprites.create(assets.image("""
    Pac-Man Right
"""), SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
tiles.place_on_tile(pacman, tiles.get_tile_location(15, 30))
pellets = 0
red_ghost = sprites.create(assets.image("""
    Red ghost
"""), SpriteKind.enemy)
pink_ghost = sprites.create(assets.image("""
    Pink Ghost
"""), SpriteKind.enemy)
cyan_ghost = sprites.create(assets.image("""
    Cyan ghost
"""), SpriteKind.enemy)
orange_ghost = sprites.create(assets.image("""
    Orange ghost
"""), SpriteKind.enemy)
Difficulty = game.ask_for_string("Difficulty (E, M, H)", 1)
Power_Pellet = sprites.create(assets.image("""
    PowerPellet
"""), SpriteKind.projectile)
Power_Pellet2 = sprites.create(assets.image("""
    PowerPellet
"""), SpriteKind.projectile)
Power_Pellet3 = sprites.create(assets.image("""
    PowerPellet
"""), SpriteKind.projectile)
Power_Pellet4 = sprites.create(assets.image("""
    PowerPellet
"""), SpriteKind.projectile)
Power_Pellet5 = sprites.create(assets.image("""
    PowerPellet
"""), SpriteKind.projectile)
Power_Pellet6 = sprites.create(assets.image("""
    PowerPellet
"""), SpriteKind.projectile)
tiles.place_on_tile(Power_Pellet, tiles.get_tile_location(1, 4))
tiles.place_on_tile(Power_Pellet2, tiles.get_tile_location(1, 29))
tiles.place_on_tile(Power_Pellet3, tiles.get_tile_location(15, 7))
tiles.place_on_tile(Power_Pellet4, tiles.get_tile_location(15, 24))
tiles.place_on_tile(Power_Pellet5, tiles.get_tile_location(30, 4))
tiles.place_on_tile(Power_Pellet6, tiles.get_tile_location(30, 29))
red_ghost.set_position(randint(50, 2000), randint(50, 2000))
red_ghost.set_bounce_on_wall(True)
pink_ghost.set_position(randint(50, 200), randint(50, 200))
pink_ghost.set_bounce_on_wall(True)
orange_ghost.set_position(randint(50, 2000), randint(50, 200))
orange_ghost.set_bounce_on_wall(True)
cyan_ghost.set_position(randint(50, 2000), randint(50, 200))
cyan_ghost.set_bounce_on_wall(True)
red_ghost.follow(pacman)
pink_ghost.follow(pacman)
orange_ghost.follow(pacman)
cyan_ghost.follow(pacman)
info.start_countdown(180)
game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
if Difficulty == "e":
    info.set_score(0)
    info.set_life(4)
    pacman.set_velocity(75, 75)
    red_ghost.set_velocity(50, 50)
    pink_ghost.set_velocity(50, 50)
    orange_ghost.set_velocity(50, 50)
    cyan_ghost.set_velocity(50, 50)
elif Difficulty == "m":
    info.set_score(0)
    info.set_life(2)
    pacman.set_velocity(50, 50)
    red_ghost.set_velocity(50, 50)
    pink_ghost.set_velocity(50, 50)
    orange_ghost.set_velocity(50, 50)
    cyan_ghost.set_velocity(50, 50)
elif Difficulty == "h":
    info.set_score(0)
    info.set_life(1)
    pacman.set_velocity(50, 50)
    red_ghost.set_velocity(75, 75)
    pink_ghost.set_velocity(50, 50)
    orange_ghost.set_velocity(50, 50)
    cyan_ghost.set_velocity(50, 50)
if pellets == 532:
    game.game_over(True)
    game.splash(info.score())
    game.splash(info.high_score())

def on_forever():
    scene.camera_follow_sprite(pacman)
    controller.move_sprite(pacman)
    game.set_game_over_effect(False, effects.melt)
    game.set_game_over_effect(True, effects.star_field)
    game.set_game_over_message(False, "YOU DIED")
    game.set_game_over_message(True, "YOU SURVIVED!")
forever(on_forever)
