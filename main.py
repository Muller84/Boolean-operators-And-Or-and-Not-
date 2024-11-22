'''
The program that decides whether a student can go on a trip.
For this, several conditions must be checked:
 
Is the student over 15 years old?
Does the student have parental consent?
Unexcused absences: Does the student have less than 3 unexcused absences?
Does the student not have a previous detention OR participate in volunteer work?
'''
def colored(r, g, b, text, bold=False, underline=False, blink=False, bg=None):
    color_code = f"\033[38;2;{r};{g};{b}m"
    bold_code = "\033[1m" if bold else ""
    bg_code = f"\033[48;2;{bg[0]};{bg[1]};{bg[2]}m" if bg else ""
    return f"{bold_code}{bg_code}{color_code}{text}\033[0m"

print(colored(255, 0, 255, "Let's see if you're trip-worthy!\n" ))
 
age = int(input("Enter your age (must be 15 or older): "))
 
if age < 15:
    print(colored(255,0,0, "You're too young for this trip! Go back to your video games.")) #This text is red
else:
    parent_consent = input("Do your parents approve? (yes/no): ").lower() == "yes"
 
    if not parent_consent:
        print(colored(255,0,0,"Parental disapproval? Bummer. No trip for you."))
    else:
        unexcused_absences = int(input("How many unexcused absences do you have? "))
        if unexcused_absences > 3:
            print(colored(255,0,0,"Too many unexcused absences. No trip for you!"))
        else:
            detention = int(input("How many detentions do you have?")) == 0
            volunteer_work = input("Do you participate in volunteer work? (yes/no): ").lower() == "yes"
 
            if detention or volunteer_work:
                print(colored(0,0, 255, "Congratulations! You're ready for the trip!", bold=True)) #This text is blue
            else:
                print(colored(255, 0, 0, "Looks like you're grounded. " ))
                print(colored(255, 0, 0, "Better luck next time!", bold=True))

