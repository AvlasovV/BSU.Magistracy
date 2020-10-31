open Hw1;;

(* is_positive: int list -> bool *)
assert(is_positive [] = true);;
assert(is_positive [4] = true);;
assert(is_positive [4; -1] = false);;
assert(is_positive [1; 2; 3; 4] = true);;
assert(is_positive [-1; 2; 3; 4] = false);;
assert(is_positive [1; 2; 3; -4] = false);;
assert(is_positive [0; 0; 3; 4] = false);;
assert(is_positive [] = true);;
assert(is_positive [-1] = false);;
assert(is_positive [1] = true);;

(* is_sorted: int list -> bool *)
assert(is_sorted [] = true);;
assert(is_sorted [4] = true);;
assert(is_sorted [4; -1] = false);;
assert(is_sorted [1;2;3;4] = true);;
assert(is_sorted [1;0;2;4] = false);;
assert(is_sorted [1;1;2;4] = true);;
assert(is_sorted [1;4;3] = false);;
assert(is_sorted [1] = true);;
assert(is_sorted [1,2] = true);;
assert(is_sorted [2;1] = false);;

(*count_branches: int_tree -> int *)
assert(count_branches Lf = 0);;
assert(count_branches (Br(1, Lf, Lf)) = 1);;
assert(count_branches (Br(1, Br(2, Br(1, Lf, Lf), Lf), Lf)) = 3);;
assert(count_branches (Br(1, Br(2, Br(1, Lf, Lf), Lf), Br(1,Br(2,Br(0, Lf, Lf), Lf), Lf))) = 6);;

(* depth: int_tree -> int *)
assert(depth (Br(1, Br(2, Br(1, Lf, Lf), Lf), Br(1,Br(2,Br(0, Lf, Lf), Lf), Lf))) = 4);;
assert(depth Lf = 0);;
assert(depth (Br(1, Lf, Lf)) = 1);;


(* gen_tree: int -> int_tree *)
assert(gen_tree 2 = Br(2, Lf, Br(1, Lf, Lf))) ;;
assert(gen_tree 0 = Lf);;
assert(gen_tree 1 = Br(1, Lf, Lf));;

(* inorder: int_tree -> int list *)
assert(inorder(Br(1, Lf, Lf))  = [1]);;
assert(inorder (Lf) = []);;
assert(inorder (Br(2, Lf, Br(1, Lf, Lf))) = [2;1]);;
assert(inorder (Br(1, Br(2, Br(7, Lf,Br(3, Lf, Lf)), Br(8,Lf,Lf)), Br(4,Br(5,Br(0, Lf, Lf), Lf), Lf)))
= [7;3;2;8;1;0;5;4]);;

(* preorder: int_tree -> int list *)
assert(preorder(Br(1, Lf, Lf))  = [1]);;
assert(preorder (Br(2, Lf, Br(1, Lf, Lf))) = [2;1]);;
assert(preorder (Br(1, Br(2, Br(7, Lf,Br(3, Lf, Lf)), Br(8,Lf,Lf)), Br(4,Br(5,Br(0, Lf, Lf), Lf), Lf))) = [1;2;7;3;8;4;5;0]);;


(* search_book: key -> book_type list -> book_type list *)
assert(search_book "hello" [] = []);;      
search_book "hello" [
{author = {fname =  "hello"; sname = "bye"}; name = "123 hello"; year = 1};
{author = {fname =  "hello"; sname = "bye"}; name = "123"; year = 1};
{author = {fname =  "1qwqqw"; sname = "hello"}; name = "ssdcshello"; year = 1};
{author = {fname =  "2hello"; sname = "bye"}; name = "123 hell dfdf hello 1"; year = 1};
{author = {fname =  "hello3"; sname = "bye"}; name = "123hello"; year = 1}];;

(* simplify: bool_expr - > bool_expr *)
assert(simplify(Const(True)) = Const(True));;
assert(simplify(And(Const(True), Const(False))) = Const(False));;
assert(simplify(Or(Const(True), Const(False))) = Const(True));;
assert(simplify(Or(Var("123"), Var("123"))) = Or(Var("123"), Var("123")));;
assert(simplify(Or(Var("123"), Const(False))) = Var("123"));;
assert(simplify(Not(Or(Const(True), Const(False)))) = Not(Const(True)));;
assert(simplify(Not(Var "123")) = Not(Var "123"));;
assert(simplify(Not(Not(Not(Const(True))))) = Not(Not(Not(Const(True)))));;
simplify(Or(Not(Not(Not(Const(True)))), Not(Var "123"))) ;;(* It's funny *)

(* lookup: string -> (string * letlang_expr) list -> letlang_expr option *)
(*
assert((lookup "x" []) = None);;
assert((lookup "x" [("x", Const 15)]) = Some (Const 15));;
assert((lookup "x" [("x", Const 15); ("x", Const 14)]) = Some (Const 15));;

(* eval: letlang_expr -> letlang_expr *)

let e1 = Const 42;;
let e2 = Var "x";;
let e3 = Let("y", Const 15, Var "y");;
let e4 = Let("y", Const 15, Let("y", Const 14, Var "y"));;

assert((eval e1) = (Const 42));;
assert(try ignore((eval e2)); false with
        | UndefinedVariable v -> (v = "x")
        | _ -> false);;

assert((eval e3) = Const(15));;
assert((eval e4) = Const(14));; *)


Printf.printf "All Tests passed!\n"
