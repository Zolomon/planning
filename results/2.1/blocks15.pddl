

(define (problem BW-rand-15)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 )
(:init
(arm-empty)
(on-table b1)
(on-table b2)
(on b3 b7)
(on b4 b8)
(on b5 b15)
(on b6 b14)
(on b7 b6)
(on-table b8)
(on-table b9)
(on b10 b2)
(on b11 b3)
(on b12 b5)
(on b13 b11)
(on-table b14)
(on b15 b10)
(clear b1)
(clear b4)
(clear b9)
(clear b12)
(clear b13)
)
(:goal
(and
(on b2 b14)
(on b3 b8)
(on b4 b10)
(on b5 b9)
(on b6 b3)
(on b7 b13)
(on b8 b2)
(on b9 b1)
(on b10 b6)
(on b11 b12)
(on b12 b7)
(on b13 b15)
(on b15 b4))
)
)

