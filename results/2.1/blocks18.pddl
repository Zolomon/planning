

(define (problem BW-rand-18)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 )
(:init
(arm-empty)
(on b1 b6)
(on b2 b4)
(on b3 b12)
(on-table b4)
(on b5 b13)
(on b6 b10)
(on b7 b17)
(on b8 b9)
(on b9 b7)
(on b10 b11)
(on b11 b16)
(on-table b12)
(on b13 b2)
(on b14 b15)
(on b15 b3)
(on b16 b14)
(on-table b17)
(on b18 b1)
(clear b5)
(clear b8)
(clear b18)
)
(:goal
(and
(on b1 b15)
(on b2 b5)
(on b3 b7)
(on b5 b1)
(on b9 b10)
(on b10 b16)
(on b12 b11)
(on b13 b6)
(on b14 b8)
(on b17 b18)
(on b18 b13))
)
)

