(define (domain wumpus)
  (:requirements :adl :typing)
  (:types tile agent wumpus pit gold arrow)
  (:predicates (alive ?entity)
					(have ?entity ?obj)
					(position ?obj ?tile)
					(adjacent ?t1 - tile ?t2 - tile)					
					(pit ?tile - tile))

  (:action move
    :parameters (?entity - agent
                 ?source - tile
                 ?destination - tile)
    :precondition (and (position ?entity ?source)
                       (adjacent ?source ?destination)
                       (alive ?entity))
    :effect (and (not (position ?entity ?source))
					  (position ?entity ?destination)
					  ;; If we walk into a pit, then we die.
					  (when (exists (?p - pit) (position ?p ?destination))
					  		 (not (alive ?entity)))
					  ;; If we walk into an alive wumpus at our destination, then we die.
					  (when (exists (?w - wumpus) (and (position ?w ?destination)
																  (alive ?w)))
					  		 (not (alive ?entity)))))

  ;; Grab some gold or arrows, if we are alive at the same tile that
  ;; the thing is, we can grab it.
  (:action take
    :parameters (?entity - agent
                 ?location - tile
                 ?obj)
    :precondition (and (position ?entity ?location)
                       (position ?obj ?location)
                       (alive ?entity))
    :effect (and (have ?entity ?obj)
                 (not (position ?obj ?location))))

  (:action fire-arrow
    :parameters (?entity - agent
                 ?location - tile
                 ?arrow - arrow
					  ?victim - wumpus
					  ?location-victim - tile)
    :precondition (and (alive ?entity)
                       (have ?entity ?arrow)
                       (position ?entity ?location)
                       (alive ?victim)
                       (position ?victim ?location-victim)
                       (adjacent ?location ?location-victim))
    :effect (and (not (alive ?victim))
                 (not (position ?victim ?location-victim))
                 (not (have ?entity ?arrow))))
)
