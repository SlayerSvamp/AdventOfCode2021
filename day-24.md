# Day 24 in markdown

## explaining the instruction flow

### z is a stack

```sh
# push y to the stack
mul z 26
add z y

# pop the stack into x
add x z
mod x 26
div z 26
```

### instructions are divided into segments

```sh
# start of segment, reads input
inp w

# end of segment, writes y to z
add z y
```

### segment structure

the segments are always the same:

1. add the last pushed value to x and then add another value
1. `[div z]` is either followed by 1 (nothing happens) or 26 (the stack is popped)
1. read the input into w and compare with x
1. if x differs from w, push (w + a value) to the stack

if [div z 1] occurs: (push segment)  
the comparison is never equal, always resulting in a push

if [div z 26] occurs: (pop segment)  
the comparison is only not equal if the input is wrong  
(this is because all extra pushes leaves the stack with values left after the program is run to a halt)

---

## breaking down the instructions (my personal input)

### converting the instructions to pseudo code

```sh
# this is my input code, reduced by hand
push w + 13
push w + 10
push w + 5
expect pop - 11 == w
push w + 5
expect pop == w
push w + 4
push w + 11
push w + 1
expect pop - 6 == w
expect pop - 10 == w
expect pop - 12 == w
expect pop - 3 == w
expect pop - 5 == w
```

### converting pseudo code into element relations

all elements are essentially either:

- pushed to the stack (being a base value [a])
- expected to be a value that is a specified value higher or lower than a popped value (being a derived value [b])

this results in ranges which is relative to each other:  
for example:

```sh
# pseudo code, example from my code:
push w + 5
expect pop - 11 == w

# translating to base and relative values:
p3 = w + 5
p4 = p3 - 11

# simplifying the expressions
p3 = w
p4 = p3 - 6

# calculating ranges
p3 = 7:9 # 7 is lowest value to leave p4 at 1
p4 = 1:3 # 3 is highest value which will leave p3 at 9
```

### converting all my instructions, according to example above

```sh
# perform steps according to example

# translate to base and relative values
p1 = w + 13
p2 = w + 10
p3 = w + 5
p4 = p3 - 11
p5 = w + 5
p6 = p5
p7 = w + 4
p8 = w + 11
p9 = w + 1
p10 = p9 - 6
p11 = p8 - 10
p12 = p7 - 12
p13 = p2 - 3
p14 = p1 - 5

# simplifying the expressions
p1 = w
p2 = w
p3 = w
p4 = p3 - 6
p5 = w
p6 = p5 + 5
p7 = w
p8 = w
p9 = w
p10 = p9 - 5
p11 = p8 + 1
p12 = p7 - 8
p13 = p2 + 7
p14 = p1 + 8

# calculate possible ranges from relative elements
p1 = 1
p2 = 1:2
p3 = 7:9
p4 = 1:3
p5 = 1:4
p6 = 6:9
p7 = 9
p8 = 1:8
p9 = 6:9
p10 = 1:4
p11 = 2:9
p12 = 1
p13 = 8:9
p14 = 9

# assembled values, part 1 taking all highest possible values in ranges and lowest taking all lower values in ranges
```

---

## summing up

### part 1:

```sh
# by concatenating the high range digits, part 1 is produced
highest = 12934998949199
```

### part 2:

```sh
# by concatenating the low range digits, part 2 is produced
lowest = 11711691612189
```
