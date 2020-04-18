numlist = [line.translate({ord('.') : None, ord('\n') : None})[::-1] for line in open("numlist.txt")]
graphdata = {"0":[0,0,0,0,0,0,0,0,0,0],"1":[0,0,0,0,0,0,0,0,0,0],"2":[0,0,0,0,0,0,0,0,0,0],"3":[0,0,0,0,0,0,0,0,0,0],"4":[0,0,0,0,0,0,0,0,0,0],"5":[0,0,0,0,0,0,0,0,0,0],"6":[0,0,0,0,0,0,0,0,0,0],"7":[0,0,0,0,0,0,0,0,0,0]}
for numbers in numlist:
  for idx,num in enumerate(numbers):
    if num == '0':
      graphdata[f"{idx}"][0] += 1
    if num == '1':
      graphdata[f"{idx}"][1] += 1
    if num == '2':
      graphdata[f"{idx}"][2] += 1
    if num == '3':
      graphdata[f"{idx}"][3] += 1
    if num == '4':
      graphdata[f"{idx}"][4] += 1
    if num == '5':
      graphdata[f"{idx}"][5] += 1
    if num == '6':
      graphdata[f"{idx}"][6] += 1
    if num == '7':
      graphdata[f"{idx}"][7] += 1
    if num == '8':
      graphdata[f"{idx}"][8] += 1
    if num == '9':
      graphdata[f"{idx}"][9] += 1

