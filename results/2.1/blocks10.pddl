

(define (problem BW-rand-10)
(:domain blocksworld)
(:objects b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 )
(:init
(arm-empty)
(on-table b1)
(on b2 b10)
(on-table b3)
(on-table b4)
(on-table b5)
(on b6 b1)
(on b7 b9)
(on b8 b4)
(on-table b9)
(on b10 b6)
(clear b2)
(clear b3)
(clear b5)
(clear b7)
(clear b8)
)
(:goal
(and
(on b1 b7)
(on b2 b6)
(on b3 b9)
(on b5 b4)
(on b6 b8)
(on b8 b5)
(on b9 b10)
(on b10 b2))
)
)


