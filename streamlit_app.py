
import streamlit as st

# ==== 價目表 ====
mini價目表 = {
    90: {'mini二節':10900,'mini三節':13400},
    100: {'mini二節':11200,'mini三節':13700},
    120: {'mini二節':11490,'mini三節':13990},
    150: {'mini二節':12400,'mini三節':14900}
    }

prime價目表 = {
100: {'prime二節':{60: 12990, 80:None},'prime三節':{60: 15490, 80:None}},
120: {'prime二節':{60: 12990, 80:13500},'prime三節':{60: 15490, 80:16000}},
150: {'prime二節':{60: 13900, 80:14500},'prime三節':{60: 16400, 80:17000}},
180: {'prime二節':{60: None, 80:16100},'prime三節':{60: None, 80:18600}}
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

桌腳_list={'prime三節':13500,'prime三節黑':13500,'prime三節白':13500,'prime二節':11000,'prime二節黑':11000,'prime二節白':11000,'mini三節':12000,'mini三節黑':12000,'mini三節白':12000,'mini二節':9500,'mini二節黑':9500,'mini二節白':9500,'force':23500,'force四柱黑腳':23500,'force四柱白腳':23500}
顏色_list={'纖維板':0,'菸草橡木':0,'雪白柚木':0,'密西根楓木':0,'北歐白橡木':0,'典雅胡桃木':0,'歐風胡桃木':0,'黑':0,'白':0,'電競':0,'加拿大楓木':0,
           '蜂巢板':0,'黑雲岩':1500,'白雲岩':1500,'泥灰岩':1500,'安藤清水模':1500,'台灣柚木':1500,'北海道榆木':1500,'維吉尼亞楓木':1500,'安德森雪松':1500,'哥倫比亞胡桃':1500,}
形狀_list={'四方前上斜':0,'弧度上斜':0,'前凹':800,'後凹':800,'':0,'四角導圓':800}    
木種成本單價list={'栓木脂接':700,'栓木直拼':900,'白橡木脂接':850,'白橡木直拼':1330}
木種對客單價乘積list={'栓木脂接':1.5,'栓木直拼':1.5,'白橡木脂接':1.4,'白橡木直拼':1.4,'琥珀木':1.6}

報價=input('請輸入mini或prime或force或訂製或製材所:')
if 報價=='mini':
# 查詢：長度 180、深度 90 的價格
    桌寬 = float(input('請輸入桌寬:'))
    桌深 = float(input('桌深固定請輸入60:'))
    桌腳=input('請輸入桌腳:')
    顏色=input('請輸入顏色:')
    形狀=input('請輸入形狀:')
    
    mini升降桌price = float(mini價目表[桌寬][桌腳])
    顏色price=顏色_list[顏色]
    形狀price=形狀_list[形狀]
    total=mini升降桌price+顏色price+形狀price

    print('和您報價')
    print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
    
elif 報價=='prime':
    桌寬 = float(input('請輸入桌寬:'))
    桌深 = float(input('請輸入桌深:'))
    桌腳=input('請輸入桌腳:')
    顏色=input('請輸入顏色:')
    形狀=input('請輸入形狀:')
    
    prime升降桌price = float(prime價目表[桌寬][桌腳][桌深])
    顏色price=顏色_list[顏色]
    形狀price=形狀_list[形狀]
    total=prime升降桌price+顏色price+形狀price

    if 45<桌深<=60:
        桌腳=桌腳+'(60)'
    elif 桌深<=45:
        桌腳=桌腳+'(45)'

    print('和您報價')
    print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
elif 報價=='force':
# 查詢：長度 180、深度 90 的價格
    桌寬 = float(input('請輸入桌寬:'))
    桌深 = float(input('請輸入桌深:'))
    桌腳='force四柱桌腳'
    顏色=input('請輸入顏色:')
    形狀=input('請輸入形狀:')
    
    force升降桌price = float(force價目表[桌寬][桌深])
    顏色price=顏色_list[顏色]
    形狀price=形狀_list[形狀]
    total=force升降桌price+顏色price+形狀price

    print('和您報價')
    print('%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
elif 報價=='訂製':
   # 客人輸入的桌寬與桌深
    桌寬 = float(input('請輸入桌寬:'))
    桌深 = float(input('請輸入桌深:'))
    桌腳= input('請輸入桌腳:')
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
        print('訂%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
    elif 桌寬<110 and (桌腳=='prime三節' or 桌腳=='prime二節'):
        if 45<桌深<=60:
            桌腳=桌腳+'(短版+腳底座60)'
        elif 桌深<=45:
            桌腳=桌腳+'(短版+腳底座45)'
        print('訂%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
    elif 桌深<57.5 and (桌腳=='prime三節' or 桌腳=='prime二節'):
        if 45<桌深<=60:
            桌腳=桌腳+'(短側片+腳底座60)'
        elif 桌深<=45:
            桌腳=桌腳+'(短側片+腳底座45)'
        print('訂%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
    elif 桌深<72 and 桌腳=='force':
        print('桌深無法安裝force!')
    else:
        print('訂%3.0f*%2.0f%s(%s)+%s=%5.0f'%(桌寬,桌深,顏色,形狀,桌腳,total))
        dicount=total*0.9
        print('優惠後為%5.0f$'%dicount)

    print('\n''備註:')
    print('1. 以上金額含運、不含安裝')
    print('2. 訂製約35天(含假日)')
    print('3. 訂製不含配送時間，配送時間另計')
else:
    木種=input('請輸入木種:')
    桌寬=float(input('請輸入桌寬:'))
    桌深=float(input('請輸入桌深:'))
    厚度=float(input('請輸入厚度(白橡木直拼3.3請輸入3.5):'))
    桌腳=input('請輸入桌腳:')
    桌腳price=桌腳_list[桌腳]

    if 木種 !='琥珀木':
        if 桌深 >= 81 and 厚度<=2.7:
            print('無法製作!!桌深厚度81cm以上，厚度需為2.7以上')
        else:
            桌板price=round(桌寬*桌深*厚度/2700*木種成本單價list[木種]*木種對客單價乘積list[木種],-2)
            total=桌板price+桌腳price
            print('和您報價')
            print('(製材所)-訂%3.0f*%2.0f*%1.1f%s+%s=%5.0f' % (桌寬,桌深,厚度,木種,桌腳,total))
    else:
        price = find_price(桌寬, 桌深)*木種對客單價乘積list[木種]
        total=桌板price+桌腳price
        print('和您報價')
        print('(製材所)-訂%3.0f*%2.0f*%1.1f%s+%s=%5.0f' % (桌寬,桌深,厚度,木種,桌腳,total))
    
    print('\n''備註:')
    print('1. 以上金額含運、不含安裝')
    print('2. 訂製約45天(含假日)')
    print('3. 訂製不含配送時間，配送時間另計')

# ==== 額外加價設定 ====
顏色加價 = {
    '原木': 0,
    '白色': 1000,
    '黑色': 1000,
    '淺胡桃色': 1000
}

形狀加價 = {
    '方形': 0,
    '圓角': 300,
    '弧形': 500
}

# ==== 報價邏輯（封裝成函數） ====
def 計算報價(桌腳種類, 桌寬, 桌深, 顏色, 形狀):
    try:
        if 桌腳種類 == 'mini':
            if 桌寬 in mini價目表 and f'mini二節' in mini價目表[桌寬]:
                價格 = mini價目表[桌寬]['mini二節']
            else:
                return "無對應尺寸"
        elif 桌腳種類 == 'prime':
            價格 = prime價目表.get(桌寬, {}).get('prime二節', {}).get(桌深)
            if 價格 is None:
                return "無對應尺寸"
        elif 桌腳種類 == 'force':
            價格 = force價目表.get(桌寬, {}).get(桌深)
            if 價格 is None:
                return "無對應尺寸"
        elif 桌腳種類 == '訂製':
            價格 = 桌寬 * 桌深 * 60 / 10000
        elif 桌腳種類 == '製材所':
            價格 = 桌寬 * 桌深 * 75 / 10000
        else:
            return "無效的桌腳種類"
        
        價格 += 顏色加價.get(顏色, 0)
        價格 += 形狀加價.get(形狀, 0)
        return round(價格)
    except:
        return "計算錯誤"

# ==== Streamlit UI ====
st.title("桌子報價系統")
st.markdown("請輸入桌子的參數來獲得報價")

桌腳種類 = st.selectbox("選擇桌腳種類", ["mini", "prime", "force", "訂製", "製材所"])
桌寬 = st.number_input("桌寬 (cm)", min_value=60, max_value=240, step=10)
桌深 = st.number_input("桌深 (cm)", min_value=50, max_value=100, step=5)
顏色 = st.selectbox("選擇顏色", ["原木", "白色", "黑色", "淺胡桃色"])
形狀 = st.selectbox("選擇形狀", ["方形", "圓角", "弧形"])

if st.button("計算報價"):
    結果 = 計算報價(桌腳種類, 桌寬, 桌深, 顏色, 形狀)
    st.success(f"報價結果：{結果} 元")
