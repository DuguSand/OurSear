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
            show = []
            light = []
            t = 0

            search = form.save(commit=False)
            length = len(search.text)
            topics = Topic.objects.all()
            for topic in topics:
                t = 0
                if search.text in topic.text:
                    show.append(topic)
                    for txt in topic.text:
                        if txt in search.text and topic.text[t:t+length+1] == search.text:
                            light.append(list(range(t, t+length+1)))
                        t += 1

            context = {'topics': show, 'search': search, 'light': light}

            return render(request, 'searcher/topics.html', context)

def topic(request, topic_id):
    """显示单个主题的所有条目"""
    topic = Topic.objects.get(id=topic_id)
    entry = Entry.objects.get(id=topic_id)
    context = {'topic':topic, 'entry': entry}
    return render(request, 'searcher/topic.html', context)
