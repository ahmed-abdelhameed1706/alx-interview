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
        pattern = re.compile(line_format)
        return bool(pattern.match(line))

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

    line_count = 0

    def print_data() -> None:
        print(f"File size: {total_size}")
        for key in sorted(status_code_count.keys()):
            if status_code_count[key] > 0:
                print(f"{key}: {status_code_count[key]}")

    try:
        for line in sys.stdin:
            line_count += 1
            if not validate_line(line):
                continue
            file_size = line.split()[-1]
            status_code = int(line.split()[-2])
            total_size += int(file_size)
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            if line_count % 10 == 0:
                print_data()

    except KeyboardInterrupt:
        print_data()
        raise
