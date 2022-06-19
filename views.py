from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SearchForm
from .models import Topic, Entry
# Create your views here.

def index(request):
    """搜索"""
    if request.method != 'POST':
        # 没提交数据就创建一个新的表单
        form = SearchForm()
        context = {'form': form}

        return render(request, 'searcher/index.html', context)

    else:
        # 如果是POST，那就对数据进行处理
        form = SearchForm(request.POST)
        if form.is_valid(): #确定是否有效
            t = 0
            tt = 0
            search = form.save(commit=False)
            length = len(search.text)
            topics = Topic.objects.all()
            top = []
            light = []
            for topic in topics:
                if search.text in topic.text:
                    t = 0
                    top.append(topic)
                    light.append(topic.text)
                    for txt in topic.text:
                        if txt in search.text and light[tt][t:t+length] == search.text:
                            light[tt] = light[tt][:t]+"<b>"+light[tt][t:t+length]+"</b>"+light[tt][t+length:]
                            t += length+7
                        else:
                            t += 1
                    tt += 1

            context = {'topics': top, 'search': search, 'lights': light}

            return render(request, 'searcher/topics.html', context)

def topic(request, topic_id):
    """显示单个主题的所有条目"""
    topic = Topic.objects.get(id=topic_id)
    entry = Entry.objects.get(id=topic_id)
    context = {'topic':topic, 'entry': entry}
    return render(request, 'searcher/topic.html', context)
