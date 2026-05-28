# independent project
# calculate a healthy calorie intake and deficit for weight loss based on hight, wieght, age, and sex
# calculates protein and fiber intake
# gives a sample for a full day eating with snakcs
# implimints seeing a doctor if certain long-term medical cases exsit like diabetes, deficincies,.....

# Welcoming the client and asking What language he would like to proceed in english or arabic

from deep_translator import GoogleTranslator
import arabic_reshaper
from bidi.algorithm import get_display
# now we define the translation helper function


def output_text(text):
    if 'language_prefered' in globals() and language_prefered == "arabic":
        # translate english to arabic
        translated = GoogleTranslator(source='en', target='ar').translate(text)
        # reshape letters so they connect cursively
        reshaped_text = arabic_reshaper.reshape(translated)
        # fix the right-to-left reading order
        return get_display(reshaped_text)
    return text


def input_text(text):
    if 'language_prefered' in globals() and language_prefered == "arabic":
        # translate arabic input into english
        translated = GoogleTranslator(source='ar', target='en').translate(text)
        # return english lowercase
        return translated.lower()
    return text.lower()


print("Hii! welcome to *UUS* were we help you'Understand Ur Self' and lose wieght in a healthy, comfortable, and easy way! ")
language_prefered = input(
    "To proceed in english type *english* / To proceed in arabic type *arabic*  ").strip().lower()
name = input(output_text(
    "I am Clara your personal helper. What is your name?  ")).strip().title()
print(output_text(f"Nice to meet you {name}!"))

# answer disclamer to note that this is a bot just to help, and seeking professional advise is extremely important
raw_disclamer = input(output_text(
    "Before we proceed, I would like to make sure you agree on the need to seek profesional advice, as i am just a bot and profesional advice is exteremely impotant... DONT start diet without medical advice. if you agree type *agree* "))
disclamer = input_text(raw_disclamer)

# print(f"DEBUG: Google translated your input to: '{disclamer}'") to make sure of what the translation is so it wont crash


if "agree" in disclamer or "ok" in disclamer or "yes" in disclamer:

    print(output_text("Cool let us go!"))
else:
    print(output_text("Sorry we cant proceed, nice to meet you though"))
    exit()


# ask whether the client wants to start evaluation or read mission
print(output_text("So, would you like to start the evaluation? or would you like to know more about aur mission and how we work?"))
what_to_know = input(output_text(
    "Wright either *start evaluation*, or *mission* to proceed  ")).strip().lower()
# print(f"DEBUG: Google translated your input to: '{what_to_know}')

# create a trigger flag
run_evealuation = False
# check user initial input

if "mission" in what_to_know or "مهمة" in what_to_know or "المهمة" in what_to_know:
    print(output_text("Empower your body by understanding your unique nutritional needs. Organization UUS (Understand Your Self) delivers personalized calorie deficits, targeted protein goals, and custom snack ideas built specifically for your lifestyle.Mission StatementTo guide individuals toward sustainable health through self-awareness, precise personalized nutrition, and practical daily eating strategies.Core PillarsSelf-Awareness First: We analyze your unique metabolism and daily activity levels.Calculated Deficits: We design safe, effective calorie limits to burn fat without starving.Protein Optimization: We target exact protein metrics to preserve lean muscle mass.Practical Snacking: We create realistic, satisfying snack alternatives tailored to your taste.Sustainable Habits: We eliminate restrictive dieting by focusing on long-term lifestyle education.Custom Strategy TemplateFocus AreaStrategy MetricTarget OutcomeEnergy BalancePersonalized Calorie DeficitSteady, predictable fat lossMuscle RetentionTailored Daily Protein GoalHigh satiety and metabolic supportHunger ManagementCustom Curated Snack IdeasZero energy crashes between meals"))
    proceed = input(output_text(
        "Now that you know what our mission is, type *yes* to start the evaluation")).strip().lower()
    if "yes" in proceed or "نعم" in proceed:
        run_evealuation = True  # trigger flag

if "start evaluation" in what_to_know or "بدء تقييم" in what_to_know:
    run_evealuation = True  # trigger flag
