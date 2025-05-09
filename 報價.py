mini價目表 = {
    'mini二節': { 90: 10900, 100:11200, 120: 11490, 150: 12400},
    'mini三節': { 90: 13400, 100:13700, 120: 13990, 150: 14900},
    'mini二節黑': { 90: 10900, 100:11200, 120: 11490, 150: 12400},
    'mini三節黑': { 90: 13400, 100:13700, 120: 13990, 150: 14900},
    'mini二節白': { 90: 10900, 100:11200, 120: 11490, 150: 12400},
    'mini三節白': { 90: 13400, 100:13700, 120: 13990, 150: 14900}
}

prime價目表 = {
    'prime二節': {
        100: {60: 12990, 80: None}, 
        120: {60: 12990, 80: 13500}, 
        150: {60: 13900, 80: 14500}, 
        180: {60: None, 80: 16100}
    },
    'prime三節': {
        100: {60: 12990, 80: None}, 
        120: {60: 12990, 80: 13500}, 
        150: {60: 13900, 80: 14500}, 
        180: {60: None, 80: 16100}
    },
    'prime二節黑': {
        100: {60: 12990, 80: None}, 
        120: {60: 12990, 80: 13500}, 
        150: {60: 13900, 80: 14500}, 
        180: {60: None, 80: 16100}
    },
    'prime三節黑': {
        100: {60: 12990, 80: None}, 
        120: {60: 12990, 80: 13500}, 
        150: {60: 13900, 80: 14500}, 
        180: {60: None, 80: 16100}
    },
    'prime二節白': {
        100: {60: 12990, 80: None}, 
        120: {60: 12990, 80: 13500}, 
        150: {60: 13900, 80: 14500}, 
        180: {60: None, 80: 16100}
    },
    'prime三節白': {
        100: {60: 12990, 80: None}, 
        120: {60: 12990, 80: 13500}, 
        150: {60: 13900, 80: 14500}, 
        180: {60: None, 80: 16100}
    }
}

force價目表 = {
    150: {80: 26000, 90: 26300},
    160: {80: 26500, 90: 26800},
    180: {80: 27600, 90: 27900},
    200: {80: 28300, 90: 28600},
    220: {80: 28800, 90: 29100}
}

import pandas as pd

data = {
    '深度範圍': ['50-60', '61-80', '81-90'],
    '90': [1990, 2500, 2800],
    '90.1-119.9': [1990, 2500, 2800],
    '120': [1990, 2500, 2800],
    '120.1-135':[2400,3000,3300],
    '135.1-149.9':[2900,3500,3800],
    '150':[2900,3500,3800],
    '150.1-165':[3400,4000,4300],
    '165.1-179.9':[3900,4500,4800],
    '180':[4400,5100,5400],
    '180.1-185':[4600,5500,5800],
    '185.1-199.9':[None,6000,6300],
    '200':[None,6000,6300],
    '200.1-219.9':[None,6800,7100],
    '220':[None,7000,7300]}



df = pd.DataFrame(data)

def in_range(value, range_str):
    if '-' in range_str:
        start, end = map(float, range_str.split('-'))
        return start <= value <= end
    else:
        return float(range_str) == value

def find_price(width, depth):
    # 找橫向欄位（桌寬）在哪一欄
    for col in df.columns[1:]:
        if in_range(width, col):
            # 找縱向列（桌深）在哪一列
            for i, row in df.iterrows():
                if in_range(depth, row['深度範圍']):
                    return df.loc[i, col]
    return '找不到符合條件的價格'

#規格品琥珀木價目表
import pandas as pd

data={'桌深範圍':['50-70','71-90'],
      '120-149.9':[9800,11500],
      '150-179.9':[12500,14500],
      '180-209.9':[14500,17500],
      '210-239.9':[16500,20500],
      '240':[18500,22500]
     }

#定義表格
df = pd.DataFrame(data)

