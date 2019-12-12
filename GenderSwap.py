# import sys


def InsertGenderLanguage(paragraph, gender):

    if (gender == "f"):
        paragraph = paragraph.replace("[Pro]", "She")
        paragraph = paragraph.replace("[pro]", "she")
        paragraph = paragraph.replace("[Pos]", "Her")
        paragraph = paragraph.replace("[pos]", "her")
        paragraph = paragraph.replace("[obj]", "her")
    elif (gender == "m"):
        paragraph = paragraph.replace("[Pro]", "He")
        paragraph = paragraph.replace("[pro]", "he")
        paragraph = paragraph.replace("[Pos]", "His")
        paragraph = paragraph.replace("[pos]", "his")
        paragraph = paragraph.replace("[obj]", "him")
    elif (gender == "t"):
        paragraph = paragraph.replace("[Pro]", "They")
        paragraph = paragraph.replace("[pro]", "they")
        paragraph = paragraph.replace("[Pos]", "Their")
        paragraph = paragraph.replace("[pos]", "their")
        paragraph = paragraph.replace("[obj]", "them")
    else:
        # if the gender is not supported
        paragraph = paragraph.replace("[Pro]", "[OOPS.]")
        paragraph = paragraph.replace("[pro]", "[OOPS.]")
        paragraph = paragraph.replace("[Pos]", "[OOPS.]")
        paragraph = paragraph.replace("[pos]", "[OOPS.]")
        paragraph = paragraph.replace("[obj]", "[OOPS.]")

    if (gender in {"m", "f"}):
        paragraph = paragraph.replace("[has]", "has")
        paragraph = paragraph.replace("[\'s]", "\'s")
    elif (gender == "t"):
        paragraph = paragraph.replace("[has]", "have")
        paragraph = paragraph.replace("[\'s]", "\'re")
        pass
    else:
        paragraph = paragraph.replace("[has]", "[OOPS]")
        paragraph = paragraph.replace("[\'s]", "[OOPS]")

    return paragraph
