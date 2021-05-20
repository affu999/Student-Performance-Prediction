from DataMining import DataMining
def returnSkills(data):
    data = DataMining.purifyData(data[2:-1])
    data = data[:-2]
    skill = [] 
    if data[9] > 0:
        skill += ["Reduce traveltime"]
    if data[10] >= 0:
        skill += ["Increase studytime"]
    if data[12] == 1:
        skill += ["Extra Education Support (schoolsup)"]
    if data[14] == 1:
        skill += ["Take Extra Classes/Tuitions (paid)"]
    if data[15] == 2:
        skill += ["Reduce extra curricular Activitive (activities)"]
    if data[17] == 2:
        skill += ["Reduce Access to Internet (internet)"]
    if data[18] == 2:
        skill += ["Spend less time with Soul Mate (romantic)"]
    if data[19] > 0:
        skill += ["Utilize free time in studies (freetime)"]
    if data[20] > 0:
        skill += ["Reduce going out with friends (gout)"]
    if data[21] > 0:
        skill += ["Reduce Consumption of Alcohol (Walc)"]
    if data[22] < 5:
        skill += ["Maintain good health condition (health)"]
    if data[23] > 0:
        skill += ["Reduce Absences (absences)"]

    return skill