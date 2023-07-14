"""
HW:11[Volkov Anton].

Write a generator function that takes a range value and chunk_size as input
and produces output as lists with length equal to the chunk size.
Example:
Call: chunk_generator(range(11), chunk_size=3)
Output:
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
[9, 10]
"""


def chunk_generator(range_value, chunk_size):
    """Iterate over range value and store i in list of length chunk_size."""
    part = []
    for i in range(range_value):
        part.append(i)
        # Save our "part" result + create new "part" if len(part) == chunk_size
        if len(part) == chunk_size:
            yield part
            part = []
    # Save our final part result if len(part) < chunk_size
    if part:
        yield part


# Call chunk_generator function and save result in "result_chunk_generator"
result_chunk_generator = chunk_generator(11, 3)
# Print parts from result
for parts in result_chunk_generator:
    print(parts)
