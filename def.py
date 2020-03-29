#函数  默认值 关键字传参 混合模式传参 序列传参 字典传参 返回值包含多个数据
#默认值
def calc_exchange_rate(amt, source, target = "USD"):
    if source == 'CNY' and target == "USD" :
        result = amt / 6.7516
        return result
r = calc_exchange_rate(100, "CNY", "USD")
print(r)
#以形参形式  关键字传参
def heal_check(name,age,height,weight,hr,hbp,lbp,glu):
    print("身体正常")
heal_check(name="z", age=10, height=10, weight=50, hr=70, hbp=10, lbp=10, glu=10)
# 混合模式传参
# * 代表之后所有参数必须使用关键字传参
def heal_check1(name,age,*,height,weight,hr,hbp,lbp,glu):
    print("身体正常")
#序列传参
def calc(a, b, c):
    return (a+b)*c
l = [1,5,10]
calc(*l)

#字典传参
def heal_check2(name,age,height,weight,hr,hbp,lbp,glu):
    print("身体正常")

params = {"name":"z", "age":10, "height":10, "weight":50, "hr":70, "hbp":10, "lbp":10, "glu":10}
heal_check2(**params)
#返回值包含多个数据
def get_detail_info():
    dict = {
        "employee": [{"name":"张三", "salary":1800}],
        "device":[
            {"id":"8888", "title":'dddd'}
        ]
    }
    return dict


