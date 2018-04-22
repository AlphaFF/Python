#!/usr/bin/env python3
# coding=utf-8

# # 使用Django自带的基本view来实现接口的使用方法
# # json不能序列化时间格式的数据
# # 必须设置 content_type='application/json'
# from django.views.generic.base import View
# from .models import Post
#
# class PostListView(View):
#     def get(self,request):
#         json_list = []
#         posts = Post.objects.all()
#         for post in posts:
#             d = {}
#             d['title'] = post.title
#             d['body'] = post.body
#             # d['publish'] = post.publish
#             json_list.append(d)
#         from django.http import HttpResponse
#         import json
#         return HttpResponse(json.dumps(json_list),content_type='application/json')