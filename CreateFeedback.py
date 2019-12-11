import sys

# TODO make vars more generic
# TODO split paragraph building and gender replacements

rubricData = []
classData = []

# get rubric file data
def ReadFiles():

    with open(sys.argv[1]) as rubric:
    # with open("Rubric8.csv") as rubric:
        readin = rubric.readlines()
        global rubricData
        for line in readin:
            rubricData.append(line.strip("\n").split("|"))

    with open(sys.argv[2]) as classList:
    # with open("TestClass.csv") as classList:
        readin = classList.readlines()
        global classData
        for line in readin:
            classData.append(line.strip("\n").split(","))


def BuildParagraph(student):
    paragraph = student[0] + "\n" + student[1]

    for i in range(0, len(rubricData)):
        # print(rubricData[i][int(student[i+3])])
        paragraph += " " + rubricData[i][int(student[i+3])]
    
    if (student[2] == "f"):
        paragraph = paragraph.replace("[Pro]", "She")
        paragraph = paragraph.replace("[pro]", "she")
        paragraph = paragraph.replace("[Pos]", "Her")
        paragraph = paragraph.replace("[pos]", "her")
        paragraph = paragraph.replace("[obj]", "her")
    elif (student[2] == "m"):
        paragraph = paragraph.replace("[Pro]", "He")
        paragraph = paragraph.replace("[pro]", "he")
        paragraph = paragraph.replace("[Pos]", "His")
        paragraph = paragraph.replace("[pos]", "his")
        paragraph = paragraph.replace("[obj]", "him")
    elif (student[2] == "t"):
        paragraph = paragraph.replace("[Pro]", "They")
        paragraph = paragraph.replace("[pro]", "they")
        paragraph = paragraph.replace("[Pos]", "Their")
        paragraph = paragraph.replace("[pos]", "their")
        paragraph = paragraph.replace("[obj]", "them")
    else:
        paragraph = "OOPS."
    
    return paragraph
    

# read student comment generation data --> Nguyen Ngoc Linh,Linh,F,1,3,2,2,1,2
# then output the generated comment to a new file
def GenerateComments():

    with open(classData[0][0] + "Comments.txt", "w") as output:
        output.write(classData[0][0] + "\n")
        output.write("\n")

        for i in range(1, len(classData)):
            studentComment = BuildParagraph(classData[i])
            
            output.write(studentComment + "\n")
            output.write("\n")

ReadFiles()
GenerateComments()
# print(rubricData)
# print(classData)