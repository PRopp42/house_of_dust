import argparse
import random



def main(count: int, template: str, collection: list[list[str]]) -> None:

    for _ in range(count):
        values = []

        for choices in collection:
            values.append(random.choice(choices))

        print(template.format(*values))
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=1)
    parser.add_argument("--template", default="a house of {},\n\tilluminated by {},\n\t\tinhabited by {}")
    parser.add_argument("--input-files", nargs="+", default=["FirstNoun.txt", "SecondLight.txt", "ThirdTenant.txt"])
    args = parser.parse_args()

    count = args.count
    template = args.template
    inputFiles = args.input_files

    inputLists = []

    for input in inputFiles:
        with open(input, "r") as choicFile:
            inputLists.append([x.rstrip() for x in choicFile.readlines() if x.rstrip() is not None])


    main(count, template, inputLists)