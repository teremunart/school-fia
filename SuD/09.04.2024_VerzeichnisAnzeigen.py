import os


def main():
    inputPath = str(input())
    renderFolderStructure(inputPath)


def renderFolderStructure(inputPath, aaaa=""):
    structure = os.listdir(inputPath)
    splitter = "-" + aaaa
    for i in structure:
        print(splitter + i)
        if not os.path.isfile(inputPath + "\\" + i):
            if len((os.listdir(inputPath + "\\" + i))) > 0:
                renderFolderStructure((inputPath + "\\" + i), splitter)


if __name__ == "__main__":
    main()
