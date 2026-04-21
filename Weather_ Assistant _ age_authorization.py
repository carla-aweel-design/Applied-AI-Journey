# Project : Interactive Lifestyle & Weather Assistant
# Author : Carla Aweel
# Purpose : A logic-based bot that handles user verification and enviromental advice.
# This is a personal project

name = input("Hello! What is your name? ").strip().title()
if name == "Max":
    print("What a lovely coinsedence! My name is also Max! Nice tomeet you!")
else:
    print(f"Nice to meet you {name}.I'm Max")

# ---USER VERIFICATION SECTION---
# Checking age and parental consent to ensure saftey

age_input = input("How old are you? ")
age = int(age_input.strip())
if age >= 18:
    print("Oh! you are an adult! Good to know that")
elif age < 18:
    answer = input(
        "Hmmm...Do you have a parent with you righ know? ").strip().lower()
    if answer == "yes":
        print("Amazing good to know!")
    if answer == "no":
        print("Sorry, come back when an adult is with you please.")
        exit()
        # we use exit() here to prevemt unauthorized users from accesing the rest of the script


color = input("What is your favorit color? ").strip()
print(f"Oh! {color} is an amazing color! You surely have an interesting eye for colors!")
opinion = input(
    "whould you like me to help you with what to wear today? ").strip().lower()
if opinion == "yes":
    temperature_input = input("You got it! What is the temperature today?  ")
    temperature = int(temperature_input)
    if temperature >= 30:
        print("Oooh today is hot! wear something light and choose a pastel color. It's a much better choice for today than dark colors!")
        advice = input(
            "Whould you like me to give you some advice to get through this hot wheather?  ").strip().lower()
        if advice == "yes":
            print("Amazing good choice!")
            print(
                "First of all, don't forget your hat today! it is extremly important to keep safe from the sun.")
            print("Second of all, fill you water bottel and keep it with you at all times! you should always be hyderated!")
            print("Try to be out of the sun as much as possible it is better.")
            print("These are three important advices to keep in mind today. Be careful!")
        if advice == "no":
            print(
                "As you wish. I'm sure you know exactly how to take care of yourself! Be careful!")
    elif temperature >= 14:
        print("Oooh the weather seems good today!A T-shirt will do. But make sure to keep a light jacket with you!It might be chill.")
        activity = input(
            "Would you like me to suggest some outdoor activities for today?  ").strip().lower()
        if activity == "yes":
            print(
                "Good choise! The weather is amazing for a lot af activities here are some of them...")
            print(
                "If you like to be alone, then going for a walk or run might be what you're looking for")
            print(
                "If you'r thinking about something with your friends you can always go for a picnic.")
            print("You can also orginize a friendly match whether footbal or basketball or any sort of competitive sport")
            print(
                "Whatever you choose to do it is important to enjoy the good weather today!")
        if activity == "no":
            print(
                "It's okay, the most important thing is to enjoy the weather and have fun!")
    else:
        print("ohhh today is cold. Be careful today and wear heavy clothes.A jacket is exteremly important.")
        advice_winter = input(
            "Whould you like me to give you advice for today?  ").strip().lower()
        if advice_winter == "yes":
            print("Good choice! I'll list some stuf you should do today...")
            print(
                "First of all, take a scarf with you. Keeping your neck warm is really important.")
            print(
                "Second of all, drink something warm it will keep you from getting cold.")
            print("Wear a lot of cloth and try not to catch a cold today.")
            print("Take care today and stay warm!")
        if advice_winter == "no":
            print("No worries! keep safe!")
if opinion == "no":
    print("Okay as you wish! Take care!")
print(f"Have a great day {name}!")

# feat: complete concierge bot with age verification with added input sanitization for better user experience
