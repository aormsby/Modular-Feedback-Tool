# Modular Feedback Tool

- [Overview](#overview)
- [How to Run](#how-to-run)
  - [Rubric file](#rubric-file)
  - [Gender Replacement](#gender-replacement)
  - [Input Data file](#input-data-file)
  - [Sample Output](#sample-output)
- [Goal: Quantity Over Quality](#goal-quantity-over-quality)
  - [Good Use Case](#good-use-case)
  - [Bad Use Case](#bad-use-case)
- [Current Features](#current-features)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
  - [Needs](#needs)
  - [Nice to have](#nice-to-have)

## Overview

This is a time-saving tool for generating _somewhat_ specialized feedback for large numbers of people. It's useful for things like student reports and staff assessment.

## How to Run

You need **2 user-created files** before running this tool.

1. A 'rubric' that contains your modular comment data **(.csv)**
2. An 'input data' file used to guide comment generation **(.csv)**

After you set these up, you can run the program in your command terminal like so:

`python CreateFeedback.py [rubric_file].csv [input_file].csv`

A **.txt** file will be generated with title taken from your input data file and placed in the script folder. It will contain all of your output text comments.

### Rubric file

In our case, the rubric is the table of qualities you are assessing in an individual. You can add as many qualities as you'd like, and you should include multiple levels for each quality to provide different levels of feedback. The rubric should be saved as a **.csv file** with **pipe separators** as in the sample below.

[Sample Rubric](Samples/SampleRubric.csv)
(sample from repository)

|                  | 1                                                                                                | 2                                                                                                   | 3                                                                                                                 |
|------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Overall Skill    | has a lot of trouble with hand to hand combat, which is really a big part of the job.            | has struggled a bit with hand to hand combat, which can sometimes get in the way of [pos] survival. | has shown great skill in hand to hand combat, which can be very helpful in the dangerous world find ourselves in. |
| Sword            | [Pro] often end[s] up with swords inside [obj] when they shouldn't be,                           | [Pro] could use a bit more training in sword handling,                                              | [Pos] deadly sword skills are second to none,                                                                     |
| Axe              | while [pro] probably couldn't lift an axe if [pro] tried.                                        | while [pos] skill with an axe could improve through experience.                                     | while [pro] [has] been known to cleave an enemy's skull in twain with [pos] heavy axes.                           |
| Wits             | Tricky situations often get the better of [obj], so sending [obj] out for scout work is a no-no. | [Pro] [has] [pos] wits about [obj] most days, so [pro] can be a good scout in an emergency.         | Always alert, even when asleep, [pro]['s] the perfect scout over any terrain.                                     |
| Party Assessment | The sad truth is I wouldn't want [obj] by my side in a battle.                                   | If the occasion calls for it, I can see myself fighting next to [obj] in battle.                    | I'm positive [pro] would absolutely slay in battle, and I always want [obj] by my side.                           |

The key here is to write out your quality text following a sort of comment template. All of your generated comments will follow that template from the beginning to the end of your rubric. The trickiest part is to make your comment pieces connect to each other grammatically, and in some cases it won't be possible. While the goal is to provide as much modularity in comment generation as needed, there will often be grammar issues that need to be tweaked after generation using your rubric. Language is pretty messy. :wink:

### Gender Replacement

In your rubric, you can (and really should) include placeholder codes for gender pronouns, possessives, and object pronouns. You will note a person's gender in the Input Data file, and the tool will automatically replace these codes with the correct words.

Supported Genders

- m - Male
- f - Female
- t - They/m

I'm happy to add support for more specific pronouns as requested.

- Pronouns - `[Pro]` -> He, She, They, `[pro]` -> he, she, they
- Object Pronouns - `[Obj]` -> Him, Her, Them, `[obj]` -> him, her, them
- Possessives - `[Pos]` -> His, Her, Their, `[pos]` -> his, her, their

Some basic verb replacements are also supported.

- `[is]` -> 'is' for m/f, 'are' for t
- `ha[s]` -> 'has' for m/f, 'have' for t

### Input Data file

Your input data file is where you set up the details for actual comment generation. It's a list of names, gender, and the level of feedback you wish to give for each section of the comments rubric you created. It's a **.csv file** with **comma separators** as in the sample below.

The first line gets set as the name of your output file. -> `[first_line]Comments.txt`. In each successive line, the Full Name, Name, and Gender data are required. After those, the number of qualities you add should be based on your rubric. My sample rubric has 5 qualities, so I added data for 5 qualities into each line.

[Sample Input](Samples/SampleInput.csv)
(sample from repository)

| Full Name             | Name      | Gender | Q1 | Q2 | Q3 | Q4 | Q5 |
|-----------------------|-----------|:------:|:--:|:--:|:--:|:--:|:--:|
| Sample (first_line) |           |        |    |    |    |    |    |
| Frodo Baggins         | Frodo     | m      | 1  | 1  | 1  | 1  | 1  |
| Meriadoc Brandybuck   | Merry     | m      | 2  | 2  | 1  | 2  | 2  |
| Nazgûl #3             | Naz       | t      | 3  | 3  | 2  | 2  | 3  |
| Arwen Undómiel        | Arwen     | f      | 3  | 3  | 1  | 3  | 3  |
| Gandalf the Grey      | Gandalf   | t      | 2  | 2  | 1  | 3  | 2  |
| Lady Galadriel        | Galadriel | f      | 3  | 3  | 2  | 2  | 2  |

For each quality, you will write the level of feedback with a number. In my sample, I have 3 levels for each quality. Therefore, I can type 1, 2, or 3 in my input data. The tool will read which level to use in the rubric and output the corresponding comment piece.

You can have as many qualities and levels as you'd like, but remember that the number of assessed qualities provided in the input data file must match the number in the rubric or it will not work.

### Sample Output

Using the two sample files from above, here is the output after running the script. -> [Sample Output](Samples/SampleComments.txt)

## Goal: Quantity Over Quality

While the level of quality in your generated reports is based directly on your rubric, there is a limit to how personalized these comments will really be. For that reason, I recommend using this tool only when a lot of reports are needed on a tight deadline.

### Good Use Case

You're a teacher, and you need to write 300+ student reports in 1 week. There's no way to fully personalize all of your comments, so you can use this tool to help generate comments for the majority who don't need much feedback. Then you can use the remaining time to focus on writing more in-depth feedback for the students who need it.

### Bad Use Case

You're a manager with about 30 people on your team, and you need to write a quarterly report on their workplace/career development. You could use this tool to help, but many of your comments may appear quite similar due to rubric limitations. Since you don't have too many employees needing and there's more time, it would be much better to write all of these comments to give them a more personal touch.

In the end, it's up to you to judge what's best for your situation. Just remember this tool is built more for quantity over quality. :smile:

## Current Features

- Automatically replaces gender through text placeholders
- Generates comments based on user-created rubric
- Asks for overwrite if output file already exists
- Runs in command terminal (not ideal for target user)

## Limitations

- Language --> This tool is currently **English-specific**, and it's highly doubtful that gender-based pronoun swapping would work in properly other languages. Moreso, there is a heavy reliance on concatenation in places where it is unhelpful to localization.
- Reliance on CLI --> My intention is to build a simple GUI to support the application for more non-technical users.

## Future Improvements

### Needs

- **Internationalization** updates to support other language needs --> I'm very keen to work on this. :slightly_smiling_face:
- Improved formatting of output file
  - e.g. can be made ready for quick copy-paste into spreadsheets, perhaps can format for multiple use cases
- Visual UI **(important)**
  - to remove need for command-line knowledge as target users are teachers and managers
  - acts as an accessible interface that can be built on as features are improved/added, grants more user control/confidence

### Nice to have

- Ability to run gender replacement script on its own -- This function is already separate, but I'm unsure of how to best implement it as a standalone option.
- Automatically mark mixed-level comments for language review to check for any grammar matching issues
