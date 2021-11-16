#16.11.2021

hamkasblar = {
    'ali':{'familiya':'valiyev',
           't_yil':1995,
           'malumoti': 'oliy',
           'tillar': ['python','c#']
           },
     'vali':{'familiya':'valiyev',
             't_yil':1997,
             'malumoti': "o'rta",
             'tillar': ['C++','html']},
     'hasan':{'familiya':'valiyev',
              't_yil':1995,
              'malumoti': "o'rta maxsus",
              'tillar': ['js','c#']}
     }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['t_yil']}-yilda tug'ilgan. \n"
          f"Ma'lumoti: {info['malumoti']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
          
     