

(define (problem BW-rand-11)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 )
(:init
(arm-empty)
(on-table b1)
(on b2 b3)
(on-table b3)
(on b4 b1)
(on b5 b6)
(on b6 b2)
(on-table b7)
(on b8 b10)
(on b9 b4)
(on b10 b9)
(on-table b11)
(clear b5)
(clear b7)
(clear b8)
(clear b11)
)
(:goal
(and
(on b1 b9)
(on b2 b10)
(on b4 b3)
(on b5 b11)
(on b6 b5)
(on b7 b2)
(on b8 b1))
)
)


