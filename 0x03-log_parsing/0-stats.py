#!/usr/bin/python3
"""script to parse logs"""
import sys
import re


if __name__ == "__main__":
    line_format = r"^\d+\.\d+\.\d+\.\d+ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] \"GET /projects/260 HTTP/1\.1\" \d+ \d+$"  # nopep8

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
    }  # no
    total_size = 0

    def print_data() -> None:
        """function to print the data"""
        print(f"File size: {total_size}")
        for key in sorted(status_code_count.keys()):
            if status_code_count[key] > 0:
                print(f"{key}: {status_code_count[key]}")

    try:
        for idx, line in enumerate(sys.stdin):
            if validate_line(line):
                file_size = line.split()[-1]
                status_code = int(line.split()[-2])
                total_size += int(file_size)
                if status_code in status_code_count.keys():
                    status_code_count[status_code] += 1
                if (idx + 1) % 10 == 0:
                    print_data()
    finally:
        print_data()
