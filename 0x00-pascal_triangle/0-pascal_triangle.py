def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the first row of Pascal's Triangle
    triangle = [[1]]

    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]
        # Start the new row with a '1'
        new_row = [1]

        # Compute the values in between the edges
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        # End the new row with a '1'
        new_row.append(1)
        # Add the new row to the triangle
        triangle.append(new_row)

    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(", ".join([str(x) for x in row])))

if __name__ == "__main__":
    # Example: Print Pascal's Triangle with 5 rows
    print_triangle(pascal_triangle(5))
    def main():
        # Example: Print Pascal's Triangle with 5 rows
        print_triangle(pascal_triangle(5))

    if __name__ == "__main__":
        main()
