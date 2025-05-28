;Write recursive Lisp functions for the following problems (optionally, you may use MAP functions):
;A binary tree is memorised in the following two ways:
;(node no-subtrees list-subtree-1 list-subtree-2 ...) (1)
;(node (list-subtree-1) (list-subtree-2) ...) (2)
;As an example, the tree
;A
;/ \
;B C
; / \
;D E
;is represented as follows:
;(A 2 B 0 C 2 D 0 E 0) (1)
;(A (B) (C (D) (E))) (2)

;9. Convert a tree of type (1) to type (2)

;function to get the left subtree
;getLeft(tree: list, vertices: integer, edges: integer)
;getLeft(l1..ln, vertices, edges) = nil if n = 0
;                                 = nil if vertices = edges + 1
;                                 = l1 + l2 + getLeft(l3..ln, vertices + 1, edges + l2) otherwise
(defun getLeft (tree vertices edges)
    (cond
        ((null tree) nil)
        ((= vertices (+ 1 edges)) nil)
        (t (cons (car tree) (cons (cadr tree) (getLeft (cddr tree) (+ 1 vertices) (+ (cadr tree) edges)))))
    )
)

;left subtree wrapper
(defun left (tree)
    (getLeft (cddr tree) 0 0)
)


;function to get the right subtree
;getRight(tree: list, vertices: integer, edges: integer)
;getRight(l1..ln, vertices, edges) = nil if n = 0
;                                  = l1..ln if vertices = edges + 1
;                                  = getRight(l3..ln, vertices + 1, edges + l2) otherwise
(defun getRight (tree vertices edges)
    (cond
        ((null tree) nil)
        ((= vertices (+ 1 edges)) tree)
        (t (getRight (cddr tree) (+ 1 vertices) (+ (cadr tree) edges)))
    )
)

;right subtree wrapper
(defun right (tree)
  (getRight (cddr tree) 0 0)
)


;function to convert the tree
;convert(l: list)
;convert(l1..ln) = nil if n = 0
;                = l1 + convert(left(l1..ln)) + convert(right(l1..ln)) otherwise
(defun convert (l)
    (cond
        ((null l) nil)
        (t (list (car l) (convert (left l)) (convert (right l))))
    )
)

;function to eliminate the nils in a non-linear list
;eliminateNils(l: list)
;eliminateNils(l1..ln) = nil if n = 0
;                      = eliminateNils(l2..ln) if l1 = nil
;                      = eliminateNils(l1) + eliminateNils(l2..ln) if listp(l1)
;                      = l1 + eliminateNils(l2..ln) otherwise
(defun eliminateNils (l)
    (cond
        ((null l) nil)
        ((null (car l)) (eliminateNils (cdr l)))
        ((listp (car l)) (cons (eliminateNils (car l)) (eliminateNils (cdr l))))
        (t (cons (car l) (eliminateNils (cdr l))))
    )
)

;function to convert the tree (wrapper)
(defun convertw (l)
    (eliminateNils (convert l))
)

;Test
(convertw '(A 2 B 0 C 2 D 0 E 0)) ; (A (B) (C (D) (E)))


