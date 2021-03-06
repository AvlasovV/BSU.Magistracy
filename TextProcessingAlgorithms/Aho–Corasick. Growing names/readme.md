﻿### Растущие названия
Имя входного файла: input.txt\
Имя выходного файла: output.txt\
Ограничение по времени: 1 с\
Ограничение по памяти: 256 МБ\
Метрополитен города χ имеет богатую историю, неразрывно связанную с историей города и страны в целом. Шли годы, менялись эпохи, менялись правители, менялся уклад жизни, приоритеты, пересматривался взгляд на исторические события и одновременно с этим переименовывались станции метро.

Иногда так получалось, что название станции не менялось полностью, а удлинялось, расширялось. Т. е. в этом случае новое название включало в себя старое. Например, одна из станций метро называлась изначально «Метростроителей», а после переименования получила название «Метростроителей им. Бещенко» (в честь одного из городских общественных деятелей, многое сделавшего для развития метро).

Проследите историю названий отдельно взятой станции. Специалисты-метрологи (изучающие историю и современность метрополитена города χ) утверждают, что это название много раз удлинялось, и просят вас определить, какой максимальной длины может быть цепочка из растущих названий.

Вам дано n различных названий станции в разные годы в произвольном порядке. Попробуйте выбрать некоторые названия и упорядочить их так, чтобы в полученной последовательности каждое следующее название содержало в себе предыдущее в качестве подстроки. Определите, какую максимальную длину может иметь такая последовательность. Разумеется, в последовательности названия не могут повторяться.

Формат входных данных\
В первой строке записано целое число n (1 ≤ n ≤ 10 000). Далее следуют n строк, каждая длиной от 1 до 1000 символов. Строки состоят только из строчных латинских букв и попарно различны. Общая длина всех строк не превосходит 1 000 000.

Формат выходных данных\
Выведите одно число — размер самой длинной последовательности растущих названий, которую можно составить.

#### Примеры
**input.txt**	\
7\
metrostroitelei\
metro\
beschenko\
stroi\
metrostroitel\
stroitel\
metr

**output.txt**\
4

#######################

**input.txt**	\
2\
abcd\
bc

**output.txt**\
2