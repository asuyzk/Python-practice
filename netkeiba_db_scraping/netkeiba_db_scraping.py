import time
import datetime
import csv
import requests as req
from bs4 import BeautifulSoup

def main():
  crt_time = datetime.datetime.now()
  print(crt_time)

  year_cnt = '2012'
  write_csv = csv.writer(open('./' + year_cnt + '_HorseID.csv','a',encoding='utf-8', newline=''))

  row_cnt = 0
  # for year_cnt in range(2020,2021):
  for id_cnt in range(1000,10000):
    try:
      horse_id = str(year_cnt) + '1' + str(id_cnt).zfill(5)
      not_raced = 'の' + str(year_cnt)

      horse_data = getHorseData(horse_id, not_raced)

      if horse_data != None:
        write_csv.writerow(horse_data)
        print(horse_data)

        row_cnt+=1
      else:
        print('None')

    except Exception as err:
      print(err)
      
    time.sleep(10)

  # write_csv.writerow(result)

  crt_time = datetime.datetime.now()
  print(crt_time)

def getHorseData(horse_id, not_raced):
  print(horse_id)

  url = 'https://db.netkeiba.com/horse/'
  headers = {'User-Agent':'Mozilla/5.0'}

  html = req.get(url + horse_id + '/', headers=headers)
  soup = BeautifulSoup(html.content, 'html.parser', from_encoding='UTF-8')

  horse_title = soup.find(attrs={'class': 'horse_title'})
  horse_blood = soup.find(attrs={'class': 'blood_table'})
  horse_prof = soup.select('[class^="db_prof_table"]')

  if horse_title != None:
    horse_title_list = horse_title.text.splitlines()
    blood_list = horse_blood.text.splitlines()
    prof_list = horse_prof[0].text.splitlines()

    if not_raced in horse_title_list[1]:
      return None

    horse_name = horse_title_list[1]
    birthday = prof_list[3]

    sex = '不'
    if horse_title_list[3] == '':
      if '牡' in horse_title_list[6]:
        sex = '牡'
      elif '牝' in horse_title_list[6]:
        sex = '牝'
      elif 'セ' in horse_title_list[6]:
        sex = 'セ'
    else:
      if '牡' in horse_title_list[3]:
        sex = '牡'
      elif '牝' in horse_title_list[3]:
        sex = '牝'
      elif 'セ' in horse_title_list[3]:
        sex = 'セ'
    
    father = blood_list[3]
    mother = blood_list[16]
    mothers_father = blood_list[19]

    trainer = prof_list[7]
    trainer_bracket = trainer.find(' (')
    trainer_name = trainer[:trainer_bracket]

    return_data = [horse_id, horse_name, birthday, sex, father, mother, mothers_father, trainer_name]
    return return_data  
  else:
    return None

main()