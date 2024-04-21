import mp3player as mp3

s1 = mp3.Song('신호등', '이무진', 3)
s2 = mp3.Song('permission', '방탄소년단', 4)
s3 = mp3.Song('butter', '방탄소년단', 2)
s4 = mp3.Song('weekend', '태연', 5)
s5 = mp3.Song('좋아좋아', '조정석', 3)

player = mp3.Player()
player.addSong(s1)
player.addSong(s2)
player.addSong(s3)
player.addSong(s4)
player.addSong(s5)

player.setIsLoop(False)
player.shuffle()
player.play()