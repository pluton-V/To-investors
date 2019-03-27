input_kihonkyuu = input('基本給：')
input_zangyo_time = input('残業時間：')
input_yakin = input('夜勤回数：')
input_shinyazangyo_time = input('深夜残業時間：')
teate = input('各種手当て：')

#時給
count_jikyu = int(input_kihonkyuu) / 150
#残業時給
count_zangyo_money = count_jikyu * 1.25
#残業代合計
count_zangyo_money_total = count_zangyo_money * float(input_zangyo_time)
#夜勤手当
count_yakin = int(input_yakin) * 4500
#深夜残業手当
count_shinyazangyo_money = count_jikyu  * 0.5
#深夜残業合計
count_shinyazangyo_money_total = count_shinyazangyo_money * float(input_shinyazangyo_time)
#総支給額
total_price = round(int(input_kihonkyuu) + count_zangyo_money_total + count_shinyazangyo_money_total + int(teate))

#控除
kenko_hoken = 13350
nenkin = 27450
juminzei = 7500
koyohoken = (total_price - int(teate)) * 3 / 1000
syotokuzei = (total_price - int(teate)) / 42.9841781

kojo_total = kenko_hoken + nenkin + juminzei + koyohoken + syotokuzei

#差し引き支給額
tedori = round(total_price - kojo_total)

print('======================')
print('総支給額')
print("￥{:,}".format(total_price))
print('差し引き支給額')
print("￥{:,}".format(tedori))

input()