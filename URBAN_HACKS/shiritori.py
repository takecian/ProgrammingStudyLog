from collections import defaultdict

# 東急電鉄全96駅の駅名でしりとりを行った際に最長となる組み合わせを算出せよ
# DFS でしりとりの長さを求める

def shiritori(stations):
  station_map = defaultdict(list)
  for station in stations:
    station_map[station[0]].append(station)

  ans = []

  def dfs(station, paths):
    chara = station[-1]
    found_next = False
    for next_station in station_map[chara]:
      if next_station in paths:
        continue
      found_next = True
      paths.append(next_station)
      dfs(next_station, paths)
      paths.pop()
    if not found_next:
      nonlocal ans
      if len(ans) < len(paths):
        ans = paths[:]
  
  for station in stations:
    dfs(station, [station])
  return ans

if __name__ == '__main__':
  a_stations = ['あおばだい', 'あざみの', 'いけがみ', 'いけじりおおはし', 'いしかわだい', 'いちがお', 'うのき', 'えた', 'えばらなかのぶ', 'えばらちょう', 'おおいまち', 'おおおかやま', 'おおくらやま', 'おおさきひろこうし', 'おくさわ', 'おやまだい', 'おんた', 'おんたけさん']
  k_stations = ['かくげいだいがく', 'かじがや', 'かまた', 'かみのけ', 'うえまち', 'きくな', 'きたせんぞく', 'くがはら', 'くほんぶつ', 'ごたんた', 'こどものくに', 'こまざわだいがく']
  s_stations = ['さぎぬま', 'さくらしんまち', 'さんげんぢゃや', 'しぶや', 'しもしんめい', 'しもたかいど', 'しもまるこ', 'しゆうがおか', 'しょういんじんじゃまえ', 'しんたかしま', 'しんつなしま', 'しんまるこ', 'しんよこはま', 'すずかけだい', 'せたがや', 'せんぞく', 'せんぞくいけ']
  t_stations = ['たいかんやま', 'たかつ', 'たな', 'たまがわ', 'たまぷらーざ', '反町', '千鳥町', 'ちゅうおうりんかん', 'つきみの', 'つくしの', 'つなしま', 'でんえんちょうふ', 'とごしぎんざ', 'とごしこうえん', 'とどろき', 'とりつだいがく']
  n_stations = ['ながつだ', 'なかのふ', 'ながはら', 'なかめぐろ', 'にしこやま', '西太子堂', 'にほんおおどおり', 'ぬまへ']
  h_stations = ['はくらく', 'ばしゃみち', 'はすぬま', 'はたのだい', 'ひがしはくらく', 'ひよし', 'ふじがおか', 'ふたこしんち', 'ふたこたまがわ', 'ふどうまえ']
  m_stations = ['まつばら', 'みずのくち', 'みなとみらい', 'みどりがおか', 'みなみまちだぐらんべりーぱーく', 'みやざきだい', 'みやのさか', 'みやまえだいら', 'みょうれんじ', 'むさしこすき', 'むさしこやま', 'むさししんでん', 'めぐろ', 'もとすみよし', 'もとまちちゅうかがい']
  y_stations = ['やぐちのわたし', 'やました', 'ゆうてんし', 'ゆきがやおおつか', 'ようか', 'よこはま', 'わかばやし']

  ans = (shiritori(a_stations + k_stations + s_stations + t_stations + n_stations + h_stations + m_stations + y_stations))
  print(len(ans))
  print(ans)
