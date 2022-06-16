from django.db import models

# Create your models here.

class Topic(models.Model):
    """标题名字"""
    text = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回text中的字符串"""
        return self.text

class Entry(models.Model):
    """主题下的内容"""
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE) #关联标题删除时一并关联
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回text中的字符串"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text