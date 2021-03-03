file_r = open('Shakespeare.txt', mode='r', encoding='utf-8')
lines = file_r.readlines() 
file_r.close()

file_w = open('Shakespeare-out.txt', mode='w', encoding='utf-8')
file_w.writelines(lines) 
file_w.close()