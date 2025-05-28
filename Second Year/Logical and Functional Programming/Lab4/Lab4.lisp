;merge two sorted lists
;mymerge(l1: list, l2: list)
;mymerge(L1..Ln, M1..Mn) = M1..Mn if n = 0
;                         = L1..Ln if m = 0
;                         = L1 + mymerge(L2..Ln, M1..Mn) if L1 < M1
;                         = M1 + mymerge(L1..Ln, M2..Mn) otherwise
(defun mymerge (l1 l2)
    (cond ((null l1) l2)
          ((null l2) l1)
          ((< (car l1) (car l2)) (cons (car l1) (mymerge (cdr l1) l2)))
          (t (cons (car l2) (mymerge l1 (cdr l2))))))

;test
(print (mymerge '(1 3 5) '(2 4 6)))

;function to replace an element E with all elements of a list L1  at all levels of a given list L
;myreplace(E: integer, L1: list, L: list)
;myreplace(E, M1..Mn, L1..Ln) = nil if n = 0
;                              = myreplace(E, M1..Mn, L1) + myreplace(E, M1..Mn, L2..Ln) if L1 is a list
;                              = M1..Mn + myreplace(E, M1..Mn, L2..Ln) if L1 = E
;                              = L1 + myreplace(E, M1..Mn, L2..Ln) otherwise
(defun myreplace (e l1 l)
    (cond ((null l) nil)
            ((listp (car l)) (cons (myreplace e l1 (car l)) (myreplace e l1 (cdr l))))
            ((eql e (car l)) (append l1 (myreplace e l1 (cdr l))))
            (t (cons (car l) (myreplace e l1 (cdr l))))))

;test
(print (myreplace 2 '(7 8) '(1 2 (3 2))))
;test with letters
(print (myreplace 'a '(b c) '(a (a b) c)))

;reverse a list
;myreverse(L: list)
;myreverse(L1..Ln) = nil if n = 0
;                  = myreverse(L2..Ln) + L1 otherwise
(defun myreverse (l)
    (cond ((null l) nil)
          (t (append (myreverse (cdr l)) (list (car l))))))

;function to determine the sum of 2 numbers in list representation without transforming them into integers
;start from the least significant digit
;mysum(L1: number as list, L2: number as list)
(defun mysum (l1 l2)
    ;reverse the lists
    (setq l1 (myreverse l1))
    (setq l2 (myreverse l2))
    (auxmysum l1 l2 0))

;numbers are now reversed and we can add them digit by digit accounting for the carry
;auxmysum(L1..Lnr, M1..Mn, carry) = nil if n = 0, m = 0 and carry = 0
;                                 = carry if n = 0, m = 0
;                                 = auxmysum((0), M1..Mn, carry) if n = 0
;                                 = auxmysum(L1..Lnr, (0), carry) if m = 0
;                                 = auxmysum(L2..Lnr, M2..Mn, (L1 + M1 + carry)/10) U ((L1 + M1 + carry) mod 10) otherwise
(defun auxmysum (l1 l2 carry)
    (cond ((and (null l1) (null l2)) (if (= carry 0) nil (list carry)))
            ((null l1) (auxmysum (list 0) l2 carry))
            ((null l2) (auxmysum l1 (list 0) carry))
          (t (let ((sum (+ (car l1) (car l2) carry)))
             (append (auxmysum (cdr l1) (cdr l2) (truncate sum 10)) (list (mod sum 10)))))))



;test
(print (mysum '(9 2 4) '(1 8 6)))
          


;greatest common divisor with division
;mygcd(a: integer, b: integer)
;mygcd(a, b) = a if b = 0
;            = mygcd(b, a mod b) otherwise
(defun mygcd (a b)
    (cond ((= b 0) a)
          (t (mygcd b (mod a b)))))

;gcd of a list
;mygcdlist(L: list)
;mygcdlist(L1..Ln) = 1 if n = 0
;                   = L1 if n = 1
;                   = mygcd(L1, mygcdlist(L2..Ln)) otherwise
(defun mygcdlist (l)
    (cond ((null l) 1)
          ((null (cdr l)) (car l))
          (t (mygcd (car l) (mygcdlist (cdr l))))))

;test
(print (mygcdlist '(12 18 24)))

