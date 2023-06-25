Clock.bpm=70
Scale.default = 'minorPentatonic'
var.cho=var([0,-2,-4,-3],8)

p1 >> piano(P[var.cho, [4,7],6,4].stutter(2).layer('mirror'), pan=(-1,1), room=2, mix=0.50, dur=var([1/2,1],[6,2]), amp=PWhite(0.6,1.2), oct=(3,[4,5])) + [0,1,2,4,2]
p2 >> sawbass([6,2,4,0], dur=2, oct=6, amp=PWhite(0.7,1.2), room=1, mix=0.20).penta().spread()
p1.stop()
p2.stop()

k1 >> bell(dur=8, room=1, mix=0.50)
b1 >> bass(var.cho, dur=8, amp=0.70, room=1, mix=0.50)
k1.stop()
b1.stop()

d1 >> play('x[::][xx]=', crush=5).every(4, 'amen')
p2 >> viola(var.cho, dur=8, amp=0.8, mix=1, room=0.50)
d1.stop()
p2.stop()

s2 >> saw(P[4,6,7][:6], dur=PDur(3,8)*2, amp=1, sus=3).every(8, 'offadd', 4).every(6, 'stutter', 4, dur=3, pan=[-1,1], oct=3)
s2.stop()
