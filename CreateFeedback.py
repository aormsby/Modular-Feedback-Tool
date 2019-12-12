import sys

rubricData = []
groupInputData = []


def Run():
    ReadFiles()
    CompileComments()
    # print(rubricData)
    # print(groupInputData)


def ReadFiles():
    """get rubric/group file data"""

    with open(sys.argv[1]) as rubric:
        # with open("Samples/SampleRubric.csv") as rubric:
        readin = rubric.readlines()
        global rubricData
        for line in readin:
            rubricData.append(line.strip("\n").split("|"))

    with open(sys.argv[2]) as classList:
        # with open("Samples/SampleInput.csv") as groupInputData:
        readin = classList.readlines()
        global groupInputData
        for line in readin:
            groupInputData.append(line.strip("\n").split(","))


def BuildParagraph(individual):
    """construct paragraph using individual data to pull pieces from rubric"""
    paragraph = individual[0] + "\n" + individual[1]

    for i in range(0, len(rubricData)):
        # print(rubricData[i][int(individual[i+3])])
        paragraph += " " + rubricData[i][int(individual[i+3])]

    if (individual[2] == "f"):
        paragraph = paragraph.replace("[Pro]", "She")
        paragraph = paragraph.replace("[pro]", "she")
        paragraph = paragraph.replace("[Pos]", "Her")
        paragraph = paragraph.replace("[pos]", "her")
        paragraph = paragraph.replace("[obj]", "her")
    elif (individual[2] == "m"):
        paragraph = paragraph.replace("[Pro]", "He")
        paragraph = paragraph.replace("[pro]", "he")
        paragraph = paragraph.replace("[Pos]", "His")
        paragraph = paragraph.replace("[pos]", "his")
        paragraph = paragraph.replace("[obj]", "him")
    elif (individual[2] == "t"):
        paragraph = paragraph.replace("[Pro]", "They")
        paragraph = paragraph.replace("[pro]", "they")
        paragraph = paragraph.replace("[Pos]", "Their")
        paragraph = paragraph.replace("[pos]", "their")
        paragraph = paragraph.replace("[obj]", "them")
    else:
        paragraph = "OOPS."

    return paragraph


def CompileComments():
    """read individual comment generation data --> Frodo Baggins,Frodo,m,1,1,1,1,1
    then output the generated comment to a new file (currently overwrites)"""

    with open(groupInputData[0][0] + "Comments.txt", "w") as output:
        output.write(groupInputData[0][0] + "\n")
        output.write("\n")

        for i in range(1, len(groupInputData)):
            individualComment = BuildParagraph(groupInputData[i])

            output.write(individualComment + "\n")
            output.write("\n")


Run()
