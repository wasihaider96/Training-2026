#Function definition
def grade_classifier(score):
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"
    
#Test with at least 5 values
print("Manual Tests")
print(grade_classifier(95)) 
print(grade_classifier(75))
print(grade_classifier(50))
print(grade_classifier(45))
print(grade_classifier(30))

#Loop through given list
scores = [45, 72, 91, 60, 38, 85]

print("\nLoop Tests")

for score in scores:
    result = grade_classifier(score)
    print(f"Score: {score} -> {result}")
