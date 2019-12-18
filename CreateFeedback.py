import sys
from GenderSwap import InsertGenderLanguage
from pathlib import Path

rubricData = []
groupInputData = []


def Run():
    ReadFiles()
    CompileComments()
    # print(rubricData)
    # print(groupInputData)


def ReadFiles():
    """get rubric/group file data"""

    # with open(sys.argv[1]) as rubric:
    with open("Samples/SampleRubric.csv") as rubric:
        readin = rubric.readlines()
        global rubricData
        for line in readin:
            rubricData.append(line.strip("\n").split("|"))

    # with open(sys.argv[2]) as groupList:
    with open("Samples/SampleInput.csv") as groupList:
        readin = groupList.readlines()
        global groupInputData
        for line in readin:
            groupInputData.append(line.strip("\n").split(","))


def BuildParagraph(individual):
    """construct paragraph using individual data to pull pieces from rubric"""
    paragraph = individual[0] + "\n" + individual[1]

    for i in range(0, len(rubricData)):
        # print(rubricData[i][int(individual[i+3])])
        paragraph += " " + rubricData[i][int(individual[i+3])]

    paragraph = InsertGenderLanguage(paragraph, individual[2])
    return paragraph


def OutputToPath(filePath):

    # with open(groupInputData[0][0] + "Comments.txt", "w") as output:
    with open(filePath, "w") as output:
        output.write(groupInputData[0][0] + "\n")
        output.write("\n")

        for i in range(1, len(groupInputData)):
            individualComment = BuildParagraph(groupInputData[i])

            output.write(individualComment + "\n")
            output.write("\n")


def CompileComments():
    """read individual comment generation data --> Frodo Baggins,Frodo,m,1,1,1,1,1
    then output the generated comment to a new file (currently overwrites)"""

    # check if output file exists, ask for overwrite
    writePath = groupInputData[0][0] + "Comments.txt"
    if Path(writePath).exists():
        if input("Output file " + writePath + " already exists. Overwrite file? [y/n]: ") == "n":
            i = 1
            while True:
                if not Path(writePath.replace(".", "("+str(i)+").")).exists():
                    writePath = writePath.replace(".", "("+str(i)+").")
                    break
                i += 1

            OutputToPath(writePath)
            print("Process completed - new file " + writePath + " created")
        else:
            OutputToPath(writePath)
            print("Process completed - " + writePath + " overwritten")
    else:
        OutputToPath(writePath)


Run()