if run_evealuation:
    print(output_text("Amazing! lets go!"))
    age = int(input(output_text(f"How old are you {name}?  ")))
    # dont proceed if age 18 or less
    if age < 18:
        print(output_text(
            "Hmm... You are still in your growing faze i prefer you ask a certified doctor to proceed safely. Thank you !"))
        exit()
    if age == 18:
        print(output_text(
            "Hmmm....You are still in your growing faze i prefer you ask a certified doctor to proceed safely. Thank you !"))
        exit()

    if age > 18:
        print(output_text("okk amazing lets go then"))
    height = int(input(output_text(
        "how tall are you? please write your height in cm  ")))
    weight = int(input(output_text(
        "how much do you weight? please write your weight in kg  ")))

    sex = input(output_text(" Are you male or female?  ")).strip().lower()
    if "female" in sex or "أنثى" in sex:
        print(output_text("Okk i will start calculatuing..."))

        # calculate BMR
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        bmr_int = int(bmr)
        print(output_text("Your Basel Metabolic Rate (BMR) is " + str(bmr_int)))
        # protein for each one pound one gram
        protein = (weight * 2.20462) * 0.7

        protein_int = int(protein)
        print(output_text(
            "based on your weight your protein intake should be around :" + str(protein_int)))
    elif "male" in sex or "ذكر" in sex:
        print(output_text("Okk i will start calculatuing..."))
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        bmr_int = int(bmr)
        print(output_text("Your Basel Metabolic Rate (BMR) is " + str(bmr_int)))
        # protein for each one pound 0.7
        protein = (weight * 2.20462) * 0.7

        protein_int = int(protein)
        print(output_text(
            "based on your weight your protein intake should be around :" + str(protein_int)))

    print(output_text("Now, we need to take your activity level into account "))
    # print(f"DEBUG: Google translated your input to: '{sex}'")
    activity_level = input(output_text("Sedentary (type : e)Little to no exercise.Desk job workers.Lightly Active (type:a)Light exercise 1-3 days per week.Teachers or retail workers who stand often.Moderately Active (type: b)Moderate exercise 3-5 days per week.Active jobs like construction or heavy cleaning.Very Active (type: c)Hard exercise 6-7 days per week.Athletes or physical laborers.Extra Active (type:d)Very intense exercise twice daily.Elite athletes or professional movers.")).strip().lower()
    if "e" in activity_level or "ه" in activity_level:
        TDEE = bmr * 1.2
    elif "a" in activity_level or "أ" in activity_level:
        TDEE = bmr * 1.375
    elif "b" in activity_level or "ب" in activity_level:
        TDEE = bmr * 1.55
    elif "c" in activity_level or "ج" in activity_level:
        TDEE = bmr * 1.725
    elif "d" in activity_level or "د" in activity_level:
        TDEE = bmr * 1.9
    TDEE_int = int(TDEE)
    print(output_text("your Total Daily Energy Expenditure is " + str(TDEE_int)))

    if TDEE <= 1800:
        total_calories_a_day = TDEE - 300
        total_calories_a_day_int = int(total_calories_a_day)
        print(output_text("since your TDEE is less than or equal to 1800, you wil be in a 300 calorie defecit so your total calories a day is " + str(total_calories_a_day_int)))
    elif TDEE > 1800:
        total_calories_a_day = TDEE - 500
        total_calories_a_day_int = int(total_calories_a_day)
        print(output_text("since your TDEE is more than 1800, you will be in a 500 calorie deficit so your total calories a day is " + str(total_calories_a_day_int)))

    print(output_text(
        "now that you know your calorie defecite, i will suggest some snacks to help you with your sweet tooth"))
    print(output_text("Greek Yogurt Parley: Non-fat Greek yogurt, chia seeds, fresh berries.Savory Crunch: Roasted chickpeas, lightly salted almonds, cucumber slices.Quick Fuel: Rice cakes with almond butter and a scoop of whey protein isolate"))
    print(output_text(
        f"Hope this helps! nice to meet you {name}! and rememmber, dont start any diet without a doctors consult!"))
