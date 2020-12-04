import re
import string

#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

validEyeColors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

filepath = 'input04'
validPassports = 0
passportString = ""
passportFieldKeys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
#passportFieldVals = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pic", "cid"}
passportIsValid = True
passportFindIdx = 0;
passportFields = {}
ppFieldVal = ""

with open(filepath) as fp:
   line = fp.readline()

   while line:
       if(line.isspace()):
           passportIsValid = True
           passportFields = passportString.split()

           if(len(passportFields) < 7):
               passportIsValid = False
           elif(len(passportFields) < 8):
               if(passportString.find("cid:") >= 0):
                   passportIsValid = False

           if(passportIsValid):
              # print("searching fields")

              for ppField in passportFields:
                  # print("Passport Field {}".format(ppField))
    #              print(ppField)
                  for ppFieldKey in passportFieldKeys:
                      if(ppField.find(ppFieldKey)>=0):
                          ppFieldVal = ppField[4:]
                          print(ppFieldVal)

                          if(ppFieldKey == "byr"):
                              if(len(ppFieldVal) != 4):
                                  passportIsValid = False
                              else:
                                  ppFieldValInt = int(ppFieldVal)
                                  if(ppFieldValInt > 2002 or ppFieldValInt < 1920):
                                      passportIsValid = False

                              if(passportIsValid == False):
                                  print("byr invalid")

                          elif(ppFieldKey == "iyr"):
                              if(len(ppFieldVal) != 4):
                                  passportIsValid = False
                              else:
                                  ppFieldValInt = int(ppFieldVal)
                                  if(ppFieldValInt > 2020 or ppFieldValInt < 2010):
                                      passportIsValid = False

                              if(passportIsValid == False):
                                  print("iyr invalid")


                          elif(ppFieldKey == "eyr"):
                              if(len(ppFieldVal) != 4):
                                  passportIsValid = False
                              else:
                                  ppFieldValInt = int(ppFieldVal)
                                  if(ppFieldValInt > 2030 or ppFieldValInt < 2020):
                                      passportIsValid = False

                              if(passportIsValid == False):
                                  print("eyr invalid")

                          elif(ppFieldKey == "hgt"):
                              # print(ppFieldVal)
                              hgtIdx = ppFieldVal.find("cm")
                              if(hgtIdx >= 0):
                                  hgtCm = int(ppFieldVal[:hgtIdx])
                                  if(hgtCm > 193 or hgtCm < 150):
                                      passportIsValid = False
                              else:
                                  hgtIdx = ppFieldVal.find("in")
                                  if(hgtIdx >= 0):
                                      hgtIn = int(ppFieldVal[:hgtIdx])
                                      if(hgtIn > 76 or hgtIn < 59):
                                          passportIsValid = False
                                  else:
                                      passportIsValid = False

                              if(passportIsValid == False):
                                  print("hgt invalid")

                          elif(ppFieldKey == "hcl"):
                              if(ppFieldVal.find('#') >= 0):
                                  hclHex = ppFieldVal[1:]
                                  if(len(hclHex) != 6):
                                      passportIsValid = False
                                  else:
                                      if(all(c in string.hexdigits for c in hclHex) == False):
                                          passportIsValid = False
                              else:
                                  passportIsValid = False

                              if(passportIsValid == False):
                                  print("hcl invalid")

                          elif(ppFieldKey == "ecl"):
                              if ppFieldVal not in validEyeColors:
                                  passportIsValid = False

                              if(passportIsValid == False):
                                  print("ecl invalid")

                          elif(ppFieldKey == "pid"):
                              if(len(ppFieldVal) != 9):
                                  passportIsValid = False;
                              elif(ppFieldVal.isdigit() == False):
                                  passportIsValid = False

                              if(passportIsValid == False):
                                  print("pid invalid")
                          break;

                  if(passportIsValid == False):
                      break

           if(passportIsValid == True):
               validPassports += 1

           passportString = ""
           # print("---End Passport Eval----")
       else:
           passportString += line

       line = fp.readline()

print("Valid Passports: {}".format(validPassports))
