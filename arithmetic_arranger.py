def arithmetic_arranger(problems, show_result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for problem in problems:
        components = problem.split()

        if len(components[0]) > 4 or len(components[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not components[0].isdigit() or not components[2].isdigit():
            return "Error: Numbers must only contain digits."

        if components[1] != '+' and components[1] != '-':
            return "Error: Operator must be '+' or '-'."

        # Determining the length of the longest operand
        max_len = max(len(components[0]), len(components[2]))

        # Forming the first line
        line1 += components[0].rjust(max_len + 2)
        line1 += "    "

        # Forming the second line
        line2 += components[1] + " " + components[2].rjust(max_len)
        line2 += "    "

        # Forming the third line
        line3 += "-" * (max_len + 2)
        line3 += "    "

        # forming the fourth line (if requested)
        if show_result:
            result = str(eval("".join(components)))
            line4 += result.rjust(max_len + 2)
            line4 += "    "

    # Removing the trailing spaces from each line
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    if show_result:
        line4 = line4.rstrip()

    # Combining the lines into a single string
    arranged_problems = line1 + "\n" + line2 + "\n" + line3
    if show_result:
        arranged_problems += "\n" + line4

    return arranged_problems


print(arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
