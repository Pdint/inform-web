from django.shortcuts import render, HttpResponse
# from django.contrib import admin
#import os
import json
#from django.http import JsonResponse

import pandas as pd 
#from .models import MyModel
#from .models import CrawledData

def index(request):
    # 데이터프레임 생성
    data = pd.read_csv("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv",encoding='utf-8')
    data_part = pd.DataFrame(data.loc[[0],['news','summary']]) # 0행, news, summary 열만 출력
    df_part = pd.DataFrame(data_part)
    df_all = pd.DataFrame(data)

    # 데이터프레임을 HTML로 변환
    html_pd_part = df_part.to_html(classes='table table-bordered table-striped', index=False)
    html_all = df_all.to_html(classes='table table-bordered table-striped', index=False)
    #context = {'html_output': html_output}
    #context_json = json.dumps(context)
    #data = json.dumps(html_output)
    #json_data = df.to_json(orient='records')
    
    context = {'data_pd_part': html_pd_part, 'data_all' : html_all}
    
    return render(request, 'index12x.html', context)




 

"""
def index(request):
    return render(request, 'index_comp.html')

def BA(request):
    data = pd.read_csv("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv",encoding='utf-8')
    data = data.loc[::-1].reset_index(drop=True) # pandas 역순 정렬
    df = pd.DataFrame(data)

    # 데이터프레임을 HTML로 변환
    html_output = df.to_html(classes='table table-bordered table-striped', index=False) # html 코드로 변경
    context = {'html_output': html_output, 'django_variable': 'Hello from Django!'}
    return render(request, 'BA.html', context)

def SUM(request): 
    data = pd.read_csv("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv",encoding='utf-8')
    data = data.loc[::-1].reset_index(drop=True) # pandas 역순 정렬
    data = pd.DataFrame(data.loc[[0],['summary']]) # 0행, summary 열만 출력

    # 데이터프레임을 HTML로 변환
    html_output = data.to_html(classes='table table-bordered table-striped', index=False) # html 코드로 변경경
    context = {'html_output': html_output, 'django_variable': 'Hello from Django!'}
    return render(request, 'SUM.html', context)
"""





























"""
def index(request):
    # 여기에서는 간단한 예시로 두 개의 게임 값을 컨텍스트에 추가하여 템플릿에 전달합니다.
    game_values = range(1, 11)

    # 사용자의 GET 요청을 확인하여 선택된 게임 값이 있는지 확인합니다.
    selected_game = request.GET.get('game_select')                                                                                                

    # 선택된 게임 값이 있다면 어떤 처리를 수행하거나 결과를 가져올 수 있습니다.
    # 이 예시에서는 그냥 출력하도록 하겠습니다.
    if selected_game:
        print(f"Selected game: {selected_game}")

    # 컨텍스트에 변수들을 추가하여 템플릿에 전달합니다.
    context = {
        'game_values': game_values,
        'selected_game': selected_game,
    }
    # render 함수를 사용하여 템플릿을 렌더링하고 응답을 생성합니다.
    return render(request, 'index.html')#, context)
"""

"""
MySQLog를 통한 연결 실패
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{"posts":posts})
"""




"""
def index(request):
    # 실제 CSV 파일 경로 (프로젝트에 맞게 경로 수정)
    csv_file_path = "C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv"

    try:
        # CSV 파일을 Pandas DataFrame으로 읽기 (인코딩 명시)
        data = pd.read_csv(csv_file_path, encoding='utf-8')

        # DataFrame을 JSON으로 변환하여 UTF-8로 인코딩
        json_data = data.to_json(orient='records', force_ascii=False)

        # JSON 데이터를 HttpResponse로 전송
        return render(request, 'index.html', {'data': json_data})
    
    except Exception as e:
        # 파일 읽기 실패 시 에러 메시지 전송
        return JsonResponse({'error': str(e)})
"""




"""
def index(request):
    data = pd.read_csv("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/BlueArchive.csv",encoding='utf-8')
    #for index, row in data.iterrows():
    #    MyModel.objects.create(column1=row['column1'], column2=row['column2'])
    #return HttpResponse('Data imported successfully!')
    json_data = data.to_json(orient='records')
    return JsonResponse({'data': json_data})
"""

"""
def index(request):
    # 데이터베이스에서 모델 가져오기
    queryset = MyModel.objects.all()

    # QuerySet을 Pandas DataFrame으로 변환
    data = pd.DataFrame(list(queryset.values()))

    # HTML 템플릿에 데이터 전달
    context = {'data': data.to_html(classes='table table-striped')}
    return render(request, 'index.html', context)
"""





"""
#임시 추가 함수 12/04
def get_json_data(request):
    # 선택된 ID 가져오기
    selected_id = request.GET.get('id')

    # JSON 파일 경로
    json_file_path = os.path.join("C:/Users/samto/OneDrive/바탕 화면/대학/1-2학기/AI프로그래밍연습/WedProject/Myapp/static/file.json")

    try:
        # JSON 파일 열기
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            
            # 선택된 ID에 해당하는 데이터 찾기
            result_data = next((item for item in data if str(item.get('id')) == selected_id), None)

            if result_data is not None:
                return JsonResponse(result_data, safe=False)
            else:
                return JsonResponse({"error": f"Data not found for id {selected_id}"}, status=404)
            
    except FileNotFoundError:
        return JsonResponse({"error": "File not found"}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format in file"}, status=500)
"""


"""
topics =[
    {'link':'Bluearchive', 'title':'Bule Archive', "body":'conntinue blue archive test'},
    {'link':'Maplestroy', 'title':'Maple Story', "body":'conntinue maple story test'},
    {'link':'Main', 'title':'Sub Site', "body":'conntinue main test'}
]

def HTMLtemp(tag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href ="/{topic["link"]}"> {topic["title"]}</a></li>'   
    return f'''
    <html>
    <body>
        <h1><a href = '/'> Home</h1>
        <ol>
            {ol}
        </ol>
        {tag}
    </body>
    </html>
    '''

# Create your views here.
def index(request):
    h2 ='''
    <h2>Hello, World!</h2>
    pratice web site
    '''
    return HttpResponse(HTMLtemp(h2))

def BA(request):
    global topics
    article = ''
    for topic in topics:
        if topic['link'] == 'Bluearchive':
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLtemp(article))

def MS(request):
    global topics
    article = ''
    for topic in topics:
        if topic['link'] == 'Maplestroy':
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLtemp(article))

def main(request):
    global topics
    article = ''
    for topic in topics:
        if topic['link'] == 'Main':
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLtemp(article))
"""