#表格桌寬桌深範圍
def in_range(value,range_str):
    if '-' in range_str:
        start,end = map(float,range_str.split('-'))
        return start <= value <= end
    else:
        return None
        
#查找表格價格
def find_price(width,depth):
    for col in df.columns[1:]:
        if in_range(width,col):
            for i, row in df.iterrows():
                if in_range(depth,row['桌深範圍']):
                    return df.loc[i,col]
                    
木種成本單價list={'栓木脂接':700,'栓木直拼':900,'白橡木脂接':850,'白橡木直拼':1330}
木種對客單價乘積list={'栓木脂接':1.5,'栓木直拼':1.5,'白橡木脂接':1.4,'白橡木直拼':1.4,'琥珀木':1.6}

桌腳_list={'prime三節':13500,'prime三節黑':13500,'prime三節白':13500,
         'prime二節':11000,'prime二節黑':11000,'prime二節白':11000,
         'mini三節':12000,'mini三節黑':12000,'mini三節白':12000,
         'mini二節':9500,'mini二節黑':9500,'mini二節白':9500,
         '固定桌腳':3980,'固定黑腳':3980,'固定白腳':3980,
         'force四柱桌腳':23500,'force四柱黑腳':23500,'force四柱白腳':23500,}
顏色_list={'纖維板':0,'菸草橡木':0,'雪白柚木':0,'密西根楓木':0,'北歐白橡木':0,'典雅胡桃木':0,'歐風胡桃木':0,'黑':0,'白':0,'電競':0,'加拿大楓木':0, 
         '蜂巢板':0,'黑雲岩':1500,'白雲岩':1500,'泥灰岩':1500,'安藤清水模':1500,'台灣柚木':1500,'北海道榆木':1500,'維吉尼亞楓木':1500,'安德森雪松':1500,'哥倫比亞胡桃':1500,}
形狀_list={'四方前上斜':0,'弧度上斜':0,'前凹':800,'後凹':800,'':0,'四角導圓':800}

