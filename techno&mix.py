Clock.bpm=144; Root.default =- 1; Scale.default="minorPentatonic"
var.cho=var([0,-2,-4,-3],8)
b1 >> bass(dur=1/4, formant=PRand(8)[:8], rate=PRand(5,10)[:8], pan=PWhite(-1,1))
b1.stop()
cp >> play("* ")
cp.stop()
d1 >> play(P["V::"][:16] & P["<v ><  |o1| >"], drive=0.1, rate=1.2)
d1.stop()

b2 >> sawbass(var([0,5,2,[3,6]],[8,6,1,1]), dur=PDur(3,8)).spread()
b2.stop()
p2 >> pasha(var.cho, dur=8, amp=0.8, mix=1, room=0.50)
p2.stop()
s2 >> saw(P[4,6,7][:6], dur=PDur(3,8)*2, amp=1, sus=3).every(8, 'offadd', 4).every(6, 'stutter', 4, dur=3, pan=[-1,1], oct=5)
s2.stop()
k1 >> bell(dur=8, room=1, mix=0.50)
k1.stop()
s3 >> prophet(P[4,6,7][:6], dur=PDur(3,8)*2, amp=1, sus=3).every(8, 'offadd', 4).every(6, 'stutter', 4, dur=3, pan=[-1,1], oct=4)
s3.stop()
a1 >> dab(dur=7).unison(4, 0.50)
a1.stop()

#2nd

Clock.bpm=130
Root.default = 4
Scale.default.set("harmonicMinor")


a1 >> pads(P[(2,3,4,5,3,1,5,4,3,1,7,5,8,2,3,4)], dur=0.25, chop=2, room=1, mix=0.3, amp=1)
a1.stop()
b2 >> dab(dur=8).unison(8, 0.50)
b2.stop()

a2 >> pasha(P[(2,6,8,7,7,4,9,7,5,4,9,7,10,4,5,6)], dur=0.25, chop=2, room=2, mix=0.3, amp=1)
a2.stop()
a3 >> prophet(oct=(3,2), shape=(0.8, 0.4), amp=(3, 0.7))
a3.stop()

b1 >> dbass(P(0,4,7), dur=4, amp=0.20, formant=P[1,5,2,4,3], lpf=700)
b1.stop()

#d&p
d1 >> play("[Is]d^~", chop=2, dur=0.5, room=0.2, mix=0.4, hpf=1000, lpf=4000, pshift=[0, (5,0,10)])
d1.stop()
d2 >> play("Xsi[rx]", chop=2, dur=1, room=0.0001, mix=0.1, hpf=300, pshift=[0, (5,0,10)], echo=0.75, amp=0.5)
d2.stop()
p1 >> play("-", dur=0.25, vpshift=[0, (0,5,10)])
p1.stop()
p2 >> play("X", dur=1, amp=2)
p2.stop()

d_all.stop()
p_all.stop()

Scale.default="minor"; Clock.bpm=140
d1 >> play("G(:-)", rate=-1/2, pshift=var([0,3],[6,2])+(0.1,0), pan=(-1,1), room=1, amp=2)
d1.stop()
d2 >> play("x-", sample=2).sometimes("stutter", 4, dur=3)
d2.stop()
d3 >> play("  I ", sample=2, hpf=(0,2000), lpf=(300,0), hpr=0.5)
d3.stop()
b1 >> dbass(var([0,6,5,2],[6,2]), dur=PDur(3,8,[0,2]), sus=2, chop=4, rate=4)
b1.stop()

p2 >> marimba([0,1,[[3,4],2]], dur=[4,3,1], drive=PWhite(0.2,0.7), oct=6, lpf=2000, room=1/2, echo=0.75, echotime=6, sus=1).penta().spread()
p2.stop()
k1 >> gong(oct=5, lpf=200, lpr=0.5)
k1.stop()

d4 >> play("---", sample=2).sometimes("stutter", 4, dur=3)
d4.stop()
p3 >> keys([0,1,[[3,4],2]], dur=[4,3,1], drive=PWhite(0.2,0.7), oct=6, lpf=2000, room=1/2, echo=0.75, echotime=6, sus=1).penta().spread()
b2 >> piano(var([0,6,5,2],[6,2]), dur=PDur(3,8,[0,2]), sus=2, chop=4, rate=4)
p3.stop()
b2.stop()
print.SynthDefs()





