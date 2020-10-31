

type int_tree = Lf | Br of int * int_tree * int_tree


type author_type = {fname: string; sname: string}
type book_type = {author: author_type; name: string; year: int}


type const = True | False
type bool_expr =
 | Const of const
 | Var of string
 | Not of bool_expr
 | And of bool_expr * bool_expr
 | Or of bool_expr * bool_expr

exception UndefinedVariable of string

(*type letlang_expr = 
  Const of int
  | Var of string
  | Let of string * letlang_expr * letlang_expr *)

(*Напишите функцию is_positive: int list -> bool, которая принимает список целых чисел
и возвращает true, если все числа в нём положительные, 
и false в противном случае. Для пустого списка возвращайте true. *)
let rec is_positive ls = 
   match ls with
   [] -> true
   | head::tail -> if head > 0 then is_positive tail else false;;
   
 (*Напишите функцию is_sorted: int list -> bool, которая принимает список целых чисел и возвращает true, 
 если он отсортирован в порядке неубывания, и false в противном случае. Пустой список считайте отсортированным и возвращайте для него true.*)
 let rec is_sorted ls =
  match ls with
  [] -> true
  | [head] -> true
  | first::second::tail -> if first > second then false else is_sorted (second::tail);;
  
 (* Напишите функцию count_branches: int_tree -> int, которая принимает корень дерева и возвращает количество внутренних узлов (ветка Br) в этом дереве.*)
 let count_branches tree = 
  let rec count (tree, c) = 
    match tree with
      Lf -> 0
      | Br (i, br1, br2) -> c + 1 + count(br1, 0) + count(br2, 0)
    in count(tree, 0) ;;
	
 (* Напишите функцию depth: int_tree -> int, которая принимает корень дерева и возвращает его максимальную глубину (depth Lf должно вернуть 0).*)
 let depth tree = 
  let rec deep (tree, d) =
    match tree with
    Lf -> 0
    | Br(i, br1, br2) -> d + 1 + max (deep(br1, 0)) (deep(br2, 0))
   in deep (tree, 0);;
   
 (* Напишите функцию gen_tree: int -> int_tree, которая получает целое число n и возвращает корень дерева следующего вида (пример для gen_tree 3): *)
 let rec gen_tree n =
   match n with
   0 -> Lf
   |n -> Br(n, Lf, gen_tree (n - 1)) ;;
   
 (* Напишите функцию inorder: int_tree -> int list, которая получает корень дерева и возвращает список значений из узлов в порядке “левое поддерево - корень - правое поддерево”*)
 let rec inorder tree = 
  match tree with
  Lf -> []
  | Br(i, br1, br2) -> (inorder br1) @ [i] @ (inorder br2);;
  
  (* Напишите функцию preorder: int_tree -> int list, которая получает корень дерева и возвращает список значений из узлов в порядке “корень - левое поддерево - правое поддерево”*)
  let rec preorder tree = 
	  match tree with
	  Lf -> []
	  | Br(i, br1, br2) -> [i] @ (preorder br1) @ (preorder br2);;
	  
  (* Напишите функцию search_book: key -> book_type list -> book_type list, которая принимает ключевое слово и список книг, 
  и возвращает список книг, в названии которых содержится ключевое слово, либо ключевое слово совпадает с именем или фамилией автора. 
  Ищите полным совпадением, для деления названия книги на слова используйте функцию String.split_on_char. 
  Считайте, что в названии нет знаков препинания, кроме пробела.*)
  let rec search_book key lst = 
    match lst with
    [] -> []
    | hd::tail -> if hd.author.fname <> key && hd.author.sname <> key 
      then 
        if
          let rec search (key, word_lst) =
            match word_lst with
            [] -> false
            | word::word_tail -> if word = key then true else search (key, word_tail)
          in search(key, String.split_on_char ' ' (hd.name))
         then hd :: search_book key tail
         else search_book key tail
      else hd :: search_book key tail;;
  
  
(*Напишите функцию simplify: bool_expr - > bool_expr, которая упрощает логическое выражение, применяя следующие правила:
And (False, bool_expr e) == False
And (True, bool_expr e) == bool_expr e
Or (True, bool_expr e) == True
Or (False, bool_expr e) = bool_expr e
Не забудьте учесть коммутативность.  *)
let rec simplify expr =
    match expr with
    | Const i -> Const(i)
    | Var str -> Var str
    (* | Not exp -> if (simplify exp) = Const(True) then Const(False) else Const(True) *)
    | Not (exp) -> Not (simplify exp)
    | And (e1, e2) -> if e1 = Const(True) 
                      then simplify e2 
                      else if e2 = Const(True)  then simplify e1
                           else if e1 = Const(False) || e2 = Const(False) 
                                then Const(False) 
                                else And ((simplify e1), (simplify e2))
    | Or (e1, e2) -> if e1 = Const(True)  || e2 = Const(True)  
                     then Const(True) 
                     else if e1 = Const(False) 
                          then simplify e2
                          else if e2 = Const(False)
                               then simplify e1
                               else Or ((simplify e1), (simplify e2));;
							   
(* Напишите функцию lookup: string -> (string * letlang_expr) list -> letlang_expr option, 
которая принимает имя переменной var в виде строки и окружение в виде списка пар (name, value). 
Функция должна возвращать None, если в списке нет связывания для имени var, и Some v, если пара (var, v) - первая в списке. *)							   

(* let rec lookup str ls = 
   let rec find_in ls = 
    match ls with
    [] -> None
    | (name, value)::tl -> if str = name 
                           then Some value 
                           else let rec func v = 
                                match v with
                                  Const v -> find_in tl
                                  | Let(name, e1, e2) -> if name = str then Some value
                                                         else 
                           
  in find_in ls;;
  
assert((lookup "x" []) = None);;
assert((lookup "x" [("x", Const 15)]) = Some (Const 15));;
assert((lookup "x" [("x", Const 15); ("x", Const 14)]) = Some (Const 15));;
(lookup "x" [("x", Let("y", Const 15, Var "y")); ("x", Const 14)]);;
assert((lookup "x" [("x", Let("y", Const 15, Var "y")); ("x", Const 14)]) = Some (Const 14));; *)

(* Too difficult for me*)