def health_calculator(age, apples_ate, cigs_smoked):
  answer = (100-age) + (apples_ate*3.5) - (cigs_smoked*2)
  print(answer)

vasu_data = [27, 20, 0]

health_calculator(vasu_data[0], vasu_data[1], vasu_data[2])
health_calculator(*vasu_data)