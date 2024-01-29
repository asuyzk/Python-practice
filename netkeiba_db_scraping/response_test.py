import requests as req
from bs4 import BeautifulSoup

horse_id = '2018105027'
url = 'https://db.netkeiba.com/horse/'
headers = {'User-Agent':'Mozilla/5.0'}

html = req.get(url + horse_id + '/', headers=headers)
print(html)

soup = BeautifulSoup(html.content, 'html.parser', from_encoding='UTF-8')

horse_title = soup.find(attrs={'class': 'horse_title'})
horse_blood = soup.find(attrs={'class': 'blood_table'})
# horse_prof = soup.find(attrs={'class':'db_prof_table no_OwnerUnit'})
horse_prof = soup.select('[class^="db_prof_table"]')

if horse_title != None:
  horse_title_list = horse_title.text.splitlines()
  blood_list = horse_blood.text.splitlines()
  prof_list = horse_prof[0].text.splitlines()
  # print(prof_list)

  trainer = prof_list[7]
  trainer_bracket = trainer.find(' (')
  trainer_name = trainer[:trainer_bracket]

  print(trainer_name)

  # sex = '不'
  # if horse_title_list[3] == '':
  #   if '牡' in horse_title_list[6]:
  #     sex = '牡'
  #   elif '牝' in horse_title_list[6]:
  #     sex = '牝'
  #   elif 'セ' in horse_title_list[6]:
  #     sex = 'セ'
  # else:
  #   if '牡' in horse_title_list[3]:
  #     sex = '牡'
  #   elif '牝' in horse_title_list[3]:
  #     sex = '牝'
  #   elif 'セ' in horse_title_list[3]:
  #     sex = 'セ'
  # print(sex)

  # print(horse_title_list[1])
  # print(blood_list[3])
  # print(blood_list[16])
  # print(blood_list[19])
else:
  print(horse_title)
