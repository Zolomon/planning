

(define (problem BW-rand-14)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 )
(:init
(arm-empty)
(on b1 b7)
(on-table b2)
(on b3 b10)
(on b4 b6)
(on-table b5)
(on b6 b11)
(on-table b7)
(on-table b8)
(on b9 b1)
(on b10 b8)
(on b11 b12)
(on b12 b9)
(on b13 b3)
(on-table b14)
(clear b2)
(clear b4)
(clear b5)
(clear b13)
(clear b14)
)
(:goal
(and
(on b1 b11)
(on b4 b12)
(on b6 b8)
(on b7 b5)
(on b8 b4)
(on b9 b2)
(on b10 b14)
(on b11 b7)
(on b12 b1)
(on b14 b9))
)
)

