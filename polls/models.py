# coding: utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
import hashlib, random, os.path, datetime, time
# Create your models here.
def getImageStorePath(self, filename):
    storepath = self._meta.app_label + "/img/" + datetime.datetime.now().strftime('%Y%m') + "/"
    self.img = hashlib.md5(str(time.time()) + str(random.randint(0, 999))).hexdigest() + os.path.splitext(filename)[1]
    print filename
    return "{storepath}/{filename}".format(storepath=storepath, filename=self.img)

class QuestionManager(models.Manager):
    def getTopFivePolls(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            SELECT q.id, q.question_text, SUM(c.votes) as num FROM polls_question q
            LEFT JOIN polls_choice c ON c.question_id = q.id
            WHERE q.status = 1
            GROUP BY q.id
            ORDER BY num DESC""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model(id=row[0], question_text=row[1])
            result_list.append(p)
        return result_list

@python_2_unicode_compatible
class Question(models.Model):
    DISACTIVE = 0
    ACTIVE = 1
    QUESTION_STATUS_CHOICES = (
        (DISACTIVE, '已停用'),
        (ACTIVE, '正常'),
    )
    question_text = models.CharField(max_length=200, verbose_name='问题内容')
    desc_text = models.TextField(max_length=500, verbose_name='调查描述', default='', blank=True)
    pub_date = models.DateTimeField('发布时间')
    img = models.ImageField(upload_to=getImageStorePath, default='', verbose_name='图片地址', blank=True)
    status = models.IntegerField(default=1, choices=QUESTION_STATUS_CHOICES, verbose_name='状态')
    objects = models.Manager()
    q_objects = QuestionManager()


    def __str__(self):
        return self.question_text

    def getVotesNum(self):
        return self.choice_set.aggregate(total_num = models.Sum('votes'))['total_num']

    def hasImg(self):
        return self.img != ''

    def isChildChoice(self, choice_id):
        return self.choice_set.get(pk=choice_id)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def isHot(self):
        return self.getVotesNum() >= 15

    class Meta:
        verbose_name = '投票问题'
        verbose_name_plural = '投票问题'

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='选项内容')
    votes = models.IntegerField(default=0, verbose_name='投票数')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = '投票选项'
        verbose_name_plural = '投票选项'