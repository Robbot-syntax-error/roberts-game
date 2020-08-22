import cx_Freeze

executables = [cx_Freeze.Executable("SUPER_GAME")]

cx_Freeze.setup(
    name="The Jungle",
    options={"build_exe": {"packages":["pygame"],
               "include_files":["ammo.png", "background.png", "BIG BOSS.png","bullet.png",
                                 "DEHYRADTION2.png", "explosion.png", "fireball backward.png", "fireball forward.png", "fireball down.png", "floor.png", "flyingmonster.png", "grenade.png", "laser facing left.png", "laser facing upward.png", "next level.WAV", "player crouch backward.png",
                                 "player crouch forward.png", "shooter backwards.png", "shooter forward.png", "shooter down.png", "small boss.png", "SPIKE.png", "start.png", "transparent.png", "walking monster.png", "you died.png"]}},
    executables = executables
    
    )
