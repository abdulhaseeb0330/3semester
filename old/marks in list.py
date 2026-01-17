list=[{"1":["faraz","20","30","50","70","0","lahore"]},
      {"2":["faraz","2","3","5","7","22","multan"]},
      {"3":["faraz","20","33","50","7","22","ibd"]},
      {"4":["faraz","20","30","50","70","22","karachi"]},
      {"5":["faraz","20","30","55","70","22","faisalabad"]}
      ]
for i in list:
    for key in i:
        total=0
        for val in i[key][1:6]:
            total+=int(val)
        avg=total/5
        print(f"student {i[key][0]} from {i[key][6]} has average marks {avg}")