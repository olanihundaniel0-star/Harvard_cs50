# CS Fundamentals Notes

## 1. Binary & Data Representation

### Bits
- **Bit** = binary digit (0 or 1)
- All computers use binary — `0` = off/low, `1` = on/high
- **Transistors** are the most elementary components in a computer, outputting either 0 or 1

### Bytes
- A **byte** is the standard unit for counting data (0–255, i.e. 8 bits)
- Example: weights of base-2 system illustrated with 3 light bulbs → counts 0 to 7

### Characters & Text
- Computers store letters by assigning numerical values to them → **ASCII codes**
  - 7-bit system, ranges from 0–127
  - Example: `65 = 'A'`
  - Includes letters, numbers, and special characters
- **Unicode** uses a larger bit system and can represent a wider range of characters, including emojis

### Colours
- Colours are represented using a **256-value (8-bit) system** per channel
- Uses the **RGB model** (Red, Green, Blue)
- Example: `HI!` → dark yellow (rendered as an RGB colour)

---

## 2. Algorithms

- An algorithm is a **process between inputs and output**
- Must be **fast, accurate, and efficient** — not just any solution
- Should account for **edge cases** (e.g. using `else` in Python to handle unexpected inputs)

### Example — Phonebook Search
- Naively searching page by page is slow
- Tearing the phonebook in half each time (binary search) drastically reduces steps
- Illustrated on a **size/complexity vs. time graph**

---

## 3. Code

- Code is simply a **language used to communicate a process (algorithm) to a computer**

### Pseudocode
- A **human-readable representation** of an algorithm
- Not actual code — used for planning logic before implementation

### Example
// Pseudocode
Input name from user
Say "Hello, " + name


- A stream of 0s and 1s at the machine level can represent instructions like printing `"Hello, World!"`

---

## 4. Scratch

- Visual programming environment where **puzzle pieces = functions**
- White input boxes = **arguments/parameters**
- The **output/result of a function** is called a side-effect

### Example — Greet User
when green flag clicked
ask "What is your name?" and wait
say (join "Hello, " (answer))



