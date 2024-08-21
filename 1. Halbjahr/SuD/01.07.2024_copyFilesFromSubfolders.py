# copyFilesFromSubfolders
# Author:   Ivanov, Rogerio
# Revision: 0.3
#

import os
import shutil
import pandas


def startup():
    # Fix for T4 source folder not existing
    print("[INFO] Checking if source folder exists...")
    if not os.path.exists(sourceFolderName):
        print("[INFO] I cannot copy form a directory that does not exists.")
        return False
    print("[INFO] Source folder found!")

    # Fix of T5 create target folder if not existing
    print("[INFO] Checking if target folder exists...")
    if not os.path.exists(targetFolderName):
        print("[INFO] Creating target folder")
        os.mkdir(targetFolderName)

    print("[INFO] Target folder found!")
    return True


def scanFolder(source, target):
    """ Scans a source folder for csv-files containing 'time_record' in the name and copies them to the target folder.
        Returns the number of files copied."""
    global counter
    numberOfFilesCopied = 0

    for content in os.scandir(source):
        if content.is_dir():
            print(content.path)
            # Recursively scan subdirectories
            numberOfFilesCopied += scanFolder(content.path, target)
        elif content.is_file():
            # Fix of T3: Only copy files containing key "time_record" in the name
            if content.path.endswith(".csv") and 'time_record' in content.name:
                print(content.path)
                # Fix of T6: Generate unique backup file name
                backupFile = f"{counter}_{content.name}"
                shutil.copy(content.path, os.path.join(target, backupFile))

                addToSummaryFile(content)

                counter += 1
                numberOfFilesCopied += 1

    return numberOfFilesCopied


# Fix of T7: Create a file that contains all the CSVs
def addToSummaryFile(fetchedFile):
    global summaryText
    global summaryLines
    global firstFile

    lineIndex: int = 0
    lines = open(fetchedFile.path, "r")

    for line in lines:
        if "time_record" in line:
            line.replace(line[:0], '')
        # Fix for T9: Do not Copy Line Header
        if firstFile:
            if line.startswith(";"):
                fixedLine = line[1:]
                summaryText += fixedLine
            else:
                summaryText += line
            summaryLines += 1
        else:
            if lineIndex != 0:
                summaryLines += 1
                summaryText += line
        lineIndex += 1

    firstFile = False


def writeToFile(target, content):
    with open(os.path.join(target, "summary.csv"), "w") as finalFile:
        finalFile.write(content)
    finalFile.close()


def generateExcelFile(filePath, backupPath):
    xlsxContent = pandas.read_csv(filePath, sep=";")
    xlsxFile = pandas.ExcelWriter(os.path.join(backupPath, "summary.xlsx"))
    xlsxContent.to_excel(xlsxFile, index=False)
    xlsxFile.close()


# configuration
path = "16.04.2024_SuD_TestDrivenDevelopment/30.04.2024_rDa_TestDrivenDevelopment\\"
sourceFolderName = path + "quellordner\\"
targetFolderName = path + "zielordner\\"

# action
print("[INFO] Starting up...")

if startup():
    global counter
    counter: int = 0

    global summaryText
    summaryText: str = ""

    global summaryLines
    summaryLines: int = 0

    global firstFile
    firstFile: bool = True

    resultNumber = scanFolder(sourceFolderName, targetFolderName)
    print(f"Anzahl kopierter Dateien:{resultNumber}")

    # Fix of T8: Not showing Final Line Count on Summary
    writeToFile(targetFolderName, summaryText)
    print(f"Total Lines of Summary: {summaryLines}")

    generateExcelFile(os.path.join(targetFolderName, "summary.csv"), targetFolderName)
    print(f"Saved XLSX File to {targetFolderName}")
