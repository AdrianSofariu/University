; Write a function that removes all occurrences of an atom from any level of a list using map-functions

;removeAtom(i, o)
;removeAtom(list, atom)
;removeAtom(l,a) = [] if l = nil
;                = nil if l is an atom and l = a
;                = list(l) if l is an atom
;                = list(Union(removeAtom(l1,a), removeAtom(l2,a), ..., removeAtom(ln,a)) if l = (l1 l2 ... ln))
                  ;using an append we can avoid writing another function to remove the nil values left by the removed atom
(defun removeAtom (l a)
  (cond
    ((null l) nil)
    ((and (atom l) (equal l a)) nil)
    ((atom l) (list l))
    (T (list (apply #'append (mapcar #'(lambda (x) (removeAtom x a)) l))))
  )
)

;removeWrapper(i, o)
;removeWrapper(list, atom)
(defun removeWrapper (l a)
  (car (removeAtom l a))
)

(print (removeWrapper '(1 2 a (b c 2 (2))) 2))