while True:
    print('\n')
    報價 =input('請輸入mini或prime或force或訂製或製材所:')


    if 報價 == 'mini':
        桌寬 = float(input('請輸入桌寬:'))
        桌深 = float(input('桌深請輸入60:'))
        桌腳=input('請輸入桌腳:')
        顏色=input('請輸入顏色:')
        形狀=input('請輸入形狀:')
    
        mini升降桌price = float(mini價目表[桌腳][桌寬])
        顏色price=顏色_list[顏色]
        形狀price=形狀_list[形狀]

        total=mini升降桌price+顏色price+形狀price

        print('和您報價')
        print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
    
    elif 報價 == 'prime':
        桌寬 = float(input('請輸入桌寬:'))
        桌深 = float(input('請輸入桌深:'))
        桌腳=input('請輸入桌腳:')
        顏色=input('請輸入顏色:')
        形狀=input('請輸入形狀:')
    
        prime升降桌price = float(prime價目表[桌腳][桌寬][桌深])
        顏色price=顏色_list[顏色]
        形狀price=形狀_list[形狀]
        total=prime升降桌price+顏色price+形狀price
        if 45<桌深<=60:
            桌腳=桌腳+'(60)'

        print('和您報價')
        print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
    
    elif 報價 == 'force':
        桌寬 = float(input('請輸入桌寬:'))
        桌深 = float(input('請輸入桌深:'))
        桌腳=input('請輸入桌腳:')
        顏色=input('請輸入顏色:')
        形狀=input('請輸入形狀:')
    
        force升降桌price = float(force價目表[桌寬][桌深])
        顏色price=顏色_list[顏色]
        形狀price=形狀_list[形狀]
        total=force升降桌price+顏色price+形狀price
        
        print('和您報價')
        print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
        
    elif 報價 == '訂製':
        桌寬 = float(input('請輸入桌寬:'))
        桌深 = float(input('請輸入桌深:'))
        桌腳=input('請輸入桌腳:')
        顏色=input('請輸入顏色:')
        形狀=input('請輸入形狀:')
    
        price = find_price(桌寬, 桌深)
        桌腳price=桌腳_list[桌腳]
        顏色price=顏色_list[顏色]
        形狀price=形狀_list[形狀]
        total=price+桌腳price+顏色price+形狀price
        
        print('和您報價')
        if 桌寬<110 and (桌腳=='prime三節' or 桌腳=='prime二節') and 桌深<57.5 and (桌腳=='prime三節' or 桌腳=='prime二節'):
            桌腳=桌腳+'(短版+短側片+腳底座45)'
            if 顏色price != 0:
                print('%3.0f*%2.0f*4%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
            else:
                print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
        
        elif 桌寬<110 and (桌腳=='prime三節' or 桌腳=='prime二節'):
            if 45<桌深<=60:
                桌腳=桌腳+'(短版+腳底座60)'
                if 顏色price != 0:
                    print('%3.0f*%2.0f*4%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
                else:
                    print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
            elif 桌深<=45:
                桌腳=桌腳+'(短版+腳底座45)'
                if 顏色price != 0:
                    print('%3.0f*%2.0f*4%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
                else:
                    print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
               
        elif 桌深<57.5 and (桌腳=='prime三節' or 桌腳=='prime二節'):
            if 45<桌深<=60:
                桌腳=桌腳+'(短側片+腳底座60)'
                if 顏色price != 0:
                    print('%3.0f*%2.0f*4%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
                else:
                    print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
            elif 桌深<=45:
                桌腳=桌腳+'(短側片+腳底座45)'
                if 顏色price != 0:
                    print('%3.0f*%2.0f*4%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
                else:
                    print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
        
        elif 桌深<72 and 桌腳=='force':
            print('桌深無法安裝force!')
        
        else:
            if 顏色price != 0:
                print('%3.0f*%2.0f*4%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
            else:
                print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
            dicount=total*0.9
            print('優惠後金額為%5.0f'%dicount)

            print('\n''備註:')
            print('1. 以上金額含運(不含宜花東地區)、不含安裝')
            print('2. 訂製約35天(含假日)')
            print('3. 製程為工廠製作時間，不包含後續的配送與安裝，實際配送日以通知為主')
    else:
        木種=input('請輸入木種:')


        if 木種 !='琥珀木':
            桌寬=float(input('請輸入桌寬:'))
            桌深=float(input('請輸入桌深:'))
            厚度=float(input('請輸入厚度(若白橡木直拼3.3請輸入3.5):'))
            桌腳=input('請輸入桌腳:') 

            if 桌深 >= 81 and 厚度<=2.7:
                print('無法製作!!桌深厚度81cm以上，厚度需為2.7以上')
            else:
                桌板price=round(桌寬*桌深*厚度/2700*木種成本單價list[木種]*木種對客單價乘積list[木種],-2)
                total=桌板price+桌腳price
                print('和您報價')
                print('(製材所)-訂%3.0f*%3.0f*%1.1f%s+%s=%5.0f' % (桌寬,桌深,厚度,木種,桌腳,total))
        else:
            桌寬=float(input('請輸入桌寬:'))
            桌深=float(input('請輸入桌深:'))
            厚度=float(input('厚度請輸入4.5:'))
            桌腳=input('請輸入桌腳:') 
            桌腳price=桌腳_list[桌腳]
        
            price = find_price(桌寬, 桌深)*木種對客單價乘積list[木種]
            total=桌板price+桌腳price
            print('和您報價')
            print('(製材所)-訂%3.0f*%3.0f*%1.1f%s+%s=%5.0f' % (桌寬,桌深,厚度,木種,桌腳,total))
    
        print('\n''備註:')
        print('1. 1.以上金額含運(不含宜花東地區)、不含安裝')
        print('2. 訂製約45工作天')
        print('3. 製程為工廠製作時間，不包含後續的配送與安裝，實際配送日以通知為主')

input('請按enter鍵結束')
    #again = input("要重新報價嗎？(y/n)：")
    #if again.lower() != 'y':
            #break