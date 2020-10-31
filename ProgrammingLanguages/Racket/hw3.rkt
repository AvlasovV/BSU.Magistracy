#lang racket

(provide (all-defined-out))


;(1) Напишите функцию list-nth-mod, которая принимает список xs и число n.
;Если n отрицательное, остановите выполнение с (error "list-nth-mod: negative number").
;Если список пустой, остановите выполнение с (error "list-nth-mod: empty list").
;Иначе, верните i-й элемент списка, где i - остаток от деления n на длину исходного списка.
;Подсказка: библиотечные функции length, remainder, car, list-tail могут здесь пригодиться.

(define (list-nth-mod xs n)
  (cond [ (< n 0) error "list-nth-mod: negative number"]
        [( = (length xs) 0) error "list-nth-mod: empty list"]
        [#t (car (list-tail xs (remainder n (length xs))))]))


;(1) Напишите функцию stream-for-n-steps, которая принимает стрим s и число n,
;и возвращает список из первых n значений, порождённых стримом. Считайте, что n неотрицательное.  
(define (stream-for-n-steps s n)
  (if (= n 0)
      ('())
      (cons (car (s))(stream-for-n-steps (cdr (s)) (- n 1)))))


;(1) Напишите функцию skip-first-n, которая принимает стрим s и число n, и возвращает стрим,
;генерирующий элементы исходного стрима, начиная с n+1 по счёту.
(define (skip-first-n s n)
  (if (> n 0)
      (skip-first-n (cdr (s)) (- n 1))
      s))
