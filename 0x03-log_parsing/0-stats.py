#!/usr/bin/python3
import sys
import re


if __name__ == "__main__":
    line_format = (
        r"^\d+\.\d+\.\d+\.\d+ - \["
        r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "
        r'"GET /projects/\d+ HTTP/1\.1" \d+ \d+$'
    )

    def validate_line(line: str) -> bool:
        """function to return line matches format or not"""
        patern = re.compile(line_format)
        return bool(patern.match(line))

    status_code_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }  # nopep8
    total_size = 0

    def print_data() -> None:
        print(f"File size: {total_size}")
        for key, value in status_code_count.items():
            if value > 0:
                print(f"{key}: {value}")

    try:
        for idx, line in enumerate(sys.stdin):
            if not validate_line(line):
                continue
            file_size = line.split()[-1]
            status_code = int(line.split()[-2])
            total_size += int(file_size)
            status_code_count[status_code] += 1
            if (idx + 1) % 10 == 0:
                print_data()

    except KeyboardInterrupt:
        print_data()
