{"filter":false,"title":"models.py","tooltip":"/contact/models.py","undoManager":{"mark":-1,"position":-1,"stack":[[{"start":{"row":8,"column":0},"end":{"row":8,"column":61},"action":"remove","lines":["    email = models.ForeignKey(User, on_delete=models.CASCADE)"],"id":21},{"start":{"row":7,"column":60},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":8,"column":19},"end":{"row":8,"column":30},"action":"remove","lines":["TextField()"],"id":20},{"start":{"row":8,"column":19},"end":{"row":8,"column":61},"action":"insert","lines":["ForeignKey(User, on_delete=models.CASCADE)"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["e"],"id":19},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["m"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["a"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["i"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["l"]}],[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["t"],"id":18},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["n"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["e"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["t"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["n"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["o"]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["c"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["n"],"id":17},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["a"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["m"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"remove","lines":["r"],"id":16},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["o"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"remove","lines":["h"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"remove","lines":["t"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"remove","lines":["u"]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"remove","lines":["a"]}],[{"start":{"row":9,"column":0},"end":{"row":11,"column":69},"action":"remove","lines":["    views = models.IntegerField(default=0)","    tag = models.CharField(max_length=30, blank=True, null=True)","    image = models.ImageField(upload_to='img', blank=True, null=True)"],"id":15},{"start":{"row":8,"column":32},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":28},"end":{"row":7,"column":0},"action":"remove","lines":["",""],"id":14}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"remove","lines":["    "],"id":13}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":36},"action":"insert","lines":["    content = models.TextField()"],"id":12}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":32},"action":"remove","lines":["    content = models.TextField()"],"id":11}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":44},"action":"remove","lines":["    title = models.CharField(max_length=100)"],"id":10},{"start":{"row":6,"column":28},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":62},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":10,"column":86},"action":"remove","lines":["    created_date = models.DateTimeField(auto_now_add=True)","    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)"],"id":8},{"start":{"row":8,"column":32},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["C"],"id":5},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["o"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["n"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["t"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["a"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["c"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["t"],"id":4},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["s"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["o"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["P"]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":33},"action":"remove","lines":["from django.utils import timezone"],"id":3},{"start":{"row":3,"column":28},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":18,"column":25},"action":"insert","lines":["# -*- coding: utf-8 -*-","from __future__ import unicode_literals","","from django.db import models","from django.utils import timezone","from django.contrib.auth.models import User","","class Post(models.Model):","    title = models.CharField(max_length=100)","    content = models.TextField()","    created_date = models.DateTimeField(auto_now_add=True)","    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)","    author = models.ForeignKey(User, on_delete=models.CASCADE)","    views = models.IntegerField(default=0)","    tag = models.CharField(max_length=30, blank=True, null=True)","    image = models.ImageField(upload_to='img', blank=True, null=True)","    ","    def __unicode__(self):","        return self.title"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1581243981061,"hash":"bb2ade0b5906d4c34ad5489e26929421fa78ce5e"}