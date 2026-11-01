# Computer Architecture: Direct-Mapped Cache Simulation

number_of_lines = 8
access_sequence = [3, 11, 3, 19, 11, 27, 3]

cache = [None] * number_of_lines
hits = 0
misses = 0

print("Block  Line  Result  Cache contents (line: block)")
print("-" * 58)

for block in access_sequence:
    line = block % number_of_lines

    if cache[line] == block:
        result = "HIT"
        hits += 1
    else:
        result = "MISS"
        misses += 1
        cache[line] = block

    contents = ", ".join(
        f"{i}: {value}"
        for i, value in enumerate(cache)
        if value is not None
    )

    if not contents:
        contents = "Empty"

    print(f"{block:<6} {line:<5} {result:<7} {contents}")

total_accesses = len(access_sequence)
hit_ratio = hits / total_accesses

print("\nTotal hits:", hits)
print("Total misses:", misses)
print(
    f"Hit ratio: {hits}/{total_accesses} = "
    f"{hit_ratio:.2f} ({hit_ratio * 100:.1f}%)"
)
