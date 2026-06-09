import sys
from src.frontend.parser_driver import ParserDriver


def main():
    if len(sys.argv) > 1:
        examples = sys.argv[1:]
    else:
        examples = [
            "examples/valid/ejemplo1.stats",
            "examples/valid/ejemplo2.stats",
            "examples/invalid/error1.stats",
        ]

    driver = ParserDriver()

    for file in examples:
        driver.run(file)


if __name__ == "__main__":
    main()