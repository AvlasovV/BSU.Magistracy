#lang racket
;Напишите функцию sequence, которая принимает аргументы low,
;high (целые числа) и step (положительное число).
;Функция sequence должна возвращать список чисел
;от low до high с шагом step.
(define (sequence low high step)
  (if (<= low high)
      (cons low (sequence (+ low step) high step))
      null
  )
)


;Напишите функцию string-append-map, которая принимает список строк xs и строку suffix,
;и возвращает список новых строк, присоединив к каждой строке исходного списка
;строку suffix (без пробелов между строкой и суффиксом).
;Используйте библиотечные функции map и string-append.
(define (string-append-map xs suffix)
  (if (null? xs)
      null
      (cons (string-append (car xs) suffix) (string-append-map (cdr xs) suffix))
  )
)



;Рассмотрим вложенный список, похожий на тот, что рассмотрен выше,
;но кроме чисел допускаются элементы другого типа.
;[UPD!] Напишите функцию sum-indifferent, которая принимает такой список
;и суммирует все элементы-числа из этого списка.
(define (sum-indifferent xs)
  (cond [(null? xs) 0]
        [(number? (car xs)) (+ (car xs) (sum-indifferent (cdr xs)))]
        [(nor (number? (car xs)) (list? (car xs))) (sum-indifferent (cdr xs))]
        [#t (+ (sum-indifferent (car xs)) (sum-indifferent (cdr xs)))]
        )
)

;Напишите функцию flatten, которая принимает вложенный список
;и возвращает "плоский" список из тех же элементов. Используйте функции append и list.
(define (flatten xs)
(cond [(null? xs) null]
      [(not (list? xs)) (list xs)]
      [#t (append (flatten (car xs)) (flatten (cdr xs)))])
 )

;Напишите функцию duplicate, которая принимает список и возвращает такой список,
;в котором все элементы продублированы.
(define (duplicate xs)
  (cond [(null? xs) null]
        [#t (cons (car xs) (cons (car xs) (duplicate (cdr xs))))])
)

;Test part

(sequence 1 5 1)
(sequence 1 5 2)
(sequence 1 5 6)
(sequence 1 0 1)

(string-append-map (list "1" "2" "3") "ab")
(string-append-map null "ab")

(sum-indifferent (list 2 (list 4 5) (list (list 1 2) (list 6)) 19 (list 14 0)))
(sum-indifferent (list "a" (list 4 5) (list (list 1 2) (list 6)) 19 (list 14 0)))
(sum-indifferent (list 2 (list "a" "b") (list (list 1 2) (list 6)) 19 (list 14 0)))

(flatten (list "a" (list 4 5) (list (list 1 2) (list 6)) 19 (list 14 0)))
(flatten (list 2 (list 4 5) (list (list 1 2) (list 6)) 19 (list 14 0)))

(duplicate (list "a" "b"))